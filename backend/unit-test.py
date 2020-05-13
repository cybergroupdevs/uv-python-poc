import u2py
import unittest
import requests
class apiTests(unittest.TestCase):
    
	# def test_get_helloworld(self):
	# 	obj=customerTest()
	# 	print("-------sdad-")
	# 	data=[
    # 		{
    #     	"phoneNo": "988012-21",
    #     	"firstName": "DERRICK",
    #     	"lastName": "ROSE",
    #     	"address": "S9 FULLER ROAD",
    #     	"city": "SAN HOSE",
    #     	"state": "CALIFORNIA",
    #     	"zip": "2210291",
    #     	"altPhoneNo": "988012-52",
    #     	"pfid": "7462133"
    #		}
	# 	]
	#	self.assertEqual(obj.customer(),data)
	def test_get_consultant3(self):
		#firstNameLastName(operator)
		obj=pocTest()
		print("-srcAssoc-")
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
		data=requests.get('http://127.0.0.1:5000/api/customer')
		print(data.json())
		return data.json()
	def consultant(self):
		data=requests.get('http://127.0.0.1:5000/api/consultant')
		return data.json()
if __name__ == '__main__':
    unittest.main()
