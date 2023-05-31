
from flask import Blueprint, jsonify, request, abort
import jwt
from models.offer import Offer
from blueprints.admin import admin_bp
from blueprints.user import user_bp
from flask_pymongo import PyMongo , ObjectId
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


import os

SECRET_KEY = 'secretkey'




@user_bp.route('/offers', methods=['GET'])
def get_all_offers():
    offers = Offer.get_all_offers()
    if offers :
        res = jsonify({"Message" : 'Get request succeeded'  , 'data': offers})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get all offers'})
        res.status_code = 404
    return res
    
@user_bp.route('/offers/filter_offers', methods=['POST'])
def filter_offers():
    data = request.get_json()
    offers = Offer.filter_offers(data)
    if offers :
        res = jsonify({"Message" : 'Get request succeeded'  , 'data': offers})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get all offers'})
        res.status_code = 404
    return res

@user_bp.route('/offers/<string:_id>', methods=['GET'])
def get_one_offer(_id):
    offer = Offer.get_one_offer(_id)
    if offer :
        res = jsonify({"Message" : 'Get request succeeded' ,'data': offer})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get offer'})
        res.status_code = 404
    return res


@user_bp.route('/offers', methods=['POST'])
def create_offer():
    data = request.get_json()
    auth_header = request.headers.get('Authorization')
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    actorRef = decoded_token['user_id']
    result = Offer.create_offer(data['quantity'], data['quality'], data['priceUnit'], data['unit'], data['state'], data['actorType'], actorRef )
    if result :
        res = jsonify({'Message': 'offer created'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get offer'})
        res.status_code = 404
    return res


@user_bp.route('/offers/<string:_id>', methods=['PUT'])
def update_offer(_id):
    offer = Offer.get_one_offer(_id)
    auth_header = request.headers.get('Authorization')
    if auth_header :
        jwt_token = auth_header.split(' ')[1]
        decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        if  decoded_token['user_id'] != offer['actorRef']:
            res = jsonify({'Error' : "Unauthorized"})
            res.status_code = 401
            abort(res)
    data = request.get_json()
    result = Offer.update_offer(_id, data)
    if result :
        res = jsonify({'Message': 'offer updated'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to update offer'})
        res.status_code = 404
    return res


@user_bp.route('/offers/buy_offer', methods=['POST'])
def buy_offer():
    data = request.get_json()
    offer = Offer.get_one_offer(data['_id'])
    auth_header = request.headers.get('Authorization')
    if auth_header :
        jwt_token = auth_header.split(' ')[1]
        decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token['user_id']
        actorType = decoded_token['type']
        result = Offer.update_offer(offer['_id'], {'actorRef': user_id, "actorType": actorType})
        if result :
            res = jsonify({'Message': 'offer Bought'})
            res.status_code = 200
        else:
            res = jsonify({'Error': 'Unable to Buy Offer'})
            res.status_code = 404
        return res
    else:
        res = jsonify({'Error': 'Header is Missing!!!'})
        res.status_code = 401
        return res

    """ 
@user_bp.route('/offers/buy_offer', methods=['POST'])
def buy_offer():
    data = request.get_json()
    offer = Offer.get_one_offer(data['_id'])
    user_id = data['user_id']
    result = Offer.update_offer(offer['_id'], {'actorRef': user_id, "actorType": data["actorType"]})
    if result :
        res = jsonify({'Message': 'offer Bought'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to Buy Offer'})
        res.status_code = 404
    return res

 """

@user_bp.route('/offers/<string:_id>', methods=['DELETE'])
def delete_offer(_id):
    offer = Offer.get_one_offer(_id)
    auth_header = request.headers.get('Authorization')
    if auth_header :
        jwt_token = auth_header.split(' ')[1]
        decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        if  decoded_token['user_id'] != offer['actorRef']:
            res = jsonify({'Error' : "Unauthorized"})
            res.status_code = 401
            abort(res)
    result = Offer.delete_offer(_id)
    if result > 0:
        res = jsonify({'Message': 'offer deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete offer'})
        res.status_code = 404
    return res
