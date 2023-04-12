
from flask import Blueprint, jsonify, request
from models.user import User
from blueprints.admin import admin_bp



@admin_bp.route('/users', methods=['GET'])
def get_all_users():
    users = User.get_all_users()
    return jsonify({'users': users})


@admin_bp.route('/users/<string:_id>', methods=['GET'])
def get_one_user(_id):
    user = User.get_one_user(email)
    return jsonify(user)


@admin_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    User.create_user(data['name'], data['email'], data['password'])
    return '', 204


@admin_bp.route('/users/<string:_id>', methods=['PUT'])
def update_user(_id):
    data = request.get_json()
    User.update_user(_id, data['email'], data['name'], data['password'])
    return '', 204


@admin_bp.route('/users/<string:_id>', methods=['DELETE'])
def delete_user(_id):
    User.delete_user(_id)
    return '', 204
