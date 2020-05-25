import json
import u2py
import pandas as pd
import random
import math


def trans1(filename, transId):
    data = bytes("MTR1", "utf-8") + u2py.VM + bytes("MTR1", "utf-8") + u2py.VM + bytes("MTR1", "utf-8")
    filename.writev(transId, 6, data)

    filename.writev(transId, 7, 'VSAL')

    data = bytes("5K6985523", "utf-8") + u2py.VM + bytes("58K385572", "utf-8") + u2py.VM + bytes("890880000", "utf-8")
    filename.writev(transId, 9, data)

    data = bytes("109.50", "utf-8") + u2py.VM + bytes("109.50", "utf-8") + u2py.VM + bytes("149.99", "utf-8")
    filename.writev(transId, 11, data)

    data = bytes("60.98", "utf-8") + u2py.VM + bytes("85.24", "utf-8") + u2py.VM + bytes("83.53", "utf-8")
    filename.writev(transId, 12, data)

    data = bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8")
    filename.writev(transId, 13, data)

    data = bytes("CK BT INFINITE", "utf-8") + u2py.VM + bytes("CKBT INFINITE", "utf-8") + u2py.VM + bytes(
        "SKY ROLL LUGGAG", "utf-8")
    filename.writev(transId, 14, data)

    data = bytes("0.00", "utf-8")+ u2py.SM + bytes("01.00", "utf-8") + u2py.VM + bytes("54.75", "utf-8") + u2py.SM + bytes("02.00", "utf-8")
    filename.writev(transId, 45, data)

    data = bytes("M", "utf-8") + u2py.VM + bytes("P", "utf-8") + u2py.VM + bytes("D", "utf-8")
    filename.writev(transId, 77, data)

    filename.writev(transId, 90, "776768")

    filename.writev(transId, 141, 'CF.CANCEL')

    data = bytes("13", "utf-8") + u2py.VM + bytes("13", "utf-8") + u2py.VM + bytes("13", "utf-8")
    filename.writev(transId, 159, data)

    data = bytes("48.52", "utf-8") + u2py.VM + bytes("24.26", "utf-8") + u2py.VM + bytes("66.46", "utf-8")
    filename.writev(transId, 241, data)

    data = bytes("0.05", "utf-8") + u2py.VM + bytes("0.05", "utf-8") + u2py.VM + bytes("0.05", "utf-8")
    filename.writev(transId, 242, data)

    data = bytes("226183", "utf-8") + u2py.VM + bytes("226183", "utf-8") + u2py.VM + bytes("226183", "utf-8")
    filename.writev(transId, 244, data)

    data = bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8")
    filename.writev(transId, 245, data)

    data = bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes(
        "TMW*CONS*SALECNS", "utf-8")
    filename.writev(transId, 246, data)

    filename = u2py.File('EM')
    filename.writev("226183", 1, 'TYNER')
    filename.writev("226183", 2, 'MICHAEL')
    filename.writev("226183", 17, 'MCT10')

# -------------------------------------------------------------------------------------------


def trans2(filename, transId):
    data = bytes("N", "utf-8") + u2py.VM + bytes("N", "utf-8") + u2py.VM + bytes("N", "utf-8")
    filename.writev(transId, 6, data)

    filename.writev(transId, 7, 'VSAL')

    data = bytes("226Z42023", "utf-8") + u2py.VM + bytes("226Z42016", "utf-8") + u2py.VM + bytes("000880000", "utf-8")
    filename.writev(transId, 9, data)

    data = bytes("99", "utf-8") + u2py.VM + bytes("99", "utf-8") + u2py.VM + bytes("8.00", "utf-8")
    filename.writev(transId, 11, data)

    data = bytes("59.01", "utf-8") + u2py.VM + bytes("59.01", "utf-8") + u2py.VM + bytes("0", "utf-8")
    filename.writev(transId, 12, data)

    data = bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8")
    filename.writev(transId, 13, data)

    data = bytes("JA SATEEN TWILL", "utf-8") + u2py.VM + bytes("JA SATEEN TWILL", "utf-8") + u2py.VM + bytes(
        "SHIPPING CHARGE", "utf-8")
    filename.writev(transId, 14, data)

    data = bytes(" ", "utf-8") + u2py.VM + bytes(" ", "utf-8") + u2py.VM + bytes(" ", "utf-8")
    filename.writev(transId, 45, data)

    data = bytes("M", "utf-8") + u2py.VM + bytes("P", "utf-8") + u2py.VM + bytes("D", "utf-8")
    filename.writev(transId, 77, data)

    filename.writev("8101*3460468", 141, 'CF.CANCEL')

    data = bytes("39.99", "utf-8") + u2py.VM + bytes("39.99", "utf-8") + u2py.VM + bytes("8", "utf-8")
    filename.writev(transId, 241, data)

    data = bytes("0", "utf-8") + u2py.VM + bytes("0", "utf-8") + u2py.VM + bytes("0", "utf-8")
    filename.writev(transId, 242, data)

    data = bytes("999999", "utf-8") + u2py.VM + bytes("999999", "utf-8") + u2py.VM + bytes("999999", "utf-8")
    filename.writev(transId, 244, data)

    data = bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8")
    filename.writev(transId, 245, data)

    data = bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes(
        "TMW*CONS*SALECNS", "utf-8")
    filename.writev(transId, 246, data)

    filename = u2py.File('EM')
    filename.writev("999999", 17, 'MCT10')


def trans3(filename, transId):
    data = bytes("MTR1", "utf-8") + u2py.VM + bytes("MTR1", "utf-8") + u2py.VM + bytes("MTR1", "utf-8")
    filename.writev(transId, 6, data)

    filename.writev(transId, 7, 'VSAL')

    data = bytes("5K6985523", "utf-8") + u2py.VM + bytes("58K385572", "utf-8") + u2py.VM + bytes("890880000", "utf-8")
    filename.writev(transId, 9, data)

    data = bytes("109.50", "utf-8") + u2py.VM + bytes("109.50", "utf-8") + u2py.VM + bytes("149.99", "utf-8")
    filename.writev(transId, 11, data)

    data = bytes("60.98", "utf-8") + u2py.VM + bytes("85.24", "utf-8") + u2py.VM + bytes("83.53", "utf-8")
    filename.writev(transId, 12, data)

    data = bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8")
    filename.writev(transId, 13, data)

    data = bytes("CK BT INFINITE", "utf-8") + u2py.VM + bytes("CKBT INFINITE", "utf-8") + u2py.VM + bytes(
        "SKY ROLL LUGGAG", "utf-8")
    filename.writev(transId, 14, data)

    data = bytes("0.00", "utf-8") + u2py.VM + bytes("54.75", "utf-8")
    filename.writev(transId, 45, data)

    data = bytes("M", "utf-8") + u2py.VM + bytes("P", "utf-8") + u2py.VM + bytes("D", "utf-8")
    filename.writev(transId, 77, data)

    filename.writev(transId, 141, 'CF.CANCEL')

    data = bytes("13", "utf-8") + u2py.VM + bytes("13", "utf-8") + u2py.VM + bytes("13", "utf-8")
    filename.writev(transId, 159, data)

    data = bytes("48.52", "utf-8") + u2py.VM + bytes("24.26", "utf-8") + u2py.VM + bytes("66.46", "utf-8")
    filename.writev(transId, 241, data)

    data = bytes("0.05", "utf-8") + u2py.VM + bytes("0.05", "utf-8") + u2py.VM + bytes("0.05", "utf-8")
    filename.writev(transId, 242, data)

    data = bytes("226183", "utf-8") + u2py.VM + bytes("226183", "utf-8") + u2py.VM + bytes("226183", "utf-8")
    filename.writev(transId, 244, data)

    data = bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8")
    filename.writev(transId, 245, data)

    data = bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes(
        "TMW*CONS*SALECNS", "utf-8")
    filename.writev(transId, 246, data)

    filename = u2py.File('EM')
    filename.writev("226183", 1, 'TYNER')
    filename.writev("226183", 2, 'MICHAEL')
    filename.writev("226183", 17, 'MCT10')


def sampleTransaction(filename,transId):
    data = bytes("545123", "utf-8") + u2py.VM + bytes("226183", "utf-8") + u2py.VM + bytes("667889", "utf-8")+u2py.VM + bytes('664098','utf-8')
    filename.writev(transId, 244, data)

    data = bytes("DESC 1", "utf-8") + u2py.VM + bytes("DESC 2", "utf-8") + u2py.VM + bytes("DESC 3", "utf-8") + u2py.VM + bytes("DESC 4", "utf-8")
    filename.writev(transId, 14, data)

    data = bytes("148.59", "utf-8") + u2py.VM + bytes("57.21", "utf-8") + u2py.VM + bytes("98.56", "utf-8") + u2py.VM + bytes("234.89", "utf-8")
    filename.writev(transId, 241, data)

    data = bytes("2", "utf-8") + u2py.VM + bytes("3", "utf-8") + u2py.VM + bytes("4", "utf-8") + u2py.VM + bytes("5", "utf-8")
    filename.writev(transId, 13, data)

    filename.writev(transId, 7, 'VSAL')

    filename.writev(transId, 141, 'CF.CANCEL')

    data = bytes("RENTAL ID 1", "utf-8") + u2py.VM + bytes("RENTAL ID 2", "utf-8") + u2py.VM + bytes("RENTAL ID 3","utf-8") + u2py.VM + bytes("RENTAL ID 3", "utf-8")
    filename.writev(transId,90, data)

    data = bytes("13", "utf-8") + u2py.VM + bytes("13", "utf-8") + u2py.VM + bytes("13", "utf-8") + u2py.VM + bytes("13", "utf-8")
    filename.writev(transId, 159, data)

    data = bytes("1", "utf-8") + u2py.SM + bytes("2", "utf-8") + u2py.VM + bytes("3", "utf-8") + u2py.SM + bytes("4", "utf-8")+ u2py.VM + bytes("5", "utf-8") + u2py.SM + bytes("6", "utf-8") + u2py.VM + bytes("7", "utf-8") + u2py.SM + bytes("8", "utf-8")
    filename.writev(transId, 45, data)

    data = bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8") + u2py.VM + bytes("1", "utf-8")
    filename.writev(transId, 167, data)

    data = bytes("109.50", "utf-8") + u2py.VM + bytes("457.50", "utf-8") + u2py.VM + bytes("149.99", "utf-8") + u2py.VM + bytes("567.99", "utf-8")
    filename.writev(transId, 11, data)

    data = bytes("60.98", "utf-8") + u2py.VM + bytes("85.24", "utf-8") + u2py.VM + bytes("83.53", "utf-8")+ u2py.VM + bytes("23.53", "utf-8")
    filename.writev(transId, 12, data)

    data = bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes("TMW*CONS*SALECNS", "utf-8") + u2py.VM + bytes("TMW*CONS*SALECNS", "utf-8")
    filename.writev(transId, 246, data)

    data = bytes("5K6985523", "utf-8") + u2py.VM + bytes("58K385572", "utf-8") + u2py.VM + bytes("890880000", "utf-8")+ u2py.VM + bytes("58K385572", "utf-8")
    filename.writev(transId, 9, data)

    data = bytes("0.05", "utf-8") + u2py.VM + bytes("0.05", "utf-8") + u2py.VM + bytes("0.05", "utf-8") + u2py.VM + bytes("0.05", "utf-8")
    filename.writev(transId, 242, data)

    data = bytes("MTR1", "utf-8") + u2py.VM + bytes("MTR1", "utf-8") + u2py.VM + bytes("MTR1", "utf-8") + u2py.VM + bytes("MTR1", "utf-8")
    filename.writev(transId, 6, data)

    data = bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8") + u2py.VM + bytes("100", "utf-8")
    filename.writev(transId, 245, data)
    sampleEm()


def sampleEm():
    filename = u2py.File('EM')
    filename.writev("545123", 1, 'IJK')
    filename.writev("545123", 2, 'MNO')
    filename.writev("545123", 17, 'MCT10')

    filename = u2py.File('EM')
    filename.writev("226183", 1, 'ABC')
    filename.writev("226183", 2, 'DEF')
    filename.writev("226183", 17, 'MCT10')

    filename = u2py.File('EM')
    filename.writev("667889", 1, 'PQR')
    filename.writev("667889", 2, 'STU')
    filename.writev("667889", 17, 'MCT10')

    filename = u2py.File('EM')
    filename.writev("667889", 1, 'VWX')
    filename.writev("667889", 2, 'YZ')
    filename.writev("667889", 17, 'MCT10')


def save_mock_data():
    transaction_file = u2py.File('TRANSACTION')
    employee_file = u2py.File('EM')
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

        transaction_file.writev(transactionId, 49, shipComment)

        transaction_file.writev(transactionId, 51, shipFName)

        transaction_file.writev(transactionId, 52, shipLName)

        transaction_file.writev(transactionId, 53, shipAddr)

        transaction_file.writev(transactionId, 54, shipCity)

        transaction_file.writev(transactionId, 55, shipState)

        transaction_file.writev(transactionId, 56, shipZip)

        transaction_file.writev(transactionId, 57, shipDate)

        transaction_file.writev(transactionId, 58, mbaOrderId)

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

        transaction_file.writev(transactionId, 82, maskedAcctNo)

        data = bytes(str(rentalId), "utf-8") + u2py.VM + bytes(str(rentalId), "utf-8") + u2py.VM + bytes(str(rentalId), "utf-8")
        transaction_file.writev(transactionId, 90, data)

        data = bytes(shipCarrier1, "utf-8") + u2py.VM + bytes(shipCarrier2, "utf-8") + u2py.VM + bytes(shipCarrier3,"utf-8")
        transaction_file.writev(transactionId, 104, data)

        data = bytes(shipTrackNo1, "utf-8") + u2py.VM + bytes(shipTrackNo2, "utf-8") + u2py.VM + bytes(shipTrackNo3,"utf-8")
        transaction_file.writev(transactionId, 105, data)

        data = bytes(couponCode1, "utf-8") + u2py.VM + bytes(couponCode2, "utf-8") + u2py.VM + bytes(couponCode3,"utf-8")
        transaction_file.writev(transactionId, 128, data)

        transaction_file.writev(transactionId, 129, signMethod)

        transaction_file.writev(transactionId, 135, pfPoints)

        transaction_file.writev(transactionId, 141, transactionSubType)


        if discountType != 'nan':
            data = bytes(str(discountType), "utf-8") + u2py.VM + bytes(str(discountType), "utf-8") + u2py.VM + bytes(str(discountType), "utf-8")
            transaction_file.writev(transactionId, 159, data)

        data = bytes(discountPodType1, "utf-8") + u2py.VM + bytes(discountPodType2, "utf-8") + u2py.VM + bytes(discountPodType3, "utf-8")
        transaction_file.writev(transactionId, 160, data)

        data = bytes(discountPodAmt1, "utf-8") + u2py.VM + bytes(discountPodAmt2, "utf-8") + u2py.VM + bytes(discountPodAmt3, "utf-8")
        transaction_file.writev(transactionId, 161, data)

        data = bytes(discountReasonCode1, "utf-8") + u2py.VM + bytes(discountReasonCode2, "utf-8") + u2py.VM + bytes(discountReasonCode3, "utf-8")
        transaction_file.writev(transactionId, 163, data)

        data = bytes(promosId1, "utf-8") + u2py.VM + bytes(promosId2, "utf-8") + u2py.VM + bytes(promosId3, "utf-8")
        transaction_file.writev(transactionId, 165, data)

        data = bytes(inAddMrkdn1, "utf-8") + u2py.VM + bytes(inAddMrkdn2, "utf-8") + u2py.VM + bytes(inAddMrkdn3, "utf-8")
        transaction_file.writev(transactionId, 166, data)

        data = bytes(str(discountConversion), "utf-8") + u2py.VM + bytes(str(discountConversion), "utf-8") + u2py.VM + bytes(str(discountConversion), "utf-8")
        transaction_file.writev(transactionId, 167, data)

        transaction_file.writev(transactionId, 214, '676987')

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

        employee_file.writev(commEmplId, 17,'MKT10')

        print('{} created {}'.format(transactionId,i))


save_mock_data()


# files = u2py.File('TRANSACTION')transaction_file.writev(transactionId,13,data)
#
# sampleTransaction(files,'TRANS')
#
# if rental_id != '':
#     discount_type = [int(key['DISCOUNT.TYPE']) for key in transaction_data['DISCOUNT.TYPE_MV']]
#     if len(discount_type) != 1 and discount_type[0] != '':
#         discount_line = transaction_file.readv(transaction_data['_ID'], 45)
#         discount = [float(x[0]) for x in discount_line]
#         discount_sum = sum(discount)
#         if discount_sum != 0:
#             search_count = discount_line.dcount(u2py.SM) + 1
#             for i in range(search_count):
#                 discount_line = list(discount_line)
#                 if float(discount_line[i][0]) > 0:
#                     discount_conversion = list(transaction_file.readv(transaction_data['_ID'], 167))
#                     break
#             if discount_conversion[0][0] != '':
#                 unconverted_discount_amount = 0
#             else:
#                 unconverted_discount_amount = discount_sum
# else:
#     unconverted_discount_amount = 0
#
# for i in range(len(retail_list)):
#     qty = quantity_list[i]
#     total = (retail_list[i] - mkdn_list[i]) * qty
#     total = total - unconverted_discount_amount
#     trans_sale_total = trans_sale_total + total
#     qty = qty * xmul
#     commission_sales_total = commission_sales_total + (commission_sale_amount[i] * qty)

# def set_description(transaction_data,transaction_file,employee_file):
#     description = transaction_file.readv(transaction_data['_ID'],14)
#     description_list = []
#     for i in range(1,len(list(description))+1):
#         temp_desc_list = []
#         value = description.extract(i)
#         if value.dcount(u2py.SM) > 1:
#             desc = value.extract(i,1)
#             if desc[1:6] != 'SJFILE':
#                 temp_desc_list.append(desc)
#             temp_desc_list.append(value.extract(i,2))
#
#             sub_count = value.dcount(u2py.SM)
#             for j in range(3,sub_count):
#                 sub_value = value.extract(i,j)
#                 if sub_value != '':
#                     try:
#                         sname = list(employee_file.readv(sub_value,17))[0][0]
#                         temp_desc_list.append(sname)
#                     except u2py.U2Error:
#                         temp_desc_list.append(sub_value)
#                 else:
#                     temp_desc_list.append(sub_value)
#         # elif value.extract(i,1)[1:10] == 'GIFT CARD-':
#         #     temp_desc_list.append(value.extract(i,1))
#         else:
#             print(list(description))
#             # description_list.append(list(description)[i][0])
#     return description_list