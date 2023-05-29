from config_web3 import web3
from config_web3 import contracts


def get_accounts_with_private_keys():
    try:
        accounts = web3.eth.accounts
        for account in accounts:
            private_key = web3.eth.account.privateKeyToHex(web3.eth.account.decrypt(account, 'your_password'))
            print(f"Account: {account}")
            print(f"Private Key: {private_key}\n")
    except Exception as e:
        print(e)

get_accounts_with_private_keys()