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
import time




load_dotenv()


SECRET_KEY = os.environ.get('SECRET_KEY')

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



class OTP:
    @staticmethod
    def sendOTP(phone):
        try:
            # Send OTP to user (e.g. via SMS or email)
            verification = client.verify.v2.services(verify_sid) \
            .verifications \
            .create(to=phone, channel="sms")

            print(verification.status)
            return verification.status
        except Exception as e:
            return(f"Unexpected error: {str(e)}")
        
        
    @staticmethod
    def verifyOTP(verified_number,otp_code):
        try:
            verification_check = client.verify.v2.services(verify_sid) \
            .verification_checks \
            .create(to=verified_number, code=otp_code)
            while verification_check.status == 'pending':
                time.sleep(1)  # Wait for 1 second
                verification_check = client.verify \
                .v2 \
                .services(verify_sid) \
                .verification_checks(verification_check.sid) \
                .fetch()
                
            return verification_check.status
        except Exception as e:
            return(f"Unexpected error: {str(e)}")
