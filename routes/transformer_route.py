
from flask import Blueprint, jsonify, request
from models.transformer import Transformer
from blueprints.admin import admin_bp
from blueprints.user import user_bp


SECRET_KEY = 'secretkey'


@admin_bp.route('/transformers', methods=['GET'])
def get_all_transformers():
    transformers = transformer.get_all_transformers()
    if transformers :
        res = jsonify({"Message" : 'Get request succeeded'  , 'data': transformers})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get all transformers'})
        res.status_code = 404
    return res


@admin_bp.route('/transformers/<string:_id>', methods=['GET'])
def get_one_transformer(_id):
    transformer = transformer.get_one_transformer(_id)
    if transformer :
        res = jsonify({"Message" : 'Get request succeeded' ,'data': transformer})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get transformer'})
        res.status_code = 404
    return res

@user_bp.route('/filter_transformer', methods=['POST'])
def filter_transformer():
    data = request.get_json()
    transformer = Offer.filter_transformer(data)
    if transformer :
        res = jsonify({"Message" : 'Get request succeeded'  , 'data': transformer})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get all transformer'})
        res.status_code = 404
    return res

@admin_bp.route('/transformers', methods=['POST'])
def create_transformer():
    data = request.get_json()
    result = transformer.create_transformer(data['localisation'] )
    if result :
        res = jsonify({'Message': 'transformer created'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get transformer'})
        res.status_code = 404
    return res


@admin_bp.route('/transformers/<string:_id>', methods=['PUT'])
def update_transformer(_id):
    data = request.get_json()
    result = transformer.update_transformer(_id, data)
    if result :
        res = jsonify({'Message': 'transformer updated'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to update transformer'})
        res.status_code = 404
    return res

@admin_bp.route('/transformers/<string:_id>', methods=['DELETE'])
def delete_transformer(_id):
    result = transformer.delete_transformer(_id)
    if result > 0:
        res = jsonify({'Message': 'transformer deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete transformer'})
        res.status_code = 404
    return res

@user_bp.route('/transformers/<string:_id>', methods=['PUT'])
def update_transformer(_id):
    auth_header = request.headers.get('Authorization')
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if  decoded_token['user_id'] != _id:
        res = jsonify({'Error' : "Unauthorized"})
        res.status_code = 401
        abort(res)
    data = request.get_json()
    result = transformer.update_transformer(_id, data)
    if result :
        res = jsonify({'Message': 'transformer updated'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to update transformer'})
        res.status_code = 404
    return res

@user_bp.route('/transformers/<string:_id>', methods=['DELETE'])
def delete_transformer(_id):
    auth_header = request.headers.get('Authorization')
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if  decoded_token['user_id'] != _id:
        res = jsonify({'Error' : "Unauthorized"})
        res.status_code = 401
        abort(res)
    result = transformer.delete_transformer(_id)
    if result > 0:
        res = jsonify({'Message': 'transformer deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete transformer'})
        res.status_code = 404
    return res
