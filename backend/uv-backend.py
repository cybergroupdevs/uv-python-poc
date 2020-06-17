import logging
from flask import Flask
from flask import request,jsonify,Response
from flask import make_response
from functools import wraps
import u2py
import pdb
import json
from datetime import datetime
from flask_cors import CORS, cross_origin

import logging

logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s %(message)s')

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(formatter)

file_handler = logging.FileHandler('./logs/api.log')
file_handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(file_handler)
logger.addHandler(console_handler)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesercretkey'
CORS(app)

#############################################################
###################### Helper Methods #######################
#############################################################

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


def set_employee_shortname(transaction_data, employee_file):
    emp_shortname_list = []
    commission_employee_id = [key['CommEmplId'] for key in transaction_data['ITEM_MV']]
    for i in range(len(commission_employee_id)):
        employee_id = commission_employee_id[i]
        if check_existing_record('EM', employee_id):
            emp_shortname = list(employee_file.readv(employee_id, 17))[0][0]
        else:
            emp_shortname = employee_id
        emp_shortname_list.append(emp_shortname)

    return emp_shortname_list


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

#############################################################
###################### Customer API #########################
#############################################################

@app.route('/customer', methods=['GET'])
def customer_details():
    customer_id=request.args.get('customerId')
    customer_file= u2py.File("CUSTOMERS")
    error={}
    cmd=f"LIST PHONE.NO F.NAME L.NAME ADDRESS CITY ZIP.CODE PHONE.LONG PFID DATA {customer_id} CUSTOMERS TOJSON"
    details=u2py.Command(cmd).run(capture=True)
    if "not found."in details:
        error["msg"]=f"{customer_id}, not found"
        return Response(
            json.dumps(error),
            status=404,
            mimetype='application/json')
    else:
        details=json.loads(details)
        del details['CUSTOMERS'][0]["_ID"]
        values=details['CUSTOMERS'][0].values()
        keys=["phoneNo","firstName","lastName","address","city","zipCode","altPhoneNo","pfid"]
        customer_dict={key: value for key, value in zip(keys, values)}
        return Response(
    	    json.dumps(customer_dict),
    	    status=200,
    	    mimetype='application/json')
      
#############################################################
###################### Consultant API #######################
#############################################################

@app.route('/consultant',methods=['GET'])
def consultant_details():
    transaction_id=request.args.get('transactionId')
    transaction_file=u2py.File("TRANSACTION")
    transaction_cmd=f"LIST PHONE CommEmplId CommEmplType FITTER DATA {transaction_id} TRANSACTION TOJSON"
    transaction_details=u2py.Command(transaction_cmd).run(capture=True)
    transaction_details=json.loads(transaction_details)
    phone_no=transaction_details['TRANSACTION'][0]["PHONE"]
    em_file=u2py.File("EM")
    details={}
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
    return Response(
		json.dumps(details),
		status=200,
		mimetype="application/json"
		)
    
#############################################################
################# Customer history API ######################
#############################################################

@app.route('/customer/history',methods=['GET'])
def customer_history():
	saved_list_name="PAGE.LIST"
	start =1
	phone_no=request.args.get('phoneNo')
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
	response = {'customerHistory':data,'count':total_count}
	return Response(
		json.dumps(response),
		status=200,
		mimetype='application/json')

#############################################################
#################### Commission API #########################
#############################################################

@app.route('/commission/<transaction_id>', methods=['GET'])
def commission_list(transaction_id):
    commission_data_list = []
    transaction_file_name = 'TRANSACTION'
    employee_file_name = 'EM'
    transaction_file = u2py.File(transaction_file_name)
    employee_file = u2py.File(employee_file_name)
    command_line = f"LIST TRANSACTION WITH @ID = '{transaction_id}' COMMISSION.TYPE ITEM.NO RETAIL LIST.PRICE TRAN.TYPE TRAN.SUB.TYPE MRKDN MKUP.STORE.QTY DESC CommSaleAmt CommEmplId CommEmplType CommRate CommEmplPercentUsed RESERVATIONS RECEIVED.ASN DISCOUNT.TYPE TOJSON"
    transaction_data = json.loads(u2py.run(command_line, capture=True))['TRANSACTION'][0]

    if transaction_data['ITEM_MV'][0]['CommEmplId'] != '':
        amount_list = calculate_amount(transaction_data)
        emp_shortname_list = set_employee_shortname(transaction_data, employee_file)
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
            commission_data['employeeShortname'] = emp_shortname_list[i]
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

#############################################################
################### Credit Card API #########################
#############################################################

@app.route('/transaction/<transactionId>/creditCard/authentication')
def credit_card_details(transactionId):
    card_details = []
    transaction_file = u2py.File('TRANSACTION')
    command_line = f"LIST TRANSACTION WITH @ID = '{transactionId}' TIME.OUT TRAN.DATE APPROVAL.TIME TIME.IN TRY.POINTER TIME.DONE ATTEMPT.TYPE ATTEMPT.AMT ACCT.METHOD AUTH.METHOD TOJSON"
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

#############################################################
###################### Order API ############################
#############################################################

@app.route('/transaction/<transactionId>/order', methods=['GET'])
def order_detail(transactionId):
    transaction_id = transactionId
    status = check_existing_record('TRANSACTION', transaction_id)
    if (status):
        transaction_file = u2py.File("TRANSACTION")
        order_detail = {}
        cmd = f"LIST TRANSACTION WITH @ID = '{transaction_id}' ECOM.ORDER.ID SHIP.DATE SHIP.FNAME SHIP.LNAME SHIP.METHOD SHIP.ADDR SHIP.CARRIER SHIP.CITY SHIP.BOLNUMBER SHIP.TRACK.NO AUDIT.FLAG GEN.COUPON.ID RETURN.TRANS ERCPT.EMAIL TOJSON"
        details = u2py.Command(cmd).run(capture=True)
        details = json.loads(details)
        order_id = details['TRANSACTION'][0]['ECOM.ORDER.ID']
        if (order_id):
            order_detail['orderNo'] = order_id
            order_detail['shipDate'] = details['TRANSACTION'][0]['SHIP.DATE']
            ship_to_first_name = details['TRANSACTION'][0]['SHIP.FNAME_MV'][0]['SHIP.FNAME']
            ship_to_last_name = details['TRANSACTION'][0]['SHIP.LNAME_MV'][0]['SHIP.LNAME']
            order_detail['shipTo'] = ship_to_first_name+" "+ship_to_last_name
            order_detail['method'] = details['TRANSACTION'][0]['SHIPGROUP_MV'][0]['SHIP.METHOD']
            order_detail['shipToAddress'] = details['TRANSACTION'][0]['SHIP.ADDR_MV'][0]['SHIP.ADDR']
            order_detail['carrier'] = details['TRANSACTION'][0]['ITEM_MV'][0]['SHIP.CARRIER']
            order_detail['csz'] = details['TRANSACTION'][0]['SHIP.CITY_MV'][0]['SHIP.CITY']
            order_detail['traceNo'] = details['TRANSACTION'][0]['ITEM_MV'][0]['SHIP.TRACK.NO']
            ship_bol_number = details['TRANSACTION'][0]['SHIP.BOLNUMBER']
            audit_flag = ''
            if (ship_bol_number):
                for x in range(0, 1):
                    if(details['TRANSACTION'][x]['SHIP.BOLNUMBER']):
                        order_detail['commentLabel'] = (
                            details['TRANSACTION'][x]['SHIP.BOLNUMBER'])
            void_reason = details['TRANSACTION'][0]['SHIP.ADDR_MV'][0]['SHIP.ADDR']
            if(void_reason):
                if('AUDIT.FLAG' in details['TRANSACTION'][0].keys()):
                    audit_flag = details['TRANSACTION'][x]['AUDIT.FLAG']
                    audit_flag = 'AUDIT FLAG: '+audit_flag
                    return_count = details['TRANSACTION'][0]['RETURN.TRANS_MV'][0]['RETURN.TRANS']
                    if (audit_flag.count("Return ") > 1 or audit_flag.count("XCHG ") > 1):
                        audit_flag = "RETURN REASON: "+str(audit_flag)
                    else:
                        audit_flag = 'VOID REASON: '+audit_flag
            coupons = details['TRANSACTION'][0]['GEN.COUPON.ID_MV'][0]['GEN.COUPON.ID']
            if(coupons):
                order_detail['coupons'] = 'GENERATED COUPON(S): '+coupons
            if('AUDIT.FLAG' in details['TRANSACTION'][0].keys() and details['TRANSACTION'][0]['AUDIT.FLAG']):
                order_detail['auditFlag'] = 'AUDIT FLAG: '+audit_flag
                return_count = details['TRANSACTION'][0]['RETURN.TRANS_MV'][0]['RETURN.TRANS']
                for i in range(len(return_count)):
                    order_detail['returnIds'] = details['TRANSACTION'][0]['SHIP.ADDR_MV'][x]['SHIP.ADDR']
            if('ERCPT.EMAIL' in details['TRANSACTION'][0].keys()):
                email = details['TRANSACTION'][0]['ERCPT.EMAIL']
                order_detail['email'] = 'ERCPT TO: '+email
            response = {
                "orderDetail": order_detail,
            }
            return Response(
                json.dumps(response),
                status=200,
                mimetype='application/json'
            )
        else:
            msg = 'Order number not found'
            data = {
                'msg': msg
            }
            return Response(
                json.dumps(data),
                status=404,
                mimetype='application/json'
            )
    else:
        msg = 'Transaction file not found'
        data = {
            'msg': msg
        }
        return Response(
            json.dumps(data),
            status=404,
            mimetype='application/json'
        )
        
#############################################################
###################### Discount API #########################
#############################################################

@app.route('/transaction/<transactionId>/discount', methods=['GET'])
def discount_detail(transactionId):
    transaction_id = transactionId
    status = check_existing_record('TRANSACTION', transaction_id)
    if(status):
        cmd = f"LIST TRANSACTION WITH @ID = '{transaction_id}' RESERVATIONS DISCOUNT.TYPE RETAIL COUPON.CODE DISCOUNT.POD.TYPE DISCOUNT.POD.AMT DISCOUNT.EMPLOYEE.ID DISCOUNT.REASON.CODE DISCOUNT.REASON.TEXT PROMOS.ID IN.ADDITION.TO.MRKDN DISC.CNV.MRKDN ADVERT.CODE CORP.ACCT.NO LINE.DISCOUNT QUANTITY LONG.MRKDN TAX.AMT TOJSON"
        details = u2py.Command(cmd).run(capture=True)
        details = json.loads(details)
        count = (len((details['TRANSACTION'][0]['DISCOUNT.TYPE_MV'][0]['DISCOUNT.TYPE'])))
        saved_list_name = "PAGE.LIST"
        u2py.run('SAVE.LIST {}'.format(saved_list_name))
        my_list = u2py.List(0, saved_list_name)
        t_id = my_list.readlist()
        total_count = t_id.dcount(u2py.FM)
        pct = ''
        sub_total = ''
        discount_details = {}
        coupon_code = details['TRANSACTION'][0]['COUPON.CODE_MV'][0]['COUPON.CODE']
        disc_type = int(details['TRANSACTION'][0]['DISCOUNT.TYPE_MV'][0]['DISCOUNT.TYPE'])
        pod_type = details['TRANSACTION'][0]['DISCOUNT.POD.TYPE_MV'][0]['DISCOUNT.POD.TYPE']
        pod_amt = details['TRANSACTION'][0]['DISCOUNT.POD.AMT_MV'][0]['DISCOUNT.POD.AMT']
        emp_id = details['TRANSACTION'][0]['DISCOUNT.EMPLOYEE.ID_MV'][0]['DISCOUNT.EMPLOYEE.ID']
        other_sub_type = details['TRANSACTION'][0]['DISCOUNT.REASON.CODE_MV'][0]['DISCOUNT.REASON.CODE']
        other_comments = details['TRANSACTION'][0]['DISCOUNT.REASON.TEXT_MV'][0]['DISCOUNT.REASON.TEXT']
        promos_id = details['TRANSACTION'][0]['PROMOS.ID_MV'][0]['PROMOS.ID']
        in_add_to_mkdn = details['TRANSACTION'][0]['IN.ADDITION.TO.MRKDN_MV'][0]['IN.ADDITION.TO.MRKDN']
        disc_conv_to_mkdn = details['TRANSACTION'][0]['DISC.CNV.MRKDN_MV'][0]['DISC.CNV.MRKDN']
        advert_code = details['TRANSACTION'][0]['ADVERT.CODE_MV'][0]['ADVERT.CODE']
        corp_id = details['TRANSACTION'][0]['CORP.ACCT.NO_MV'][0]['CORP.ACCT.NO']
        scr_discount = 0
        discount = 0
        for y in range(0,1):
            scr_discount = scr_discount+(int(details['TRANSACTION'][0]['ITEM_MV'][y]['RESERVATIONS'])*float(details['TRANSACTION'][y]['ITEM_MV'][count]['LINE.DISCOUNT']))
            discount = discount+float(details['TRANSACTION'][y]['ITEM_MV'][0]['QUANTITY'])*float(details['TRANSACTION'][y]['ITEM_MV'][count]['LINE.DISCOUNT'])
        employee_cmd = f"LIST EM WITH @ID = '{emp_id}' SHORTNAME TOJSON"
        employee_details = u2py.Command(cmd).run(capture=True)
        employee_details = json.loads(employee_details)
        if(disc_type == 1):
            pct = 'Employee'
            EM_file = u2py.File("EM")
            s_name = employee_details['EM'][0]['ITEMS_MV'][0]['SHORTNAME']
            if(s_name):
                pct = pct+s_name
        elif(disc_type == 2):
            pct = 'Family'
            s_name = employee_details['EM'][0]['ITEMS_MV'][0]['SHORTNAME']
            if(s_name):
                pct = pct+'of '+s_name
        elif(disc_type == 3):
            pct = 'Other'
            if(other_sub_type == 1):
                pct = pct+' (mall associate)'
            elif(other_sub_type == 2):
                pct = pct+' (CLERGY)'
            elif(other_sub_type == 3):
                pct = pct+' (police)'
            elif(other_sub_type == 4):
                pct = pct+' (SHOES)'
            elif(other_sub_type == 98):
                pct = pct+' (CUSTOMER SERVICE)'
            elif(other_sub_type == 99):
                pct = pct+' (OTHER)'
            else:
                pct = pct+' (?)'
        elif(disc_type == 5):
            pct = 'Advertising [code '+advert_code+']'
        elif(disc_type == 6):
            pct = 'Customer Appreciation'
        elif(disc_type == 7):
            pct = 'Store relocation'
        elif(disc_type == 8):
            pct = 'Corporate'
            pct = pct+' (ID '+corp_id+')'
        elif(disc_type == 9):
            pct = 'Affiliate employee'
            kg_em_cmd = f"LIST KG.EM WITH @ID = '{emp_id}' LNAME FNAME COMPANY.CODE TOJSON"
            kg_em_details = u2py.Command(kg_em_cmd).run(capture=True)
            kg_em_details = json.loads(kg_em_details)
            pct = kg_em_details["KG.EM"]["0"]["COMPANY.CODE"]+' employee'
            pct = pct + \
                ' ('+kg_em_details["KG.EM"]["0"]["FNAME"] + \
                ' '+kg_em_details["KG.EM"]["0"]["LNAME"]+')'
        elif(disc_type == 10):
            pct = 'Affiliate employee family'
            pct = kg_em_details["KG.EM"]["0"]["COMPANY.CODE"] + \
                ' employee family'
            pct = pct + \
                ' (of '+kg_em_details["KG.EM"]["0"]["FNAME"] + \
                ' '+kg_em_details["KG.EM"]["0"]["LNAME"]+')'
        elif(disc_type == 11):
            pct = 'Coupon [id '+coupon_code+']'
        elif(disc_type == 12):
            pct = 'Perfect Fit signup'
        elif(disc_type == 13):
            pct = ' "PROMO"'
            pct = pct+' ('+promos_id+')'
            if(other_sub_type == 1):
                pct = pct+' (automatically applied)'
            elif(other_sub_type == 2):
                pct = pct+' (required a coupon)'
            else:
                pct = pct+' (?)'
        elif(disc_type == 14):
            pct = "N-FOR"
            pct = pct+' ('+promos_id+')'
        else:
            pct = 'NO'
        sale_total = discount
        data = str(pct)+' discount of '+str(scr_discount*100)
        if (disc_conv_to_mkdn):
            data = data+' converted to markdown.'
        else:
            data = data+'.'
        items_mv=len(details['TRANSACTION'][0]['ITEM_MV'])
        for i in range(0,items_mv):
                retail=float(details['TRANSACTION'][0]['ITEM_MV'][count]['RETAIL'])
                mrkdn=float(details['TRANSACTION'][0]['ITEM_MV'][count]['LONG.MRKDN'])
                quantity=int(details['TRANSACTION'][0]['ITEM_MV'][count]['QUANTITY'])
                sale_total=sale_total+(retail-mrkdn)*quantity
        sale_total=sale_total+float(details['TRANSACTION'][0]["TAX.AMT"])
        sale_total=sale_total-discount
        discount_details['pct'] = pct
        discount_details['subTotal'] = sale_total
        response = {
            "discountDetails": discount_details
        }
        return Response(
            json.dumps(response),
            status=200,
            mimetype='application/json')
    else:
        msg = 'Transaction file not found'
        data = {
            'msg': msg
        }
        return Response(
            json.dumps(data),
            status=404,
            mimetype='application/json'
        )

#############################################################
####################### Refund API ##########################
#############################################################

@app.route('/transaction/<transactionId>/refund', methods=['GET'])
def refund_detail(transactionId):
    transaction_id = transactionId
    status = check_existing_record('TRANSACTION', transaction_id)
    if(status):
        data_file = u2py.File("TRANSACTION")
        cmd = f"LIST TRANSACTION WITH @ID = '{transaction_id}' LIKE.TENDER.OVERRIDE.MGR.ID HAND.TKT.NO TOJSON"
        details = u2py.Command(cmd).run(capture=True)
        details = json.loads(details)
        refund_mgr_id = details['TRANSACTION'][0]['LIKE.TENDER.OVERRIDE.MGR.ID']
        em_cmd= f"LIST EM WITH @ID = '{refund_mgr_id}' NICKNAME FNAME LNAME SHORTNAME TOJSON"
        em_details=u2py.Command(em_cmd).run(capture=True)
        em_details=json.loads(em_details)
        if(refund_mgr_id):
            if("NICKNAME" in em_details['EM'][0].keys()):
                refund_mgr_name = em_details['EM'][0]['NICKNAME']
            else:
                refund_mgr_name = em_details['EM'][0]['FNAME']	
        refund_mgr_name = f"{refund_mgr_name} {em_details['EM'][0]['LNAME']} ({em_details['EM'][0]['SHORTNAME']})"
        refund_data = {}
        refund_data['refundMgrName'] =  refund_mgr_name
        ticket_number = details['TRANSACTION'][0]['HAND.TKT.NO']
        if(ticket_number):
            refund_data['ticketNumber'] = details['TRANSACTION'][0]['HAND.TKT.NO']
        response = {
            "refundData": refund_data
        }
        return Response(
            json.dumps(response),
            status=200,
            mimetype='application/json')
    else:
        msg = 'Transaction file not found'
        data = {
            'msg': msg
        }
        return Response(
            json.dumps(data),
            status=404,
            mimetype='application/json'
        )


#############################################################
###################### Transaction API ######################
#############################################################

@app.route('/transaction/<transactionId>', methods=['GET'])
def transaction_detail(transactionId):
    transaction_id = transactionId
    transaction_details_list = []
    status = check_existing_record('TRANSACTION', transaction_id)
    if status:
        transaction={}
        cmd= f"LIST TRANSACTION WITH @ID = '{transaction_id}' DESC ALT.PHONE ITEM.NO RETAIL PHONE TRAN.DATE MRKDN TRANSFER.CARTONS QUANTITY LONG.MRKDN TUX.RENTAL.AMT TUX.INSURANCE.AMT TUX.RUSH.AMT TUX.MARKDOWN.AMT RESERVATIONS MKDN.AUDIT ITEM.SHIP.GROUP RETURN.QTY SHIP.GROUP CommEmplId TRAN.TYPE TOJSON"
        details=u2py.Command(cmd).run(capture=True)
        details=json.loads(details)
        transaction['transactionId'] = transaction_id
        transaction['phoneNo'] = details['TRANSACTION'][0]['PHONE']
        transaction['date'] = details['TRANSACTION'][0]['TRAN.DATE']
        if 'TRAN.TYPE' in details['TRANSACTION'][0].keys():
            transaction['transactionType'] = details['TRANSACTION'][0]['TRAN.TYPE']
        if 'TRANSFER.CARTONS' in details['TRANSACTION'][0].keys():
            transaction['rentalNo'] = details['TRANSACTION'][0]['TRANSFER.CARTONS']
        comm_empl_id = details['TRANSACTION'][0]['ITEM_MV'][0]['CommEmplId']
        em_cmd= f"LIST EM WITH @ID = '{comm_empl_id}' NICKNAME FNAME LNAME TOJSON"
        em_details=u2py.Command(em_cmd).run(capture=True)
        em_details=json.loads(em_details)
        if 'NICKNAME' in em_details['EM'][0].keys():
            operator = em_details['EM'][0]['NICKNAME']
        else:
            operator = em_details['EM'][0]['FNAME']
        operator = operator + ' '+ em_details['EM'][0]['LNAME']
        transaction['operator'] = operator
        if 'NICKNAME' in em_details['EM'][0].keys():
            tux_consult = em_details['EM'][0]['NICKNAME']
        else:
            tux_consult = em_details['EM'][0]['FNAME']
        tux_consult = tux_consult + ' '+ em_details['EM'][0]['LNAME']
        if len(tux_consult)<5:
            tux_consult = 'UNKNOWN'
        transaction['tuxConsult'] = tux_consult
        # alt_phone_number is the RELATING FIELD BETWEEN CUSTOMER AND TRANSACTION
        alt_phone_number = details['TRANSACTION'][0]['ALT.PHONE']
        transaction['alternatePhone'] = alt_phone_number
        customer_cmd="LIST CUSTOMERS WITH @ID = {} PHONE.NO FNAME LNAME PFID TOJSON".format(alt_phone_number)
        customer_details=u2py.Command(customer_cmd).run(capture=True)
        customer_details=json.loads(customer_details)
        transaction['phone'] = customer_details['CUSTOMERS'][0]['PHONE.NO']
        transaction['name'] = customer_details['CUSTOMERS'][0]['FNAME'] +' '+ customer_details['CUSTOMERS'][0]['LNAME']
        transaction['pfid'] = customer_details['CUSTOMERS'][0]['PFID']
        tux_consult = em_details['EM'][0]
        n_lines = len(details['TRANSACTION'][0]['ITEM_MV'])
        for x in range(0, n_lines):
            transaction_details = {}
            item_no = details['TRANSACTION'][0]['ITEM_MV'][x]['ITEM.NO']
            transaction_details['class'] = item_no[0:4]
            transaction_details['sku'] = item_no[4:8]
            transaction_mkdn = details['TRANSACTION'][0]['ITEM_MV'][x]['LONG.MRKDN']
            if transaction_mkdn != 0 or transaction_mkdn != '':
                legend_description = ''
                mkdn_flag = details['TRANSACTION'][0]['ITEM_MV'][0]['MKDN.AUDIT']
                if mkdn_flag == 'M':
                    print_mkdn_legend = 1
                    legend_description = 'Manual markdown'
                elif mkdn_flag == 1:
                    mkdn_flag = 'M'
                    print_mkdn_legend = 1
                    legend_description = 'Manual markdown'
                elif mkdn_flag == 'D':
                    print_mkdn_legend = 1
                    legend_description = 'Damaged markdown'
                elif mkdn_flag == 'P':
                    print_mkdn_legend = 1
                    legend_description = 'Price Adjustment markdown '
                elif mkdn_flag == 'A':
                    print_mkdn_legend = 1
                    legend_description = 'Alteration Adjustment markdown'
                elif mkdn_flag == 'C':
                    print_mkdn_legend = 1
                    legend_description = 'Customer Service markdown'
                else:
                    mkdn_flag = ' '
                if legend_description != '':
                    transaction_mkdn = mkdn_flag
                transaction_details['mkdn'] = transaction_mkdn
            else:
                transaction_details['mkdn'] = ''
            transaction_details['desc'] = details['TRANSACTION'][0]['ITEM_MV'][x]['DESC']
            rental_id = details['TRANSACTION'][0]['ITEM_MV'][x]['RESERVATIONS']
            if rental_id != '':
                tux_rental_amount = details['TRANSACTION'][0]['ITEM_MV'][x]['TUX.RENTAL.AMT']
                tux_insurance_amount = details['TRANSACTION'][0]['ITEM_MV'][x]['TUX.INSURANCE.AMT']
                tux_rush_amount = details['TRANSACTION'][0]['ITEM_MV'][x]['TUX.RUSH.AMT']
                tux_markdown_amount = details['TRANSACTION'][0]['ITEM_MV'][x]['TUX.MARKDOWN.AMT']
                rental = '(Rental {} for {},{} ins,{} rush'.format(rental_id,tux_rental_amount,tux_insurance_amount,tux_rush_amount)
                if tux_markdown_amount != '':
                    rental = rental + ', {} mkdn)'.format(tux_markdown_amount)
            else:
                rental = ''
            transaction_details['rental'] = rental
            transaction_details_list.append(transaction_details)
        response = {
            "transactionDetails": transaction_details_list,
            "customerDetails": transaction
        }
        return Response(
            json.dumps(response),
            status=200,
            mimetype='application/json'
        )
    else:
        response = { 'error': 'No transaction existed'}
        return Response(
            json.dumps(response),
            status=404,
            mimetype='application/json'
        )

if __name__ == '__main__':
    app.run()
