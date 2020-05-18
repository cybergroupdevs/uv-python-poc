import u2py
from flask import Flask, Response
import json

from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesercretkey'
CORS(app)


def convert_field_formats(field_data, field_format, format):
    data = u2py.DynArray()
    data.insert(1, 0, 0, field_data)
    if format == 'external':
        formatted_data = str(data.extract(1).oconv(field_format))
    else:
        formatted_data = str(data.extract(1).iconv(field_format))
    return formatted_data


def check_existing_record(file_object, record_ID):
    try:
        file_object.read(record_ID)
        return True
    except u2py.U2Error:
        return False


def calculate_xmul(trans_data):
    transaction_type = trans_data['TRAN.TYPE']
    trans_sub_type = trans_data['TRAN.SUB.TYPE']
    if transaction_type == 'VSAL':
        if trans_sub_type == 'CF.CANCEL':
            xmul = 1
        else:
            xmul = -1
    else:
        xmul = 1
    return xmul


def calculate_amount(trans_data):
    amount_list = []
    comm_sale_amount = [float(key['CommSaleAmt']) for key in trans_data['ITEM_MV']]
    quantity_list = [int(key['MKUP.STORE.QTY']) for key in trans_data['MKUP.STORE.QTY_MV']]
    xmul = calculate_xmul(trans_data)
    for i in range(len(comm_sale_amount)):
        amount = comm_sale_amount[i]
        if amount != 0:
            quantity = quantity_list[i] * xmul
            amount = convert_field_formats(amount * quantity * 100, 'MD2', 'external')
            amount_list.append(amount)
        else:
            amount_list.append(' ')
    return amount_list


def calculate_commission_amount(trans_data):
    xmul = calculate_xmul(trans_data)
    commission_amount = 0
    empId = [key['CommEmplId'] for key in trans_data['ITEM_MV']]
    comm_sale_amount = [float(key['CommSaleAmt']) for key in trans_data['ITEM_MV']]
    quantity_list = [int(key['MKUP.STORE.QTY']) for key in trans_data['MKUP.STORE.QTY_MV']]
    for i in range(len(empId)):
        quantity = xmul * quantity_list[i]
        commission_amount = commission_amount + comm_sale_amount[i] * quantity
    return commission_amount


def set_empsn_values(trans_data, em_file):
    empsn_list = []
    comm_emp_id = [key['CommEmplId'] for key in trans_data['ITEM_MV']]
    for i in range(len(comm_emp_id)):
        empId = comm_emp_id[i]
        if check_existing_record(em_file, empId):
            empsn = list(em_file.readv(empId, 17))[0][0]
        else:
            empsn = empId
        empsn_list.append(empsn)

    return empsn_list


def set_emp_total(trans_data, transactionFile):
    rentalId = trans_data['RECEIVED.ASN']
    comm_sale_amount = [float(key['CommSaleAmt']) for key in trans_data['ITEM_MV']]
    trans_sale_total = 0
    comm_sales_total = 0
    disc_conv_to_mkdn = ''
    unconverted_dis_amt = 0
    if rentalId != '':
        discountType = [int(key['DISCOUNT.TYPE']) for key in trans_data['DISCOUNT.TYPE_MV']]
        if len(discountType) != 1 and discountType[0] != '':
            discountLine = transactionFile.readv(trans_data['_ID'], 45)
            discount = [float(x[0]) for x in discountLine]
            discountSum = sum(discount)
            if discountSum != 0:
                searchCount = discountLine.dcount(u2py.SM) + 1
                for i in range(searchCount):
                    discountLine = list(discountLine)
                    if float(discountLine[i][0]) > 0:
                        disc_conv_to_mkdn = list(transactionFile.readv(trans_data['_ID'], 167))
                        break
                if disc_conv_to_mkdn[0][0] != '':
                    unconverted_dis_amt = 0
                else:
                    unconverted_dis_amt = discountSum
    else:
        unconverted_dis_amt = 0

    xmul = calculate_xmul(trans_data)
    quantity_list = [int(key['MKUP.STORE.QTY']) for key in trans_data['MKUP.STORE.QTY_MV']]
    retail_list = [float(key['RETAIL']) for key in trans_data['ITEM_MV']]
    mkdnList = [float(key['MRKDN']) for key in trans_data['ITEM_MV']]
    for i in range(len(retail_list)):
        qty = quantity_list[i]
        total = (retail_list[i] - mkdnList[i]) * qty
        total = total - unconverted_dis_amt
        trans_sale_total = trans_sale_total + total
        qty = qty * xmul
        comm_sales_total = comm_sales_total + (comm_sale_amount[i] * qty)

    return comm_sales_total


def calculate_sale_percentage(comm_emp_id, em_file):
    empId = comm_emp_id[0]
    try:
        em_record = list(em_file.readv(empId, 17))
    except u2py.U2Error:
        em_record = empId
    return em_record


def calculate_comm_emp_type(emp_type):
    emp_type = emp_type.split("*")[2]
    return emp_type


@app.route('/commission/<transId>', methods=['GET'])
def commission_list(transId):
    commission_data = []
    trans_file_name = 'TRANSACTION'
    em_file_name = 'EM'
    transFile = u2py.File(trans_file_name)
    em_file = u2py.File(em_file_name)
    command_line = "LIST TRANSACTION WITH @ID = '{}' COMMISSION.TYPE ITEM.NO RETAIL LIST.PRICE TRAN.TYPE TRAN.SUB.TYPE MRKDN MKUP.STORE.QTY DESC CommSaleAmt CommEmplId CommEmplType CommRate CommEmplPercentUsed RECEIVED.ASN DISCOUNT.TYPE TOJSON".format(transId)
    trans_data = json.loads(u2py.run(command_line, capture=True))['TRANSACTION'][0]
    description = [key['DESC'] for key in trans_data['ITEM_MV']]
    if trans_data['ITEM_MV'][0]['CommEmplId'] != '':
        amount_list = calculate_amount(trans_data)
        empsn_list = set_empsn_values(trans_data, em_file)
        emp_total = set_emp_total(trans_data, transFile)
        commission_amount = calculate_commission_amount(trans_data)
        commRate = [key['CommRate'] for key in trans_data['ITEM_MV']]
        commEmpType = [key['CommEmplType'] for key in trans_data['ITEM_MV']]
        for i in range(len(description)):
            comm_data = {}
            comm_data['class'] = trans_data['ITEM_MV'][i]['ITEM.NO'][0:4]
            comm_data['sku'] = trans_data['ITEM_MV'][i]['ITEM.NO'][4:9]
            comm_data['retail'] = trans_data['ITEM_MV'][i]['RETAIL']
            comm_data['mkdn'] = trans_data['ITEM_MV'][i]['MRKDN']
            comm_data['quantity'] = trans_data['MKUP.STORE.QTY_MV'][i]['MKUP.STORE.QTY']
            comm_data['desc'] = description[i]
            comm_data['commissionType'] = trans_data['ITEM_MV'][i]['COMMISSION.TYPE']
            comm_data['amount'] = amount_list[i]
            comm_data['empPercentage'] = convert_field_formats(commRate[i], 'MD2', 'internal')
            comm_data['salePercentage'] = trans_data['ITEM_MV'][i]['CommEmplPercentUsed']
            comm_data['commEmpId'] = empsn_list[i]
            comm_data['empCommissionType'] = calculate_comm_emp_type(commEmpType[i])
            commission_data.append(comm_data)
        response = {
            'commissionList': commission_data,
            'retailAmount': emp_total,
            'commissionAmount': commission_amount
        }
    else:
        response = {"error": "No commission information for this transaction Id"}
    return Response(json.dumps(response), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()

