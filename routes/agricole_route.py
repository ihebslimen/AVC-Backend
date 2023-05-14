
from flask import Blueprint, jsonify, request
from models.agricole import Agricole
from blueprints.admin import admin_bp



@admin_bp.route('/agricoles', methods=['GET'])
def get_all_agricoles():
    agricoles = Agricole.get_all_agricoles()
    if agricoles :
        res = jsonify({"message" : 'Get request succeeded'  , 'data': agricoles})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get all agricoles'})
        res.status_code = 404
    return res


@admin_bp.route('/agricoles/<string:_id>', methods=['GET'])
def get_one_agricole(_id):
    agricole = Agricole.get_one_agricole(_id)
    if agricole :
        res = jsonify({"message" : 'Get request succeeded' ,'data': agricole})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get agricole'})
        res.status_code = 404
    return res


@user_bp.route('/filter_agricole', methods=['POST'])
def filter_agricole():
    data = request.get_json()
    agricole = Offer.filter_agricole(data)
    if agricole :
        res = jsonify({"message" : 'Get request succeeded'  , 'data': agricole})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get all agricole'})
        res.status_code = 404
    return res

@admin_bp.route('/agricoles', methods=['POST'])
def create_agricole():
    data = request.get_json()
    result = Agricole.create_agricole(data['localisation'] )
    if result :
        res = jsonify({'message': 'Agricole created'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get agricole'})
        res.status_code = 404
    return res


@admin_bp.route('/agricoles/<string:_id>', methods=['PUT'])
def update_agricole(_id):
    data = request.get_json()
    result = Agricole.update_agricole(_id, data['localisation'])
    if result :
        res = jsonify({'message': 'Agricole updated'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to update agricole'})
        res.status_code = 404
    return res

@admin_bp.route('/agricoles/<string:_id>', methods=['DELETE'])
def delete_agricole(_id):
    result = Agricole.delete_agricole(_id)
    if result > 0:
        res = jsonify({'message': 'Agricole deleted'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to delete agricole'})
        res.status_code = 404
    return res
