import unittest
import requests


class CommissionData():
    def __init__(self):
        self.commissionsDetails = {
            'class': '5K69',
            'sku': '85523',
            'retail': '109.50',
            'mkdn': '60.98',
            'quantity': '1',
            'desc': 'CK BT INFINITE',
            'commissionType': 'MTR1',
            'amount': '48.52',
            'empPercentage': '5',
            'salePercentage': '100',
            'commEmpId': 'MCT10',
            'empCommissionType': 'SALECNS'
        }

    def commissionDetailsList(self):
        return self.commissionsDetails

    def commissionDetailError(self):
        return "No commission information for this transaction Id"

    def consultName(self):
        return "NO CONSULTANT"


class TestCases(unittest.TestCase):
    def testCommissionList(self):
        obj = CommissionData()
        response = requests.get("http://localhost:5000/commission/1234*12*4321")
        data = response.json()['commissionList']
        self.assertEqual(data[0],obj.commissionDetailsList())

    def testCommissionData(self):
        obj = CommissionData()
        response = requests.get("http://localhost:5000/commission/9876*00*1234")
        data = response.json()['error']
        self.assertEqual(data,obj.commissionDetailError())

    def testConsultantName(self):
        obj = CommissionData()
        response = requests.get("http://localhost:5000/commission/8101*3460468")
        data = response.json()['consultantName']
        self.assertEqual(data,obj.consultName())


if __name__ == '__main__':
    unittest.main()