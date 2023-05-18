
from flask import Blueprint, jsonify, request

from models.offer import Offer
from blueprints.admin import admin_bp
from blueprints.user import user_bp
from flask_jwt_extended import  jwt_required, get_jwt_identity

@user_bp.route('/offers', methods=['GET'])
@jwt_required()
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
@jwt_required()
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
@jwt_required()
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
@jwt_required()
def create_offer():
    data = request.get_json()
    actorRef = get_jwt_identity()
    result = Offer.create_offer(data['quantity'], data['quality'], data['priceUnit'], data['unit'], data['state'], data['actorType'], actorRef )
    if result :
        res = jsonify({'Message': 'offer created'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to get offer'})
        res.status_code = 404
    return res


@user_bp.route('/offers/<string:_id>', methods=['PUT'])
@jwt_required()
def update_offer(_id):
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
@jwt_required()
def delete_offer(_id):
    result = Offer.delete_offer(_id)
    if result > 0:
        res = jsonify({'Message': 'offer deleted'})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Unable to delete offer'})
        res.status_code = 404
    return res
