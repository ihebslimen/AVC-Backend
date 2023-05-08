
from flask import Blueprint, jsonify, request

from models.offer import Offer
from blueprints.user import user_bp



@user_bp.route('/offers', methods=['GET'])
def get_all_offers():
    offers = Offer.get_all_offers()
    return jsonify({'offers': offers})
    
@user_bp.route('/offers/filter/<string:key>/<string:value>', methods=['GET'])
def filter_offers(key, value):
    offers = Offer.get_all_offers_by_actor(actorRef)
    return jsonify(offers)

@user_bp.route('/offers/<string:_id>', methods=['GET'])
def get_one_offer(_id):
    offers = Offer.get_all_offers_by_actor(_id)
    return jsonify(offers)


@user_bp.route('/offers', methods=['POST'])
def create_offer():
    data = request.get_json()
    print(data)
    Offer.create_offer(data['quantity'], data['quality'], data['priceUnit'], data['unit'], data['state'], data['actorType'], data['actorRef'] )
    return '', 204


@user_bp.route('/offers/<string:_id>', methods=['PUT'])
def update_offer(_id):
    data = request.get_json()
    Offer.update_offer(_id, data['quantity'], data['quality'], data['priceUnit'], data['unit'],data['state'], data['actorType'], data['actorRef'])
    return '', 204


@user_bp.route('/offers/<string:_id>', methods=['DELETE'])
def delete_offer(_id):
    Offer.delete_offer(_id)
    return '', 204
