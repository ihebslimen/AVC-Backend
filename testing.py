import unittest
from flask import Flask, request
from app import app
import requests
import json

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.test_app = app.test_client()


    def test_create_product(self):
        url = 'http://localhost:5000/api/user/blockchain/create_product'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "product_id": 5,
                    "product_quantity": 1,
                    "product_quality": 1
                    }
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 404)
        #self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should Create Product ID To Blockchain : passed!") 

    def test_create_duplicated_product(self):
        url = 'http://localhost:5000/api/user/blockchain/create_product'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "product_id": 5,
                    "product_quantity": 1,
                    "product_quality": 1
                    }
        response = requests.post(url,headers=headers , json=data)        
        self.assertEqual(response.status_code, 404)
        #self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should Not Have Duplicated Product ID To Blockchain : passed!") 

    def test_invalid_product_quality(self):
        url = 'http://localhost:5000/api/user/blockchain/create_product'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "product_id": 5,
                    "product_quantity": 1,
                    "product_quality": 4
                    }
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 404)
        print("Should Only Have Product Quality [1,2,3] To Blockchain : passed!") 


    def test_update_product(self):
        url = 'http://localhost:5000/api/user/blockchain/update_product'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "product_id": 5,
                    "product_quantity": 2,
                    "product_quality": 2
                    }
        response = requests.post(url,headers=headers , json=data)        
        self.assertEqual(response.status_code, 200)
        print("Should Update Product Quality And Quality To Blockchain : passed!") 



    def test_check_product_product(self):
        url = 'http://localhost:5000/api/user/blockchain/check_owner_product'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "pub_key": "0xC7d138b89b55535Da5E4bd5E470B8Df81decFDAa",
                    "product_id" : 1
                    }
        response = requests.post(url,headers=headers , json=data)
        self.assertEqual(response.status_code, 200)
        print("Should Confirm Product Ownership To Blockchain : passed!") 

    
    def test_get_Products_by_owner(self):
        url = 'http://localhost:5000/api/user/blockchain/get_products'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "pub_key": "0xC7d138b89b55535Da5E4bd5E470B8Df81decFDAa"
                    }
        response = requests.post(url,headers=headers , json=data)
        self.assertEqual(response.status_code, 200)
        print("Should Return All Actor's Products from Blockchain : passed!")

    def create_offer(self):
        url = 'http://localhost:5000/api/user/blockchain/create_offer'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "offer_id": 5,
                    "product_id": 5,
                    "product_quantity": 1,
                    "price": 1
                    }
        response = requests.post(url,headers=headers , json=data)
        self.assertEqual(response.status_code, 404)
        print("Should Create Offer In Blockchain : passed!") 

    def test_get_Offers_by_owner(self):
        url = 'http://localhost:5000/api/user/blockchain/get_actor_offers'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "pub_key": "0xC7d138b89b55535Da5E4bd5E470B8Df81decFDAa"
                    }
        response = requests.post(url,headers=headers , json=data)
        self.assertEqual(response.status_code, 200)
        print("Should Return All Actor's Offer from Blockchain : passed!") 


    def test_get_all_offers(self):
        url = 'http://localhost:5000/api/user/blockchain/get_all_offers'
        headers = {"Content-Type": "application/json"}
        data ={
                    "pub_key": "0xC7d138b89b55535Da5E4bd5E470B8Df81decFDAa"
                }
        response = requests.post(url)
        self.assertEqual(response.status_code, 200)
        print("Should Return All Offers On Blockchain : passed!") 


    def test_buy_offer(self):
        url = 'http://localhost:5000/api/user/blockchain/buy_offer'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "offer_id" : 5
                    }
        response = requests.post(url,headers=headers , json=data)        
        self.assertEqual(response.status_code, 200)
        print("Should Buy Offer In Blockchain : passed!") 

    def test_delete_product(self):
        url = 'http://localhost:5000/api/user/blockchain/delete_product'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    {
                    "product_id": 2
                    }
        response = requests.post(url,headers=headers , json=data)        
        self.assertEqual(response.status_code, 200)
        print("Should Delete Product To Blockchain : passed!")


"""
    def test_add_admin(self):
        url = 'http://localhost:5000/api/admin/blockchain/add_admin'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "pub_key" : "0x9Aa1297EFa5b155b90a777876bB571A3d0c73e2c"}
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should Add Admin To Blockchain : passed!") 

    def test_add_farmer(self):
        url = 'http://localhost:5000/api/admin/blockchain/add_farmer'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "pub_key" : "0x0f17280E07F9E0F3843Ecfd0E7483baC117cF065"}
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should Add Farmer To Blockchain : passed!") 

    def test_add_transformer(self):
        url = 'http://localhost:5000/api/admin/blockchain/add_transformer'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "pub_key" : "0x6783dB16B89390cb181903422B811Eb14Ccd0a27"}
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should Add Transformer To Blockchain : passed!") 


    def test_remove_actor(self):
        url = 'http://localhost:5000/api/admin/blockchain/remove_actor'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "pub_key" : "0x6783dB16B89390cb181903422B811Eb14Ccd0a27"}
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should Revoke Account Actor Type of Blockchain : passed!") 

    def test_delete_account(self):
        url = 'http://localhost:5000/api/admin/blockchain/delete_account'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "pub_key" : "0x0f17280E07F9E0F3843Ecfd0E7483baC117cF065"}
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should Delete Account From Blockchain : passed!") 

    def test_get_actor_type(self):
        url = 'http://localhost:5000/api/admin/blockchain/actor_type'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "pub_key" : "0xCCcA87c5831B9526543E53eB7C12e8871F1F8449"}
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should Get Account Actor Type of Blockchain : passed!") 
 """

""" def test_hello_route(self):
        url = 'http://localhost:5000/'  # Replace with the actual URL of the route
        response = requests.get(url)
        data = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 200,msg="should return 200")
        self.assertEqual(data['data'], 'hello world', msg="should return")  # Assert the response data is 'hello world'
        print("Should get access home : passed!")  # Print a message when the test passes
    
    def test_get_user(self):
        url = 'http://localhost:5000/api/admin/users'  # Replace with the actual URL of the route
        response = requests.get(url)
        res_json = response.json()  # Parse the raw response data as JSON
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_json['Message'], 'Get request succeeded')  # Assert the response data is 'hello world'
        print("Should get users : passed!") 
    
    
    def test_add_user(self):
        url = 'http://localhost:5000/api/admin/users'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "cin": "6",
            "email": "test2@gmail.com",
            "name": "test1",
            "phone": "222222222",
            "role": "user",
            "state": "approved",
            "type": "transformateur",
            "actorInfoJson": {
                "label": "label",
                "localisation" : "soliman"
            }

        }
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON

        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_json['Message'], 'User created')  
        print("Should add user : passed!") 
    
    def test_readd_user(self):
        url = 'http://localhost:5000/api/admin/users'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data =    { "cin": "0000000",
            "email": "test@gmail.com",
            "name": "test",
            "phone": "11111111",
            "role": "user",
            "state": "approved",
            "type": "transformateur",
            "actorInfoJson": {
                "label": "label",
                "localisation" : "soliman"
            }

        }
        response = requests.post(url,headers=headers , json=data)
        res_json = response.json()  # Parse the raw response data as JSON

        self.assertEqual(response.status_code, 404)
        self.assertEqual(res_json['Message'], 'User already signed up')  
        print("Should not add user : passed!") 
    

    def test_update_user(self):
        url = 'http://localhost:5000/api/admin/users/6464f0ecc8fed61664b085e4'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data ={ "email": "test1@gmail.com"}  
        response = requests.put(url,headers=headers , json=data)
        res_json = response.json() 
        self.assertEqual(response.status_code, 200)
        self.assertEqual(res_json['Message'], 'User updated')  
        print("Should update user : passed!") 
   
    def test_update_user(self):
        url = 'http://localhost:5000/api/admin/users/646d54637b34b496bd69388e'  # Replace with the actual URL of the route
        headers = {"Content-Type": "application/json"}
        data ={ "cin": "1111111"}
        response = requests.put(url,headers=headers , json=data)
        res_json = response.json() 
        self.assertEqual(response.status_code, 400)
        #self.assertEqual(res_json['Message'], 'User updated')  
        print("Should not update user: passed!") 

    def test_delete_user(self):
        url = 'http://localhost:5000/api/admin/users/646d546c7b34b496bd693890'  # Replace with the actual URL of the route
        response = requests.delete(url)
        res_json = response.json() 
        self.assertEqual(response.status_code, 200)
        #self.assertEqual(res_json['Message'], 'User updated')  
        print("Should delete user: passed!")  """

    

if __name__ == '__main__':
    unittest.main()