from flask import Flask
from db import mongo
from models.actor import Actor
from flask_pymongo import PyMongo , ObjectId


class Offer(Actor):
    def __init__(self, quantity, quality, priceUnit, unit, state, actorType, actorRef):
        super.__init__(_id,  type)
        self.quantity = quantity
        self.quality = quality
        self.priceUnit = priceUnit
        self.unit = unit
        self.state = state
        self.actorType = actorType
        self.actorRef = actorRef


    @staticmethod
    def get_all_offers():
        offers = mongo.db.offer.find()
        result = []
        for offer in offers:
            result.append({'_id': str(offer['_id']), 'quantity': offer['quantity'], 'quality' : offer['quality'], 'priceUnit' : offer['priceUnit'], 'unit' : offer['unit'], 'actorType' : offer['actorType'], 'actorRef' : str(offer['actorRef'])})
        return result
    @staticmethod
    def get_all_offers_by_actor(actorRef):
        offers = mongo.db.offer.find({'actorRef' : ObjectId(actorRef)})
        result = []
        for offer in offers:
            result.append({'_id': str(offer['_id']), 'quantity': offer['quantity'], 'quality' : offer['quality'], 'priceUnit' : offer['priceUnit'], 'unit' : offer['unit'], 'actorType' : offer['actorType'], 'actorRef' : str(offer['actorRef'])})
        return result

    @staticmethod
    def get_one_offer(_id):
        offer = mongo.db.offer.find_one({'_id': _id})
        return {'_id': str(offer['_id']), 'quantity': offer['quantity'], 'quality' : offer['quality'], 'priceUnit' : offer['priceUnit'], 'unit' : offer['unit'], 'actorType' : offer['actorType'], 'actorRef' : str(offer['actorRef'])}

    @staticmethod
    def create_offer(  quantity, quality, priceUnit, unit, state, actorType, actorRef):
        offer = {'quantity': quantity, 'quality' : quality, 'priceUnit' : priceUnit, 'unit' : unit, 'actorType' : actorType, 'actorRef' :ObjectId(actorRef)}
        mongo.db.offer.insert_one(offer)

    @staticmethod
    def update_offer(_id, quantity, quality, priceUnit, unit, state, actorType, actorRef):
        mongo.db.offer.update_one({'_id': ObjectId(_id)}, {'$set': {'quantity': quantity, 'quality' : quality, 'priceUnit' : priceUnit, 'unit' : unit,'state' : state, 'actorType' : actorType, 'actorRef' : actorRef}})

    @staticmethod
    def delete_offer(_id):
        mongo.db.offer.delete_one({'_id':ObjectId(_id)})
