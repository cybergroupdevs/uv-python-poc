from flask import Flask
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

#############################################################
###################### Order API ############################
#############################################################

@app.route('/api/order/<transactionId>', methods=['GET'])
def orderGet(transactionId):
    status = checkExistingRecord('TRANSACTION',transactionId )
    if (status):
        transactionFile = u2py.File("TRANSACTION")
        orderDetails={}
        orderId=(list(transactionFile.readv(transactionId, 58))[0][0])
        if (orderId):
            orderDetails['orderNo']=orderId
            orderDetails['shipDate']=(convertDateFormat(list(transactionFile.readv(transactionId, 57))[0][0], 'external'))
            shipToFirstName=(list(transactionFile.readv(transactionId, 51))[0][0])
            shipToLastName=(list(transactionFile.readv(transactionId, 52))[0][0])
            orderDetails['shipTo']=shipToFirstName+" "+shipToLastName
            orderDetails['method']=(list(transactionFile.readv(transactionId, 46))[0][0])
            orderDetails['shipToAddress']=(list(transactionFile.readv(transactionId, 53))[0][0])
            orderDetails['carrier']=(list(transactionFile.readv(transactionId, 104))[0][0])
            orderDetails['csz']=(list(transactionFile.readv(transactionId, 54))[0][0])
            orderDetails['traceNo']=(list(transactionFile.readv(transactionId, 105))[0][0])
            shipBolNumber=(list(transactionFile.readv(transactionId, 49))[0][0])
            auditFlag=''
            if (shipBolNumber):
                for x in range(1,3)
                    if((list(transactionFile.readv(transactionId,49))[x][0])):     
                        orderDetails['commentLabel']=(list(transactionFile.readv(transactionId,49))[x][0])
            voidReason=(list(transactionFile.readv(transactionId, 31))[0][0])
            if(voidReason):
                auditFlagRecord=(list(transactionFile.readv(transactionId, 21))[0][0])
                if (auditFlagRecord.count("Return ")>1 or auditFlagRecord.count("XCHG ")>1):
                    auditFlag="RETURN REASON: "+str(auditFlag)
                else:
                    auditFlag='VOID REASON: '+auditFlag
            coupons=(list(transactionFile.readv(transactionId, 158))[0][0])
            if(coupons):
                orderDetails['coupons']='GENERATED COUPON(S): '+coupons
            if((list(transactionFile.readv(transactionId, 21))[0][0])):
                orderDetails['auditFlag']='AUDIT FLAG: '+auditFlag
                returnCount=(list(transactionFile.readv(transactionId, 33)[0][0]))
                for i in range(len(returnCount)):
                    orderDetails['returnIds']=(list(transactionFile.readv(transactionId,33))[i][0])
            email=(list(transactionFile.readv(transactionId,219))[0][0])
            orderDetails['email']='ERCPT TO: '+email
            response={
                "orderDetails": orderDetails,
                    }
            return Response(
                json.dumps(response),
                status=200,
                mimetype='application/json'
                
            )
        else:
            msg='Order number not found'
            data={
                 'msg':msg        
                 }
            return Response(
                json.dumps(data),
                status=404,
                mimetype='application/json'
            )
    else:
        msg ='Transaction file not found'
        data={
             'msg':msg
             }
        return Response(
            json.dumps(data),
            status=404,
            mimetype='application/json'
        )

#############################################################
###################### Discount API #########################
#############################################################
        
@app.route('/api/transaction/discount/<transactionId>', methods=['GET'])
def discount(transactionId):
    status = checkExistingRecord('TRANSACTION',transactionId )
    if(status):
        dataFile = u2py.File("TRANSACTION")
        if((list(dataFile.readv(transactionId,90)) <> ''))
            # NULL?
        elif(presaleDetail <> 'Y'):
            count=(count(list(dataFile.readv(transactionId, 159))[0][0]))
            savedList_name="PAGE.LIST"
            u2py.run('SAVE.LIST {}'.format(savedList_name))
            myList=u2py.List(0, savedList_name)
	        t_id = myList.readlist()
	        totalCount = t_id.dcount(u2py.FM)
            pct=''
            subTotal=''        
            discountDetails={}    
            for x in range(1,totalCount)
                ids=t_id.extract(x)
                couponCode=list(dataFile.readv(ids, 128))[0][0]
                discType=list(dataFile.readv(ids, 159))[0][0]
                podType=list(dataFile.readv(ids, 160))[0][0]
                podAmt=list(dataFile.readv(ids, 161))[0][0]
                emplId=list(dataFile.readv(ids, 162))[0][0]
                otherSubType=list(dataFile.readv(ids, 163))[0][0]
                otherComments=list(dataFile.readv(ids, 164))[0][0]
                promosId=list(dataFile.readv(ids, 165))[0][0]
                inAddToMkdn=list(dataFile.readv(ids, 166))[0][0]
                discConvToMkdn=list(dataFile.readv(ids, 167))[0][0]
                advertCode=list(dataFile.readv(ids, 168))[0][0]
                corpId=list(dataFile.readv(ids, 169))[0][0]
                scrDiscount=0
                discount=0
                for y in range(1,nLines)
                    scrDiscount=scrDiscount+(list(dataFile.readv(ids, 13))[y][0])*(list(dataFile.readv(ids, 45))[y][x])
                    if ((list(dataFile.readv(ids, 167))[0][x]) == 1):
                        continue
                    discount=discount+(list(dataFile.readv(ids, 13))[y][0])*(list(dataFile.readv(ids, 45))[y][x])
                if(discType==1):
                    pct='Employee'
                    emFile= u2py.File("EM")
                    sName=list(emFile.readv(emplId,17)[0][0])
                    if(sName):
                        pct=pct+sName
                elif(discType==2):
                    pct='Family'
                    sName=list(emFile.readv(emplId,17)[0][0])
                    if(sName):
                        pct=pct+'of '+sName
                elif(discType==3):
                    pct='Other'
                    if(otherSubType==1):
                        pct=pct+' (mall associate)'
                    elif(otherSubType==2):
                        pct=pct+' (CLERGY)'
                    elif(otherSubType==3):
                        pct=pct+' (police)'
                    elif(otherSubType==4):
                        pct=pct+' (SHOES)'
                    elif(otherSubType==98):
                        pct=pct+' (CUSTOMER SERVICE)'
                    elif(otherSubType==99):
                        pct=pct+' (OTHER)'
                    else:
                        pct=pct+' (?)'
                elif(discType==5):
                    pct='Advertising [code '+advertCode+']'
                elif(discType==6):
                    pct='Customer Appreciation'
                elif(discType==7):
                    pct='Store relocation'
                elif(discType==8):
                    pct='Corporate'
                    pct=pct+' (ID '+corpId+')'
                elif(discType==9):
                    pct='Affiliate employee'
                    kgEmFile = u2py.File("KG.EM")
                    if(kgEmFile):
                    pct=(list(kgEmFile.readv(emplId,5))[0][0])+' employee'
                    pct=pct+' ('+(list(kgEmFile.readv(emplId,2))[1][1])+' '+(list(kgEmFile.readv(emplId,1))[0][0])+')'
                elif(discType==10):
                    pct='Affiliate employee family'
                    pct=(list(kgEmFile.readv(emplId,5))[0][0])+' employee family'
                    pct=pct+' (of '+(list(kgEmFile.readv(emplId,2))[1][1])+' '+(list(kgEmFile.readv(emplId,1))[0][0])+')'
                elif(discType==11):
                    pct='Coupon [id '+couponCode+']'
                elif(discType==12):
                    pct='Perfect Fit signup'
                elif(discType==13):
                    pct=' "PROMO"'
                    pct=pct+' ('+promosId+')'
                    if(otherSubType==1):
                        pct=pct+' (automatically applied)'
                    elif(otherSubType==2):
                        pct=pct+' (required a coupon)'
                    else:
                        pct=pct+' (?)'
                elif(discType==14):
                    pct="N-FOR"
                    pct=pct+' ('+promosId+')'
                else:
                    pct='NO'
                saleTot=saleTot-discount
                data=pct+' discount of '+(scrDiscount*100) #OCONV missing
                if (discConvToMkdn):
                    data=data+' converted to markdown.'
                else:
                    data=data+'.'
            if((list(dataFile.readv(ids, 159))[0][0])<>0):
                subTotal=convert(saleTot,external)
            discountDetails['pct']=pct
            discountDetails['subTotal']=subTotal
            response={
                "discountDetails": discountDetails
                    }
            return Response(
                json.dumps(response),
                status=200,
                mimetype='application/json'
    else:
        msg ='Transaction file not found'
        data={
             'msg':msg
             }
        return Response(
            json.dumps(data),
            status=404,
            mimetype='application/json'
        )

#############################################################
###################### Helper Methods #######################
#############################################################

def checkExistingRecord(filename, recordID):
    fileObject = u2py.File(filename)
    try:
        recordObject = fileObject.read(recordID)
        return True
    except u2py.U2Error as e:
        return False


def convertDateFormat(orderDate,format):
    date = u2py.DynArray()
    date.insert(1, 0, 0, orderDate)
    if format == 'internal':
        formattedDate = date.extract(1).iconv('D-')
    else:
        formattedDate = str(date.extract(1).oconv('D-'))
    return formattedDate


if __name__ == '__main__':
    app.run()

