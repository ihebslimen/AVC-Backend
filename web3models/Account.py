from web3 import Web3, WebsocketProvider
from flask import Flask, jsonify, request

from config_web3 import web3
from config_web3 import contracts
import os


contract_address_access = contracts["AccessControl"]["address"]
contract_abi_access = contracts["AccessControl"]["abi"]
AccessControlContract =web3.eth.contract(address=contract_address_access, abi=contract_abi_access)
contract_address_product = contracts["Product"]["address"]
contract_abi_product = contracts["Product"]["abi"]
ProductContract =web3.eth.contract(address=contract_address_product, abi=contract_abi_product)

contract_address_offer = contracts["Offer"]["address"]
contract_abi_offer = contracts["Offer"]["abi"]
OfferContract =web3.eth.contract(address=contract_address_offer, abi=contract_abi_offer)

class Account:
    def __init__(self, pub_key , priv_key) -> None:
        self.pub_key = pub_key
        self.priv_key = priv_key
   
    def hasUserType(self, _addr,type_ref) -> None:
        functionCall = AccessControlContract.functions.hasUserType(
             _addr, type_ref
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")


    def setUserType(self, _addr,_type_ref) -> None:
        functionCall = AccessControlContract.functions.setUserType(
             _addr,_type_ref
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")
        
    def delUserType(self, _addr,_type_ref) -> None:
        functionCall = AccessControlContract.functions.delUserType(
             _addr,_type_ref
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return(True)
        else:
            return(False)




    def createProduct(self, _prod_id,_prod_qty,_prod_qlt ) -> None:
        functionCall = ProductContract.functions.createProduct(
              _prod_id,_prod_qty,_prod_qlt 
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")

    def updateProduct(self, _prod_id,_prod_qty,_prod_qlt ) -> None:
        functionCall = ProductContract.functions.updateProduct(
              _prod_id,_prod_qty,_prod_qlt 
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")

    def deleteProduct(self, _prod_id) -> None:
        functionCall = ProductContract.functions.deleteProduct(
              _prod_id
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")

    def isProductOwner(self, _addr, _prod_id) -> None:
        functionCall = ProductContract.functions.isProductOwner(
              _addr, _prod_id
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")

    

    def getProductsByAddress(self, _addr) -> None:
        functionCall = ProductContract.functions.getProductsByAddress(
              _addr
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")


    def createOffer(self, _offer_id, _prod_id, _prod_qty, _price) -> None:
        functionCall = OfferContract.functions.createOffer(
              _offer_id, _prod_id, _prod_qty, _price
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")

    def isOfferOwner(self, _addr,  _offer_id) -> None:
        functionCall = OfferContract.functions.isOfferOwner(
              _addr,  _offer_id
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")



    def buyOffer(self, _offer_id) -> None:
        functionCall = OfferContract.functions.buyOffer(
              _offer_id
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id,
                'value' : 10**18
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")

    def getOfferByOwner(self, _addr) -> None:
        functionCall = OfferContract.functions.getOfferByOwner(
              _addr
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")

    def listAllOffers() -> None:
        functionCall = OfferContract.functions.listAllOffers(
        
        ).build_transaction(
            {   
                'from' : self.pub_key,
                'gasPrice': web3.eth.gas_price,
                'nonce': web3.eth.get_transaction_count(self.pub_key),
                "chainId" : web3.eth.chain_id
            }
        )
        signed_tx = web3.eth.account.sign_transaction(functionCall, private_key=self.priv_key)
        send_tx = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        tx_receipt = web3.eth.wait_for_transaction_receipt(send_tx)
        #print(tx_receipt)
        if tx_receipt['status'] == 1:
            return("transaction successful")
        else:
            return("transaction failed")