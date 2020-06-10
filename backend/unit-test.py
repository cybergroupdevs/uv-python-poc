import u2py
import unittest
import requests


class customerTests(unittest.TestCase):
    def test_get_customer(self):
        obj = PocTest()
        print("-------customer---")
        data =
            {
                "phoneNo": "988012-21",
                "firstName": "DERRICK",
                "lastName": "ROSE",
                "address": "S9 FULLER ROAD",
                "city": "SAN HOSE",
                "zipCode": "2210291",
                "altPhoneNo": "8054544097",
                "pfid": "7462133"
            }
        self.assertEqual(obj.customer(), data)


class customerHistoryTests(unittest.TestCase):
    def test_get_customer_history(self):
        obj = PocTest()
        print("--customerHistoryMultiple--")
        data = {
    "customerHistory": [
        {
            "firstName": "Ruprecht",
            "lastName": "Batter",
            "address": "8 Carberry Way",
            "city": "Sioux Falls",
            "pf": "pf"
        },
        {
            "firstName": "Ervin",
            "lastName": "Mottershaw",
            "address": "518 Corscot Road",
            "city": "Charlottesville",
            "pf": "pf"
        },
        {
            "firstName": "Ranice",
            "lastName": "Aidler",
            "address": "7841 Mccormick Drive",
            "city": "Los Angeles",
            "pf": "pf"
        },
        {
            "firstName": "Agnes",
            "lastName": "Marcroft",
            "address": "67 Lakewood Gardens Way",
            "city": "Pittsburgh",
            "pf": "pf"
        },
        {
            "firstName": "Andrus",
            "lastName": "Copcutt",
            "address": "50 Crest Line Lane",
            "city": "Greensboro",
            "pf": "pf"
        }
    ],
    "count": 29
}
        self.assertEqual(obj.customer_history(), data)

    def test_get_customer_history_empty(self):
        obj = PocTest()
        print("--No history--")
        data = {"customerHistory":["No customer History available"],"count":0}
        self.assertEqual(obj.customer_history_empty(), data)
class consultantTests(unittest.TestCase):

    def test_get_consultant_empty(self):
        #Noconsultant is there
        obj = PocTest()
        print("-No consultant-")
        data = {"operator": "RON SIMS (SION)", "SLS CONSULT": "No consultant"}
        self.assertEqual(obj.consultant_empty(), data)

    def test_get_consultant_operator(self):
        # firstNameLastName(operator)
        obj = PocTest()
        print("-operator-FirstName-")
        data = {"operator": "RON SIMS (SION)", "SALECNS": "RON SIMS (SION)"}
        self.assertEqual(obj.consultant_operator(), data)

    def test_get_consultant_src(self):
        # srcAssoc
        obj = PocTest()
        print("-srcAssoc-")
        data = 
            {"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)", "SRC ASSOC": "LEBRON JAMES (LBJ)"}
        self.assertEqual(obj.consultant_src(), data)

    def test_get_consultant_sales(self):
        # salesCns
        obj = PocTest()
        print("-------salesCns-----")
        data =
            {"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)"}
        self.assertEqual(obj.consultant_sales(), data)

    def test_get_consultant_business_name(self):
        # businessName
        obj = PocTest()
        print("-------businessName----")
        data = 
            {"operator": "RON SIMS (SION)", "SLS CONSULT": "RON SIMS (SION)"}
        self.assertEqual(obj.consultant_business_name(), data)


class PocTest():
    def customer(self):
        data = requests.get(
            'http://127.0.0.1:5000/customer?customerId=0001')
        return data.json()
    def consultant_sales(self):
        data = requests.get(
            'http://127.0.0.1:5000/consultant?transactionId=999888')
        return data.json()
    def consultant_src(self):
        data = requests.get(
            'http://127.0.0.1:5000/consultant?transactionId=000111')
        return data.json()
    def consultant_operator(self):
        data = requests.get(
            'http://127.0.0.1:5000/consultant?transactionId=222111')
        return data.json()
    def consultant_empty(self):
        data = requests.get(
            'http://127.0.0.1:5000/consultant?transactionId=555666')
        return data.json()
    def consultant_business_name(self):
        data = requests.get(
            'http://127.0.0.1:5000/consultant?transactionId=444555')
        return data.json()
    def customer_history(self):
        data = requests.get(
            'http://127.0.0.1:5000/customer/history?phoneNo=804-334-6333&pageIndex=0&pageSize=5')
        return data.json()
    def customer_history_empty(self):
        data = requests.get(
            'http://127.0.0.1:5000/customer/history?phoneNo=637382228&pageIndex=0&pageSize=5')
        return data.json()
    def consultant(self):
        data=requests.get(
            'http://127.0.0.1:5000/consultant?transactionId=999888')
        return data.json()

class CommissionData():
    def __init__(self):
        self.commission_details = {
            "class": "4926",
            "sku": "6856",
            "retail": "190.78",
            "mkdn": "58.37",
            "quantity": "1",
            "desc": "rhoncus mauris enim",
            "commissionType": "MTR1",
            "amount": "15.55",
            "employeePercentage": "56",
            "salePercentage": "100",
            "employeeShortname": "MOY61",
            "employeeCommissionType": "SALECNS"
        }

    def commission_details_list(self):
        return self.commission_details

    def commission_detail_error(self):
        return "No commission information for this transaction Id"


class CreditCardData():
    def __init__(self):
        self.credit_card_details = {
            "sent": "02:52:29pm",
            "rcvd": "03:28:16pm",
            "done": "04:59:30pm",
            "type": "BCRD",
            "entry": "RENTR",
            "auth": "AUTO APPROVED"
        }


class CommissionTestCases(unittest.TestCase):
    def test_commission_list(self):
        obj = CommissionData()
        response = requests.get("http://127.0.0.1:5000/commission/4830*35*1672")
        data = response.json()['commissionList']
        self.assertEqual(data[0],obj.commission_details_list())
    
    def test_commission_data(self):
        obj = CommissionData()
        response = requests.get("http://127.0.0.1:5000/commission/5823*83*2072")
        data = response.json()['error']
        self.assertEqual(data,obj.commission_detail_error())


    def test_credit_card_details(self):
        obj = CreditCardData()
        response = requests.get("http://127.0.0.1:5000/transaction/4830*35*1672/creditCard/authentication")
        data = response.json()['cardDetails'][0]
        print(data)
        self.assertEqual(data,obj.credit_card_details)

if __name__ == '__main__':
    unittest.main()
