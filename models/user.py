from flask import Flask
from flask_pymongo import PyMongo
from db import mongo


class User():
    def __init__(self,_id, cin, name, email, phone, role):
        self._id
        self.cin = cin
        self.name = name
        self.email = email
        self.phone = phone
        self.role = role

    @staticmethod
    def get_all_users():
        users = mongo.db.users.find()
        result = []
        for user in users:
            result.append({'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role'])})
        return result

    @staticmethod
    def get_one_user(_id):
        user = mongo.db.users.find_one({'_id': _id})
        return {'_id': str(user['_id']),'cin': str(user['cin']), 'name': user['name'], 'email': user['email'], 'phone': user['phone'], 'role': str(user['role'])}

    @staticmethod
    def create_user(cin, name, email, phone, role):
        user = {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role}
        mongo.db.users.insert_one(user)

    @staticmethod
    def update_user(cin, name, email, phone, role):
        mongo.db.users.update_one({'_id': ObjectId(_id)}, {'$set': {'cin': cin, 'name':name, 'email': email, 'phone': phone, 'role': role}})

    @staticmethod
    def delete_user(_id):
        mongo.db.users.delete_one({'_id':ObjectId(_id)})
