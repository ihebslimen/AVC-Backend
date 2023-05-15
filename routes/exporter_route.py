
from flask import Blueprint, jsonify, request
from models.exporter import exporter
from blueprints.admin import admin_bp



@admin_bp.route('/exporters', methods=['GET'])
def get_all_exporters():
    exporters = exporter.get_all_exporters()
    if exporters :
        res = jsonify({"message" : 'Get request succeeded'  , 'data': exporters})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get all exporters'})
        res.status_code = 404
    return res


@admin_bp.route('/exporters/<string:_id>', methods=['GET'])
def get_one_exporter(_id):
    exporter = exporter.get_one_exporter(_id)
    if exporter :
        res = jsonify({"message" : 'Get request succeeded' ,'data': exporter})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get exporter'})
        res.status_code = 404
    return res

@user_bp.route('/filter_exporter', methods=['POST'])
def filter_exporter():
    data = request.get_json()
    exporter = Offer.filter_exporter(data)
    if exporter :
        res = jsonify({"message" : 'Get request succeeded'  , 'data': exporter})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get all exporter'})
        res.status_code = 404
    return res

@admin_bp.route('/exporters', methods=['POST'])
def create_exporter():
    data = request.get_json()
    result = exporter.create_exporter(data['localisation'] )
    if result :
        res = jsonify({'Message': 'exporter created'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get exporter'})
        res.status_code = 404
    return res


@admin_bp.route('/exporters/<string:_id>', methods=['PUT'])
def update_exporter(_id):
    data = request.get_json()
    result = exporter.update_exporter(_id, data)
    if result :
        res = jsonify({'Message': 'exporter updated'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to update exporter'})
        res.status_code = 404
    return res

@admin_bp.route('/exporters/<string:_id>', methods=['DELETE'])
def delete_exporter(_id):
    result = exporter.delete_exporter(_id)
    if result > 0:
        res = jsonify({'Message': 'exporter deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete exporter'})
        res.status_code = 404
    return res

@user_bp.route('/exporters/<string:_id>', methods=['PUT'])
def update_exporter(_id):
    auth_header = request.headers.get('Authorization')
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if  decoded_token['user_id'] != _id:
        res = jsonify({'Error' : "Unauthorized"})
        res.status_code = 401
        abort(res)
    data = request.get_json()
    result = exporter.update_exporter(_id, data)
    if result :
        res = jsonify({'Message': 'exporter updated'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to update exporter'})
        res.status_code = 404
    return res

@user_bp.route('/exporters/<string:_id>', methods=['DELETE'])
def delete_exporter(_id):
    auth_header = request.headers.get('Authorization')
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    if  decoded_token['user_id'] != _id:
        res = jsonify({'Error' : "Unauthorized"})
        res.status_code = 401
        abort(res)
    result = exporter.delete_exporter(_id)
    if result > 0:
        res = jsonify({'Message': 'exporter deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete exporter'})
        res.status_code = 404
    return res
