from flask import Flask
from db import mongo
from models.actor import Actor
from flask_pymongo import PyMongo , ObjectId



class Transformer(Actor):
    def __init__(self,_id, label,localisation):
        self.label = label
        self.localisation = localisation

    @staticmethod
    def get_all_transformers():
        transformers = mongo.db.transformer.find()
        result = []
        for transformer in transformers:
            result.append({'_id': str(transformer['_id']), 'label' : transformer['label'],  'localisation' : transformer['localisation'],'user_ref' : transformer['user_ref']})
        return result

    @staticmethod
    def get_one_transformer(_id):
        transformer = mongo.db.transformer.find_one({'_id': ObjectId(_id) })
        return {'_id': str(transformer['_id']), 'label' : transformer['label'], 'localisation' : transformer['localisation'], 'user_ref' : transformer['user_ref']}


    @staticmethod
    def filter_transformer(query):
        if '_id' in query:
            query['_id'] = ObjectId(query[value])
        transformers = mongo.db.transformer.find(query)
        result = []
        for transformer in transformers:
            result.append({'_id': str(transformer['_id']), 'label' : transformer['label'],  'localisation' : transformer['localisation'],'user_ref' : transformer['user_ref']})
        return result

    @staticmethod
    def create_transformer( label, localisation):
        transformer = { 'label' : label , 'localisation' : localisation}
        res = mongo.db.transformer.insert_one(transformer)
        return res.acknowledged

    @staticmethod
    def update_transformer(_id, query):
        res = mongo.db.transformer.update_one({'_id': ObjectId(_id)}, {'$set': query})
        return res.acknowledged

    @staticmethod
    def delete_transformer(_id):
        res = mongo.db.transformer.delete_one({'_id':ObjectId(_id)})
        return res.deleted_count
