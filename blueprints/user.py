
from flask import Blueprint, request, abort, jsonify
import jwt
import os
from flask_cors import CORS
from flask_jwt_extended import  jwt_required

SECRET_KEY = os.environ.get('SECRET_KEY')


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
    if ( decoded_token['role'] != 'user'):
        res = jsonify({"Error" : "Unauthorized Access Request"})
        res.status_code = 401
        abort(res)