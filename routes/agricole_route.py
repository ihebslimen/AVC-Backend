
from flask import Blueprint, jsonify, request
from models.agricole import Agricole
from blueprints.admin import admin_bp



@admin_bp.route('/agricoles', methods=['GET'])
def get_all_agricoles():
    agricoles = Agricole.get_all_agricoles()
    return jsonify({'agricoles': agricoles})


@admin_bp.route('/agricoles/<string:_id>', methods=['GET'])
def get_one_agricole(_id):
    agricole = Agricole.get_one_agricole(_id)
    return jsonify(agricole)


@admin_bp.route('/agricoles', methods=['POST'])
def create_agricole():
    data = request.get_json()
    Agricole.create_agricole(data['localisation'] )
    return '', 204


@admin_bp.route('/agricoles/<string:_id>', methods=['PUT'])
def update_agricole(_id):
    data = request.get_json()
    Agricole.update_agricole(_id, data['privateKey'], data['publicKey'], data['type'],data['localisation'])
    return '', 204


@admin_bp.route('/agricoles/<string:_id>', methods=['DELETE'])
def delete_agricole(_id):
    Agricole.delete_agricole(_id)
    return '', 204
