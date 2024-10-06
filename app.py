from flask import Flask, request
import africastalking
import os
import sqlite3

app = Flask(__name__)
username = "sandbox"
api_key = ""
africastalking.initialize(username, api_key)

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect('craft_marketplace.db')
    cursor = conn.cursor()
    # Create table for carts
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS carts (
            phone_number TEXT,
            item TEXT,
            price INTEGER
        )
    ''')
    conn.commit()
    conn.close()

# Add item to cart
def add_to_cart(phone_number, item, price):
    conn = sqlite3.connect('craft_marketplace.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO carts (phone_number, item, price) VALUES (?, ?, ?)', (phone_number, item, price))
    conn.commit()
    conn.close()

# Get items in the cart
def get_cart(phone_number):
    conn = sqlite3.connect('craft_marketplace.db')
    cursor = conn.cursor()
    cursor.execute('SELECT item, price FROM carts WHERE phone_number=?', (phone_number,))
    cart_items = cursor.fetchall()
    conn.close()
    return cart_items

# Clear cart after purchase
def clear_cart(phone_number):
    conn = sqlite3.connect('craft_marketplace.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM carts WHERE phone_number=?', (phone_number,))
    conn.commit()
    conn.close()

@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
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
        response += "0. Back to Main Menu\n"

    # Jewelry Items
    elif text == "1*1":
        response = "CON Choose a Jewelry Item:\n"
        response += "1. Beaded Necklace - KES 1,000\n"
        response += "2. Handmade Bracelet - KES 500\n"
        response += "3. Custom Earrings - KES 700\n"
        response += "4. Back to Categories\n"
    
    # Adding Jewelry to Cart
    elif text == "1*1*1":
        response = "END Beaded Necklace added to your cart for KES 1,000."
        add_to_cart(phone_number, "Beaded Necklace", 1000)
    
    elif text == "1*1*2":
        response = "END Handmade Bracelet added to your cart for KES 500."
        add_to_cart(phone_number, "Handmade Bracelet", 500)

    elif text == "1*1*3":
        response = "END Custom Earrings added to your cart for KES 700."
        add_to_cart(phone_number, "Custom Earrings", 700)

    # Adding Pottery to Cart
    elif text == "1*2*1":
        response = "END Clay Mug added to your cart for KES 800."
        add_to_cart(phone_number, "Clay Mug", 800)

    elif text == "1*2*2":
        response = "END Sculpted Vase added to your cart for KES 2,500."
        add_to_cart(phone_number, "Sculpted Vase", 2500)

    elif text == "1*2*3":
        response = "END Ceramic Plate added to your cart for KES 1,200."
        add_to_cart(phone_number, "Ceramic Plate", 1200)

    # Handwoven Textiles Items
    elif text == "1*3":
        response = "CON Choose a Handwoven Textile Item:\n"
        response += "1. Handwoven Scarf - KES 1,500\n"
        response += "2. Cotton Blanket - KES 3,000\n"
        response += "3. Traditional Mat - KES 2,000\n"
        response += "4. Back to Categories\n"

    # Adding Textiles to Cart
    elif text == "1*3*1":
        response = "END Handwoven Scarf added to your cart for KES 1,500."
        add_to_cart(phone_number, "Handwoven Scarf", 1500)

    elif text == "1*3*2":
        response = "END Cotton Blanket added to your cart for KES 3,000."
        add_to_cart(phone_number, "Cotton Blanket", 3000)

    elif text == "1*3*3":
        response = "END Traditional Mat added to your cart for KES 2,000."
        add_to_cart(phone_number, "Traditional Mat", 2000)

    # Paintings Items
    elif text == "1*4":
        response = "CON Choose a Painting:\n"
        response += "1. Abstract Art - KES 5,000\n"
        response += "2. Portrait - KES 3,500\n"
        response += "3. Landscape - KES 4,000\n"
        response += "4. Back to Categories\n"

    # Adding Paintings to Cart
    elif text == "1*4*1":
        response = "END Abstract Art added to your cart for KES 5,000."
        add_to_cart(phone_number, "Abstract Art", 5000)

    elif text == "1*4*2":
        response = "END Portrait added to your cart for KES 3,500."
        add_to_cart(phone_number, "Portrait", 3500)

    elif text == "1*4*3":
        response = "END Landscape added to your cart for KES 4,000."
        add_to_cart(phone_number, "Landscape", 4000)

    # View Popular Items
    elif text == "2":
        response = "CON Popular Craft Items:\n"
        response += "1. Beaded Necklace - KES 1,000\n"
        response += "2. Clay Mug - KES 800\n"
        response += "3. Sculpted Vase - KES 2,500\n"
        response += "0. Back to Main Menu\n"

    # Popular Items Menu
    elif text == "2":
        response = "CON Popular Craft Items:\n"
        response += "1. Beaded Necklace - KES 1,000\n"
        response += "2. Clay Mug - KES 800\n"
        response += "3. Sculpted Vase - KES 2,500\n"
        response += "0. Back to Main Menu\n"
    
    # Popular Items - Adding to cart
    elif text == "2*1":
        response = "END Beaded Necklace added to your cart for KES 1,000."
        add_to_cart(phone_number, "Beaded Necklace", 1000)

    elif text == "2*2":
        response = "END Clay Mug added to your cart for KES 800."
        add_to_cart(phone_number, "Clay Mug", 800)

    elif text == "2*3":
        response = "END Sculpted Vase added to your cart for KES 2,500."
        add_to_cart(phone_number, "Sculpted Vase", 2500)

    elif text == "0":
        response = "CON Welcome to Craft Marketplace\n"
        response += "1. Browse Craft Items\n"
        response += "2. View Popular Items\n"
        response += "3. Customer Support\n"
        response += "4. View Cart\n"
        response += "5. Checkout\n"

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

    # View Cart
    elif text == "4":
        cart_items = get_cart(phone_number)
        if len(cart_items) == 0:
            response = "CON Your cart is empty. Add items to your cart by browsing categories.\n"
            response += "1. Back to Main Menu\n"
        else:
            response = "CON Your Cart:\n"
            total = 0
            for item, price in cart_items:
                response += f"{item} - KES {price}\n"
                total += price
            response += f"Total: KES {total}\n"
            response += "1. Checkout\n"
            response += "0. Continue Shopping\n"

    # Checkout
    elif text == "5" or text == "4*1":
        cart_items = get_cart(phone_number)
        if len(cart_items) == 0:
            response = "CON Your cart is empty. Add items to your cart by browsing categories.\n"
            response += "0. Back to Main Menu\n"
        else:
            response = "END Thank you for your purchase! We will contact you shortly for delivery details."
            message = "Your order has been received and is being processed."
            sms.send(message, sms_phone_number, sender)
            clear_cart(phone_number)  # Clear cart after checkout

    else:
        response = "END Invalid input. Please try again."

    return response


if __name__ == "__main__":
    init_db()  # Initialize the database when the app starts
    app.run(host="0.0.0.0", port=os.environ.get("PORT"))
