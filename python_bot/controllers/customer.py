import requests
from server_utils import backend_params

""" A Class to group request queries into one file 
    Work with this carefully
"""
class Customer_Queries:
    url = backend_params('customers_url')
    
    def create_user(self, tel, firstName):
        create_url = self.url + "create"

        r = requests.post(create_url, json={
            'tel': tel,
            'firstName': firstName
        })
        status = r.status_code
        res = r.json()
    
        
        if status != 200:
            return {
                "status": status,
                "message": res["message"]
            }
        
        else:
            return {
                "status": status,
                "message": "Welcome aboard, " + res["firstName"].title() + "! 😊"
            }


    def update_user(self, tel, data):
        create_url = self.url + tel
        r = requests.put(create_url, json=data)
        status = r.status_code

        res = r.json()
        
        if status != 200:
            return {
                "status": status,
                "message": res["message"]
            }
        
        else:
            return {
                "status": status,
                "message": res
            }

    def get_user(self, tel):
        create_url = self.url + tel
        r = requests.get(create_url)
        status = r.status_code
        res = r.json()

        if status != 200:
            return {
                "status": status,
                "message": res["message"]
            }
        
        else:
            return {
                "status": status,
                "customer": res
            }


    def update_lastname(self, tel, name):
        update_query = self.update_user(tel, {"lastName": name})
        status = update_query["status"]
        if status != 200:
            return {
                "status": status,
                "message": res["message"]
            }
        else:
            return {
                "status": status,
                "customer": update_query["message"],
                "message": "last name registered successfully"
            }
