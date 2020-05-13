from flask import Flask
import pdb
from flask import request,jsonify,Response
from flask import make_response
from functools import wraps
import u2py
import xmltodict
import pprint
import json
import random
import jwt
from datetime import datetime
from collections import OrderedDict
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesercretkey'
CORS(app)
########################
#### HELPER METHODS ####
########################
def checkExistingRecord(filename, recordID):
    fileObject = u2py.File(filename)
    try:
        recordObject = fileObject.read(recordID)
        return True
    except u2py.U2Error as e:
        return False
########################
#### CUSTOMER API   ####
########################
@app.route('/api/customer', methods=['GET'])
def customerDetails():
	customerId="0001"
	customerFile=orderFile = u2py.File("CUSTOMERS")
	#cmd=u2py.Command("LIST PHONE.NO F.NAME L.NAME ADDRESS CITY ZIP.CODE PHONE.LONG PFID DATA CUSTOMERS TOJSON").run(capture=True)
	#cmd = cmd[1:-1]
	data=[]
	customerDetails={}
	customerDetails['phoneNo']=list(customerFile.readv(customerId,1))[0][0]
	customerDetails['firstName']=list(customerFile.readv(customerId,2))[0][0]
	customerDetails['lastName']=list(customerFile.readv(customerId,3))[0][0]
	customerDetails['address']=list(customerFile.readv(customerId,4))[0][0]
	customerDetails['city']=list(customerFile.readv(customerId,5))[0][0]
	customerDetails['state']=list(customerFile.readv(customerId,6))[0][0]
	customerDetails['zip']=list(customerFile.readv(customerId,7))[0][0]
	customerDetails['altPhoneNo']=list(customerFile.readv(customerId,12))[0][0]
	customerDetails['pfid']=list(customerFile.readv(customerId,33))[0][0]
	data.append(customerDetails)
	return Response(
	json.dumps(data),
	status=200,
	mimetype='application/json')
########################
#### CONSULTANT API ####
########################
@app.route('/api/consultant',methods=['GET'])
def consultantDetials():
	#pdb.set_trace()
	transactionId="999888"
	transactionFile=u2py.File("TRANSACTION")
	transNo=list(transactionFile.readv(transactionId,1))[0][0]
	phoneNo=list(transactionFile.readv(transactionId,2))[0][0]
	emFile=u2py.File("EM")
	consultantDetails={}
	data=[]
	businessName=list(emFile.readv(phoneNo,27))[0][0]
	firstName=list(emFile.readv(phoneNo,2))[0][0]
	lastName=list(emFile.readv(phoneNo,1))[0][0]	
	shortName=list(emFile.readv(phoneNo,17))[0][0]
        ####checks the businessName if present it replaces the firstname
	if(businessName!=''):
		operator=str(businessName)
	else:
		operator=str(firstName)
	operator=operator+" "+str(lastName)
	if(len(operator)+len(shortName)<23):
		operator=operator+" ("+str(shortName)+")"
	consultantDetails["operator"]=operator
	####they only want length till 23(used for extra precaution)
	operator=str(operator[0:23])
	tempType=list(transactionFile.readv(transactionId,246))[0][0]
	if tempType =='':
		tempType="SLS CONSULT"
	else:
		tempType=tempType.split("*")
		tempType=str(tempType[2])
	employeeId=list(transactionFile.readv(transactionId,244))[0][0]
	if(checkExistingRecord("EM",employeeId)==True):
	####sets name to Noconsultant if record not found
		emFirstName=list(emFile.readv(employeeId,2))[0][0]
		emLastName=list(emFile.readv(employeeId,1))[0][0]
		emShortName=list(emFile.readv(employeeId,17))[0][0]
		consultantDetails[tempType]=str(emFirstName)+" "+str(emLastName)+" ("+str(emShortName)+")"
	else:
		consultantDetails[tempType]="No consultant"
	fitterId=list(transactionFile.readv(transactionId,248))[0][0]
        ####add name from em file where recordId is we get from record<248> of transaction
	if(fitterId!=""):
		fitterFirstName=list(emFile.readv(fitterId,2))[0][0]
		fitterLastName=list(emFile.readv(fitterId,1))[0][0]
		fitterShortName=list(emFile.readv(fitterId,17))[0][0]
		fitterName=str(fitterFirstName)+" "+str(fitterLastName)+" ("+str(fitterShortName)+")"
	else:
		fitterName=fitterId
	if(fitterId!=""):
	####only adds if there is a fitterId(doubt why they set its value null)
		consultantDetails["SRC ASSOC"]=fitterName
	data.append(consultantDetails)
	return Response(
		json.dumps(data),
		status=200,
		mimetype="application/json"
		)
if __name__ == '__main__':
    app.run()

