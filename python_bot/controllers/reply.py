import requests
from server_utils import backend_params, get_req_field
from controllers.customer import Customer_Queries


def get_step(tel):
    return tel

""" Check if the person has started registering before"""
def has_started(tel, reply):
    errMessage = None
    customer = None
    url = backend_params("customers_url") + str(tel)
    r = requests.get(url)
    status = r.status_code
    res = r.json()
    if status != 200:
        errMessage = res['message']
        reply(str(errMessage))

    else:
        customer = res
        successMessage = "Welcome back! " + str(res['firstName'].title() + " 😁")
        reply(successMessage)

    return {
        "customer": customer,
        "step": get_step(customer)
    }



def reply_request(request, responseObj, step, session_handler):
    msg = get_req_field(request, 'Body').lower()
    tel = get_req_field(request, 'WaId')

    def increment_session():
        return session_handler.create_tel_session(tel, int(session_handler.retrieve_tel_session(tel)) + 1)

    customer_queries = Customer_Queries()

    print("msg-->", msg)

    step = session_handler.retrieve_tel_session(tel);

    reply = responseObj.message

    tel = get_req_field(request, 'WaId')

    if step == 0:
        reply("Welcome to ... We collect a survey of individuals for some reason 😂😂")
        has_started(tel, reply)
        increment_session()
    
    if step == 1:
        if(len(msg) < 3):
            reply("Invalid firstname. Cannot be less than 3 letters 😒😒")
        else:
            result = customer_queries.create_user(tel, msg)
            print(result)

            if result["status"] == 200:
                reply(result["message"])
                reply("Now, your Last Name 😁😁")
                increment_session()
            else:
                reply(result["message"])

    if step == 2:
        if(len(msg) < 3):
            reply("Invalid lastname. Cannot be less than 3 letters 😒😒")
        else:
            result = customer_queries.update_lastname(tel, msg)
            
            if result["status"] == 200:
                reply(result["message"])
                confirmation_str = "first name: " + result["customer"]['firstName'].title() + "\n" + "last name: " + result["customer"]["lastName"].title()
                reply(confirmation_str)
                # increment_session()
            
            else:
                reply(result["message"])
        
    

    return responseObj
