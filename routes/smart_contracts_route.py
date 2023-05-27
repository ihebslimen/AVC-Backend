from flask import Flask, jsonify, request
from models.transaction import Transaction
import json
import os
from blueprints.user import user_bp
from blueprints.admin import admin_bp
from web3models.Account import *

Admin = Account('0x5D2D4A1e21BBAa13D253Ee131C93De2E617D5461', '0x05ec8f1e5e541c6bf36113a7673fa39263951c5352e77f2773a38c92bc673462')
#Farmer = Account('0x15220960a8844306d54D149de4e775F82d1f2B19', '0x813ac0a9db697bb7846de1c4f6ddbe8385d7341d40d24e8a1df31d599fdabb97')
Farmer = Account('0x421472051071af95d1425E290D814dFd55d81b14', '0x3d9aa950abab7b58435322af7788962cee9fcccf6fa7eaadff1125e0d326d981')
map_actor_type = {'notype' : 0,"admin": 1, "farmer": 2, "transformer":3}

@user_bp.route('/blockchain/actor_type', methods=['POST'])
def actor_type():
    data = request.get_json()
    for i in range(0,3):
        try:
            result = AccessControlContract.functions.hasUserType(data['pub_key'],i).call()
        except Exception as e:
            error_msg = str(e).split("revert")[-1].strip()
            res= jsonify({'Error': error_msg})
            res.status_code = 404
            return res
        if result:
            if result == 0:
                actor_type = None
            elif result == 1:
                actor_type = 'Admin'
            elif result == 2:
                actor_type = 'Farmer'
            elif i == 3:
                actor_type = 'Transformer'
            break
        else :
            continue
    
    if actor_type == None:
        res = jsonify({'Error' : 'This address is not subscribed to the chain' })
        res.status_code = 404
    else:
        res = jsonify({'Message' : actor_type })
        res.status_code = 200  
    return res

@admin_bp.route('/blockchain/actor_type', methods=['POST'])
def actor_type():
    data = request.get_json()
    for i in range(0,3):
        try:
            result = AccessControlContract.functions.hasUserType(data['pub_key'],i).call()
        except Exception as e:
            error_msg = str(e).split("revert")[-1].strip()
            res= jsonify({'Error': error_msg})
            res.status_code = 404
            return res
        print(result)
        if result:
            if i == 0:
                actor_type = None
                break
            elif i == 1:
                actor_type = 'Admin'
                break
            elif i == 2:
                actor_type = 'Farmer'
                break
            elif i == 3:
                actor_type = 'Transformer'
                break
        else :
            continue
    
    if actor_type == None:
        res = jsonify({'Error' : 'This address is not subscribed to the chain' })
        res.status_code = 404
    else:
        res = jsonify({'Message' : actor_type })
        res.status_code = 200  
    return res

@admin_bp.route('/blockchain/add_farmer', methods=['POST'])
def add_farmer():
    try:
        data = request.get_json()
        result = Admin.setUserType( data['pub_key'], 2)
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
        result = Admin.setUserType( data['pub_key'], 3)
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
        result = Admin.setUserType( data['pub_key'], 1)
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
        result = Admin.setUserType( data['pub_key'], 0)
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
        result = Admin.delUserType( data['pub_key'], map_actor_type[data['actor_type']])
        print(result)
    except Exception as e:
        error_msg = str(e).split("revert")[-1].strip()
        res= jsonify({'Error': error_msg})
        res.status_code = 404
        return res
    if result:
        res = jsonify({'Message': 'Account Deleted'})
        res.status_code = 200
    elif not result:
        res = jsonify({'Error': 'Deleting Account Failed'})
        res.status_code = 404
    return res


@user_bp.route('/blockchain/create_product', methods=['POST'])
def create_product():
    data = request.get_json()
    try:
        result = Farmer.createProduct( data['product_id'],data['product_quantity'],data['product_quality'])
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




@user_bp.route('/blockchain/update_product', methods=['POST'])
def update_product():
    data = request.get_json()
    try:
        result = Farmer.updateProduct( data['product_id'],data['product_quantity'],data['product_quality'])
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

@user_bp.route('/blockchain/delete_product', methods=['POST'])
def delete_product():
    data = request.get_json()
    try:
        result = Farmer.deleteProduct( data['product_id'])
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



@user_bp.route('/blockchain/get_products', methods=['POST'])
def get_products():
    data = request.get_json()
    try:
        result_tx = Farmer.getProductsByAddress(data['pub_key'])
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
        result = Farmer.createOffer( data['offer_id'], data['product_id'],data['product_quantity'],data['price'])
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
def buy_offer():
    data = request.get_json()
    try:
        result = Farmer.buyOffer( data['offer_id'])
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
        result_tx = Farmer.getOfferByOwner(data['pub_key'])
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
