import u2py
import unittest
import requests
class customerTests(unittest.TestCase):
	def test_get_customer(self):
		obj=PocTest()
		print("-------customer---")
		data=[
     		{
         	"phoneNo": "988012-21",
         	"firstName": "DERRICK",
         	"lastName": "ROSE",
         	"address": "S9 FULLER ROAD",
         	"city": "SAN HOSE",
         	"state": "CALIFORNIA",
         	"zip": "2210291",
         	"altPhoneNo": "988012-52",
        	"pfid": "7462133"
    		}
	 	]
		self.assertEqual(obj.customer(),data)
class customerHistoryTests(unittest.TestCase):
	def test_get_customerHistory1(self):
		obj=PocTest()
		print("--customerHistory-")
		data=[
     		{
         	"firstName": "DERRICK",
         	"lastName": "ROSE",
         	"address": "S9 FULLER ROAD",
         	"city": "SAN HOSE",
        	"pf": "pf"
    		}
	 	]
		self.assertEqual(obj.customer_history(),data)
	def test_get_customerHistory2(self):
		obj=PocTest()
		print("--customerHistory--")
		data=[
     		{
         	"firstName": "DERRICK",
         	"lastName": "ROSE",
         	"address": "S9 FULLER ROAD",
         	"city": "SAN HOSE",
        	"pf": ""
    		}
	 	]
		self.assertEqual(obj.customer_history(),data)
	def test_get_customerHistory2(self):
		obj=PocTest()
		print("--customerHistoryMultiple--")
		data=[
    	{
        "firstName": "RICK",
        "lastName": "SANCHEZ",
        "address": "PLANET EARTH",
        "city": "SEATTLE",
        "pf": ""
    	},
    	{
        "firstName": "DERRICK",
        "lastName": "ROSE",
        "address": "S9 FULLER ROAD",
        "city": "SAN HOSE",
        "pf": "pf"
    	}
		]
		self.assertEqual(obj.customer_history(),data)
class consultantTests(unittest.TestCase):
    
	def test_get_consultant5(self):
		#Noconsultant is there
		obj=PocTest()
		print("-No consultant-")
		data=[{"operator": "RON SIMS (SION)", "SALECNS": "No consultant"}]
		self.assertEqual(obj.consultant(),data)
	def test_get_consultant4(self):
		#firstNameLastName(operator)
		obj=PocTest()
		print("-operator-FirstName-")
		data=[{"operator": "RON SIMS (SION)", "SALECNS": "RON SIMS (SION)"}]
		self.assertEqual(obj.consultant(),data)
	def test_get_consultant3(self):
		#srcAssoc
		obj=PocTest()
		print("-srcAssoc-")
		data=[{"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)", "SRC ASSOC": "LEBRON JAMES (LBJ)"}]
		self.assertEqual(obj.consultant(),data)
	def test_get_consultant2(self):
		#salesCns
		obj=PocTest()
		print("-------salesCns-----")
		data=[{"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)"}]
		self.assertEqual(obj.consultant(),data)
	def test_get_consultant1(self):
		#businessName
		obj=PocTest()
		print("-------businessName----")
		data=[{"operator": "SHOUT INC SIMS (SION)", "SLS CONSULT": "RON SIMS (SION)"}]
		self.assertEqual(obj.consultant(),data)
class PocTest():
	def customer(self):
		data=requests.get('http://127.0.0.1:5000/api/customer?customerId=0001')
		return data.json()
	def consultant(self):
		data=requests.get('http://127.0.0.1:5000/api/consultant?transactionId=999888')
		return data.json()
	def customer_history(self):
		data=requests.get('http://127.0.0.1:5000/api/customer/history?phoneNo=8054544097&pageIndex=0&pageSize=5')
		return data.json()

class CommissionData():
    def __init__(self):
        self.commission_details = {
            "class": "4929",
            "sku": "9167",
            "retail": "190.78",
            "mkdn": "58.37",
            "quantity": "1",
            "desc": "rhoncus mauris enim",
            "commissionType": "MTR1",
            "amount": "15.55",
            "employeePercentage": "56",
            "salePercentage": "100",
            "commEmpId": "MKT10",
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
