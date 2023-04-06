# Download the helper library from https://www.twilio.com/docs/python/install
from flask import Blueprint, jsonify, request, session
from twilio.rest import Client
from random import randint
import os
from twilio.rest import Client
import pyotp
import datetime
from db import mongo
import jwt
from bson import  json_util
import json
from dotenv import load_dotenv



load_dotenv()


otp_bp = Blueprint('otp', __name__)
SECRET_KEY = os.environ.get('SECRET_KEY')

# Define OTP parameters
OTP_LENGTH = 6
OTP_VALIDITY_TIME = 300  # seconds



# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = os.environ.get('TWILIO_ACCOUNT_ID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
verify_sid = os.environ.get('TWILIO_VERIFY_ID')

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
    res = mongo.db.users.find_one({'email': data['email'] })
    if res is None :
        return 'Wrong Credentials'
    
    # Store OTP secret and timestamp in session
    serialized_user_id = json.loads(json_util.dumps(res['_id']))
    session['user_id'] = serialized_user_id
    session['phone']=res['phone']
    session['otp_timestamp'] = datetime.datetime.now().timestamp()

    # Send OTP to user (e.g. via SMS or email)
    verification = client.verify.v2.services(verify_sid) \
      .verifications \
      .create(to=res['phone'], channel="sms")

    print(verification.status)
    return 'OTP generated successfully'


# Verify an OTP and return an access token
@otp_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    # Verify OTP
    data = request.get_json()
    user_id = session.get('user_id')
    verified_number = session.get('phone')
    otp_timestamp = session.get('otp_timestamp')
    print(user_id , otp_timestamp)
    if not user_id or not otp_timestamp:
        return 'Invalid session', 401

    # Check OTP validity
    if datetime.datetime.now().timestamp() - otp_timestamp > OTP_VALIDITY_TIME:
        return 'OTP has expired', 401

    verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=data['otp_code'])
    print(verification_check.status) 
    
    # Create access token (e.g. using JWT)
    
    access_token = jwt.encode({'user_id': user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, SECRET_KEY)
    return jsonify({'access_token': access_token})
