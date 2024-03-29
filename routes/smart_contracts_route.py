from flask import Flask, jsonify, request,url_for,session, g
from models.transaction import Transaction
from models.achat import Achat
import json
import os
import requests
from blueprints.user import user_bp
from blueprints.admin import admin_bp
from web3models.Account import *
import jwt

SECRET_KEY = 'secretkey'


def serialize_function(obj):
    if isinstance(obj, type):
        return str(obj)
    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")


def mappingTX(tuple_data):
    function_name = str(tuple_data[0]).split('Function')[-1].strip().split('(')[0].strip()
    arguments = tuple_data[1]
    if function_name == "createProduct":
        return {"tache": "Creation Produit" , "product_id" : arguments['_prod_id'], "product_quality" : arguments['_prod_qlt'], "product_quantity" : arguments['_prod_qty']}
    if function_name == "updateProduct":
        return {"tache": "Mise a Jour Produit" , "product_id" : arguments['_prod_id'], "product_quality" : arguments['_prod_qlt'], "product_quantity" : arguments['_prod_qty']}
    if function_name == "deleteProduct":
            return {"tache": "Supprimer Produit" , "product_id" : arguments['_prod_id'], "product_quality" : arguments['_prod_qlt'], "product_quantity" : arguments['_prod_qty']}
    if function_name == "createOffer":
            return {"tache": "Creation Offre" , "offer_id" : arguments['_offer_id'],"product_id" : arguments['_prod_id'], "product_quantity" : arguments['_prod_qty'], "prix_unity" : arguments['_price']}
    if function_name == "buyOffer":
            return {"tache": "Acheter Offre" , "offer_id" : arguments['_offer_id']}
    if function_name == "listAllOffers":
            return {"tache": "Lister Offres" }

def process_events(tuple_data):
    serialized_data = str(tuple_data[0])
    parsed_data = json.loads(serialized_data)

    function_name = parsed_data['function']
    print(function_name)

    serialized_data = json.dumps({
        'function': str(tuple_data[0]),
        'arguments': tuple_data[1]
    })
    print(serialized_data)
    history.append(serialized_data)


map_actor_type = {'notype' : 0,"admin": 1, "farmer": 2, "transformer":3}

@user_bp.route('/blockchain/actor_type', methods=['POST'])
def actor_type():
    data = request.get_json()
    for  key, val  in map_actor_type.items():
        try:
            result = AccessControlContract.functions.hasUserType(data['pub_key'],val).call()
            if result:
                res = jsonify({'Message' : key })
                res.status_code = 200  
                return res
        except Exception as e:
            error_msg = str(e).split("revert")[-1].strip()
            res= jsonify({'Error': error_msg})
            res.status_code = 404
            return res
        
    res = jsonify({'Error' : 'This address is not subscribed to the chain' })
    res.status_code = 404
    return res

@admin_bp.route('/blockchain/actor_type', methods=['POST'])
def actor_type():

    data = request.get_json()
    for  key, val  in map_actor_type.items():
        try:
            result = AccessControlContract.functions.hasUserType(data['pub_key'],val).call()
            if result:
                res = jsonify({'Message' : key })
                res.status_code = 200  
                return res
        except Exception as e:
            error_msg = str(e).split("revert")[-1].strip()
            res= jsonify({'Error': error_msg})
            res.status_code = 404
            return res
        
    res = jsonify({'Error' : 'This address is not subscribed to the chain' })
    res.status_code = 404
    return res

    

@admin_bp.route('/blockchain/add_farmer', methods=['POST'])
def add_farmer():

    try:
        data = request.get_json()
        result = g.account_loggedIn.setUserType( data['pub_key'], 2)
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Farmer Added'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Adding Farmer Failed'})
        res.status_code = 404
    return res

@admin_bp.route('/blockchain/add_transformer', methods=['POST'])
def add_transformer():

    try:
        data = request.get_json()
        result = g.account_loggedIn.setUserType( data['pub_key'], 3)
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Transformer Added'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Adding Transformer Failed'})
        res.status_code = 404
    return res

@admin_bp.route('/blockchain/add_admin', methods=['POST'])
def add_admin():

    try:
        data = request.get_json()
        result = g.account_loggedIn.setUserType( data['pub_key'], 1)
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Admin Added'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Adding Admin Failed'})
        res.status_code = 404
    return res

@admin_bp.route('/blockchain/remove_actor', methods=['POST'])
def remove_actor():

    try:
        data = request.get_json()
        result = g.account_loggedIn.setUserType( data['pub_key'], 0)
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Actor Removed'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Removing Actor Failed'})
        res.status_code = 404
    return res

@admin_bp.route('/blockchain/delete_account', methods=['POST'])
def delete_account():

    try:
        data = request.get_json()
        for key, val in map_actor_type.items():
            result = AccessControlContract.functions.hasUserType(data['pub_key'],val).call()
            if result:
                break
        print(val)
        result1 = g.account_loggedIn.delUserType( data['pub_key'], val)
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result1:
        res = jsonify({'Message': 'Account Deleted'})
        res.status_code = 200
    elif not result1:
        res = jsonify({'Error': 'Deleting Account Failed'})
        res.status_code = 404
    return res

@user_bp.route('/blockchain/create_product', methods=['POST'])
def create_product():

    data = request.get_json()
    objects = dir(g)
    print(' '.join(objects))


    try:
        print(g.account_loggedIn.pub_key)
        result = g.account_loggedIn.createProduct( data['product_id'],data['product_quantity'],data['product_quality'])
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Product Created'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Creating Product Failed'})
        res.status_code = 404
    return res

@user_bp.route('/blockchain/delete_product', methods=['POST'])
def delete_product():

    data = request.get_json()
    try:
        result = g.account_loggedIn.deleteProduct( data['product_id'])
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Product Deleted'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Deleting Product Failed'})
        res.status_code = 404
    return res


@user_bp.route('/blockchain/update_product', methods=['POST'])
def update_product():

    data = request.get_json()
    try:
        result = g.account_loggedIn.updateProduct( data['product_id'],data['product_quantity'],data['product_quality'])
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Product Updated'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Updating Product Failed'})
        res.status_code = 404
    return res

@user_bp.route('/blockchain/check_owner_product', methods=['POST'])
def get_product_owner():

    data = request.get_json()
    try:
        result = ProductContract.functions.isProductOwner( data['pub_key'],data['product_id']).call()
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Owner of Product!!'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Not the Owner'})
        res.status_code = 404
    return res


@admin_bp.route('/blockchain/check_owner_product', methods=['POST'])
def get_product_owner():

    data = request.get_json()
    try:
        result = ProductContract.functions.isProductOwner( data['pub_key'],data['product_id']).call()
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Owner of Product!!'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Not the Owner'})
        res.status_code = 404
    return res



@user_bp.route('/blockchain/get_actor_products', methods=['POST'])
def get_products():
    data = request.get_json()
    try:
        result_tx = g.account_loggedIn.getProductsByAddress(data['pub_key'])
        products = ProductContract.functions.getProductsByAddress(data['pub_key']).call()
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if products and result_tx:
        print(products)
        res = jsonify({'Message': 'Get All Products Succeeded!!', 'data': products})
        res.status_code = 200
    elif not result_tx:
        res = jsonify({'Error': 'Not the Owner'})
        res.status_code = 404
    return res


@user_bp.route('/blockchain/create_offer', methods=['POST'])
def create_offer_blockchain():
    data = request.get_json()
    try:
        result = g.account_loggedIn.createOffer( data['offer_id'], data['product_id'],data['product_quantity'],data['price'])
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Offer Created'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Creating Offer Failed'})
        res.status_code = 404
    return res




@user_bp.route('/blockchain/check_owner_offer', methods=['POST'])
def get_offer_owner():
    data = request.get_json()
    try:
        result = OfferContract.functions.isOfferOwner( data['pub_key'],data['offer_id']).call()
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Owner of Offer!!'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Not the Offer Owner'})
        res.status_code = 404
    return res

@user_bp.route('/blockchain/buy_offer', methods=['POST'])
def buy_offer_blockchain():
    data = request.get_json()
    try:
        result = g.account_loggedIn.buyOffer( data['offer_id'])
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Buying Offer Succeeded!!'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Buying Offer Failed'})
        res.status_code = 404
    return res



@user_bp.route('/blockchain/get_actor_offers', methods=['POST'])
def get_offers():
    data = request.get_json()
    try:
        result_tx = g.account_loggedIn.getOfferByOwner(data['pub_key'])
        offers = OfferContract.functions.getOfferByOwner(data['pub_key']).call()
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if offers and result_tx:
        print(offers)
        res = jsonify({'Message': 'Get All Offers by Acteur Succeeded!!', 'data': offers})
        res.status_code = 200
    elif not result_tx:
        res = jsonify({'Error': 'Get All Offers by Acteur Failed!!'})
        res.status_code = 404
    return res

@user_bp.route('/blockchain/get_all_offers', methods=['POST'])
def get_all_offers_blockchain():
    try:
        offers = OfferContract.functions.listAllOffers().call()
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if offers :
        print(offers)
        res = jsonify({'Message': 'Get All Offers Succeeded!!', 'data': offers})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Get All Offers Failed!!'})
        res.status_code = 404
    return res



@admin_bp.route('/blockchain/transaction_history', methods=['POST'])
def transaction_history():
    history = []
    try:

        event_filter_offer = web3.eth.filter({
            "fromBlock": "earliest",
            "toBlock": "latest", 
            "address": OfferContract.address})
        event_filter_product = web3.eth.filter({
            "fromBlock": "earliest",
            "toBlock": "latest", 
            "address": ProductContract.address})

        event_filter_actor = web3.eth.filter({
            "fromBlock": "earliest",
            "toBlock": "latest", 
            "address": AccessControlContract.address})

        for log in event_filter_product.get_all_entries():
            txh = log.get("transactionHash")
            transaction = web3.eth.get_transaction(txh)
            tuple_data = ProductContract.decode_function_input(transaction.input)
            function_name = str(tuple_data[0]).split('Function')[-1].strip().split('(')[0].strip()
            arguments = tuple_data[1]
            serialized_data = {'function': function_name, 'args': arguments }
            history.append(serialized_data)

        for log in event_filter_offer.get_all_entries():

            txh = log.get("transactionHash")
            transaction = web3.eth.get_transaction(txh)
            tuple_data = OfferContract.decode_function_input(transaction.input)
            function_name = str(tuple_data[0]).split('Function')[-1].strip().split('(')[0].strip()
            arguments = tuple_data[1]
            serialized_data = {'function': function_name, 'args': arguments }
            history.append(serialized_data)

        for log in event_filter_actor.get_all_entries():
            txh = log.get("transactionHash")
            transaction = web3.eth.get_transaction(txh)
            tuple_data = AccessControlContract.decode_function_input(transaction.input)
            function_name = str(tuple_data[0]).split('Function')[-1].strip().split('(')[0].strip()
            arguments = tuple_data[1]
            serialized_data = {'function': function_name, 'args': arguments }
            history.append(serialized_data)

    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if len(history) > -1 :
        res = jsonify({'Message': 'Get Transactions History Succeeded!!', 'data': history})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Get Transactions History Failed!!'})
        res.status_code = 404
    return res


@user_bp.route('/blockchain/account_transaction_history', methods=['GET'])
def account_transaction_history():
    auth_header = request.headers.get('Authorization')
    if not auth_header:
        res = jsonify({"Error" : " Authorization Header Missing"})
        res.status_code = 401
        abort(res)
    jwt_token = auth_header.split(' ')[1]
    decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
    pub_key = decoded_token['public_key']

    history = []
    try:

        event_filter_offer = web3.eth.filter({
            "fromBlock": "earliest",
            "toBlock": "latest", 
            "address": OfferContract.address})
        event_filter_product = web3.eth.filter({
            "fromBlock": "earliest",
            "toBlock": "latest", 
            "address": ProductContract.address})

        event_filter_actor = web3.eth.filter({
            "fromBlock": "earliest",
            "toBlock": "latest", 
            "address": AccessControlContract.address})

        for log in event_filter_product.get_all_entries():
            txh = log.get("transactionHash")
            transaction = web3.eth.get_transaction(txh)
            
            if transaction['from'] == pub_key:
                block = web3.eth.get_block(transaction['blockNumber'])
                timestamp = block['timestamp']
                tuple_data = ProductContract.decode_function_input(transaction.input)
                function_name = str(tuple_data[0]).split('Function')[-1].strip().split('(')[0].strip()
                arguments = tuple_data[1]
                mapped_data = mappingTX(tuple_data)
                mapped_data['timestamp'] = timestamp
                print(mapped_data)


                #serialized_data = {'function': function_name, 'args': arguments, "timestamp": timestamp}
                
                
                
                history.append(mapped_data)

        for log in event_filter_offer.get_all_entries():

            txh = log.get("transactionHash")
            transaction = web3.eth.get_transaction(txh)
            if transaction['from'] == pub_key:
                tuple_data = OfferContract.decode_function_input(transaction.input)
                function_name = str(tuple_data[0]).split('Function')[-1].strip().split('(')[0].strip()
                arguments = tuple_data[1]
                serialized_data = {'function': function_name, 'args': arguments }
                history.append(serialized_data)

        for log in event_filter_actor.get_all_entries():
            txh = log.get("transactionHash")
            transaction = web3.eth.get_transaction(txh)
            if transaction['from'] == pub_key:
                tuple_data = AccessControlContract.decode_function_input(transaction.input)
                function_name = str(tuple_data[0]).split('Function')[-1].strip().split('(')[0].strip()
                arguments = tuple_data[1]
                serialized_data = {'function': function_name, 'args': arguments }
                history.append(serialized_data)

    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    print(history)
    if len(history) >-1 :
        res = jsonify({'Message': 'Get Account Transactions History Succeeded!!', 'data': history})
        res.status_code = 200
    else:
        res = jsonify({'Error': 'Get Account Transactions History Failed!!'})
        res.status_code = 404
    return res



@user_bp.route('/historique_achats', methods=['GET'])
def get_achat():

    auth_header = request.headers.get('Authorization')
    if auth_header :
        jwt_token = auth_header.split(' ')[1]
        decoded_token = jwt.decode(jwt_token, SECRET_KEY, algorithms=['HS256'])
        achats = Achat.get_all_achats(decoded_token['user_id'])

        if achats :
            res = jsonify({"Message" : 'Get request succeeded' ,'data': achats})
            res.status_code = 200
        else:
            res = jsonify({'Error': 'Unable to get Historique Achats'})
            res.status_code = 404
        return res
