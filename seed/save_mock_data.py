import json
import u2py
import pandas as pd
import random
import math

def save_mock_data():
    transaction_file = u2py.File('TRANSACTION')
    employee_file = u2py.File('EM')
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
        commEmplPercentUsed = data_dict['commEmplPercentUsed'][i]
        discountType = str(data_dict['discountType'][i])
        listPrice = data_dict['listPrice'][i]
        lineDiscount = data_dict['lineDiscount'][i]
        firstName = data_dict['firstName'][i]
        lastName = data_dict['lastName'][i]
        phone = data_dict['phone'][i]
        operatorId = data_dict['operatorId'][i]
        tranDate = str(data_dict['tranDate'][i])
        tranAmount = str(data_dict['tranDate'][i])
        svChanged1 = str(data_dict['svChanged1'][i])
        svChanged2 = str(data_dict['svChanged2'][i])
        svChanged3 = str(data_dict['svChanged3'][i])
        transactionType = str(data_dict['type'][i])
        auditFlag = str(data_dict['auditFlag'][i])
        certNo = str(data_dict['certNo'][i])
        returnTrans = str(data_dict['returnTrans'][i])
        ccName = str(data_dict['ccName'][i])
        reserNo = str(data_dict['r2rReserNo'][i])
        shipMethod = str(data_dict['shipMethod'][i])
        shipComment = str(data_dict['shipComment'][i])
        shipFName = str(data_dict['shipFName'][i])
        shipLName = str(data_dict['shipLName'][i])
        shipAddr = str(data_dict['shipAddr'][i])
        shipCity = str(data_dict['shipCity'][i])
        shipState = str(data_dict['shipState'][i])
        shipZip = str(data_dict['shipZip'][i])
        shipDate = str(data_dict['shipDate'][i])
        mbaOrderId = str(data_dict['mbaOrderId'][i])
        maskedAcctNo = str(data_dict['maskedAcctNo'][i])
        shipCarrier1 = str(data_dict['shipCarrier1'][i])
        shipCarrier2 = str(data_dict['shipCarrier2'][i])
        shipCarrier3 = str(data_dict['shipCarrier3'][i])
        shipTrackNo1 = str(data_dict['shipTrackNo1'][i])
        shipTrackNo2 = str(data_dict['shipTrackNo2'][i])
        shipTrackNo3 = str(data_dict['shipTrackNo3'][i])
        signMethod = str(data_dict['signMethod'][i])
        pfPoints = str(data_dict['pfPoints'][i])
        couponCode1 = str(data_dict['couponCode1'][i])
        couponCode2 = str(data_dict['couponCode2'][i])
        couponCode3 = str(data_dict['couponCode3'][i])
        discountPodType1 = str(data_dict['discountPodType1'][i])
        discountPodType2 = str(data_dict['discountPodType2'][i])
        discountPodType3 = str(data_dict['discountPodType3'][i])
        discountPodAmt1 = str(data_dict['discountPodAmt1'][i])
        discountPodAmt2 = str(data_dict['discountPodAmt2'][i])
        discountPodAmt3 = str(data_dict['discountPodAmt3'][i])
        discountReasonCode1 = str(data_dict['discountReasonCode1'][i])
        discountReasonCode2 = str(data_dict['discountReasonCode2'][i])
        discountReasonCode3 = str(data_dict['discountReasonCode3'][i])
        promosId1 = str(data_dict['promosId1'][i])
        promosId2 = str(data_dict['promosId2'][i])
        promosId3 = str(data_dict['promosId3'][i])
        inAddMrkdn1 = str(data_dict['inAdditionToMrkdn1'][i])
        inAddMrkdn2 = str(data_dict['inAdditionToMrkdn2'][i])
        inAddMrkdn3 = str(data_dict['inAdditionToMrkdn3'][i])
        likeTenderOverrideMgrId = str(data_dict['likeTenderOverrideMgrId'][i])
        discountEmployeeId = str(data_dict['discountEmployeeId'][i])
        ercptEmail = (data_dict['ercptEmail'][i])
        employeeId = (data_dict['employeeId'][i])
        kg_em_last_name = (data_dict['emLastName'][i])
        kg_em_first_name = (data_dict['emFirstName'][i])
        advertCode = str(data_dict['advertCode'][i])
        corpAcctNo = str(data_dict['corpAcctNo'][i])
        authTerminalId = str(data_dict['authTerminalId'][i])
        handTktNo = str(data_dict['handTktNo'][i])
        
        transaction_file.writev(transaction_id, 2, phone)

        # # data = bytes(str(random.randint(50000, 70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)),"utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)), "utf-8")
        transaction_file.writev(transaction_id, 3, tranDate)

        transaction_file.writev(transaction_id, 4, operatorId)

        data = bytes(str(commission_type), "utf-8") + u2py.VM + bytes(str(commission_type), "utf-8") + u2py.VM + bytes(str(commission_type), "utf-8")
        transaction_file.writev(transaction_id,6,data)

        transaction_file.writev(transaction_id, 7, transactionType)

        transaction_file.writev(transaction_id, 8, tranAmount)

        data = bytes(str(item_no+random.randint(5000,40000)),"utf-8")+ u2py.VM + bytes(str(item_no+random.randint(5000,40000)),"utf-8")+ u2py.VM + bytes(str(item_no+random.randint(5000,40000)),"utf-8")
        transaction_file.writev(transaction_id,9,data)

        data = bytes(svChanged1,"utf-8") + u2py.VM + bytes(svChanged2,"utf-8") + u2py.VM + bytes(svChanged3,"utf-8")
        transaction_file.writev(transaction_id,11,data)

        data1 = bytes(str(markdown_1), "utf-8") + u2py.VM + bytes(str(markdown_2), "utf-8") + u2py.VM + bytes(str(markdown_3), "utf-8")
        transaction_file.writev(transaction_id,12,data1)

        data = bytes(str(mkup_strote_qty), "utf-8") + u2py.VM + bytes(str(mkup_strote_qty), "utf-8") + u2py.VM + bytes(str(mkup_strote_qty), "utf-8")
        transaction_file.writev(transaction_id,13,data)

        data = bytes(str(description_1),"utf-8") + u2py.VM + bytes(str(description_2),"utf-8") + u2py.VM + bytes(str(description_3),"utf-8")
        transaction_file.writev(transaction_id,14, data)

        data = bytes(str('CASH'), "utf-8") + u2py.VM + bytes(str('CASH'), "utf-8") + u2py.VM + bytes(str('CASH'),"utf-8")
        transaction_file.writev(transaction_id, 15, data)

        transaction_file.writev(transaction_id, 21, auditFlag)

        transaction_file.writev(transaction_id, 25, 'VOID VALUE')

        transaction_file.writev(transaction_id, 30, certNo)

        transaction_file.writev(transaction_id, 33, returnTrans)

        transaction_file.writev(transaction_id, 35, ccName)

        transaction_file.writev(transaction_id, 38, random.randint(100000, 300000))

        transaction_file.writev(transaction_id, 43, reserNo)

        data = bytes(str(lineDiscount), "utf-8") + u2py.SM + bytes(str(lineDiscount), "utf-8") + u2py.VM + bytes(
            str(lineDiscount), "utf-8") + u2py.SM + bytes(
            str(lineDiscount), "utf-8") + u2py.VM + bytes(str(lineDiscount), "utf-8") + u2py.SM + bytes(
            str(lineDiscount), "utf-8")
        transaction_file.writev(transaction_id, 45, data)

        transaction_file.writev(transaction_id, 46, shipMethod)
        
        transaction_file.writev(transaction_id, 48, authTerminalId)

        transaction_file.writev(transaction_id, 49, shipComment)

        transaction_file.writev(transaction_id, 51, shipFName)

        transaction_file.writev(transaction_id, 52, shipLName)

        transaction_file.writev(transaction_id, 53, shipAddr)

        transaction_file.writev(transaction_id, 54, shipCity)

        transaction_file.writev(transaction_id, 55, shipState)

        transaction_file.writev(transaction_id, 56, shipZip)

        transaction_file.writev(transaction_id, 57, shipDate)

        transaction_file.writev(transaction_id, 58, mbaOrderId)
        
        transaction_file.writev(transaction_id, 64, handTktNo)

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

        transaction_file.writev(transaction_id, 82, maskedAcctNo)

        data = bytes(str(rental_id), "utf-8") + u2py.VM + bytes(str(rental_id), "utf-8") + u2py.VM + bytes(str(rental_id), "utf-8")
        transaction_file.writev(transaction_id, 90, data)

        data = bytes(shipCarrier1, "utf-8") + u2py.VM + bytes(shipCarrier2, "utf-8") + u2py.VM + bytes(shipCarrier3,"utf-8")
        transaction_file.writev(transaction_id, 104, data)

        data = bytes(shipTrackNo1, "utf-8") + u2py.VM + bytes(shipTrackNo2, "utf-8") + u2py.VM + bytes(shipTrackNo3,"utf-8")
        transaction_file.writev(transaction_id, 105, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transaction_id, 111, data)
        
        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transaction_id, 112, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transaction_id, 113, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transaction_id, 115, data)

        data = bytes(couponCode1, "utf-8") + u2py.VM + bytes(couponCode2, "utf-8") + u2py.VM + bytes(couponCode3,"utf-8")
        transaction_file.writev(transaction_id, 128, data)

        transaction_file.writev(transaction_id, 129, signMethod)

        transaction_file.writev(transaction_id, 135, pfPoints)

        transaction_file.writev(transaction_id, 137, likeTenderOverrideMgrId)

        transaction_file.writev(transaction_id, 141, transaction_sub_type)

        if discountType != 'nan':
            data = bytes(str(discountType), "utf-8") + u2py.VM + bytes(str(discountType), "utf-8") + u2py.VM + bytes(str(discountType), "utf-8")
            transaction_file.writev(transaction_id, 159, data)

        data = bytes(discountPodType1, "utf-8") + u2py.VM + bytes(discountPodType2, "utf-8") + u2py.VM + bytes(discountPodType3, "utf-8")
        transaction_file.writev(transaction_id, 160, data)

        data = bytes(discountPodAmt1, "utf-8") + u2py.VM + bytes(discountPodAmt2, "utf-8") + u2py.VM + bytes(discountPodAmt3, "utf-8")
        transaction_file.writev(transaction_id, 161, data)

        transaction_file.writev(transaction_id, 162, discountEmployeeId)

        data = bytes(discountReasonCode1, "utf-8") + u2py.VM + bytes(discountReasonCode2, "utf-8") + u2py.VM + bytes(discountReasonCode3, "utf-8")
        transaction_file.writev(transaction_id, 163, data)

        data = bytes(promosId1, "utf-8") + u2py.VM + bytes(promosId2, "utf-8") + u2py.VM + bytes(promosId3, "utf-8")
        transaction_file.writev(transaction_id, 165, data)

        data = bytes(inAddMrkdn1, "utf-8") + u2py.VM + bytes(inAddMrkdn2, "utf-8") + u2py.VM + bytes(inAddMrkdn3, "utf-8")
        transaction_file.writev(transaction_id, 166, data)

        data = bytes(str(discount_conversion), "utf-8") + u2py.VM + bytes(str(discount_conversion), "utf-8") + u2py.VM + bytes(str(discount_conversion), "utf-8")
        transaction_file.writev(transaction_id, 167, data)

        if advertCode != 'nan':
            transaction_file.writev(transaction_id, 168, advertCode)

        if corpAcctNo != 'nan':
            transaction_file.writev(transaction_id, 169, corpAcctNo)
        
        data = bytes(str(random.randint(100000, 300000)), "utf-8") + u2py.VM + bytes(str(random.randint(100000, 300000)),"utf-8") + u2py.VM + bytes(str(random.randint(100000, 300000)), "utf-8")
        transaction_file.writev(transaction_id, 198, data)

        data = bytes(str(random.randint(10000, 30000)), "utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)),"utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)), "utf-8")
        transaction_file.writev(transaction_id, 199, data)


        transaction_file.writev(transaction_id, 214, '676987')

        transaction_file.writev(transaction_id, 219, ercptEmail)
        
        data = bytes(str(random.randint(10000, 30000)), "utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)),"utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)), "utf-8")
        transaction_file.writev(transaction_id, 223, data)


        data = bytes(str(comm_sale_amount_1), "utf-8") + u2py.VM + bytes(str(comm_sale_amount_2),"utf-8") + u2py.VM + bytes(str(comm_sale_amount_3), "utf-8")
        transaction_file.writev(transaction_id, 241, data)

        data = bytes(str(comm_rate), "utf-8") + u2py.VM + bytes(str(comm_rate),"utf-8") + u2py.VM + bytes(str(comm_rate), "utf-8")
        transaction_file.writev(transaction_id, 242, data)

        if comm_empl_id != 'nan':
            data = bytes(comm_empl_id, "utf-8") + u2py.VM + bytes(comm_empl_id, "utf-8") + u2py.VM + bytes(comm_empl_id, "utf-8")
            transaction_file.writev(transaction_id, 244, data)

        data = bytes(str(commEmplPercentUsed), "utf-8") + u2py.VM + bytes(str(commEmplPercentUsed), "utf-8") + u2py.VM + bytes(str(commEmplPercentUsed), "utf-8")
        transaction_file.writev(transaction_id, 245, data)

        data = bytes(str(comm_empl_type), "utf-8") + u2py.VM + bytes(str(comm_empl_type),"utf-8") + u2py.VM + bytes(str(comm_empl_type), "utf-8")
        transaction_file.writev(transaction_id, 246, data)

        employee_file.writev(comm_empl_id,1,firstName)

        employee_file.writev(comm_empl_id, 2,lastName)

        employee_file.writev(comm_empl_id,17,firstName[0:3].upper()+str(random.randint(10,100)))

        employee_file.writev(comm_empl_id,27,firstName)

        kg_employee_file.writev(employeeId,1,kg_em_first_name)
        
        kg_employee_file.writev(employeeId,2,kg_em_last_name)
        
        print('{} created {}'.format(transaction_id,i))


save_mock_data()

