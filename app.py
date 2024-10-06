from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "Kwepo"
api_key = "atsk_6c751b9348517e4d6631e8b4ee476f4f72deeb533c7655d861d0ef9dba9e0853dfd44c23"
africastalking.initialize(username, api_key)

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    print(phone_number)
    text = request.values.get("text", "default")
    sms_phone_number = []
    sms_phone_number.append(phone_number)
    sms = africastalking.SMS

    sender = "AFTKNG"

    if text == "":
        response = "CON Welcome to Craft Marketplace\n"
        response += "1. Browse Craft Items\n"
        response += "2. View Popular Items\n"
        response += "3. Customer Support\n"
        response += "4. View Cart\n"
        response += "5. Checkout\n"

    

    else:
        response = "END Invalid input. Please try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
