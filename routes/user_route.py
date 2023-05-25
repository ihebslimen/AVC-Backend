
from flask import Blueprint, jsonify, request
from models.user import User
from blueprints.admin import admin_bp
from blueprints.user import user_bp
from flask_cors import CORS , cross_origin
import jwt
import os

SECRET_KEY = 'secretkey'


@admin_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.get_all_users()
    if users :
        res = jsonify({"Message" : 'Get request succeeded'  , 'data': users})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get all users'})
        res.status_code = 404
    return res

@admin_bp.route('/filter_users', methods=['POST'])
def filter_users():
    data = request.get_json()
    users = User.filter_users(data)
    print(users)
    if users :
        res = jsonify({"Message" : 'Get request succeeded'  , 'data': users})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get all users'})
        res.status_code = 404
    return res



@admin_bp.route('/users/<string:_id>', methods=['GET'])
def get_one_user(_id):
    user = User.get_one_user(_id)
    if user :
        res = jsonify({"Message" : 'Get request succeeded' ,'data': user})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get user'})
        res.status_code = 404
    return res


@admin_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    
    if data['role'] == 'admin':
        result = User.create_user(data['cin'], data['name'], data['email'], data['phone'], data['role'], data['state'])
    else :
        result = User.create_user(data['cin'], data['name'], data['email'], data['phone'], data['role'], data['state'],data['type'], data['actorInfoJson'])
    if result == 'User already signed up':
        res = jsonify({'Message': 'User already signed up'})
        res.status_code = 404
    elif result == 'succeed':
        res = jsonify({'Message': 'User created'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get user'})
        res.status_code = 404
    return res


@admin_bp.route('/users/<string:_id>', methods=['PUT'])
def update_user(_id):
    data = request.get_json()
    result = User.update_user(_id, data)
    if 'Unable to update' in result:
        res = jsonify({'Error': result})
        res.status_code = 400
    elif result == 'updated':
        res = jsonify({'Message': 'User updated'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to update user'})
        res.status_code = 404
    return res

@user_bp.route('/users/<string:_id>', methods=['PUT'])
def update_user(_id):
    auth_header = request.headers.get('Authorization')
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if  decoded_token['user_id'] != _id:
        res = jsonify({'Error' : "Unauthorized"})
        res.status_code = 401
        abort(res)
    data = request.get_json()
    result = User.update_user(_id, data)
    if result :
        res = jsonify({'Message': 'user updated'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to update user'})
        res.status_code = 404
    return res



@admin_bp.route('/users/<string:_id>', methods=['DELETE'])
def delete_user(_id):
    result = User.delete_user(_id)
    if result > 0:
        res = jsonify({'Message': 'user deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete user'})
        res.status_code = 404
    return res

@user_bp.route('/users/<string:_id>', methods=['DELETE'])
def delete_user(_id):
    auth_header = request.headers.get('Authorization')
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if  decoded_token['user_id'] != _id:
        res = jsonify({'Error' : "Unauthorized"})
        res.status_code = 401
        abort(res)
    result = User.delete_user(_id)
    if result > 0:
        res = jsonify({'Message': 'user deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete user'})
        res.status_code = 404
    return res
