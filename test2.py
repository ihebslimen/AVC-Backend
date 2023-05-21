from db import mongo
from flask import Flask
import os
from flask_pymongo import ObjectId


MONGO_URI = os.environ.get('MONGO_URI')

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo.init_app(app)



#session = mongo.cx.start_session()
supplychain_users = mongo.db.users


with mongo.cx.start_session() as session:
    with session.start_transaction():
        print(session)

        user = {'cin': "12345", 'name':"testo", 'email': "a@a.a", 'phone': "12345", 'role': "user", 'type' : "agro",'state': "not","public_key": "pub","private_key" : "priv" }
        inserted_id = supplychain_users.insert_one(user, session=session).inserted_id
        print(inserted_id)
        user = mongo.db.users.find_one({'_id': ObjectId(inserted_id)})
        print(user)
        raise Exception

        #raise Exception
