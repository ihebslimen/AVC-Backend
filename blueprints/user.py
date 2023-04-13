
from flask import Blueprint


user_bp = Blueprint('user', __name__)

@user_bp.before_request
def permissions_check():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        abort(401)
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if not ( decoded_token['role']== 'user'):
        abort(401)