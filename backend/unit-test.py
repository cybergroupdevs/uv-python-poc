import u2py
import unittest
import requests
class customerTests(unittest.TestCase):
	def test_get_customer(self):
		obj=pocTest()
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
		obj=pocTest()
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
		self.assertEqual(obj.customerHistory(),data)
	def test_get_customerHistory2(self):
		obj=pocTest()
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
		self.assertEqual(obj.customerHistory(),data)
	def test_get_customerHistory2(self):
		obj=pocTest()
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
		self.assertEqual(obj.customerHistory(),data)
class consultantTests(unittest.TestCase):
    
	def test_get_consultant5(self):
		#Noconsultant is there
		obj=pocTest()
		print("-No consultant-")
		data=[{"operator": "RON SIMS (SION)", "SALECNS": "No consultant"}]
		self.assertEqual(obj.consultant(),data)
	def test_get_consultant4(self):
		#firstNameLastName(operator)
		obj=pocTest()
		print("-operator-FirstName-")
		data=[{"operator": "RON SIMS (SION)", "SALECNS": "RON SIMS (SION)"}]
		self.assertEqual(obj.consultant(),data)
	def test_get_consultant3(self):
		#srcAssoc
		obj=pocTest()
		print("-srcAssoc-")
		data=[{"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)", "SRC ASSOC": "LEBRON JAMES (LBJ)"}]
		self.assertEqual(obj.consultant(),data)
	def test_get_consultant2(self):
		#salesCns
		obj=pocTest()
		print("-------salesCns-----")
		data=[{"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)"}]
		self.assertEqual(obj.consultant(),data)
	def test_get_consultant1(self):
		#businessName
		obj=pocTest()
		print("-------businessName----")
		data=[{"operator": "SHOUT INC SIMS (SION)", "SLS CONSULT": "RON SIMS (SION)"}]
		self.assertEqual(obj.consultant(),data)
class pocTest():
	def customer(self):
		data=requests.get('http://127.0.0.1:5000/api/customer?customerId=0001')
		return data.json()
	def consultant(self):
		data=requests.get('http://127.0.0.1:5000/api/consultant?transactionId=999888')
		return data.json()
	def customerHistory(self):
		data=requests.get('http://127.0.0.1:5000/api/customer/history?phoneNo=8054544097&pageIndex=0&pageSize=5')
		return data.json()
if __name__ == '__main__':
    unittest.main()
