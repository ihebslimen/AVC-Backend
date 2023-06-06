from flask import Flask
from db import mongo
from models.actor import Actor
from flask_pymongo import PyMongo , ObjectId



class Achat(Actor):
    def __init__(self, buyer,  seller , quantity, quality, priceUnit):
        super.__init__(_id,  type)
        self.quantity = quantity
        self.quality = quality
        self.price = price
        self.buyer = buyer
        self.seller = seller



    @staticmethod
    def get_all_achats(acteur):
        achats1 = mongo.db.achat.find({"buyer" : acteur })
        achats2 = mongo.db.achat.find({"seller" : acteur })

        result = []
        for achat in achats1:
            result.append({'buyer': 'Moi', 'seller' : achat['seller'], 'quantity' : achat['quantity'], 'quality' : achat['quality'],'price' : achat['price']})
        
        for achat in achats2:
            result.append({'buyer': achat['buyer'], 'seller' : 'Moi', 'quantity' : achat['quantity'], 'quality' : achat['quality'],'price' : achat['price']})
        
        
        return result
        
   
    @staticmethod
    def create_achat(  buyer, seller, quality, quantity, price):
        achat = {'buyer':buyer,'seller':seller, 'quantity': quantity, 'quality' : quality, 'price' : price}
        res = mongo.db.achat.insert_one(achat)
        return res.acknowledged


