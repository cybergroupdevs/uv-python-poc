from flask import Flask
import pdb
from flask import request,jsonify,Response
from flask import make_response
from functools import wraps
import u2py
import json
from datetime import datetime
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesercretkey'
CORS(app)
########################
#### HELPER METHODS ####
########################
def key_exists(detail,data):
	if(detail in data.keys()):
		return True
	else:
		return False
def check_existing_record(file_name, record_id):
    file_object = u2py.File(file_name)
    try:
        record_object = file_object.read(record_id)
        return True
    except u2py.U2Error as e:
        return False
def map_customer_history(first_name,last_name,address,city,pfid):
	customer={}
	customer["firstName"]=first_name
	customer["lastName"]=last_name
	customer["address"]=address
	customer["city"]=city
	if pfid!="":
		customer["pf"]="pf"
	else:
		customer["pf"]=""
	return customer

def convert_field_formats(field_data, field_format, format):
    data = u2py.DynArray()
    data.insert(1, 0, 0, field_data)
    if format == 'external':
        formatted_data = str(data.extract(1).oconv(field_format))
    else:
        formatted_data = str(data.extract(1).iconv(field_format))
    return formatted_data

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
    employee_id = [key['CommEmplId'] for key in transaction_data['ITEM_MV']]
    commission_sale_amount = [float(key['CommSaleAmt']) for key in transaction_data['ITEM_MV']]
    quantity_list = [int(key['MKUP.STORE.QTY']) for key in transaction_data['MKUP.STORE.QTY_MV']]
    for i in range(len(employee_id)):
        quantity = xmul * quantity_list[i]
        commission_amount = commission_amount + commission_sale_amount[i] * quantity
    return commission_amount


def set_empsn_values(transaction_data, employee_file):
    empsn_list = []
    commission_employee_id = [key['CommEmplId'] for key in transaction_data['ITEM_MV']]
    for i in range(len(commission_employee_id)):
        employee_id = commission_employee_id[i]
        if check_existing_record(employee_file, employee_id):
            empsn = list(employee_file.readv(employee_id, 17))[0][0]
        else:
            empsn = employee_id
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

def transaction_credit_details(transaction_data, pmt_val):
    credit_details = {}
    pmt_val = int(pmt_val) - 1
    times_out = [key['TIME.OUT'] for key in transaction_data['PAY_MV']][pmt_val]
    times_in = [key['TIME.IN'] for key in transaction_data['PAY_MV']][pmt_val]
    times_done = [key['TIME.DONE'] for key in transaction_data['PAY_MV']][pmt_val]
    attempt_types = [key['ATTEMPT.TYPE'] for key in transaction_data['PAY_MV']][pmt_val]
    acc_methods = [key['ACCT.METHOD'] for key in transaction_data['PAY_MV']][pmt_val]
    auth_methods = [key['AUTH.METHOD'] for key in transaction_data['PAY_MV']][pmt_val]
    credit_details['sent'] = times_out
    credit_details['rcvd'] = times_in
    credit_details['done'] = times_done
    credit_details['type'] = attempt_types
    entry_mode = acc_methods[0]

    approval_time = [key['APPROVAL.TIME'] for key in transaction_data['PAY_MV']][pmt_val]
    transaction_date_int = transaction_data['TRAN.DATE']
    if approval_time != '':
        entry_mode = 'RENTR'
    elif entry_mode == '90':
        entry_mode = 'SWIPE'
    elif entry_mode == '91' and transaction_date_int == '18629':
        entry_mode = 'CLESS'
    elif entry_mode == '91':
        entry_mode = 'SWIPE'
    elif entry_mode == '02':
        entry_mode = 'SWIPE'
    elif entry_mode == '00':
        entry_mode = 'HAND'
    elif entry_mode == '01':
        entry_mode = 'HAND'
    elif entry_mode == 'MANUALLY [48]':
        entry_mode = 'HAND'
    elif entry_mode == 'SWIPED [49]':
        entry_mode = 'SWIPE'
    else:
        entry_mode = "????"
    credit_details['entry'] = entry_mode

    if auth_methods == 'D':
        auth_methods = 'CALL CENTER'
    elif auth_methods == 'E':
        auth_methods = 'TIMEOUT'
    else:
        auth_methods = 'AUTO APPROVED'
    credit_details['auth'] = auth_methods

    return credit_details

########################
#### CUSTOMER API   ####
########################
@app.route('/api/customer', methods=['GET'])
def customer_details():
    customer_id=request.args.get('customerId')
    customer_file= u2py.File("CUSTOMERS")
    data=[]
    error={}
    cmd=f"LIST PHONE.NO F.NAME L.NAME ADDRESS CITY ZIP.CODE PHONE.LONG PFID DATA {customer_id} CUSTOMERS TOJSON"
    details=u2py.Command(cmd).run(capture=True)
    if "not found."in details:
        error["msg"]=f"{customer_id}, not found"
        data.append(error)
        return Response(
            json.dumps(data),
            status=404,
            mimetype='application/json')
    else:
        details=json.loads(details)
        del details['CUSTOMERS'][0]["_ID"]
        values=details['CUSTOMERS'][0].values()
        keys=["phoneNo","firstName","lastName","address","city","zipCode","altPhoneNo","pfid"]
        customer_dict={key: value for key, value in zip(keys, values)}
        data.append(customer_dict)
        return Response(
    	    json.dumps(data),
    	    status=200,
    	    mimetype='application/json')
########################
#### CONSULTANT API ####
########################
@app.route('/api/consultant',methods=['GET'])
def consultant_details():
    transaction_id=request.args.get('transactionId')
    transaction_file=u2py.File("TRANSACTION")
    transaction_cmd=f"LIST TRANS.NO PHONE CommEmplId CommEmplType FITTER DATA {transaction_id} TRANSACTION TOJSON"
    transaction_details=u2py.Command(transaction_cmd).run(capture=True)
    transaction_details=json.loads(transaction_details)
    trans_no=transaction_details['TRANSACTION'][0]["TRANS.NO"]
    phone_no=transaction_details['TRANSACTION'][0]["PHONE"]
    em_file=u2py.File("EM")
    details={}
    data=[]
    consultant_cmd=f"LIST FNAME LNAME SHORTNAME NICKNAME DATA {phone_no} EM TOJSON"
    consultant_details=u2py.Command(consultant_cmd).run(capture=True)
    consultant_details=json.loads(consultant_details)
    if(("NICKNAME",consultant_details['EM'][0])==True):
        business_name=consultant_details['EM'][0]["NICKNAME"]
    else:
        business_name=""
    first_name=consultant_details['EM'][0]["FNAME"]
    last_name=consultant_details['EM'][0]["LNAME"]
    short_name=consultant_details['EM'][0]["SHORTNAME"]
        ####checks the businessName if present it replaces the firstname
    if(business_name!=''):
        operator=str(business_name)
    else:
        operator=str(first_name)
    operator=operator+" "+str(last_name)
    if(len(operator)+len(short_name)<23):
        operator=operator+" ("+str(short_name)+")"
    details["operator"]=operator
	####they only want length till 23(used for extra precaution)
    operator=str(operator[0:23])
    if(key_exists('CommEmplType',transaction_details['TRANSACTION'][0]["ITEM_MV"][0])):
        employee_type=transaction_details['TRANSACTION'][0]["ITEM_MV"][0]['CommEmplType']
    else:
        employee_type=''
    if employee_type =='':
        employee_type="SLS CONSULT"
    else:
        employee_type=employee_type.split("*")
        employee_type=str(employee_type[2])
    if(key_exists('CommEmplId',transaction_details['TRANSACTION'][0]["ITEM_MV"][0])):
        employee_id=transaction_details['TRANSACTION'][0]["ITEM_MV"][0]['CommEmplId']
    else:
        employee_id=""
    if(check_existing_record("EM",employee_id)):
	####sets name to Noconsultant if record not found
        employee_cmd=f"LIST FNAME LNAME SHORTNAME DATA {employee_id} EM TOJSON"
        employee_details=u2py.Command(employee_cmd).run(capture=True)
        employee_details=json.loads(employee_details)
        employee_first_name=employee_details['EM'][0]["FNAME"]
        employee_last_name=employee_details['EM'][0]["LNAME"]
        employee_short_name=employee_details['EM'][0]["SHORTNAME"]
        details[employee_type]=f"{employee_first_name} {employee_last_name} ({employee_short_name})"
    else:
        details[employee_type]="No consultant"
        ####add name from em file where recordId is we get from record<248> of transaction
    if(key_exists("FITTER",transaction_details['TRANSACTION'][0])):
        fitter_id=transaction_details['TRANSACTION'][0]["FITTER"]
        if(fitter_id!=""):
            fitter_cmd=f"LIST FNAME LNAME SHORTNAME DATA {fitter_id} EM TOJSON"
            fitter_details=u2py.Command(fitter_cmd).run(capture=True)
            fitter_details=json.loads(fitter_details)
            fitter_first_name=fitter_details['EM'][0]["FNAME"]
            fitter_last_name=fitter_details['EM'][0]["LNAME"]
            fitter_short_name=fitter_details['EM'][0]["SHORTNAME"]
            fitter_name=f"{fitter_first_name} {fitter_last_name} ({fitter_short_name})"
            details["SRC ASSOC"]=fitter_name
        else:
            fitter_name=fitter_id
	####only adds if there is a fitterId(doubt why they set its value null if not sending
    data.append(details)
    return Response(
		json.dumps(data),
		status=200,
		mimetype="application/json"
		)
@app.route('/api/customer/history',methods=['GET'])
def customer_history():
	saved_list_name="PAGE.LIST"
	start =1
	phone_no=int(request.args.get('phoneNo'))
	page_index =int(request.args.get('pageIndex'))
	page_size =int(request.args.get('pageSize'))
	start = page_index * page_size + 1
	end = (page_index + 1) * page_size
	command_line = f'SELECT CUSTOMERS WITH PHONE.LONG = {phone_no}'
	u2py.run(command_line, capture=True)
	u2py.run(f'SAVE.LIST {saved_list_name}')
	data_file=u2py.File("CUSTOMERS")
	my_list=u2py.List(0, saved_list_name)
	t_id = my_list.readlist()
	total_count = t_id.dcount(u2py.FM)
	data=[]
	if(total_count==0):
		data.append("No customer History available")
	else:
		for x in range(start, end + 1):
			if x > total_count:
				break
			ids=t_id.extract(x)
			cmd=f"LIST F.NAME L.NAME ADDRESS CITY PFID DATA {ids} CUSTOMERS TOJSON"
			customer_details=u2py.Command(cmd).run(capture=True)
			customer_details=json.loads(customer_details)
			first_name=customer_details['CUSTOMERS'][0]['F.NAME']
			last_name=customer_details['CUSTOMERS'][0]['L.NAME']
			address=customer_details['CUSTOMERS'][0]['ADDRESS']
			city=customer_details['CUSTOMERS'][0]['CITY']
			if("PFID" in customer_details['CUSTOMERS'][0] and customer_details['CUSTOMERS'][0]['PFID']!=""):
				pfid=customer_details['CUSTOMERS'][0]['PFID']
			else:
				pfid=""
			customer_history=map_customer_history(first_name,last_name,address,city,pfid)
			data.append(customer_history)
			
	return Response(
		json.dumps(data),
		status=200,
		mimetype='application/json')

########################
#### COMMISSION API ####
########################
@app.route('/commission/<transId>', methods=['GET'])
def commission_list(transId):
    commission_data_list = []
    transaction_file_name = 'TRANSACTION'
    employee_file_name = 'EM'
    transaction_file = u2py.File(transaction_file_name)
    employee_file = u2py.File(employee_file_name)
    command_line = "LIST TRANSACTION WITH @ID = '{}' COMMISSION.TYPE ITEM.NO RETAIL LIST.PRICE TRAN.TYPE TRAN.SUB.TYPE MRKDN MKUP.STORE.QTY DESC CommSaleAmt CommEmplId CommEmplType CommRate CommEmplPercentUsed RESERVATIONS RECEIVED.ASN DISCOUNT.TYPE TOJSON".format(
        transId)
    transaction_data = json.loads(u2py.run(command_line, capture=True))['TRANSACTION'][0]

    if transaction_data['ITEM_MV'][0]['CommEmplId'] != '':
        amount_list = calculate_amount(transaction_data)
        empsn_list = set_empsn_values(transaction_data, employee_file)
        description = [key['DESC'] for key in transaction_data['ITEM_MV']]
        employee_total = set_employee_total(transaction_data, transaction_file, len(description))
        commission_amount = calculate_commission_amount(transaction_data)
        commission_rate = [key['CommRate'] for key in transaction_data['ITEM_MV']]
        commission_employee_type = [key['CommEmplType'] for key in transaction_data['ITEM_MV']]
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
            commission_data['employeePercentage'] = convert_field_formats(commission_rate[i], 'MD2', 'internal')
            commission_data['salePercentage'] = transaction_data['ITEM_MV'][i]['CommEmplPercentUsed']
            commission_data['commEmpId'] = empsn_list[i]
            commission_data['employeeCommissionType'] = calculate_commission_employee_type(commission_employee_type[i])
            commission_data_list.append(commission_data)
        response = {
            'commissionList': commission_data_list,
            'retailAmount': employee_total,
            'commissionAmount': commission_amount
        }
    else:
        response = {"error": "No commission information for this transaction Id"}
    return Response(json.dumps(response), status=200, mimetype='application/json')

#########################
#### CREDIT CARD API ####
#########################
@app.route('/transaction/<transactionId>/creditCard/authentication')
def credit_card_details(transactionId):
    card_details = []
    transaction_file = u2py.File('TRANSACTION')
    command_line = "LIST TRANSACTION WITH @ID = '{}' TIME.OUT TRAN.DATE APPROVAL.TIME TIME.IN TRY.POINTER TIME.DONE ATTEMPT.TYPE ATTEMPT.AMT ACCT.METHOD AUTH.METHOD TOJSON".format(
        transactionId)
    transaction_data = json.loads(u2py.run(command_line, capture=True))['TRANSACTION'][0]
    try_pointer = [int(key['TRY.POINTER']) for key in transaction_data['PAY_MV']]
    attempts_to_print = [key['TIME.DONE'] for key in transaction_data['PAY_MV']]
    transaction_type = transaction_file.readv(transactionId, 15)
    type_count = transaction_type.dcount(u2py.VM)
    for i in range(1, type_count + 1):
        pmt_val = try_pointer[i - 1]
        if pmt_val != '':
            attempts_to_print[i - 1] = '*'
            data = transaction_credit_details(transaction_data, pmt_val)
            card_details.append(data)
    pmt_count = transaction_file.readv(transactionId, 68).dcount(u2py.VM)
    for i in range(pmt_count):
        attempts = attempts_to_print[i - 1]
        if attempts != '*':
            pmt_val = i
            data = transaction_credit_details(transaction_data, pmt_val)
            card_details.append(data)
    response = {
        'cardDetails': card_details
    }
    return Response(json.dumps(response), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
