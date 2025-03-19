from flask import Flask, request, jsonify
import main
import quote

app = Flask(__name__)

@app.route('/')
def home():    
    return 'index.html'

@app.route('/onboarding', methods=['POST'])
def register_user():
    data = request.json
    phone_number = data.get('PHONE_NUMBER')
    email_address = data.get('EMAIL_ADDRESS')
    carrier_gateway = data.get('CARRIER_GATEWAY')
    goal = data.get('GOAL')

    if main.set_email_address(email_address=email_address) and main.set_phone_number(phone_number) and main.set_carrier(carrier_gateway) and quote.set_user_goal(goal):
        return #verification text
@app.route('verification-text')
def send_verifcation():
    data = request.json()
    phone_number = data.get('PHONE_NUMBER')

    if not phone_number:
        return jsonify({
            "error": "no phone number"
        })
    name = data.get('EMAIL_ADDRESS')
    goal = data.get('GOAL')
    verifcation_message = f'Hey {name}, you goal is {goal}! Welcome to Motivational Bot, yotu got this!'
    send_data = {
        "verification_message" : verifcation_message,
        "status" : "good",
        "goal" : goal
    }