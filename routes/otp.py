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
import json
from dotenv import load_dotenv
from blueprints.admin import admin_bp
from blueprints.shared import shared_bp




load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')

# Define OTP parameters
OTP_LENGTH = 6
OTP_VALIDITY_TIME = 300  # seconds
# Set the expiration time of the token to 1 hour
expiration_time = datetime.timedelta(hours=12)


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
@shared_bp.route('/login', methods=['POST'])
def login():
    # Authenticate user
    #username = request.form['email']
    data = request.get_json()
    res = mongo.db.users.find_one({'cin': data['cin'] })
    if res is None :
        res = jsonify({"Error" : 'Wrong Credentials'})
        res.status_code = 401
        return res
    elif res['state'] != "approved":
        res = jsonify({"Error" : 'User not approved by admin'})
        res.status_code = 401
        return res
    
    # Store OTP secret and timestamp in session
    serialized_user_id = str(res['_id'])
    session['user_id'] = serialized_user_id
    session['phone']=res['phone']
    session['role']=res['role']
    session['otp_timestamp'] = datetime.datetime.now().timestamp()
    session['public_key'] = res['public_key']
    session['private_key'] = res['private_key']

    # Send OTP to user (e.g. via SMS or email)
    verification = client.verify.v2.services(verify_sid) \
      .verifications \
      .create(to=res['phone'], channel="sms")

    print(verification.status)
    res.status_code = 401
    res = jsonify({"Message" : verification.status})
    res.status_code = 200
    return res


# Verify an OTP and return an access token
@shared_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    # Verify OTP
    data = request.get_json()
    user_id = session.get('user_id')
    verified_number = session.get('phone')
    role = session.get('role')
    otp_timestamp = session.get('otp_timestamp')
    public_key = session.get('public_key')
    private_key = session.get('private_key')
    print(user_id , otp_timestamp)
    if not user_id or not otp_timestamp:
        res = jsonify({"Message" :'Invalid session' })
        res.status_code = 401
        return res

    # Check OTP validity
    if datetime.datetime.now().timestamp() - otp_timestamp > OTP_VALIDITY_TIME:
        res = jsonify({"Message" :'OTP has expired' })
        res.status_code = 401
        return res

    verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=data['otp_code'])
    print(verification_check.status) 
    
    # Create access token (e.g. using JWT)
    payload = {'user_id': user_id, 'role' : role, 'public_key' : public_key , 'private_key' : private_key, 'exp': datetime.datetime(9999, 12, 31)}
    access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    res = jsonify({"Message" :verification_check.status , "data": access_token })
    res.status_code = 200
    #access_token = create_access_token(identity= {'id': user_id , 'role' : role},  expires_delta=expiration_time)
    return res
