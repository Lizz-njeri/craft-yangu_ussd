from flask import Flask, request
import africastalking
import os

app = Flask(__name__)
username = "sandbox"
api_key = ""
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

    # Browse Craft Items
    elif text == "1":
        response = "CON Choose a category:\n"
        response += "1. Jewelry\n"
        response += "2. Pottery\n"
        response += "3. Handwoven Textiles\n"
        response += "4. Paintings\n"
        response += "5. Back to Main Menu\n"

    # Jewelry Items
    elif text == "1*1":
        response = "CON Choose a Jewelry Item:\n"
        response += "1. Beaded Necklace - KES 1,000\n"
        response += "2. Handmade Bracelet - KES 500\n"
        response += "3. Custom Earrings - KES 700\n"
        response += "4. Back to Categories\n"
    
    # Jewelry selection confirmation
    elif text == "1*1*1":
        response = "CON You selected Beaded Necklace for KES 1,000\n"
        response += "1. Add to Cart\n"
        response += "2. Back to Jewelry Items\n"
    
    elif text == "1*1*2":
        response = "CON You selected Handmade Bracelet for KES 500\n"
        response += "1. Add to Cart\n"
        response += "2. Back to Jewelry Items\n"

    elif text == "1*1*3":
        response = "CON You selected Custom Earrings for KES 700\n"
        response += "1. Add to Cart\n"
        response += "2. Back to Jewelry Items\n"

    # Other categories (Pottery, Textiles, Paintings) follow similar structure
    elif text == "1*2":
        response = "CON Choose a Pottery Item:\n"
        response += "1. Clay Mug - KES 800\n"
        response += "2. Ceramic Bowl - KES 1,200\n"
        response += "3. Sculpted Vase - KES 2,500\n"
        response += "4. Back to Categories\n"

    # Add to Cart option
    elif text.endswith("*1"):
        response = "END Item added to your cart! Continue shopping or proceed to checkout.\n"
        # You can send an SMS confirmation to the user about the item added.
        message = "You've added an item to your cart at Craft Marketplace."
        sms.send(message, sms_phone_number, sender)

    # Popular Items
    elif text == "2":
        response = "CON Popular Craft Items:\n"
        response += "1. Beaded Necklace - KES 1,000\n"
        response += "2. Clay Mug - KES 800\n"
        response += "3. Sculpted Vase - KES 2,500\n"
        response += "4. Back to Main Menu\n"

    # Customer Support
    elif text == "3":
        response = "CON How can we assist you?\n"
        response += "1. Call Customer Support\n"
        response += "2. Receive SMS with Support Contacts\n"
    
    elif text == "3*1":
        response = "END Please call this number for assistance: +254700123456"

    elif text == "3*2":
        response = "END You will receive an SMS with support contacts shortly."
        sms.send("Support contacts: +254700123456, +254711654321", sms_phone_number, sender)

    # Cart and Checkout
    elif text == "4":
        response = "CON Your Cart is empty. Add items to your cart by browsing categories.\n"
        response += "1. Back to Main Menu\n"

    elif text == "5":
        response = "CON Your Cart:\n"
        response += "1. Beaded Necklace - KES 1,000\n"  # Example item
        response += "Total: KES 1,000\n"
        response += "1. Confirm Purchase\n"
        response += "2. Back to Main Menu\n"

    elif text == "5*1":
        response = "END Thank you for your purchase! We will contact you shortly for delivery details."
        message = "Your order has been received and is being processed."
        sms.send(message, sms_phone_number, sender)

    else:
        response = "END Invalid input. Please try again."

    return response


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
