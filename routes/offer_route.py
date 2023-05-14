
from flask import Blueprint, jsonify, request

from models.offer import Offer
from blueprints.user import user_bp



@user_bp.route('/offers', methods=['GET'])
def get_all_offers():
    offers = Offer.get_all_offers()
    if offers :
        res = jsonify({"message" : 'Get request succeeded'  , 'data': offers})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get all offers'})
        res.status_code = 404
    return res
    


@user_bp.route('/filter_offers', methods=['POST'])
def filter_offers():
    data = request.get_json()
    offers = Offer.filter_offers(data)
    if offers :
        res = jsonify({"message" : 'Get request succeeded'  , 'data': offers})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get all offers'})
        res.status_code = 404
    return res

@user_bp.route('/offers/<string:_id>', methods=['GET'])
def get_one_offer(_id):
    offer = Offer.get_one_offer(_id)
    if offer :
        res = jsonify({"message" : 'Get request succeeded' ,'data': offer})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get offer'})
        res.status_code = 404
    return res


@user_bp.route('/offers', methods=['POST'])
def create_offer():
    data = request.get_json()
    print(data)
    result = Offer.create_offer(data['quantity'], data['quality'], data['priceUnit'], data['unit'], data['state'], data['actorType'], data['actorRef'] )
    if result :
        res = jsonify({'message': 'offer created'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to get offer'})
        res.status_code = 404
    return res


@user_bp.route('/offers/<string:_id>', methods=['PUT'])
def update_offer(_id):
    data = request.get_json()
    result = Offer.update_offer(_id, data['quantity'], data['quality'], data['priceUnit'], data['unit'],data['state'], data['actorType'], data['actorRef'])
    if result :
        res = jsonify({'message': 'offer updated'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to update offer'})
        res.status_code = 404
    return res


@user_bp.route('/offers/<string:_id>', methods=['DELETE'])
def delete_offer(_id):
    result = Offer.delete_offer(_id)
    if result > 0:
        res = jsonify({'message': 'offer deleted'})
        res.status_code = 200
    else:
        res = jsonify({'message': 'Unable to delete offer'})
        res.status_code = 404
    return res
