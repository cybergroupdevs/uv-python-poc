import logging
from flask import Flask
from flask import request, jsonify, Response
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
    transaction_id = transactionId
    pdb.set_trace()
    status = check_existing_record('TRANSACTION', transaction_id)
    if (status):
        transaction_file = u2py.File("TRANSACTION")
        order_detail = {}
        cmd = "LIST ECOM.ORDER.ID SHIP.DATE SHIP.FNAME SHIP.LNAME SHIP.METHOD SHIP.ADDR SHIP.CARRIER SHIP.CITY SHIP.BOLNUMBER SHIP.TRACK.NO AUDIT.FLAG GEN.COUPON.ID RETURN.TRANS ERCPT.EMAIL DATA {} TRANSACTION TOJSON".format(
            transaction_id)
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


@app.route('/api/transaction/discount/<transactionId>', methods=['GET'])
def discount(transactionId):
    transaction_id = transactionId
    status = check_existing_record('TRANSACTION', transaction_id)
    if(status):
        presale_detail=True
        cmd = "LIST DATA RESERVATIONS DISCOUNT.TYPE RETAIL COUPON.CODE DISCOUNT.POD.TYPE DISCOUNT.POD.AMT DISCOUNT.EMPLOYEE.ID DISCOUNT.REASON.CODE DISCOUNT.REASON.TEXT PROMOS.ID IN.ADDITION.TO.MRKDN DISC.CNV.MRKDN ADVERT.CODE CORP.ACCT.NO LINE.DISCOUNT QUANTITY LONG.MRKDN TAX.AMT {} TRANSACTION TOJSON".format(transaction_id)
        details = u2py.Command(cmd).run(capture=True)
        details = json.loads(details)
        if(presale_detail == True):
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
                discount = discount+float(details['TRANSACTION'][y]['ITEM_MV'][0]['QUANTITY'])*float(
                    details['TRANSACTION'][y]['ITEM_MV'][count]['LINE.DISCOUNT'])
            employee_cmd = "LIST DATA SHORTNAME {} EM TOJSON".format(
                emp_id)
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
                kgm_cmd = "LIST DATA LNAME FNAME COMPANY.CODE {} KG.EM ToJSON".format(
                    emp_id)
                kgm_details = u2py.Command(kgm_cmd).run(capture=True)
                kgm_details = json.loads(kgm_details)
                pct = kgm_details["KG.EM"]["0"]["COMPANY.CODE"]+' employee'
                pct = pct + \
                    ' ('+kgm_details["KG.EM"]["0"]["FNAME"] + \
                    ' '+kgm_details["KG.EM"]["0"]["LNAME"]+')'
            elif(disc_type == 10):
                pct = 'Affiliate employee family'
                pct = kgm_details["KG.EM"]["0"]["COMPANY.CODE"] + \
                    ' employee family'
                pct = pct + \
                    ' (of '+kgm_details["KG.EM"]["0"]["FNAME"] + \
                    ' '+kgm_details["KG.EM"]["0"]["LNAME"]+')'
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
            data = str(pct)+' discount of '+str(scr_discount*100)  # OCONV missing
            if (disc_conv_to_mkdn):
                data = data+' converted to markdown.'
            else:
                data = data+'.'
            sale_total=0
            items_mv=len(details['TRANSACTION'][0]['ITEM_MV'])
            for i in range(0,items_mv):
                 retail=float(details['TRANSACTION'][0]['ITEM_MV'][count]['RETAIL'])
                 mrkdn=float(details['TRANSACTION'][0]['ITEM_MV'][count]['LONG.MRKDN'])
                 quantity=int(details['TRANSACTION'][0]['ITEM_MV'][count]['QUANTITY'])
                 sale_total=sale_total+(retail-mrkdn)*quantity
            sale_total=sale_total+float(details['TRANSACTION'][0]["TAX.AMT"])
            #if(details['TRANSACTION'][0]['DISCOUNT.TYPE_MV'][0]['DISCOUNT.TYPE'] != 0):
               # sub_total = convert(sale_total, external)
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


@app.route('/api/transaction/refund/<transactionId>', methods=['GET'])
def refund(transactionId):
    pdb.set_trace()
    transaction_id = transactionId
    status = check_existing_record('TRANSACTION', transaction_id)
    if(status):
        data_file = u2py.File("TRANSACTION")
        cmd = "LIST DATA LIKE.TENDER.OVERRIDE.MGR.ID HAND.TKT.NO {} TRANSACTION TOJSON".format(
            transaction_id)
        details = u2py.Command(cmd).run(capture=True)
        details = json.loads(details)
        refund_mgr_id = details['TRANSACTION'][0]['LIKE.TENDER.OVERRIDE.MGR.ID']
        em_cmd="LIST DATA NICKNAME FNAME LNAME SHORTNAME {} EM TOJSON".format(177092.0)
        em_details=u2py.Command(em_cmd).run(capture=True)
        em_details=json.loads(em_details)
        if(refund_mgr_id):
            if("NICKNAME" in em_details['EM'][0].keys()):
                refund_mgr_name = em_details['EM'][0]['NICKNAME']
            else:
                refund_mgr_name = em_details['EM'][0]['FNAME']	
        refund_mgr_name = refund_mgr_name,em_details['EM'][0]['LNAME'],'(',em_details['EM'][0]['SHORTNAME'],')'
        refund_data = {}
        refund_data['refundMgrName'] = 'MGR OVERRIDING SUGGESTED REFUND TYPE: ' + str(refund_mgr_name)
        ticket_number = details['TRANSACTION'][0]['HAND.TKT.NO']
        if(ticket_number):
            refund_data['ticketNumber'] = 'HANDWRITTEN TICKET NUMBER: ' + \
                details['TRANSACTION'][0]['HAND.TKT.NO']
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

@app.route('/api/transaction/<transactionId>', methods=['GET'])
def transactionGet(transactionId):
    transaction_id = transactionId
    status = check_existing_record('TRANSACTION', transaction_id)
    if status:
        data_file = u2py.File("TRANSACTION")
        EM_file = u2py.File("EM")
        order_detail = {}
        transaction_details = {}
        display_comm_flag = False
        cmd = "LIST TRANSACTION WITH @ID = {} DESC ITEM.NO RETAIL MRKDN QUANTITY LONG.MRKDN TUX.RENTAL.AMT TUX.INSURANCE.AMT TUX.RUSH.AMT TUX.MARKDOWN.AMT RESERVATIONS MKDN.AUDIT ITEM.SHIP.GROUP RETURN.QTY SHIP.GROUP CommEmplId TRAN.TYPE TOJSON".format(
            transaction_id)
        details = u2py.Command(cmd).run(capture=True)
        details = json.loads(details)
        unconverted_disc_amount = 0
        total_accumulated_line = 0
        presale_detail = 'Y'
        print(details)
        n_lines = len(details['TRANSACTION'][0]['ITEM_MV'])
        for x in range(0, n_lines):
            old_display_comm_flag = display_comm_flag
            backup_flag = 0
            if( presale_detail != 'Y'):
                item_no = details['TRANSACTION'][0]['ITEM_MV'][x]['ITEM.NO']
                transaction_class = item_no[0:4]
                transaction_ssku = item_no[4:8]
                transaction_mkdn = details['TRANSACTION'][0]['ITEM_MV'][x]['LONG.MRKDN']
                if(transaction_mkdn != 0 or transaction_mkdn != ''):
                    legend_desciption = ''
                    mkdn_flag = details['TRANSACTION'][0]['ITEM_MV'][0]['MKDN.AUDIT']
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
                        # line 631
                        transaction_mkdn = mkdn_flag
                else:
                    mkdn_flag = ''
                detail_loop = 1
                if((display_comm_flag != old_display_comm_flag) or (backup_flag)):
                    old_display_comm_flag = display_comm_flag
                    backup_flag = 0
                # line 650 (print)
            else:
                item_ship_group = details['TRANSACTION'][0]['ITEM_MV'][x]['ITEM.SHIP.GROUP']

                curr_ship_group = details['TRANSACTION'][0]['SHIPGROUP_MV'][0]['SHIP.GROUP']
                if(item_ship_group == curr_ship_group):
                    sale_total = 0
                    line_total = (float(details['TRANSACTION'][0]['ITEM_MV'][x]['RETAIL'])-float(
                        details['TRANSACTION'][0]['ITEM_MV'][x]['LONG.MRKDN']))*int(details['TRANSACTION'][0]['ITEM_MV'][x]['QUANTITY'])
                    line_total = line_total - unconverted_disc_amount
                    if(x > total_accumulated_line):
                        sale_total = sale_total+line_total
                        total_accumulated_line = total_accumulated_line+1
                transaction_sku = details['TRANSACTION'][0]['ITEM_MV'][x]['ITEM.NO'][1:9]
                transaction_details['sku'] = transaction_sku
            description_output = []
            extCommOut = ''
            desc = data_file.readv(
                details['TRANSACTION'][0]['_ID'], 14).dcount(u2py.SM)
            if(desc == 1):
                if(presale_detail == 'Y'):
                    emp_id = int(
                        float(details['TRANSACTION'][0]['ITEM_MV'][x]['CommEmplId']))

                    try:
                        empsn = list(EM_file.readv(str(emp_id), 17))[0][0]
                        empsn = emp_id
                    except:
                        pass
                    if(display_comm_flag == False):
                        return_quantity = details['TRANSACTION'][0]['ITEM_MV'][x]['QUANTITY']
                        ship_group_count = ship_status_count = 0
                        if(ship_group_count > 0 or ship_status_count > 0):
                            description_output = description_output + \
                                (details['TRANSACTION'][0]['ITEM_MV']
                                 [1][x]['LIST.ITEM.STATUS'])
                    if((details['TRANSACTION'][0]['TRAN.TYPE']) == 'VSAL' or (details['TRANSACTION'][0]['TRAN.TYPE']) == 'XCHG'):
                        description_output = description_output + \
                            (details['TRANSACTION'][0]
                             ['ITEM_MV'][1][x]['IGNORE.PROMOS'])
                # line 829

                description_count = n_lines
                rental_id = details['TRANSACTION'][0]['ITEM_MV'][x]['RESERVATIONS']
                if(rental_id != ''):
                    rental = ' (Rental '+rental_id+' for'+((details['TRANSACTION'][0]['ITEM_MV'][x]['TUX.RENTAL.AMT'])*100)+', '+(
                        (details['TRANSACTION'][0]['ITEM_MV'][x]['TUX.INSURANCE.AMT'])*100)+' ins, '+((details['TRANSACTION'][0]['ITEM_MV'][x]['TUX.RUSH.AMT'])*100)+' rush'
                    rental = rental + \
                        ((details['TRANSACTION'][0]['ITEM_MV']
                          [x]['TUX.INSURANCE.AMT'])*100)
                    rental = rental + \
                        ((details['TRANSACTION'][0]
                          ['ITEM_MV'][x]['TUX.RUSH.AMT'])*100)
                    if (details['TRANSACTION'][0]['ITEM_MV'][x]['TUX.MARKDOWN.AMT'] != ''):
                        rental = rental+', ' + \
                            ((details['TRANSACTION'][0]['ITEMS_MV']
                              [x]['TUX.MARKDOWN.AMT'])*100)+' mkdn'
                    rental = rental+')'
                else:
                    unconverted_dist_total = 0
                line_total = (float(details['TRANSACTION'][0]['ITEM_MV'][x]['RETAIL'])-(float(
                    details['TRANSACTION'][0]['ITEM_MV'][x]['MRKDN'])))*(int(details['TRANSACTION'][0]['ITEM_MV'][x]['QUANTITY']))
                line_total = line_total-unconverted_disc_amount
                if(x > total_accumulated_line):
                    sale_total = sale_total+line_total
                    total_accumulated_line = total_accumulated_line+1
        response = {
            "orderDetail": order_detail,
        }
        return Response(
            json.dumps(response),
            status=200,
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


def convertDateFormat(orderDate, format):
    date = u2py.DynArray()
    date.insert(1, 0, 0, orderDate)
    if format == 'internal':
        formattedDate = date.extract(1).iconv('D-')
    else:
        formattedDate = str(date.extract(1).oconv('D-'))
    return formattedDate


if __name__ == '__main__':
    app.run()


