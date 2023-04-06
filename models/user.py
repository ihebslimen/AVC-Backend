from flask import Flask
from flask_pymongo import PyMongo
from db import mongo
from werkzeug.security import generate_password_hash, check_password_hash



class User:
    def __init__(self,_id, name, email, password):
        self._id
        self.name = name
        self.email = email
        self.password = password

    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        result = []
        for user in users:
            result.append({'_id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']})
        return result

    @staticmethod
    def get_one_user(_id):
        user = mongo.db.users.find_one({'_id': _id})
        return {'_id': str(user['_id']), 'name': user['name'], 'email': user['email'], 'password': user['password']}

    @staticmethod
    def create_user(name, email, password):
        user = {'name': name, 'email': email, 'password': generate_password_hash(password)}
        mongo.db.users.insert_one(user)

    @staticmethod
    def update_user(_id, email, name, password):
        mongo.db.users.update_one({'_id': ObjectId(_id)}, {'$set': {'email':email, 'name': name, 'password': generate_password_hash(password)}})

    @staticmethod
    def delete_user(_id):
        mongo.db.users.delete_one({'_id':ObjectId(_id)})
