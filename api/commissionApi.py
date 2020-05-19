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


def transaction_xmul_value(transaction_data):
    # xmul is temporary local variable
    transaction_type = transaction_data['TRAN.TYPE']
    transaction_sub_type = transaction_data['TRAN.SUB.TYPE']
    if transaction_type == 'VSAL':
        if transaction_sub_type == 'CF.CANCEL':
            xmul = 1
        else:
            xmul = -1
    else:
        xmul = 1
    return xmul


def calculate_amount(transaction_data):
    amount_list = []
    commission_sale_amount = [float(key['CommSaleAmt']) for key in transaction_data['ITEM_MV']]
    quantity_list = [int(key['MKUP.STORE.QTY']) for key in transaction_data['MKUP.STORE.QTY_MV']]
    xmul = transaction_xmul_value(transaction_data)
    for i in range(len(commission_sale_amount)):
        amount = commission_sale_amount[i]
        if amount != 0:
            quantity = quantity_list[i] * xmul
            amount = convert_field_formats(amount * quantity * 100, 'MD2', 'external')
            amount_list.append(amount)
        else:
            amount_list.append(' ')
    return amount_list


def calculate_commission_amount(transaction_data):
    xmul = transaction_xmul_value(transaction_data)
    commission_amount = 0
    employeeId = [key['CommEmplId'] for key in transaction_data['ITEM_MV']]
    commission_sale_amount = [float(key['CommSaleAmt']) for key in transaction_data['ITEM_MV']]
    quantity_list = [int(key['MKUP.STORE.QTY']) for key in transaction_data['MKUP.STORE.QTY_MV']]
    for i in range(len(employeeId)):
        quantity = xmul * quantity_list[i]
        commission_amount = commission_amount + commission_sale_amount[i] * quantity
    return commission_amount


def set_empsn_values(transaction_data, employee_file):
    empsn_list = []
    commission_employee_id = [key['CommEmplId'] for key in transaction_data['ITEM_MV']]
    for i in range(len(commission_employee_id)):
        employeeId = commission_employee_id[i]
        if check_existing_record(employee_file, employeeId):
            empsn = list(employee_file.readv(employeeId, 17))[0][0]
        else:
            empsn = employeeId
        empsn_list.append(empsn)

    return empsn_list


def set_employee_total(transaction_data, transaction_file, desc_length):
    rental_id_list = [key['RESERVATIONS'] for key in transaction_data['ITEM_MV']]
    commission_sale_amount = [float(key['CommSaleAmt']) for key in transaction_data['ITEM_MV']]
    transaction_sale_total = 0
    commission_sales_total = 0
    discount_conversion = ''
    unconverted_discount_amount = 0
    discount_amount_list = transaction_file.readv(transaction_data['_ID'], 45).to_list()[0]
    discount_conversion_list = transaction_file.readv(transaction_data['_ID'], 167).to_list()
    if len(discount_conversion_list) != 0:
        discount_conversion_list = discount_conversion_list[0]
    xmul = transaction_xmul_value(transaction_data)
    quantity_list = [int(key['MKUP.STORE.QTY']) for key in transaction_data['MKUP.STORE.QTY_MV']]
    retail_list = [float(key['RETAIL']) for key in transaction_data['ITEM_MV']]
    mkdn_list = [float(key['MRKDN']) for key in transaction_data['ITEM_MV']]
    for i in range(desc_length):
        if rental_id_list[i] != '':
            discount_type = [int(key['DISCOUNT.TYPE']) for key in transaction_data['DISCOUNT.TYPE_MV']]
            discount_amount = [float(value) for value in discount_amount_list[i]]
            discount_sum = sum(discount_amount)
            if discount_sum != 0:
                for j in range(len(discount_amount)):
                    if discount_amount[j] > 0:
                        discount_conversion = discount_conversion_list[j]
                        break
                if discount_conversion != '':
                    unconverted_discount_amount = 0
                else:
                    unconverted_discount_amount = discount_sum
        else:
            unconverted_discount_amount = 0
        qty = quantity_list[i]
        total = (retail_list[i] - mkdn_list[i]) * qty
        total = total - unconverted_discount_amount
        transaction_sale_total = transaction_sale_total + total
        qty = qty * xmul
        commission_sales_total = commission_sales_total + (commission_sale_amount[i] * qty)
    return commission_sales_total


def calculate_sale_percentage(commission_employee_id, employee_file):
    employee_id = commission_employee_id[0]
    try:
        employee_record = list(employee_file.readv(employee_id, 17))
    except u2py.U2Error:
        employee_record = employee_id
    return employee_record


def calculate_commission_employee_type(employee_type):
    employee_type = employee_type.split("*")[2]
    return employee_type


@app.route('/commission/<transId>', methods=['GET'])
def commission_list(transId):
    commission_data_list = []
    transaction_file_name = 'TRANSACTION'
    employee_file_name = 'EM'
    transFile = u2py.File(transaction_file_name)
    employee_file = u2py.File(employee_file_name)
    command_line = "LIST TRANSACTION WITH @ID = '{}' COMMISSION.TYPE ITEM.NO RETAIL LIST.PRICE TRAN.TYPE TRAN.SUB.TYPE MRKDN MKUP.STORE.QTY DESC CommSaleAmt CommEmplId CommEmplType CommRate CommEmplPercentUsed RESERVATIONS RECEIVED.ASN DISCOUNT.TYPE TOJSON".format(
        transId)
    transaction_data = json.loads(u2py.run(command_line, capture=True))['TRANSACTION'][0]
    description = [key['DESC'] for key in transaction_data['ITEM_MV']]
    if transaction_data['ITEM_MV'][0]['CommEmplId'] != '':
        amount_list = calculate_amount(transaction_data)
        empsn_list = set_empsn_values(transaction_data, employee_file)
        employee_total = set_employee_total(transaction_data, transFile, len(description))
        commission_amount = calculate_commission_amount(transaction_data)
        commissionRate = [key['CommRate'] for key in transaction_data['ITEM_MV']]
        commissionEmpType = [key['CommEmplType'] for key in transaction_data['ITEM_MV']]
        for i in range(len(description)):
            commission_data = {}
            commission_data['class'] = transaction_data['ITEM_MV'][i]['ITEM.NO'][0:4]
            commission_data['sku'] = transaction_data['ITEM_MV'][i]['ITEM.NO'][4:9]
            commission_data['retail'] = transaction_data['ITEM_MV'][i]['RETAIL']
            commission_data['mkdn'] = transaction_data['ITEM_MV'][i]['MRKDN']
            commission_data['quantity'] = transaction_data['MKUP.STORE.QTY_MV'][i]['MKUP.STORE.QTY']
            commission_data['desc'] = description[i]
            commission_data['commissionType'] = transaction_data['ITEM_MV'][i]['COMMISSION.TYPE']
            commission_data['amount'] = amount_list[i]
            commission_data['employeePercentage'] = convert_field_formats(commissionRate[i], 'MD2', 'internal')
            commission_data['salePercentage'] = transaction_data['ITEM_MV'][i]['CommEmplPercentUsed']
            commission_data['commEmpId'] = empsn_list[i]
            commission_data['employeeCommissionType'] = calculate_commission_employee_type(commissionEmpType[i])
            commission_data_list.append(commission_data)
        response = {
            'commissionList': commission_data_list,
            'retailAmount': employee_total,
            'commissionAmount': commission_amount
        }
    else:
        response = {"error": "No commission information for this transaction Id"}
    return Response(json.dumps(response), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
