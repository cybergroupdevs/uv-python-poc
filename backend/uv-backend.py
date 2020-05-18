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
def check_existing_record(file_name, record_id):
    file_object = u2py.File(file_name)
    try:
        record_object = file_object.read(record_id)
        return True
    except u2py.U2Error as e:
        return False
def mapping_customer(first_name,last_name,address,city,pfid):
	details={}
	details["firstName"]=first_name
	details["lastName"]=last_name
	details["address"]=address
	details["city"]=city
	if pfid!="":
		details["pf"]="pf"
	else:
		details["pf"]=""
	return details
########################
#### CUSTOMER API   ####
########################
@app.route('/api/customer', methods=['GET'])
def customer_details():
	customer_id=request.args.get('customerId')
	customer_file= u2py.File("CUSTOMERS")
	data=[]
	cmd="LIST PHONE.NO F.NAME L.NAME ADDRESS CITY ZIP.CODE PHONE.LONG PFID DATA {} CUSTOMERS TOJSON".format(customer_id)
	details=u2py.Command(cmd).run(capture=True)
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
	pdb.set_trace()
	transaction_id=request.args.get('transactionId')
	transaction_file=u2py.File("TRANSACTION")
	trans_no=list(transaction_file.readv(transaction_id,1))[0][0]
	phone_no=list(transaction_file.readv(transaction_id,2))[0][0]
	em_file=u2py.File("EM")
	consultant_details={}
	data=[]
	consultant_cmd="LIST FNAME LNAME SHORTNAME NICKNAME DATA {} EM TOJSON".format(phone_no)
	details=u2py.Command(consultant_cmd).run(capture=True)
	details=json.loads(details)
	business_name=details['EM'][0]["NICKNAME"]
	first_name=details['EM'][0]["FNAME"]
	last_name=details['EM'][0]["LNAME"]
	short_name=details['EM'][0]["SHORTNAME"]
        ####checks the businessName if present it replaces the firstname
	if(business_name!=''):
		operator=str(business_name)
	else:
		operator=str(first_name)
	operator=operator+" "+str(last_name)
	if(len(operator)+len(short_name)<23):
		operator=operator+" ("+str(short_name)+")"
	consultant_details["operator"]=operator
	####they only want length till 23(used for extra precaution)
	operator=str(operator[0:23])
	temp_type=list(transaction_file.readv(transaction_id,246))[0][0]
	if temp_type =='':
		temp_type="SLS CONSULT"
	else:
		temp_type=temp_type.split("*")
		temp_type=str(temp_type[2])
	employee_id=list(transaction_file.readv(transaction_id,244))[0][0]
	if(check_existing_record("EM",employee_id)==True):
	####sets name to Noconsultant if record not found
		em_cmd="LIST FNAME LNAME SHORTNAME DATA {} EM TOJSON".format(employee_id)
		em_details=u2py.Command(em_cmd).run(capture=True)
		em_details=json.loads(em_details)
		em_first_name=em_details['EM'][0]["FNAME"]
		em_last_name=em_details['EM'][0]["LNAME"]
		em_short_name=em_details['EM'][0]["SHORTNAME"]
		consultant_details[temp_type]=str(em_first_name)+" "+str(em_last_name)+" ("+str(em_short_name)+")"
	else:
		consultant_details[tempType]="No consultant"
	fitter_id=list(transaction_file.readv(transaction_id,248))[0][0]
        ####add name from em file where recordId is we get from record<248> of transaction
	if(fitter_id!=""):
		fitter_cmd="LIST FNAME LNAME SHORTNAME DATA {} EM TOJSON".format(fitter_id)
		fitter_details=u2py.Command(fitter_cmd).run(capture=True)
		fitter_details=json.loads(fitter_details)
		fitter_first_name=fitter_details['EM'][0]["FNAME"]
		fitter_last_name=fitter_details['EM'][0]["LNAME"]
		fitter_short_name=fitter_details['EM'][0]["SHORTNAME"]
		fitter_name=str(fitter_first_name)+" "+str(fitter_last_name)+" ("+str(fitter_short_name)+")"
	else:
		fitter_name=fitter_id
	if(fitter_id!=""):
	####only adds if there is a fitterId(doubt why they set its value null if not sending)
		consultant_details["SRC ASSOC"]=fitter_name
	data.append(consultant_details)
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
	commandLine = 'SELECT {} WITH PHONE.LONG = {}'.format('CUSTOMERS',phone_no)
	u2py.run(commandLine, capture=True)
	u2py.run('SAVE.LIST {}'.format(saved_list_name))
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
			cmd="LIST F.NAME L.NAME ADDRESS CITY PFID DATA {} CUSTOMERS TOJSON".format(ids)
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
			customer_history=mapping_customer(first_name,last_name,address,city,pfid)
			data.append(customer_history)
			
	return Response(
		json.dumps(data),
		status=200,
		mimetype='application/json')
