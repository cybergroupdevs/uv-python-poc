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
        transactionId = data_dict['transactionID'][i]
        commEmplId = str(data_dict['CommEmplId'][i])
        commSaleAmount1 = data_dict['CommsaleAmt1'][i]
        commSaleAmount2 = data_dict['CommsaleAmt2'][i]
        commSaleAmount3 = data_dict['CommsaleAmt3'][i]
        mkupStoreQty = data_dict['mkupStoreQty'][i]
        transactionSubType = data_dict['transactionSubType'][i]
        description1 = data_dict['description1'][i]
        description2 = data_dict['description2'][i]
        description3 = data_dict['description3'][i]
        rentalId = data_dict['rentalId'][i]
        discountConversion = data_dict['discountConversion'][i]
        markDown1 = data_dict['markDown1'][i]
        markDown2 = data_dict['markDown2'][i]
        markDown3 = data_dict['markDown3'][i]
        commRate = data_dict['CommRate'][i]
        commEmplType = data_dict['CommEmplType'][i]
        itemNo = data_dict['itemNo'][i]
        commissionType = data_dict['commissionType'][i]
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
        
        transaction_file.writev(transactionId, 2, phone)

        # # data = bytes(str(random.randint(50000, 70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)),"utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)), "utf-8")
        transaction_file.writev(transactionId, 3, tranDate)

        transaction_file.writev(transactionId, 4, operatorId)

        data = bytes(str(commissionType), "utf-8") + u2py.VM + bytes(str(commissionType), "utf-8") + u2py.VM + bytes(str(commissionType), "utf-8")
        transaction_file.writev(transactionId,6,data)

        transaction_file.writev(transactionId, 7, transactionType)

        transaction_file.writev(transactionId, 8, tranAmount)

        data = bytes(str(itemNo+random.randint(5000,40000)),"utf-8")+ u2py.VM + bytes(str(itemNo+random.randint(5000,40000)),"utf-8")+ u2py.VM + bytes(str(itemNo+random.randint(5000,40000)),"utf-8")
        transaction_file.writev(transactionId,9,data)

        data = bytes(svChanged1,"utf-8") + u2py.VM + bytes(svChanged2,"utf-8") + u2py.VM + bytes(svChanged3,"utf-8")
        transaction_file.writev(transactionId,11,data)

        data1 = bytes(str(markDown1), "utf-8") + u2py.VM + bytes(str(markDown2), "utf-8") + u2py.VM + bytes(str(markDown3), "utf-8")
        transaction_file.writev(transactionId,12,data1)

        data = bytes(str(mkupStoreQty), "utf-8") + u2py.VM + bytes(str(mkupStoreQty), "utf-8") + u2py.VM + bytes(str(mkupStoreQty), "utf-8")
        transaction_file.writev(transactionId,13,data)

        data = bytes(str(description1),"utf-8") + u2py.VM + bytes(str(description2),"utf-8") + u2py.VM + bytes(str(description3),"utf-8")
        transaction_file.writev(transactionId,14, data)

        data = bytes(str('CASH'), "utf-8") + u2py.VM + bytes(str('CASH'), "utf-8") + u2py.VM + bytes(str('CASH'),"utf-8")
        transaction_file.writev(transactionId, 15, data)

        transaction_file.writev(transactionId, 21, auditFlag)

        transaction_file.writev(transactionId, 25, 'VOID VALUE')

        transaction_file.writev(transactionId, 30, certNo)

        transaction_file.writev(transactionId, 33, returnTrans)

        transaction_file.writev(transactionId, 35, ccName)

        transaction_file.writev(transactionId, 43, reserNo)

        data = bytes(str(lineDiscount), "utf-8") + u2py.SM + bytes(str(lineDiscount), "utf-8") + u2py.VM + bytes(
            str(lineDiscount), "utf-8") + u2py.SM + bytes(
            str(lineDiscount), "utf-8") + u2py.VM + bytes(str(lineDiscount), "utf-8") + u2py.SM + bytes(
            str(lineDiscount), "utf-8")
        transaction_file.writev(transactionId, 45, data)

        transaction_file.writev(transactionId, 46, shipMethod)
        
        transaction_file.writev(transactionId, 48, authTerminalId)

        transaction_file.writev(transactionId, 49, shipComment)

        transaction_file.writev(transactionId, 51, shipFName)

        transaction_file.writev(transactionId, 52, shipLName)

        transaction_file.writev(transactionId, 53, shipAddr)

        transaction_file.writev(transactionId, 54, shipCity)

        transaction_file.writev(transactionId, 55, shipState)

        transaction_file.writev(transactionId, 56, shipZip)

        transaction_file.writev(transactionId, 57, shipDate)

        transaction_file.writev(transactionId, 58, mbaOrderId)
        
        transaction_file.writev(transactionId, 64, handTktNo)

        data = bytes('1', "utf-8") + u2py.VM + bytes('2', "utf-8") + u2py.VM + bytes('3', "utf-8")
        transaction_file.writev(transactionId, 65, data)

        data = bytes(str(random.randint(50000,70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000,70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000,70000)), "utf-8")
        transaction_file.writev(transactionId, 66, data)

        data = bytes(str(random.randint(50000, 70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)),"utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)), "utf-8")
        transaction_file.writev(transactionId, 67, data)

        data = bytes(str(random.randint(50000, 70000)), "utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)),"utf-8") + u2py.VM + bytes(str(random.randint(50000, 70000)), "utf-8")
        transaction_file.writev(transactionId, 68, data)

        data = bytes('BCRD', "utf-8") + u2py.VM + bytes('AMEX', "utf-8") + u2py.VM + bytes('CHEK', "utf-8")
        transaction_file.writev(transactionId, 69, data)

        data1 = bytes(str(markDown1), "utf-8") + u2py.VM + bytes(str(markDown2), "utf-8") + u2py.VM + bytes(str(markDown3), "utf-8")
        transaction_file.writev(transactionId, 70, data1)

        data1 = bytes('00', "utf-8") + u2py.VM + bytes('05', "utf-8") + u2py.VM + bytes('00', "utf-8")
        transaction_file.writev(transactionId, 71, data1)

        data1 = bytes('1', "utf-8") + u2py.VM + bytes('1', "utf-8") + u2py.VM + bytes('1', "utf-8")
        transaction_file.writev(transactionId, 72, data1)

        data = bytes(str(random.randint(10000, 30000)), "utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)),"utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)), "utf-8")
        transaction_file.writev(transactionId, 77, data)

        transaction_file.writev(transactionId, 82, maskedAcctNo)

        data = bytes(str(rentalId), "utf-8") + u2py.VM + bytes(str(rentalId), "utf-8") + u2py.VM + bytes(str(rentalId), "utf-8")
        transaction_file.writev(transactionId, 90, data)

        data = bytes(shipCarrier1, "utf-8") + u2py.VM + bytes(shipCarrier2, "utf-8") + u2py.VM + bytes(shipCarrier3,"utf-8")
        transaction_file.writev(transactionId, 104, data)

        data = bytes(shipTrackNo1, "utf-8") + u2py.VM + bytes(shipTrackNo2, "utf-8") + u2py.VM + bytes(shipTrackNo3,"utf-8")
        transaction_file.writev(transactionId, 105, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transactionId, 111, data)
        
        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transactionId, 112, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transactionId, 113, data)

        data = bytes(str(random.randint(10, 300)), "utf-8") + u2py.VM + bytes(str(random.randint(10, 300)),"utf-8") + u2py.VM + bytes(str(random.randint(100, 300)), "utf-8")
        transaction_file.writev(transactionId, 115, data)

        data = bytes(couponCode1, "utf-8") + u2py.VM + bytes(couponCode2, "utf-8") + u2py.VM + bytes(couponCode3,"utf-8")
        transaction_file.writev(transactionId, 128, data)

        transaction_file.writev(transactionId, 129, signMethod)

        transaction_file.writev(transactionId, 135, pfPoints)

        transaction_file.writev(transactionId, 137, likeTenderOverrideMgrId)

        transaction_file.writev(transactionId, 141, transactionSubType)

        if discountType != 'nan':
            data = bytes(str(discountType), "utf-8") + u2py.VM + bytes(str(discountType), "utf-8") + u2py.VM + bytes(str(discountType), "utf-8")
            transaction_file.writev(transactionId, 159, data)

        data = bytes(discountPodType1, "utf-8") + u2py.VM + bytes(discountPodType2, "utf-8") + u2py.VM + bytes(discountPodType3, "utf-8")
        transaction_file.writev(transactionId, 160, data)

        data = bytes(discountPodAmt1, "utf-8") + u2py.VM + bytes(discountPodAmt2, "utf-8") + u2py.VM + bytes(discountPodAmt3, "utf-8")
        transaction_file.writev(transactionId, 161, data)

        transaction_file.writev(transactionId, 162, discountEmployeeId)

        data = bytes(discountReasonCode1, "utf-8") + u2py.VM + bytes(discountReasonCode2, "utf-8") + u2py.VM + bytes(discountReasonCode3, "utf-8")
        transaction_file.writev(transactionId, 163, data)

        data = bytes(promosId1, "utf-8") + u2py.VM + bytes(promosId2, "utf-8") + u2py.VM + bytes(promosId3, "utf-8")
        transaction_file.writev(transactionId, 165, data)

        data = bytes(inAddMrkdn1, "utf-8") + u2py.VM + bytes(inAddMrkdn2, "utf-8") + u2py.VM + bytes(inAddMrkdn3, "utf-8")
        transaction_file.writev(transactionId, 166, data)

        data = bytes(str(discountConversion), "utf-8") + u2py.VM + bytes(str(discountConversion), "utf-8") + u2py.VM + bytes(str(discountConversion), "utf-8")
        transaction_file.writev(transactionId, 167, data)

        if advertCode != 'nan':
            transaction_file.writev(transactionId, 168, advertCode)

        if corpAcctNo != 'nan':
            transaction_file.writev(transactionId, 169, corpAcctNo)
        
        data = bytes(str(random.randint(100000, 300000)), "utf-8") + u2py.VM + bytes(str(random.randint(100000, 300000)),"utf-8") + u2py.VM + bytes(str(random.randint(100000, 300000)), "utf-8")
        transaction_file.writev(transactionId, 198, data)

        data = bytes(str(random.randint(10000, 30000)), "utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)),"utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)), "utf-8")
        transaction_file.writev(transactionId, 199, data)


        transaction_file.writev(transactionId, 214, '676987')

        transaction_file.writev(transactionId, 219, ercptEmail)
        
        data = bytes(str(random.randint(10000, 30000)), "utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)),"utf-8") + u2py.VM + bytes(str(random.randint(10000, 30000)), "utf-8")
        transaction_file.writev(transactionId, 223, data)


        data = bytes(str(commSaleAmount1), "utf-8") + u2py.VM + bytes(str(commSaleAmount2),"utf-8") + u2py.VM + bytes(str(commSaleAmount3), "utf-8")
        transaction_file.writev(transactionId, 241, data)

        data = bytes(str(commRate), "utf-8") + u2py.VM + bytes(str(commRate),"utf-8") + u2py.VM + bytes(str(commRate), "utf-8")
        transaction_file.writev(transactionId, 242, data)

        if commEmplId != 'nan':
            data = bytes(commEmplId, "utf-8") + u2py.VM + bytes(commEmplId, "utf-8") + u2py.VM + bytes(commEmplId, "utf-8")
            transaction_file.writev(transactionId, 244, data)

        data = bytes(str(commEmplPercentUsed), "utf-8") + u2py.VM + bytes(str(commEmplPercentUsed), "utf-8") + u2py.VM + bytes(str(commEmplPercentUsed), "utf-8")
        transaction_file.writev(transactionId, 245, data)

        data = bytes(str(commEmplType), "utf-8") + u2py.VM + bytes(str(commEmplType),"utf-8") + u2py.VM + bytes(str(commEmplType), "utf-8")
        transaction_file.writev(transactionId, 246, data)

        employee_file.writev(commEmplId,1,firstName)

        employee_file.writev(commEmplId, 2,lastName)

        employee_file.writev(commEmplId,17,firstName[0:3].upper()+str(random.randint(10,100)))

        employee_file.writev(commEmplId,27,firstName)

        kg_employee_file.writev(employeeId,1,kg_em_first_name)
        
        kg_employee_file.writev(employeeId,2,kg_em_last_name)
        
        print('{} created {}'.format(transactionId,i))


save_mock_data()

