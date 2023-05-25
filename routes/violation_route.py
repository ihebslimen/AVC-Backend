
from flask import Blueprint, jsonify, request, abort
import jwt
from models.violation import Violation
from blueprints.admin import admin_bp
from blueprints.user import user_bp
from flask_pymongo import PyMongo , ObjectId

import os

SECRET_KEY = 'secretkey'

@admin_bp.route('/violations', methods=['GET'])
def get_all_violations():
    violations = Violation.get_all_violations()
    if violations :
        res = jsonify({"Message" : 'Get request succeeded'  , 'data': violations})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get all violations'})
        res.status_code = 404
    return res
    


@admin_bp.route('/filter_violations', methods=['POST'])
def filter_violations():
    data = request.get_json()
    violations = Violation.filter_violations(data)
    if violations :
        res = jsonify({"Message" : 'Get request succeeded'  , 'data': violations})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get all violations'})
        res.status_code = 404
    return res

@admin_bp.route('/violations/<string:_id>', methods=['GET'])
def get_one_violation(_id):
    violation = Violation.get_one_violation(_id)
    if violation :
        res = jsonify({"Message" : 'Get request succeeded' ,'data': violation})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get violation'})
        res.status_code = 404
    return res


@user_bp.route('/violations', methods=['POST'])
def create_violation():
    auth_header = request.headers.get('Authorization')
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    user_id = decoded_token['user_id']
    data = request.get_json()
    print(data)
    result = Violation.create_violation(data['msg'], user_id)
    if result :
        res = jsonify({'Message': 'violation created'})
        res.status_code = 200
    else:   
        res = jsonify({'Error': 'Unable to get violation'})
        res.status_code = 404
    return res



@admin_bp.route('/violations/<string:_id>', methods=['DELETE'])
def delete_violation(_id):
    result = Violation.delete_violation(_id)
    if result > 0:
        res = jsonify({'Message': 'violation deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete violation'})
        res.status_code = 404
    return res
