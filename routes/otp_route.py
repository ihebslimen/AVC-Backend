# Download the helper library from https://www.twilio.com/docs/python/install
from flask import Blueprint, jsonify, request, session,g
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
from models.otp import OTP
from models.user import User
from web3models.Account import Account




load_dotenv()


SECRET_KEY = 'secretkey'

# Define OTP parameters
OTP_LENGTH = 6
OTP_VALIDITY_TIME = 300  # seconds
# Set the expiration time of the token to 1 hour
expiration_time = datetime.timedelta(hours=12)


# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = 'AC5782b21395fb63eb3edb8080ca84b22e'
auth_token = '6b0bff9560371d0f1b2045631d9a625c'
verify_sid = 'VAdfe95cc61a3700fa82d2088bf0be189c'



client = Client(account_sid, auth_token)



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

    elif res['role'] == 'user':
    
        if res['state'] != "approved":
            res = jsonify({"Error" : 'User not approved by admin'})
            res.status_code = 401
            return res
    
    serialized_user_id = str(res['_id'])
    result = OTP.sendOTP(res['phone'])
    if result != 'pending':
        res = jsonify({"Error" : result})
        res.status_code = 404
        return res

    res = jsonify({"Message" : "Login OTP generated successfully", 'data': {'_id':serialized_user_id}})
    res.status_code = 200
    return res


# Verify an OTP and return an access token
@shared_bp.route('/login_verification', methods=['POST'])
def login_verification():
    # Verify OTP
    data = request.get_json()
    res = User.login(data['_id'])
    user_id =data['_id']
    verified_number = res['phone']
    role = res['role']
    public_key = res['public_key']
    private_key = res['private_key']

    result = OTP.verifyOTP(verified_number,data['otp_code'])
    print(result)
    if result != 'approved':
        res = jsonify({"Error" : result})
        res.status_code = 404
        return res
    print("###### Creating account logged in")
    g.account_loggedIn = Account(private_key,private_key)
    print("######## account logged in created ",g.account_loggedIn)
    # Create access token (e.g. using JWT)
    if(role == 'admin'):
        payload = {'user_id': user_id, 'role' : role, 'public_key' : public_key ,'private_key' : private_key ,  'exp': datetime.datetime(9999, 12, 31)}
    
    elif(role == 'user'):
        actorType = res['type']
        payload = {'user_id': user_id, 'role' : role,'type':actorType ,'public_key' : public_key , 'private_key' : private_key, 'exp': datetime.datetime(9999, 12, 31)}

    
    access_token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    res = jsonify({"Message" :"Login successfully" , "data": access_token })
    res.status_code = 200
    return res

@shared_bp.route('/signup',  methods=['POST'])
def signup():
    data = request.get_json()
    result = OTP.sendOTP(data['phone'])
    if result != 'pending':
        res = jsonify({"Error" : result})
        res.status_code = 404
        return res

    res = jsonify({"Message" : "Signup OTP generated successfully"})
    res.status_code = 200
    return res

@shared_bp.route('/signup_verification', methods=['POST'])
def signup_verification():
    data = request.get_json()
    result = OTP.verifyOTP(data['phone'],data['otp_code'])
    if result != 'approved':
        res = jsonify({"Error" : result})
        res.status_code = 404
        return res
    
    result1 = User.create_user(data['cin'], data['name'], data['email'], data['phone'], role='user',state = "waiting")
    
    if result1 :
        res = jsonify({'Message': "Signup request successful, waiting for the admin to approve it" })
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to add user'})
        res.status_code = 404
    return res

