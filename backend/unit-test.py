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
    # def test_get_customerHistory1(self):
    #     obj = PocTest()
    #     print("--customerHistory-")
    #     data = [
    #         {
    #             "firstName": "DERRICK",
    #             "lastName": "ROSE",
    #             "address": "S9 FULLER ROAD",
    #             "city": "SAN HOSE",
    #             "pf": "pf"
    #         }
    #     ]
    #     self.assertEqual(obj.customer_history(), data)
    def test_get_customerHistory2(self):
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


class consultantTests(unittest.TestCase):

    def test_get_consultant5(self):
        #Noconsultant is there
        obj = PocTest()
        print("-No consultant-")
        data = [{"operator": "RON SIMS (SION)", "SLS CONSULT": "No consultant"}]
        self.assertEqual(obj.consultant5(), data)

    def test_get_consultant4(self):
        # firstNameLastName(operator)
        obj = PocTest()
        print("-operator-FirstName-")
        data = [{"operator": "RON SIMS (SION)", "SALECNS": "RON SIMS (SION)"}]
        self.assertEqual(obj.consultant4(), data)

    def test_get_consultant3(self):
        # srcAssoc
        obj = PocTest()
        print("-srcAssoc-")
        data = [
            {"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)", "SRC ASSOC": "LEBRON JAMES (LBJ)"}]
        self.assertEqual(obj.consultant3(), data)

    def test_get_consultant2(self):
        # salesCns
        obj = PocTest()
        print("-------salesCns-----")
        data = [
            {"operator": "SHOUT INC SIMS (SION)", "SALECNS": "RON SIMS (SION)"}]
        self.assertEqual(obj.consultant2(), data)

    def test_get_consultant1(self):
        # businessName
        obj = PocTest()
        print("-------businessName----")
        data = [
            {"operator": "RON SIMS (SION)", "SLS CONSULT": "RON SIMS (SION)"}]
        self.assertEqual(obj.consultant1(), data)


class PocTest():
    def customer(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/customer?customerId=0001')
        return data.json()

    def consultant2(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=999888')
        return data.json()
    def consultant3(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=000111')
        return data.json()
    def consultant4(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=222111')
        return data.json()
    def consultant5(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=555666')
        return data.json()
    def consultant1(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/consultant?transactionId=444555')
        return data.json()
    def customer_history(self):
        data = requests.get(
            'http://127.0.0.1:5000/api/customer/history?phoneNo=8054544097&pageIndex=0&pageSize=5')
        return data.json()


if __name__ == '__main__':
    unittest.main()
