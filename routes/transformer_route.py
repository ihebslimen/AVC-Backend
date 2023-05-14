
from flask import Blueprint, jsonify, request
from models.transformer import transformer
from blueprints.admin import admin_bp



@admin_bp.route('/transformers', methods=['GET'])
def get_all_transformers():
    transformers = transformer.get_all_transformers()
    if transformers :
        res = jsonify({"message" : 'Get request succeeded'  , 'data': transformers})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get all transformers'})
        res.status_code = 404
    return res


@admin_bp.route('/transformers/<string:_id>', methods=['GET'])
def get_one_transformer(_id):
    transformer = transformer.get_one_transformer(_id)
    if transformer :
        res = jsonify({"message" : 'Get request succeeded' ,'data': transformer})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get transformer'})
        res.status_code = 404
    return res

@user_bp.route('/filter_transformer', methods=['POST'])
def filter_transformer():
    data = request.get_json()
    transformer = Offer.filter_transformer(data)
    if transformer :
        res = jsonify({"message" : 'Get request succeeded'  , 'data': transformer})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get all transformer'})
        res.status_code = 404
    return res

@admin_bp.route('/transformers', methods=['POST'])
def create_transformer():
    data = request.get_json()
    result = transformer.create_transformer(data['localisation'] )
    if result :
        res = jsonify({'message': 'transformer created'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get transformer'})
        res.status_code = 404
    return res


@admin_bp.route('/transformers/<string:_id>', methods=['PUT'])
def update_transformer(_id):
    data = request.get_json()
    result = transformer.update_transformer(_id, data['localisation'])
    if result :
        res = jsonify({'message': 'transformer updated'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to update transformer'})
        res.status_code = 404
    return res

@admin_bp.route('/transformers/<string:_id>', methods=['DELETE'])
def delete_transformer(_id):
    result = transformer.delete_transformer(_id)
    if result > 0:
        res = jsonify({'message': 'transformer deleted'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to delete transformer'})
        res.status_code = 404
    return res
