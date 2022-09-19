from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from controllers.reply import reply_request
import requests
from server_utils import backend_params, get_req_field
from flask_session import Session
from datetime import timedelta

""" Note: Put all the parameters in a json file just like the .env file in the node one and created a function to access it. You can modify it to your preference 'params.json' """

""" Initialised the flask app with sessions """
app = Flask(__name__)
app.config["SESSION_PERMANENT"] = True
app.config["SESSION_TYPE"] = "filesystem"

""" Session is to expire after 2 hours """
app.config['PERMANENT_SESSION_LIFETIME'] =  timedelta(hours=2)
app.config.from_object(__name__)
Session(app)

""" Function to check if the node backend is online"""
def backend_ready():
    """ Make a request to the root url which is to return 'online' """
    try:
        backend_url = backend_params("root_url")
        r = requests.get(backend_url)
        return True
    except:
        """ If it fails to return a value, you assume it is down and return false """
        return False

""" A class to hold session creating and retrieving easy
## ---------- TO BE UPDATED ---------------- # """
class Session_handlers:
    def create_tel_session(self, tel, value):
        tel = str(tel)
        session[tel] = value
        return str(value)


    def retrieve_tel_session(self, tel):
        tel = str(tel)
        return session[tel]

""" The endpoint that twilio sends the request to. Root endpoint that's gonna handle our replies and stuff """
@app.route("/", methods=['POST'])
def wa_sms_reply():
    
    """Instantiate the session object"""
    session_handler = Session_handlers()

    """ Get the telephone number of the person trying to access the stuff """
    tel = get_req_field(request, 'WaId')

    """ Initialised step variable to undefined and set it to the session holding the telephone number if that session exists, else to 0
    ## ---------- TO BE UPDATED ---------------- # """
    step = None
    try:
        step = session_handler.retrieve_tel_session(tel)
    except KeyError:
        step = session_handler.create_tel_session(tel, 0)
    
    # step = session_handler.create_tel_session(tel, 0)

    # print(step)
    # print(request.form)

    """ Get the object we'll use to reply """
    resp = MessagingResponse()

    """ Make sure node backend is ready """
    if not backend_ready():
        resp.message("Unable to connect to our servers. Please try again later. Sorry 🙏🙏")
        return("")

    """ Reply 😁😁 """
    return str(reply_request(request, resp, step, session_handler))


if __name__ == "__main__":
    app.run(debug=True)
