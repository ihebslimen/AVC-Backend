
from flask import Blueprint, request, abort,jsonify
import jwt
import os
from flask_cors import CORS
from flask_jwt_extended import  jwt_required

SECRET_KEY = 'secretkey'


admin_bp = Blueprint('admin', __name__)
""" @jwt_required()
@admin_bp.before_request
def permissions_check():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        res = jsonify({"Error" : " Authorization Header Missing"})
        res.status_code = 401
        abort(res)
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if decoded_token['role'] != 'admin':
        res = jsonify({"Error" : "Unauthorized Access Request"})
        res.status_code = 401
        abort(res) """