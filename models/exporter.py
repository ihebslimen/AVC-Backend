from flask import Flask
from db import mongo
from models.actor import Actor
from flask_pymongo import PyMongo , ObjectId



class Exporter(Actor):
    def __init__(self,_id,label):
        self.label = label

    @staticmethod
    def get_all_exporters():
        exporters = mongo.db.exporter.find()
        result = []
        for exporter in exporters:
            result.append({'_id': str(exporter['_id']), 'label' : exporter['label'], 'user_ref' : exporter['user_ref']})
        return result

    @staticmethod
    def get_one_exporter(_id):
        exporter = mongo.db.exporter.find_one({'_id': ObjectId(_id) })
        return {'_id': str(exporter['_id']), 'label' : exporter['label'], 'user_ref' : exporter['user_ref']}


    @staticmethod
    def filter_exporter(query):
        if '_id' in query:
            query['_id'] = ObjectId(query[value])
        exporters = mongo.db.exporter.find(query)
        result = []
        for exporter in exporters:
            result.append({'_id': str(exporter['_id']), 'label' : exporter['label'],  'user_ref' : exporter['user_ref']})
        return result

    @staticmethod
    def create_exporter( label, localisation):
        exporter = { 'label' : label }
        res = mongo.db.exporter.insert_one(exporter)
        return res.acknowledged

    @staticmethod
    def update_exporter(_id, label):
        res = mongo.db.exporter.update_one({'_id': ObjectId(_id)}, {'$set': {'label' : label }})
        return res.acknowledged

    @staticmethod
    def delete_exporter(_id):
        res = mongo.db.exporter.delete_one({'_id':ObjectId(_id)})
        return res.deleted_count
