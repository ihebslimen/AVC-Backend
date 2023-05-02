
from flask import Blueprint, request, abort
import jwt
import os

admin_bp = Blueprint('admin', __name__)
SECRET_KEY = os.environ.get('SECRET_KEY')

@admin_bp.before_request
def permissions_check():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        abort(401)
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if not ( decoded_token['role']== 'admin'):
        abort(401)