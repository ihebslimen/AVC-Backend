# Download the helper library from https://www.twilio.com/docs/python/install
from flask import Blueprint, jsonify, request, session
from twilio.rest import Client
from random import randint
import os
from twilio.rest import Client
import pyotp
import datetime



otp_bp = Blueprint('otp', __name__)

# Define OTP parameters
OTP_LENGTH = 6
OTP_VALIDITY_TIME = 300  # seconds



# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC83f8ff69932eb7732bcdc8ffab17811e"
auth_token = "4400fed24b0559d20eaf4c381ef82574"
verify_sid = "VA7c70e19f60cbff7b003c99a726fd9fbd"
verified_number = "+21655554907"

client = Client(account_sid, auth_token)

# Generate an OTP code
def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32(), digits=OTP_LENGTH, interval=OTP_VALIDITY_TIME)
    return totp.now()

# Verify an OTP code
def verify_otp(otp, secret):
    totp = pyotp.TOTP(secret, digits=OTP_LENGTH, interval=OTP_VALIDITY_TIME)
    return totp.verify(otp)

# Authenticate a user and generate an OTP
@otp_bp.route('/login', methods=['POST'])
def login():
    # Authenticate user
    #username = request.form['email']
    data = request.get_json()
    
    # Store OTP secret and timestamp in session
    session['username'] = data['email']
    session['otp_timestamp'] = datetime.datetime.now().timestamp()

    # Send OTP to user (e.g. via SMS or email)
    verification = client.verify.v2.services(verify_sid) \
      .verifications \
      .create(to=verified_number, channel="sms")

    print(verification.status)
    return 'OTP generated successfully'


# Verify an OTP and return an access token
@otp_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    # Verify OTP
    data = request.get_json()
    username = session.get('username')
    otp_timestamp = session.get('otp_timestamp')
    print(username , otp_timestamp)
    if not username or not otp_timestamp:
        return 'Invalid session', 401

    # Check OTP validity
    if datetime.datetime.now().timestamp() - otp_timestamp > OTP_VALIDITY_TIME:
        return 'OTP has expired', 401

    verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=data['otp_code'])
    print(verification_check.status) 
    # Create access token (e.g. using JWT)

    return 'OTP verified successfully'








""" 
verification = client.verify.v2.services(verify_sid) \
  .verifications \
  .create(to=verified_number,code=  , channel="sms")

print(verification.status)

otp_code = input("Please enter the OTP:")

verification_check = client.verify.v2.services(verify_sid) \
  .verification_checks \
  .create(to=verified_number, code=otp_code)
print(verification_check.status) """