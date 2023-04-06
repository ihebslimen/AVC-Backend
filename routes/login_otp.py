from flask import Blueprint, jsonify, request
from twilio.rest import Client
from random import randint
import os

otp_bp = Blueprint('otp', __name__)

# Set environment variables for your credentials
# Read more at http://twil.io/secure
account_sid = "AC83f8ff69932eb7732bcdc8ffab17811e"
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
verify_sid = "VA7c70e19f60cbff7b003c99a726fd9fbd"
verified_number = "+21655554907"

client = Client(account_sid, auth_token)

@otp_bp.route('/send_otp', methods=['POST'])
def send_otp():
    #verified_number = request.form.get('mobile_number')
    data = request.get_json()

    verification = client.verify.v2.services(verify_sid) \
        .verifications \
        .create(to=data['mobile_number'], channel="sms")

    return verification.status

@otp_bp.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.get_json()
    verification_check = client.verify.v2.services(verify_sid) \
        .verification_checks \
        .create(to=verified_number, code=data['otp'])
    return verification_check.status
