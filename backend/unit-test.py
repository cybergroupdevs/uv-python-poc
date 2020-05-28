import u2py
import unittest
import requests


class customerTests(unittest.TestCase):
    def test_get_customer(self):
        obj = PocTest()
        print("-------customer---")
        data = [
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
        ]
        self.assertEqual(obj.customer(), data)


class customerHistoryTests(unittest.TestCase):
    def test_get_customerHistory(self):
        obj = PocTest()
        print("--customerHistoryMultiple--")
        data = [
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
        self.assertEqual(obj.customer_history(), data)

    def test_get_customerHistory_noHistory(self):
        obj = PocTest()
        print("--No history--")
        data = ["No customer History available"]
        self.assertEqual(obj.customer_history_noHistory(), data)
class consultantTests(unittest.TestCase):

    def test_get_consultant_empty(self):
        #Noconsultant is there
        obj = PocTest()
        print("-No consultant-")
        data = [{"operator": "RON SIMS (SION)", "SLS CONSULT": "No consultant"}]
        self.assertEqual(obj.consultant_empty(), data)

    def test_get_consultant_operator(self):
        # firstNameLastName(operator)
        obj = PocTest()
        print("-operator-FirstName-")
        data = [{"operator": "RON SIMS (SION)", "SALECNS": "RON SIMS (SION)"}]
        self.assertEqual(obj.consultant_operator(), data)

    def test_get_consultant_src(self):
        # srcAssoc
        obj = PocTest()
        print("-srcAssoc-")
        data = [
            {"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)", "SRC ASSOC": "LEBRON JAMES (LBJ)"}]
        self.assertEqual(obj.consultant_src(), data)

    def test_get_consultant_sales(self):
        # salesCns
        obj = PocTest()
        print("-------salesCns-----")
        data = [
            {"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)"}]
        self.assertEqual(obj.consultant_sales(), data)

    def test_get_consultant_businessName(self):
        # businessName
        obj = PocTest()
        print("-------businessName----")
        data = [
            {"operator": "RON SIMS (SION)", "SLS CONSULT": "RON SIMS (SION)"}]
        self.assertEqual(obj.consultant_businessName(), data)


class PocTest():
    def customer(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/customer?customerId=0001')
        return data.json()
    def consultant_sales(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=999888')
        return data.json()
    def consultant_src(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=000111')
        return data.json()
    def consultant_operator(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=222111')
        return data.json()
    def consultant_empty(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=555666')
        return data.json()
    def consultant_businessName(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=444555')
        return data.json()
    def customer_history(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/customer/history?phoneNo=8054544097&pageIndex=0&pageSize=5')
        return data.json()
    def customer_history_noHistory(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/customer/history?phoneNo=637382228&pageIndex=0&pageSize=5')
        return data.json()
if __name__ == '__main__':
    unittest.main()
