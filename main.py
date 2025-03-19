import smtplib
from email.mime.text import MIMEText
import os
import quote


SMTP_SERVER = os.getenv('SMTP_SERVER')
SMTP_PORT = os.getenv('SMTP_PORT')
EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

PHONE_NUMBER = os.getenv('PHONE_NUMBER')

CARRIER_GATEWAY = ''

carrier_gateway_list = {
    "AT&T" : '@txt.att.net',
    "Verizon" : '@vtext.com',
    "T-Mobile" : '@tmomail.net',
    "Sprint" : '@messaging.sprintpcs.com',
    "Boost Network" : "@sms.myboostmobile.com",
    "Cricket" : "@sms.myboostmobile.com",
    "MetroPCS" : "@sms.myboostmobile.com"
}


def set_email_address(email_address : str):
    EMAIL_ADDRESS = email_address
    if EMAIL_ADDRESS:
        return True
    return False

def set_phone_number(phoneNumber : int):
    PHONE_NUMBER = phoneNumber
    if PHONE_NUMBER:
        return True
    return False 


def set_carrier(carrier):
    global CARRIER_GATEWAY
    if carrier in carrier_gateway_list:
        CARRIER_GATEWAY = carrier_gateway_list[carrier]
        return True
    return False

def set_sms_recipient(carrier_gateway, PHONE_NUMBER):
    return PHONE_NUMBER+carrier_gateway


goal = input("Enter your goal")

quote = quote.create_motivational_quote(goal)

SMS_RECIPIENT = set_sms_recipient(carrier_gateway=set_carrier("T-Mobile"), PHONE_NUMBER=PHONE_NUMBER)

msg = MIMEText(quote)
msg["From"] = EMAIL_ADDRESS
msg["To"] = SMS_RECIPIENT
msg["Subject"] = "" 


with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
    server.starttls()  # Secure the connection
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    server.sendmail(EMAIL_ADDRESS, SMS_RECIPIENT, msg.as_string())

print("✅ Motivational quote sent!")
    
