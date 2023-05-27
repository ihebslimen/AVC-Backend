from web3models.Account import *


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
    # Access the relevant information from the log
    print(log)
    txh = log.get("transactionHash")
    transaction = web3.eth.get_transaction(txh)
    print(ProductContract.decode_function_input(transaction.input))

for log in event_filter_offer.get_all_entries():
    # Access the relevant information from the log
    print(log)
    txh = log.get("transactionHash")
    transaction = web3.eth.get_transaction(txh)
    print(OfferContract.decode_function_input(transaction.input))
for log in event_filter_actor.get_all_entries():
    
    # Access the relevant information from the log
    print(log)
    txh = log.get("transactionHash")
    transaction = web3.eth.get_transaction(txh)
    print(AccessControlContract.decode_function_input(transaction.input))



""" 
A = Account( "0x5D2D4A1e21BBAa13D253Ee131C93De2E617D5461",  "0x05ec8f1e5e541c6bf36113a7673fa39263951c5352e77f2773a38c92bc673462")
P = Account("0x15220960a8844306d54D149de4e775F82d1f2B19",  "0x813ac0a9db697bb7846de1c4f6ddbe8385d7341d40d24e8a1df31d599fdabb97")
P1 = Account('0x421472051071af95d1425E290D814dFd55d81b14', '0x3d9aa950abab7b58435322af7788962cee9fcccf6fa7eaadff1125e0d326d981') 


result = AccessControlContract.functions.hasUserType(A.pub_key,1).call()
print('###### has user type',result)
 """
""" result = P.createProduct(2, 2, 1)
print('###### create product',result) 

result = P.createOffer(2, 1, 1, 1)
print('###### create offer',result) 

result = P1.buyOffer(2)
print('###### buy offer',result)

result = OfferContract.functions.getOfferByOwner(P.pub_key).call()
print('###### get Offer By Owner ',result)

 """
""" event_filter = web3.eth.filter({"fromBlock": "earliest",
    "toBlock": "latest", "address": OfferContract.address})

event_filter1 = web3.eth.filter({"fromBlock": "earliest",
    "toBlock": "latest", "address": ProductContract.address})

for log in event_filter.get_all_entries():
    # Access the relevant information from the log
    txh = log.get("transactionHash")
    transaction = web3.eth.get_transaction(txh)
    print(OfferContract.decode_function_input(transaction.input))

for log in event_filter1.get_all_entries():
    # Access the relevant information from the log
    txh = log.get("transactionHash")
    transaction = web3.eth.get_transaction(txh)
    print(ProductContract.decode_function_input(transaction.input))

 """
#result = A.setUserType("0xCB69CAE44C467DB8f8e859890789E9a846e0BDBC",1)
""" result = AccessControlContract.functions.hasUserType("0xCB69CAE44C467DB8f8e859890789E9a846e0BDBC",1).call()
print('###### has user type',result) """
""" 


result = A.setUserType("0x9D14f2d9b3afAC6Dd20d1d70c27890B6BB27d778",1)
print('###### set user type',result)


 """

""" 
result = P.createProduct(P.pub_key,3, 1, 1)
print('###### create product',result) 
result = ProductContract.functions.isProductOwner(P.pub_key, 3).call()
print('###### is Product Owner',result)
 """

""" 



 """

""" 

result = P.deleteProduct(1)
print('###### create product',result)

result = P.updateProduct(1, 3, 3)
print('###### update Product',result)




result = P.isProductOwner('0xF5D67A0179BA2EF800B23383e1a71429E8e7FBa4', 1)
print('###### is Product Owner',result)


result = P.transferProduct('0x9D14f2d9b3afAC6Dd20d1d70c27890B6BB27d778', 1,1)
print('###### transfer Product',result)

result = P.createOffer(1, 1, 1, 1)
print('###### create offer',result)

result = P.isOfferOwner("0xF5D67A0179BA2EF800B23383e1a71429E8e7FBa4", 1)
print('###### is Offer Owner',result)





result = A.delUserType("0xF5D67A0179BA2EF800B23383e1a71429E8e7FBa4",1)
print('###### delete user type',result) """