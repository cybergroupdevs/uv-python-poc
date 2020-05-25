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
        order_id=details['TRANSACTION'][0]['ECOM.ORDER.ID']     ## for single value
        if (order_id):
            order_detail['orderNo']= order_id   
            order_detail['shipDate']=details['TRANSACTION'][0]['SHIP.DATE']
            ship_to_first_name=details['TRANSACTION'][0]['SHIP.FNAME_MV'][0]['SHIP.FNAME']
            ship_to_last_name=details['TRANSACTION'][0]['SHIP.LNAME_MV'][0]['SHIP.LNAME']
            order_detail['shipTo']=ship_to_first_name+" "+ship_to_last_name
            order_detail['method']=details['TRANSACTION'][0]['SHIPGROUP_MV'][0]['SHIP.METHOD']
            order_detail['shipToAddress']=details['TRANSACTION'][0]['SHIP.ADDR_MV'][0]['SHIP.ADDR'] ## for multivalue
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
                    audit_flag_record=details['TRANSACTION'][x]['AUDIT.FLAG']
                    order_detail['auditFlag']='AUDIT FLAG: '+audit_flag
                    return_count=details['TRANSACTION'][0]['RETURN.TRANS_MV'][0]['RETURN.TRANS']
                    if (audit_flag_record.count("Return ")>1 or audit_flag_record.count("XCHG ")>1):
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
###################### Discount API #########################
#############################################################
        
@app.route('/api/transaction/discount/<transactionId>', methods=['GET'])
def discount(transactionId):
    transaction_id= transactionId
    status = check_existing_record('TRANSACTION',transaction_id )
    if(status):
        #data_file = u2py.File("TRANSACTION")
        cmd="LIST DATA RESERVATIONS DISCOUNT.TYPE ".format()
        details=u2py.Command(cmd).run(capture=True)
        details=json.loads(details)
        if(presale_detail != 'Y'):
            count=(count((details['TRANSACTION'][0]['DISCOUNT.TYPE_MV'][0]['DISCOUNT.TYPE']))
            saved_list_name="PAGE.LIST"
            u2py.run('SAVE.LIST {}'.format(saved_list_name))
            my_list=u2py.List(0, saved_list_name)
            t_id = my_list.readlist()
            total_count = t_id.dcount(u2py.FM)
            pct=''
            sub_total=''        
            discount_details={}    
            for x in range(1,total_count):
                ids=t_id.extract(x)
                coupon_code=details['TRANSACTION'][0]['COUPON.CODE_MV'][0]['COUPON.CODE']
                disc_type=details['TRANSACTION'][0]['DISCOUNT.TYPE_MV'][0]['DISCOUNT.TYPE']
                pod_type=details['TRANSACTION'][0]['DISCOUNT.POD.TYPE_MV'][0]['DISCOUNT.POD.TYPE']
                pod_amt=details['TRANSACTION'][0]['DISCOUNT.POD.AMT_MV'][0]['DISCOUNT.POD.AMT']
                emp_id=details['TRANSACTION'][0]['DISCOUNT.EMPLOYEE.ID_MV'][0]['DISCOUNT.EMPLOYEE.ID']
                other_sub_type=details['TRANSACTION'][0]['DISCOUNT.REASON.CODE_MV'][0]['DISCOUNT.REASON.CODE']
                other_comments=details['TRANSACTION'][0]['DISCOUNT.REASON.TEXT_MV'][0]['DISCOUNT.REASON.TEXT']
                promos_id=details['TRANSACTION'][0]['PROMOS.ID_MV'][0]['PROMOS.ID']
                in_add_to_mkdn=details['TRANSACTION'][0]['IN.ADDITION.TO.MRKDN_MV'][0]['IN.ADDITION.TO.MRKDN']
                disc_conv_to_mkdn=details['TRANSACTION'][0]['ITEMS_MV'][0]['DISC.CNV.MRKDN']
                advert_code=details['TRANSACTION'][0]['ADVERT.CODE_MV'][0]['ADVERT.CODE']
                corp_id=details['TRANSACTION'][0]['CORP.ACCT.NO_MV'][0]['CORP.ACCT.NO']
                scr_discount=0
                discount=0
                for y in range(1,n_lines):
                    scr_discount=scr_discount+((details['TRANSACTION'][0]['ITEMS_MV'][y]['RESERVATIONS'])*((details['TRANSACTION'][y]['ITEMS_MV'][x]['LINE.DISCOUNT'])
                        continue
                    discount=discount+(details['TRANSACTION'][y]['ITEMS_MV'][0]['QUANTITY'])*(details['TRANSACTION'][y]['ITEMS_MV'][x]['LINE.DISCOUNT'])
                if(disc_type==1):
                    pct='Employee'
                    EM_file= u2py.File("EM")
                    s_name=details['EM'][0]['ITEMS_MV'][0]['SHORTNAME']
                    if(s_name):
                        pct=pct+s_name
                elif(disc_type==2):
                    pct='Family'
                    s_name=details['EM'][0]['ITEMS_MV'][0]['SHORTNAME']
                    if(s_name):
                        pct=pct+'of '+s_name
                elif(disc_type==3):
                    pct='Other'
                    if(other_sub_type==1):
                        pct=pct+' (mall associate)'
                    elif(other_sub_type==2):
                        pct=pct+' (CLERGY)'
                    elif(other_sub_type==3):
                        pct=pct+' (police)'
                    elif(other_sub_type==4):
                        pct=pct+' (SHOES)'
                    elif(other_sub_type==98):
                        pct=pct+' (CUSTOMER SERVICE)'
                    elif(other_sub_type==99):
                        pct=pct+' (OTHER)'
                    else:
                        pct=pct+' (?)'
                elif(disc_type==5):
                    pct='Advertising [code '+advert_code+']'
                elif(disc_type==6):
                    pct='Customer Appreciation'
                elif(disc_type==7):
                    pct='Store relocation'
                elif(disc_type==8):
                    pct='Corporate'
                    pct=pct+' (ID '+corp_id+')'
                elif(disc_type==9):
                    pct='Affiliate employee'
                    KG_EM_file = u2py.File("KG.EM")
                    if(KG_EM_file):
                        pct=(list(KG_EM_file.readv(emp_id,5))[0][0])+' employee'
                        pct=pct+' ('+(list(KG_EM_file.readv(emp_id,2))[1][1])+' '+(list(KG_EM_file.readv(emp_id,1))[0][0])+')'
                elif(disc_type==10):
                    pct='Affiliate employee family'
                    pct=(list(KG_EM_file.readv(emp_id,5))[0][0])+' employee family'
                    pct=pct+' (of '+(list(KG_EM_file.readv(emp_id,2))[1][1])+' '+(list(KG_EM_file.readv(emp_id,1))[0][0])+')'
                elif(disc_type==11):
                    pct='Coupon [id '+coupon_code+']'
                elif(disc_type==12):
                    pct='Perfect Fit signup'
                elif(disc_type==13):
                    pct=' "PROMO"'
                    pct=pct+' ('+promos_id+')'
                    if(other_sub_type==1):
                        pct=pct+' (automatically applied)'
                    elif(other_sub_type==2):
                        pct=pct+' (required a coupon)'
                    else:
                        pct=pct+' (?)'
                elif(disc_type==14):
                    pct="N-FOR"
                    pct=pct+' ('+promos_id+')'
                else:
                    pct='NO'
                sale_total=sale_total-discount
                data=pct+' discount of '+(scr_discount*100) 
                if (disc_conv_to_mkdn):
                    data=data+' converted to markdown.'
                else:
                    data=data+'.'
            if(details['TRANSACTION'][0]['DISCOUNT.TYPE_MV'][0]['DISCOUNT.TYPE']!=0):
                sub_total=convert(sale_total,external)
            discount_details['pct']=pct
            discount_details['subTotal']=sub_total
            response={
                "discountDetails": discount_details
                    }
            return Response(
                json.dumps(response),
                status=200,
                mimetype='application/json')
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
####################### Refund API ##########################
#############################################################

@app.route('/api/transaction/refund/<transaction_id>', methods=['GET'])
def refund(transactionId):
    transaction_id=transactionId
    status = check_existing_record('TRANSACTION',transaction_id )
    if(status):
        data_file = u2py.File("TRANSACTION")
        cmd="LIST DATA  ".format()
	    details=u2py.Command(cmd).run(capture=True)
	    details=json.loads(details)
        refund_mgr_id=details['TRANSACTION'][0]['LIKE.TENDER.OVERRIDE.MGR.ID']
        if(refund_mgr_id):
            EM_file = u2py.File("EM")
            EM_record = (list(EM_file.readv(refund_mgr_id))[0][0])  #
        else:
            EM_record = ''
        if(details['EM'][0]['NICKNAME']):
            refund_mgr_name = details['EM'][0]['NICKNAME']
        else:
            refund_mgr_name = details['EM'][0]['FNAME']
        refund_mgr_name = refund_mgr_name + ' '+(details['EM'][0]['LNAME'])+' ('+(details['EM'][0]['SHORTNAME'])+')'
        refund_data={}
        refund_data['refundMgrName']='MGR OVERRIDING SUGGESTED REFUND TYPE: '+ refund_mgr_name
        ticket_number = details['TRANSACTION'][0]['HAND.TKT.NO']
        if(ticket_number):
            refund_data['ticketNumber'] = 'HANDWRITTEN TICKET NUMBER: '+details['TRANSACTION'][0]['HAND.TKT.NO']
        response={
            "refundData": refund_data
                }
        return Response(
            json.dumps(response),
            status=200,
            mimetype='application/json') 
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
###################### Transaction API ######################
#############################################################

@app.route('/api/transaction/<transactionId>', methods=['GET'])
def transactionGet(transactionId):
    transaction_id=transactionId
    status = check_existing_record('TRANSACTION',transaction_id )
    if(status):
        data_file = u2py.File("TRANSACTION")
        transaction_details={}
        display_comm_flag=0
        cmd="LIST DATA RESERVATIONS D.TYPE ".format()
	    details=u2py.Command(cmd).run(capture=True)
	    details=json.loads(details)
        unconverted_disc_amount=0
        total_accumulated_line=0
        for x in range(1,n_lines):
            old_display_comm_flag=display_comm_flag
            backup_flag=0
            if(presale_detail != 'Y'):
                transaction_class = details['TRANSACTION'][0]['ITEMS_MV'][0]['ITEM.NO']#TODO
                transaction_ssku = details['TRANSACTION'][0]['ITEMS_MV'][x]['ITEM.NO']
                transaction_mkdn= details['TRANSACTION'][0]['ITEMS_MV'][x]['MRKDN.LONG']
                if(transaction_mkdn!= 0 or transaction_mkdn!= ''):
                    legend_desciption = ''
                    mkdn_flag = details['TRANSACTION'][0]['ITEMS_MV'][0]['MKDN.AUDIT']
                    if(mkdn_flag == 'M'):
                        print_mkdn_legend = 1
                        legend_desciption = 'Manual markdown'
                    elif(mkdn_flag == 1):
                        mkdn_flag = 'M'
                        print_mkdn_legend = 1
                        legend_desciption = 'Manual markdown'
                    elif(mkdn_flag == 'D'):
                        print_mkdn_legend = 1
                        legend_desciption = 'Damaged markdown'
                    elif(mkdn_flag == 'P'):
                        print_mkdn_legend = 1
                        legend_desciption = 'Price Adjustment markdown '
                    elif(mkdn_flag == 'A'):
                        print_mkdn_legend = 1
                        legend_desciption = 'Alteration Adjustment markdown'
                    elif(mkdn_flag == 'C'):
                        print_mkdn_legend = 1
                        legend_desciption = 'Customer Service markdown'
                    else:
                        mkdn_flag = ' '
                    
                    if(legend_desciption != ''):
                        transaction_mkdn= mkdn_flag
                else:
                    mkdn_flag=''
                detail_loop=1
                if((display_comm_flag != old_display_comm_flag) or (backup_flag)):
                    old_display_comm_flag = display_comm_flag
                    backup_flag=0
            else:
                item_ship_group= details['TRANSACTION'][0]['ITEMS_MV'][x]['ITEM.SHIP.GROUP']
                if(item_ship_group!=curr_ship_group):
                    line_total=(details['TRANSACTION'][0]['ITEMS_MV'][x]['RETAIL'])-(details['TRANSACTION'][0]['ITEMS_MV'][x]['MRKDN.LONG'])*(details['TRANSACTION'][0]['ITEMS_MV'][x]['QUANTITY'])
                    line_total= line_total - unconverted_disc_amount
                    if(x>total_accumulated_line):
                        sale_total=sale_total+line_total
                        total_accumulated_line= total_accumulated_line+1
                    continue
                transaction_sku=(details['TRANSACTION'][0]['ITEMS_MV'][x]['ITEM.NO']) 
                transaction_details['sku']=transaction_sku
            description_output=[]
            extCommOut=''
            desc= dcount(list(details['TRANSACTION'][0]['ITEMS_MV'][x]['DESC'])
            if(desc>1):
                if((details['TRANSACTION'][0]['ITEMS_MV'][x]['DESC'])!='SJFILE'): 
                    description_output.append(details) 
                description_output.append(details['TRANSACTION'][0]['ITEMS_MV'][x][2]['DESC'])
                sub_item_count=dcount(details['TRANSACTION'][0]['ITEMS_MV'][x]['DESC'])    
                for y in range(3,sub_item_count):
                    transaction_desc=details['TRANSACTION'][0]['ITEMS_MV'][x][y]['ITEM.SHIP.GROUP']
                    if(transaction_desc!=''):   
                        EM_file=u2py.File("EM")
                        s_name=listdetails['TRANSACTION'][0]['ITEMS_MV'][0]['EXP.DATE']
                        if(s_name):
                            description_output.append(s_name)
                        else:
                            description_output.append(transaction_desc)
                    else:
                        description_output.append(transaction_desc)
                if(len(details['TRANSACTION'][0]['ITEMS_MV'][x]['DESC'])>20 and (details['TRANSACTION'][0]['ITEMS_MV'][x][1][10]['DESC'])=='GIFT CARD-'): 
                    description_output.append(details['TRANSACTION'][0]['ITEMS_MV'][x][1][10]['DESC'])
                    description_output.append(details['TRANSACTION'][0]['ITEMS_MV'][x][11][99]['DESC'])
                else:
                    if(presale_detail!='Y'):
                        if((details['TRANSACTION'][0]['ITEMS_MV'][x][1][12]['DESC'])=='Custom Ord #'):
                            description_output.append(details['TRANSACTION'][0]['ITEMS_MV'][1][x]['DESC'])
                        else:
                            description_output.append(details['TRANSACTION'][0]['ITEMS_MV'][1][x][1:17]['DESC'])
                        commission_type=(details['TRANSACTION'][0]['ITEMS_MV'][1][x][1]['COMMISSION.TYPE'])
                        commission_type=len(description_output)
                        description_output=description_output+commission_type
                        if((details['TRANSACTION'][0]['ITEMS_MV'][1][x][1]['CommSaleAmt'])+0 != 0):
                            item_quantity= (details['TRANSACTION'][0]['ITEMS_MV'][1][x]['VALUE.IS'])
                            quantity_XMUL = item_quantity*xmul
                            description_output=description_output+()  
                        else:
                            description_output=description_output+' '
                        temp_rate=(details['TRANSACTION'][0]['ITEMS_MV'][1][x][1]['CommRate'])+0
                        description_output=description_output+temp_rate
                        temp_rate=(details['TRANSACTION'][0]['ITEMS_MV'][1][x][1]['CommRate'])
                        description_output=description_output+temp_rate  
                        temp_rate=(details['TRANSACTION'][0]['ITEMS_MV'][1][x][1]['CommEmplPercentUsed'])
                        description_output=description_output+temp_rate  
                        emp_id=details['TRANSACTION'][0]['ITEMS_MV'][1][x][1]['CommEmplId']
                        empsn=list(EM_file.readv(emp_id,17))[0][0]
                        if(empsn):
                            empsn=emp_id
                        description_output=description_output+empsn 
                        commission_count=dcount(details['TRANSACTION'][0]['ITEMS_MV'][1][x]['COMMISSION.TYPE']) 
                        if(display_comm_flag==false):
                            description_output=description_output+(details['TRANSACTION'][0]['ITEMS_MV'][1][x]['QUANTITY'])
                            if(ship_group_count>0 or ship_status_count>0):
                                description_output=description_output+(details['TRANSACTION'][0]['ITEMS_MV'][1][x]['LIST.ITEM.STATUS'])
                        if((details['TRANSACTION'][0]['ITEMS_MV'][0]['TRAN.TYPE'])=='VSAL' or (details['TRANSACTION'][0]['ITEMS_MV'][0]['TRAN.TYPE'])=='XCHG'):
                                description_output=description_output+(details['TRANSACTION'][0]['ITEMS_MV'][1][x]['IGNORE.PROMOS'])
                for i in range(1,description_count):
                    transaction_details['descr']=description_output[i]
                rental_id=(details['TRANSACTION'][0]['ITEMS_MV'][1][x]['RESERVATIONS'])
                if(rental_id != ''):
                    rental=' (Rental '+rental_id+' for'+((details['TRANSACTION'][0]['ITEMS_MV'][1][x]['TUX.RENTAL.AMT'])*100)+', '+((details['TRANSACTION'][0]['ITEMS_MV'][1][x]['TUX.INSURANCE.AMT'])*100)+' ins, '+((details['TRANSACTION'][0]['ITEMS_MV'][1][x]['TUX.RUSH.AMT'])*100)+' rush'
                    rental=rental+((details['TRANSACTION'][0]['ITEMS_MV'][1][x]['TUX.INSURANCE.AMT'])*100)
                    rental=rental+((details['TRANSACTION'][0]['ITEMS_MV'][1][x]['TUX.RUSH.AMT'])*100) 
                    if (details['TRANSACTION'][0]['ITEMS_MV'][1][x]['TUX.MARKDOWN.AMT'] != ''):
                        rental=rental+', '+((details['TRANSACTION'][0]['ITEMS_MV'][1][x]['TUX.MARKDOWN.AMT'])*100)+' mkdn' 
                    rental=rental+')'
                else:
                    unconverted_dist_total=0
                line_total=((list(data_file.readv(transaction_id,11))[1][x])-(list(data_file.readv(transaction_id,12))[1][x]))*(list(data_fileS.readv(transaction_id,13))[1][x])
                line_total=line_total-unconverted_disc_amount
                if(x> total_accumulated_line):
                    sale_total=sale_total+line_total
                    total_accumulated_line=total_accumulated_line+1
                
