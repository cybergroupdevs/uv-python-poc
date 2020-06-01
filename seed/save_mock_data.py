import json
import u2py
import pandas as pd
import random
import math

def save_mock_data():
    transaction_file = u2py.File('TRANSACTION')
    employee_file = u2py.File('EM')
    customer_file = u2py.File('CUSTOMERS')
    kg_employee_file = u2py.File('KG.EM')
    data = pd.read_csv('/usr/uv/PY/UPDATED_TRANSACTION.csv')
    data_dict = data.to_dict()
    length = len(data_dict['transactionID'])
    for i in range(length):
        transaction_id = data_dict['transactionID'][i]
        comm_empl_id = str(data_dict['CommEmplId'][i])
        comm_sale_amount_1 = data_dict['CommsaleAmt1'][i]
        comm_sale_amount_2 = data_dict['CommsaleAmt2'][i]
        comm_sale_amount_3 = data_dict['CommsaleAmt3'][i]
        mkup_strote_qty = data_dict['mkupStoreQty'][i]
        transaction_sub_type = data_dict['transactionSubType'][i]
        description_1 = data_dict['description1'][i]
        description_2 = data_dict['description2'][i]
        description_3 = data_dict['description3'][i]
        rental_id = data_dict['rentalId'][i]
        discount_conversion = data_dict['discountConversion'][i]
        markdown_1 = data_dict['markDown1'][i]
        markdown_2 = data_dict['markDown2'][i]
        markdown_3 = data_dict['markDown3'][i]
        comm_rate = data_dict['CommRate'][i]
        comm_empl_type = data_dict['CommEmplType'][i]
        item_no = data_dict['itemNo'][i]
        commission_type = data_dict['commissionType'][i]
        comm_empl_percent_used = data_dict['commEmplPercentUsed'][i]
        discount_type = str(data_dict['discountType'][i])
        list_price = data_dict['listPrice'][i]
        line_discount = data_dict['lineDiscount'][i]
        first_name = data_dict['firstName'][i]
        last_name = data_dict['lastName'][i]
        phone = data_dict['phone'][i]
        operator_id = data_dict['operatorId'][i]
        tran_date = str(data_dict['tranDate'][i])
        tran_amount = str(data_dict['tranAmount'][i])
        sv_changed_1 = str(data_dict['svChanged1'][i])
        sv_changed_2 = str(data_dict['svChanged2'][i])
        sv_changed_3 = str(data_dict['svChanged3'][i])
        transaction_type = str(data_dict['type'][i])
        audit_flag = str(data_dict['auditFlag'][i])
        cert_no = str(data_dict['certNo'][i])
        return_trans = str(data_dict['returnTrans'][i])
        credit_card_name = str(data_dict['ccName'][i])
        reser_no = str(data_dict['r2rReserNo'][i])
        ship_method = str(data_dict['shipMethod'][i])
        ship_comment = str(data_dict['shipComment'][i])
        ship_first_name = str(data_dict['shipFName'][i])
        ship_last_name = str(data_dict['shipLName'][i])
        ship_address = str(data_dict['shipAddr'][i])
        ship_city = str(data_dict['shipCity'][i])
        ship_state = str(data_dict['shipState'][i])
        ship_zip = str(data_dict['shipZip'][i])
        ship_date = str(data_dict['shipDate'][i])
        mba_order_id = str(data_dict['mbaOrderId'][i])
        masked_acct_no = str(data_dict['maskedAcctNo'][i])
        ship_carrier_1 = str(data_dict['shipCarrier1'][i])
        ship_carrier_2 = str(data_dict['shipCarrier2'][i])
        ship_carrier_3 = str(data_dict['shipCarrier3'][i])
        ship_track_no_1 = str(data_dict['shipTrackNo1'][i])
        ship_track_no_2 = str(data_dict['shipTrackNo2'][i])
        ship_track_no_3 = str(data_dict['shipTrackNo3'][i])
        sign_method = str(data_dict['signMethod'][i])
        pf_points = str(data_dict['pfPoints'][i])
        coupon_code_1 = str(data_dict['couponCode1'][i])
        coupon_code_2 = str(data_dict['couponCode2'][i])
        coupon_code_3 = str(data_dict['couponCode3'][i])
        discount_pod_type_1 = str(data_dict['discountPodType1'][i])
        discount_pod_type_2 = str(data_dict['discountPodType2'][i])
        discount_pod_type_3 = str(data_dict['discountPodType3'][i])
        discount_pod_amount_1 = str(data_dict['discountPodAmt1'][i])
        discount_pod_amount_2 = str(data_dict['discountPodAmt2'][i])
        discount_pod_amount_3 = str(data_dict['discountPodAmt3'][i])
        discount_reason_code_1 = str(data_dict['discountReasonCode1'][i])
        discount_reason_code_2 = str(data_dict['discountReasonCode2'][i])
        discount_reason_code_3 = str(data_dict['discountReasonCode3'][i])
        promos_id_1 = str(data_dict['promosId1'][i])
        promos_id_2 = str(data_dict['promosId2'][i])
        promos_id_3 = str(data_dict['promosId3'][i])
        in_add_mrkdn_1 = str(data_dict['inAdditionToMrkdn1'][i])
        in_add_mrkdn_2 = str(data_dict['inAdditionToMrkdn2'][i])
        in_add_mrkdn_3 = str(data_dict['inAdditionToMrkdn3'][i])
        like_tender_override_mgr_id = str(data_dict['likeTenderOverrideMgrId'][i])
        discount_employee_id = str(data_dict['discountEmployeeId'][i])
        ercpt_email = (data_dict['ercptEmail'][i])
        employee_id = (data_dict['employeeId'][i])
        kg_em_last_name = (data_dict['emLastName'][i])
        kg_em_first_name = (data_dict['emFirstName'][i])
        advert_code = str(data_dict['advertCode'][i])
        corp_acct_no = str(data_dict['corpAcctNo'][i])
        auth_terminal_id = str(data_dict['authTerminalId'][i])
        hand_tkt_no = str(data_dict['handTktNo'][i])
        alternate_phone_no = str(data_dict['altPhoneNo'][i])
        alternate_phone_no = "".join(alternate_phone_no.split())

        customer_first_name = data_dict['CUFirstName'][i]
        customer_last_name = data_dict['CULastName'][i]
        customer_zip_code = data_dict['zipCode'][i]
        customer_phone = data_dict['phone'][i]
        customer_alternate_phone = data_dict['altPhoneNo'][i]
        customer_state = data_dict['state'][i]
        customer_city = data_dict['city'][i]
        customer_address = data_dict['address'][i]

        customer_file.writev(alternate_phone_no, 1, customer_phone)
        customer_file.writev(alternate_phone_no,2,customer_first_name)
        customer_file.writev(alternate_phone_no, 3, customer_last_name)
        customer_file.writev(alternate_phone_no, 4, customer_address)
        customer_file.writev(alternate_phone_no, 5, customer_city)
        customer_file.writev(alternate_phone_no, 6, customer_state)
        customer_file.writev(alternate_phone_no, 7, customer_zip_code)
        customer_file.writev(alternate_phone_no, 8, customer_alternate_phone)
        customer_file.writev(alternate_phone_no,33,str(random.randint(0000,9999)))
  
        transaction_file.writev(transaction_id, 2, phone)

        transaction_file.writev(transaction_id, 3, tran_date)

        transaction_file.writev(transaction_id, 4, operator_id)

        data = bytes(str(commission_type), "utf-8") + u2py.VM + bytes(str(commission_type), "utf-8") + u2py.VM + bytes(str(commission_type), "utf-8")
        transaction_file.writev(transaction_id,6,data)

        transaction_file.writev(transaction_id, 7, transaction_type)

        transaction_file.writev(transaction_id, 8, tran_amount)

        data = bytes(str(item_no+random.randint(5000,40000)),"utf-8")+ u2py.VM + bytes(str(item_no+random.randint(5000,40000)),"utf-8")+ u2py.VM + bytes(str(item_no+random.randint(5000,40000)),"utf-8")
        transaction_file.writev(transaction_id,9,data)

        data = bytes(sv_changed_1,"utf-8") + u2py.VM + bytes(sv_changed_2,"utf-8") + u2py.VM + bytes(sv_changed_3,"utf-8")
        transaction_file.writev(transaction_id,11,data)

        data1 = bytes(str(markdown_1), "utf-8") + u2py.VM + bytes(str(markdown_2), "utf-8") + u2py.VM + bytes(str(markdown_3), "utf-8")
        transaction_file.writev(transaction_id,12,data1)

        data = bytes(str(mkup_strote_qty), "utf-8") + u2py.VM + bytes(str(mkup_strote_qty), "utf-8") + u2py.VM + bytes(str(mkup_strote_qty), "utf-8")
        transaction_file.writev(transaction_id,13,data)

        data = bytes(str(description_1),"utf-8") + u2py.VM + bytes(str(description_2),"utf-8") + u2py.VM + bytes(str(description_3),"utf-8")
        transaction_file.writev(transaction_id,14, data)

        data = bytes(str('CASH'), "utf-8") + u2py.VM + bytes(str('CASH'), "utf-8") + u2py.VM + bytes(str('CASH'),"utf-8")
        transaction_file.writev(transaction_id, 15, data)

        transaction_file.writev(transaction_id, 21, audit_flag)

        transaction_file.writev(transaction_id, 25, 'VOID VALUE')
        
        transaction_file.writev(transaction_id, 29, alternate_phone_no)

        transaction_file.writev(transaction_id, 30, cert_no)

        transaction_file.writev(transaction_id, 33, return_trans)

        transaction_file.writev(transaction_id, 35, credit_card_name)

        transaction_file.writev(transaction_id, 38, random.randint(100000, 300000))

        transaction_file.writev(transaction_id, 43, reser_no)

        data = bytes(str(line_discount), "utf-8") + u2py.SM + bytes(str(line_discount), "utf-8") + u2py.VM + bytes(str(line_discount), "utf-8") + u2py.SM + bytes(str(line_discount), "utf-8") + u2py.VM + bytes(str(line_discount), "utf-8") + u2py.SM + bytes(str(line_discount), "utf-8")
        transaction_file.writev(transaction_id, 45, data)

        transaction_file.writev(transaction_id, 46, ship_method)
        
        transaction_file.writev(transaction_id, 48, auth_terminal_id)

        transaction_file.writev(transaction_id, 49, ship_comment)

        transaction_file.writev(transaction_id, 51, ship_first_name)

        transaction_file.writev(transaction_id, 52, ship_last_name)

        transaction_file.writev(transaction_id, 53, ship_address)

        transaction_file.writev(transaction_id, 54, ship_city)

        transaction_file.writev(transaction_id, 55, ship_state)

        transaction_file.writev(transaction_id, 56, ship_zip)

        transaction_file.writev(transaction_id, 57, ship_date)

        transaction_file.writev(transaction_id, 58, mba_order_id)
        
        transaction_file.writev(transaction_id, 64, hand_tkt_no)

        data = bytes('1', "utf-8") + u2py.VM + bytes('2', "utf-8") + u2py.VM + bytes('3', "utf-8")
        transaction_file.writev(transaction_id, 65, data)

        data = bytes(str(random.randint(50000,70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000,70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000,70000)), "utf-8")
        transaction_file.writev(transaction_id, 66, data)

        data = bytes(str(random.randint(50000, 70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)),"utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)), "utf-8")
        transaction_file.writev(transaction_id, 67, data)

        data = bytes(str(random.randint(50000, 70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)),"utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)), "utf-8")
        transaction_file.writev(transaction_id, 68, data)

        data = bytes('BCRD', "utf-8") + u2py.VM + bytes('AMEX', "utf-8") + u2py.VM + bytes('CHEK', "utf-8")
        transaction_file.writev(transaction_id, 69, data)

        data1 = bytes(str(markdown_1), "utf-8") + u2py.VM + bytes(str(markdown_2), "utf-8") + u2py.VM + bytes(str(markdown_3), "utf-8")
        transaction_file.writev(transaction_id, 70, data1)

        data1 = bytes('00', "utf-8") + u2py.VM + bytes('05', "utf-8") + u2py.VM + bytes('00', "utf-8")
        transaction_file.writev(transaction_id, 71, data1)

        data1 = bytes('1', "utf-8") + u2py.VM + bytes('1', "utf-8") + u2py.VM + bytes('1', "utf-8")
        transaction_file.writev(transaction_id, 72, data1)

        data = bytes(str(random.randint(10000, 30000)), "utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)),"utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)), "utf-8")
        transaction_file.writev(transaction_id, 77, data)

        transaction_file.writev(transaction_id, 82, masked_acct_no)

        data = bytes(str(rental_id), "utf-8") + u2py.VM + bytes(str(rental_id), "utf-8") + u2py.VM + bytes(str(rental_id), "utf-8")
        transaction_file.writev(transaction_id, 90, data)

        data = bytes(ship_carrier_1, "utf-8") + u2py.VM + bytes(ship_carrier_2, "utf-8") + u2py.VM + bytes(ship_carrier_3,"utf-8")
        transaction_file.writev(transaction_id, 104, data)

        data = bytes(ship_track_no_1, "utf-8") + u2py.VM + bytes(ship_track_no_2, "utf-8") + u2py.VM + bytes(ship_track_no_3,"utf-8")
        transaction_file.writev(transaction_id, 105, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transaction_id, 111, data)
        
        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transaction_id, 112, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transaction_id, 113, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transaction_id, 115, data)

        data = bytes(coupon_code_1, "utf-8") + u2py.VM + bytes(coupon_code_2, "utf-8") + u2py.VM + bytes(coupon_code_3,"utf-8")
        transaction_file.writev(transaction_id, 128, data)

        transaction_file.writev(transaction_id, 129, sign_method)

        transaction_file.writev(transaction_id, 135, pf_points)

        transaction_file.writev(transaction_id, 137, like_tender_override_mgr_id)

        transaction_file.writev(transaction_id, 141, transaction_sub_type)

        if discount_type != 'nan':
            data = bytes(str(discount_type), "utf-8") + u2py.VM + bytes(str(discount_type), "utf-8") + u2py.VM + bytes(str(discount_type), "utf-8")
            transaction_file.writev(transaction_id, 159, data)

        data = bytes(discount_pod_type_1, "utf-8") + u2py.VM + bytes(discount_pod_type_2, "utf-8") + u2py.VM + bytes(discount_pod_type_3, "utf-8")
        transaction_file.writev(transaction_id, 160, data)

        data = bytes(discount_pod_amount_1, "utf-8") + u2py.VM + bytes(discount_pod_amount_2, "utf-8") + u2py.VM + bytes(discount_pod_amount_3, "utf-8")
        transaction_file.writev(transaction_id, 161, data)

        transaction_file.writev(transaction_id, 162, discount_employee_id)

        data = bytes(discount_reason_code_1, "utf-8") + u2py.VM + bytes(discount_reason_code_2, "utf-8") + u2py.VM + bytes(discount_reason_code_3, "utf-8")
        transaction_file.writev(transaction_id, 163, data)

        data = bytes(promos_id_1, "utf-8") + u2py.VM + bytes(promos_id_2, "utf-8") + u2py.VM + bytes(promos_id_3, "utf-8")
        transaction_file.writev(transaction_id, 165, data)

        data = bytes(in_add_mrkdn_1, "utf-8") + u2py.VM + bytes(in_add_mrkdn_2, "utf-8") + u2py.VM + bytes(in_add_mrkdn_3, "utf-8")
        transaction_file.writev(transaction_id, 166, data)

        data = bytes(str(discount_conversion), "utf-8") + u2py.VM + bytes(str(discount_conversion), "utf-8") + u2py.VM + bytes(str(discount_conversion), "utf-8")
        transaction_file.writev(transaction_id, 167, data)

        if advert_code != 'nan':
            transaction_file.writev(transaction_id, 168, advert_code)

        if corp_acct_no != 'nan':
            transaction_file.writev(transaction_id, 169, corp_acct_no)
        
        data = bytes(str(random.randint(100000, 300000)), "utf-8") + u2py.VM + bytes(str(random.randint(100000, 300000)),"utf-8") + u2py.VM + bytes(str(random.randint(100000, 300000)), "utf-8")
        transaction_file.writev(transaction_id, 198, data)

        data = bytes(str(random.randint(10000, 30000)), "utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)),"utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)), "utf-8")
        transaction_file.writev(transaction_id, 199, data)


        transaction_file.writev(transaction_id, 214, '676987')

        transaction_file.writev(transaction_id, 219, ercpt_email)
        
        data = bytes(str(random.randint(10000, 30000)), "utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)),"utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)), "utf-8")
        transaction_file.writev(transaction_id, 223, data)


        data = bytes(str(comm_sale_amount_1), "utf-8") + u2py.VM + bytes(str(comm_sale_amount_2),"utf-8") + u2py.VM + bytes(str(comm_sale_amount_3), "utf-8")
        transaction_file.writev(transaction_id, 241, data)

        data = bytes(str(comm_rate), "utf-8") + u2py.VM + bytes(str(comm_rate),"utf-8") + u2py.VM + bytes(str(comm_rate), "utf-8")
        transaction_file.writev(transaction_id, 242, data)

        if comm_empl_id != 'nan':
            comm_empl_id = int(float(comm_empl_id))
            data = bytes(str(comm_empl_id), "utf-8") + u2py.VM + bytes(str(comm_empl_id), "utf-8") + u2py.VM + bytes(str(comm_empl_id), "utf-8")
            transaction_file.writev(transaction_id, 244, data)

        data = bytes(str(comm_empl_percent_used), "utf-8") + u2py.VM + bytes(str(comm_empl_percent_used), "utf-8") + u2py.VM + bytes(str(comm_empl_percent_used), "utf-8")
        transaction_file.writev(transaction_id, 245, data)

        data = bytes(str(comm_empl_type), "utf-8") + u2py.VM + bytes(str(comm_empl_type),"utf-8") + u2py.VM + bytes(str(comm_empl_type), "utf-8")
        transaction_file.writev(transaction_id, 246, data)

        if comm_empl_id != 'nan':
            comm_empl_id = str(comm_empl_id)
            employee_file.writev(comm_empl_id,1,first_name)
            employee_file.writev(comm_empl_id, 2,last_name)
            employee_file.writev(comm_empl_id,17,first_name[0:3].upper()+str(random.randint(10,100)))
            employee_file.writev(comm_empl_id,27,first_name)
        
        phone = phone.replace('-','')
        employee_file.writev(phone,1,first_name)

        employee_file.writev(phone,2,last_name)

        employee_file.writev(phone,17,first_name[0:3].upper()+str(random.randint(10,100)))
        
        employee_file.writev(phone,27,first_name)

        kg_employee_file.writev(employee_id,1,kg_em_first_name)
        
        kg_employee_file.writev(employee_id,2,kg_em_last_name)
        
        print('{} created {}'.format(transaction_id,i))


save_mock_data()

