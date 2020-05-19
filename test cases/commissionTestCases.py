import unittest
import requests


class CommissionData():
    def __init__(self):
        self.commission_details = {
            'class': '5K69',
            'sku': '85523',
            'retail': '109.50',
            'mkdn': '60.98',
            'quantity': '1',
            'desc': 'CK BT INFINITE',
            'commission_type': 'MTR1',
            'amount': '48.52',
            'employee_percentage': '5',
            'sale_percentage': '100',
            'commission_emp_id': 'MCT10',
            'employee_commission_type': 'SALECNS'
        }

    def commission_details_list(self):
        return self.commission_details

    def commission_detail_error(self):
        return "No commission information for this transaction Id"

    def consult_name(self):
        return "NO CONSULTANT"


class TestCases(unittest.TestCase):
    def test_commission_list(self):
        obj = CommissionData()
        response = requests.get("http://localhost:5000/commission/1234*12*4321")
        data = response.json()['commissionList']
        self.assertEqual(data[0],obj.commission_details_list())

    def test_commission_data(self):
        obj = CommissionData()
        response = requests.get("http://localhost:5000/commission/9876*00*1234")
        data = response.json()['error']
        self.assertEqual(data,obj.commission_detail_error())

    def test_consultant_name(self):
        obj = CommissionData()
        response = requests.get("http://localhost:5000/commission/8101*3460468")
        data = response.json()['consultantName']
        self.assertEqual(data,obj.consult_name())
        self.assertEqual(data,obj.consult_name())


if __name__ == '__main__':
    unittest.main()
