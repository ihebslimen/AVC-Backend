
from flask import Blueprint, jsonify, request
import jwt
from models.offer import Offer
from blueprints.admin import admin_bp
from blueprints.user import user_bp



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
    


@user_bp.route('/filter_offers', methods=['POST'])
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
    print(data)
    result = Offer.create_offer(data['quantity'], data['quality'], data['priceUnit'], data['unit'], data['state'], data['actorType'], data['actorRef'] )
    if result :
        res = jsonify({'Message': 'offer created'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get offer'})
        res.status_code = 404
    return res


@user_bp.route('/offers/<string:_id>', methods=['PUT'])
def update_offer(_id):
    auth_header = request.headers.get('Authorization')
    if auth_header :
        jwt_token = auth_header.split(' ')[1]
        decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        if  decoded_token['user_id'] != _id:
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


@user_bp.route('/offers/<string:_id>', methods=['DELETE'])
def delete_offer(_id):
    auth_header = request.headers.get('Authorization')
    if auth_header :
        jwt_token = auth_header.split(' ')[1]
        decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        if  decoded_token['user_id'] != _id:
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
