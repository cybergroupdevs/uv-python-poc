from flask import Flask
from flask import request,jsonify,Response
from flask import make_response
from functools import wraps
import u2py
import pdb
import json
from datetime import datetime
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
def order_get(transactionId):
    transaction_id=transactionId
    pdb.set_trace()
    status = check_existing_record('TRANSACTION',transaction_id )
    if (status):
        transaction_file = u2py.File("TRANSACTION")
        order_detail={}
        cmd="LIST ECOM.ORDER.ID SHIP.DATE SHIP.FNAME SHIP.LNAME SHIP.METHOD SHIP.ADDR SHIP.CARRIER SHIP.CITY SHIP.BOLNUMBER SHIP.TRACK.NO AUDIT.FLAG GEN.COUPON.ID RETURN.TRANS ERCPT.EMAIL DATA {} TRANSACTION TOJSON".format(transaction_id)
        details=u2py.Command(cmd).run(capture=True)
        details=json.loads(details)
        order_id=details['TRANSACTION'][0]['ECOM.ORDER.ID']
        if (order_id):
            order_detail['orderNo']= order_id   
            order_detail['shipDate']=details['TRANSACTION'][0]['SHIP.DATE']
            ship_to_first_name=details['TRANSACTION'][0]['SHIP.FNAME_MV'][0]['SHIP.FNAME']
            ship_to_last_name=details['TRANSACTION'][0]['SHIP.LNAME_MV'][0]['SHIP.LNAME']
            order_detail['shipToCustomerName']=ship_to_first_name+" "+ship_to_last_name
            order_detail['method']=details['TRANSACTION'][0]['SHIPGROUP_MV'][0]['SHIP.METHOD']
            order_detail['shipToAddress']=details['TRANSACTION'][0]['SHIP.ADDR_MV'][0]['SHIP.ADDR']
            order_detail['carrier']=details['TRANSACTION'][0]['ITEM_MV'][0]['SHIP.CARRIER']
            order_detail['csz']=details['TRANSACTION'][0]['SHIP.CITY_MV'][0]['SHIP.CITY']
            order_detail['traceNo']=details['TRANSACTION'][0]['ITEM_MV'][0]['SHIP.TRACK.NO']
            ship_bol_number=details['TRANSACTION'][0]['SHIP.BOLNUMBER']
            audit_flag=''
            if (ship_bol_number):
                for x in range(0,1):
                    if(details['TRANSACTION'][x]['SHIP.BOLNUMBER']):     
                        order_detail['commentLabel']=(details['TRANSACTION'][x]['SHIP.BOLNUMBER'])
            void_reason=details['TRANSACTION'][0]['SHIP.ADDR_MV'][0]['SHIP.ADDR']
            if(void_reason):
                if('AUDIT.FLAG' in details['TRANSACTION'][0].keys()):
                    audit_flag=details['TRANSACTION'][x]['AUDIT.FLAG']
                    audit_flag='AUDIT FLAG: '+audit_flag
                    return_count=details['TRANSACTION'][0]['RETURN.TRANS_MV'][0]['RETURN.TRANS']
                    if (audit_flag.count("Return ")>1 or audit_flag.count("XCHG ")>1):
                        audit_flag="RETURN REASON: "+str(audit_flag)
                    else:
                        audit_flag='VOID REASON: '+audit_flag
            coupons=details['TRANSACTION'][0]['GEN.COUPON.ID_MV'][0]['GEN.COUPON.ID']
            if(coupons):
                order_detail['coupons']='GENERATED COUPON(S): '+coupons
            if('AUDIT.FLAG' in details['TRANSACTION'][0].keys()and details['TRANSACTION'][0]['AUDIT.FLAG']):
                order_detail['auditFlag']='AUDIT FLAG: '+audit_flag
                return_count=details['TRANSACTION'][0]['RETURN.TRANS_MV'][0]['RETURN.TRANS']
                for i in range(len(return_count)):
                    order_detail['returnIds']=details['TRANSACTION'][0]['SHIP.ADDR_MV'][x]['SHIP.ADDR']
            if('ERCPT.EMAIL' in details['TRANSACTION'][0].keys()):
            	email=details['TRANSACTION'][0]['ERCPT.EMAIL']
            	order_detail['email']='ERCPT TO: '+email
            response={
                "orderDetail": order_detail,
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
###################### Helper Methods #######################
#############################################################

def check_existing_record(filename, recordID):
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



