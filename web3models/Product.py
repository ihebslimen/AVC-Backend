from web3 import Web3, WebsocketProvider
from flask import Flask, jsonify, request

from config_web3 import web3
from config_web3 import contracts
import os


contract_address = contracts["Product"]["address"]
contract_abi = contracts["Product"]["abi"]
ProductContract =web3.eth.contract(address=contract_address, abi=contract_abi)

contract_address_offer = contracts["Offer"]["address"]
contract_abi_offer = contracts["Offer"]["abi"]
OfferContract =web3.eth.contract(address=contract_address_offer, abi=contract_abi_offer)



class Product:
    def __init__(self, pub_key , priv_key) -> None:
        self.pub_key = pub_key
        self.priv_key = priv_key


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


    def updateProductQuantity(self, _prod_id,_prod_qty ) -> None:
        functionCall = ProductContract.functions.updateProductQuantity(
              _prod_id,_prod_qty
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

        

    def updateProductQuality(self, _prod_id,_prod_qlt ) -> None:
        functionCall = ProductContract.functions.updateProductQuantity(
              _prod_id,_prod_qlt
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

    def transferProduct(self, _addr, _prod_id, _prod_qty) -> None:
        functionCall = ProductContract.functions.transferProduct(
              _addr, _prod_id, _prod_qty
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
        functionCall = ProductContract.functions.isOfferOwner(
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