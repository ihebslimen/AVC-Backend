
from web3 import Web3
import sys
import os


class Wallet:

    def __init__(self):
        return
    def signTx(self, tx):
        privateKey = self.getPrivateKey()
        signed_tx = web3.eth.account.sign_transaction(tx, privateKey)
        return signed_tx
    
    def getPrivateKey(self):
        with open('private_key.txt', 'wb') as f:
            privateKey = f.read()
        
        return privateKey



""" 
def GetPrivateKey():
    return

def signTranx():
    return


transaction = ''
signedTransaction = ''

return signedTransaction """