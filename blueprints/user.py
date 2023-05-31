
from flask import Blueprint, request, abort, jsonify, g
import jwt
import os
from flask_cors import CORS
from flask_jwt_extended import  jwt_required
from web3models.Account import Account

SECRET_KEY = 'secretkey'


user_bp = Blueprint('user', __name__)
@jwt_required
@user_bp.before_request
def permissions_check():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        res = jsonify({"Error" : " Authorization Header Missing"})
        res.status_code = 401
        abort(res)

    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    g.account_loggedIn = Account(decoded_token['public_key'],decoded_token['private_key'])
    if ( decoded_token['role'] != 'user'):
        res = jsonify({"Error" : "Unauthorized Access Request"})
        res.status_code = 401
        abort(res)
