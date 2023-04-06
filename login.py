from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime
from flask_pymongo import PyMongo , ObjectId
from bson import  json_util
import json

# Create Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

app.config['MONGO_URI']= 'mongodb+srv://iheb:iheb@cluster0.bjpaw5n.mongodb.net/supplychain?retryWrites=true&w=majority'
mongo = PyMongo(app)
# Define login route
@app.route('/api/login', methods=['POST'])
def login():
    auth = request.json
    res = mongo.db.users.find_one({'email': auth['email'] })
    if res is None :
        return 'Wrong Credentials'
    else:
        if check_password_hash(res['password'], auth['password']):
            user_id = res['_id']
            serialized_user_id = json.loads(json_util.dumps(user_id))
            access_token = jwt.encode({'user_id': serialized_user_id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.config['SECRET_KEY'])
            return jsonify({'access_token': access_token})

# Run the app
if __name__ == '__main__':
    app.run(port=5001,debug=True)
