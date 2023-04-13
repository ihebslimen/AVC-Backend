
from flask import Blueprint, jsonify, request
from models.user import User
from blueprints.admin import admin_bp
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
import jwt
import os

SECRET_KEY = os.environ.get('SECRET_KEY')

@admin_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.get_all_users()

    return jsonify({'users': users})

@admin_bp.route('/decode_jwt', methods=['GET'])
def decode_jwt():
    auth_header = request.headers.get('Authorization')
    if auth_header is None:
        return {'error': 'Authorization header is missing'}, 401
    try:
        jwt_token = auth_header.split(' ')[1]
        decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        return {'decoded_token': decoded_token}, 200
    except jwt.exceptions.InvalidTokenError:
        return {'error': 'Invalid JWT token'}, 401

@admin_bp.route('/users/<string:_id>', methods=['GET'])
def get_one_user(_id):
    user = User.get_one_user(_id)
    return jsonify(user)


@admin_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    User.create_user(data['cin'], data['name'], data['email'], data['phone'], data['role'])
    return '', 204


@admin_bp.route('/users/<string:_id>', methods=['PUT'])
def update_user(_id):
    data = request.get_json()
    User.update_user(_id, data['cin'], data['name'], data['email'], data['phone'], data['role'])
    return '', 204


@admin_bp.route('/users/<string:_id>', methods=['DELETE'])
def delete_user(_id):
    User.delete_user(_id)
    return '', 204
