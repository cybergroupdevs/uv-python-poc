import u2py
from flask import Flask, Response
import json

from flask_cors import CORS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisisthesercretkey'
CORS(app)
commission

def convertFieldFormats(fieldData, fieldFormat, format):
    data = u2py.DynArray()
    data.insert(1, 0, 0, fieldData)
    if format == 'external':
        formattedData = str(data.extract(1).oconv(fieldFormat))
    else:
        formattedData = str(data.extract(1).iconv(fieldFormat))
    return formattedData


def checkExistingRecord(fileObject, recordID):
    try:
        fileObject.read(recordID)
        return True
    except u2py.U2Error:
        return False


def calculateXmul(transactionFile, recordId):
    transactionType = list(transactionFile.readv(recordId, 7))[0][0]
    transSubType = list(transactionFile.readv(recordId, 141))[0][0]
    if transactionType == 'VSAL':
        if transSubType == 'CF.CANCEL':
            xmul = 1
        else:
            xmul = -1
    else:
        xmul = 1
    return xmul


def calculateAmount(transactionFile, recordId, itemQuantity):
    amountList = []
    commSaleAmount = list(transactionFile.readv(recordId, 241))
    xmul = calculateXmul(transactionFile, recordId)
    for i in range(len(commSaleAmount)):
        amount = float(commSaleAmount[i][0])
        if amount != 0:
            quantity = int(itemQuantity[i][0]) * xmul
            amount = convertFieldFormats(amount * quantity * 100, 'MD2', 'external')
            amountList.append(amount)
        else:
            amountList.append(' ')

    return amountList


def calculateCommissionAmount(transactionFile,recordId,emplId,itemQty):
    xmul = calculateXmul(transactionFile, recordId)
    commissionAmount = 0
    commSaleAmount = list(transactionFile.readv(recordId, 241))
    for i in range(len(emplId)):
        quantity = xmul * int(itemQty[i][0])
        commissionAmount = commissionAmount + float(commSaleAmount[i][0])* quantity
    return commissionAmount


def setEmpsnValues(transactionFile, emFile, recordId):
    empsnList = []
    commEmpId = list(transactionFile.readv(recordId, 244))

    for i in range(len(commEmpId)):
        empId = commEmpId[i][0]
        if checkExistingRecord(emFile, empId):
            empsn = list(emFile.readv(empId, 17))[0][0]
        else:
            empsn = empId
        empsnList.append(empsn)

    return empsnList


def setEmpTotal(transactionFile, recordId, retail, mkdn, itemQty):
    rentalId = list(transactionFile.readv(recordId, 91))
    commSaleAmount = list(transactionFile.readv(recordId, 241))
    transSaleTotal = 0
    commSalesTotal = 0
    discConvToMkdn = ''
    unconvertedDiscAmt = 0
    if len(rentalId) != 1 and rentalId[0][0] != '':
        discountType = list(transactionFile.readv(recordId, 159))
        if len(discountType) != 1 and discountType[0][0] != '':
            discountLine = transactionFile.readv(recordId, 45)
            discountSum = 0
            for discount in list(discountLine):
                if discount != '':
                    discountSum = discountSum + float(discount[0])
            if discountSum != 0:
                for discount in discountLine:
                    searchCount = discount.dcount(u2py.SM)
                    for i in range(1,searchCount):
                        value = discountLine[i].dcount(u2py.SM)
                        if value > 1:
                            discConvToMkdn = list(transactionFile.readv(recordId, 167))[i][0]
                            break
                    if discConvToMkdn:
                        unconvertedDiscAmt = 0
                    else:
                        unconvertedDiscAmt = discountSum
    else:
        unconvertedDiscAmt = 0

    xmul = calculateXmul(transactionFile, recordId)
    for i in range(len(retail)):
        qty = int(itemQty[i][0])
        total = (float(retail[i][0]) - float(mkdn[i][0])) * qty
        total = total - unconvertedDiscAmt
        transSaleTotal = transSaleTotal + total
        qty = qty * xmul
        commSalesTotal = commSalesTotal + (float(commSaleAmount[i][0]) * qty)

    return commSalesTotal


def calculateSalePercentage(commEmpId, emFile):
    empId = commEmpId[0]
    try:
        emRecord = list(emFile.readv(empId, 17))
    except u2py.U2Error:
        emRecord = empId
    return emRecord


def calculateCommEmpType(empType):
    empType = empType.split("*")[2]
    return empType


def setDescription(transactionFile, transId, markDown):
    pass


def readRecord(transactionFile,transId):
    data = {}
    data['commType'] = list(transactionFile.readv(transId, 6))
    data['itemNo'] = list(transactionFile.readv(transId, 9))
    data['retail'] = list(transactionFile.readv(transId, 11))
    data['mkdn'] = list(transactionFile.readv(transId, 12))
    data['itemQty'] = list(transactionFile.readv(transId, 13))
    data['desc'] = list(transactionFile.readv(transId, 14))
    data['commRate'] = list(transactionFile.readv(transId, 242))
    data['commEmpPerUsed'] = list(transactionFile.readv(transId, 245))
    data['commEmpType'] = list(transactionFile.readv(transId, 246))
    return data


def consultantName(emFile, employeeId):
    status = checkExistingRecord(emFile,employeeId)
    if status:
        fName = list(emFile.readv(employeeId, 1))[0][0]
        lName = list(emFile.readv(employeeId, 2))[0][0]
        sName = list(emFile.readv(employeeId, 17))[0][0]
        consultName = "{} {} ({})".format(fName,lName,sName)
    else:
        consultName = 'NO CONSULTANT'
    return consultName



@app.route('/commission/<transId>', methods=['GET'])
def commissionList(transId):
    commissionData = []
    transFilename = 'TRANSACTION'
    emFileName = 'EM'
    transFile = u2py.File(transFilename)
    emFile = u2py.File(emFileName)
    employeeId = list(transFile.readv(transId, 244))
    if employeeId[0][0] != '':
        recordData = readRecord(transFile,transId)
        setDescription(transFile,transId,recordData['mkdn'])
        amountList = calculateAmount(transFile, transId, recordData['itemQty'])
        empsnList = setEmpsnValues(transFile, emFile, transId)
        empTotal = setEmpTotal(transFile, transId, recordData['retail'], recordData['mkdn'], recordData['itemQty'])
        commissionAmount = calculateCommissionAmount(transFile,transId,employeeId,recordData['itemQty'])
        consultName = consultantName(emFile,employeeId[0][0])
        for i in range(len(recordData['desc'])):
            commData = {}
            commData['class'] = recordData['itemNo'][i][0][0:4]
            commData['sku'] = recordData['itemNo'][i][0][4:9]
            commData['retail'] = recordData['retail'][i][0]
            commData['mkdn'] = recordData['mkdn'][i][0]
            commData['quantity'] = recordData['itemQty'][i][0]
            commData['desc'] = recordData['desc'][i][0]
            commData['commissionType'] = recordData['commType'][i][0]
            commData['amount'] = amountList[i]
            commData['empPercentage'] = convertFieldFormats(recordData['commRate'][i][0], 'MD2', 'internal')
            commData['salePercentage'] = recordData['commEmpPerUsed'][i][0]
            commData['commEmpId'] = empsnList[i]
            commData['empCommissionType'] = calculateCommEmpType(recordData['commEmpType'][i][0])
            commissionData.append(commData)
        response = {
            'commissionList': commissionData,
            'retailAmount':empTotal,
            'commissionAmount':commissionAmount,
            'consultantName':consultName
        }
    else:
        response = {"error": "No commission information for this transaction Id"}
    return Response(json.dumps(response), status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run()
