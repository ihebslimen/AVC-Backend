from web3models.Farmer import Farmer
from web3models.AccessControl import AccessControl  
from web3models.Product import Product ,ProductContract




A = AccessControl( "0x3601CC532A0Eda5AE73968f7309d3faB86dCDbD2",  "0x142d68b9650d0a43c4a2d4388c0df087b0112a692d65ee9e40f040d8493d2623")
P = Product("0xF5D67A0179BA2EF800B23383e1a71429E8e7FBa4",  "0x35264236e3fc2e3efdb75b6858417ef908e892d4fe2e54be7fe4c201e8dfdd61")
P1  = Product('0x9D14f2d9b3afAC6Dd20d1d70c27890B6BB27d778', '0x58180787bede620fe369c788a187e9c74ca60ce56a2a317221a4f5e3b922eb52') 
""" result = A.hasUserType("0x3601CC532A0Eda5AE73968f7309d3faB86dCDbD2",0)
print('###### has user type',result)

result = A.setUserType("0xF5D67A0179BA2EF800B23383e1a71429E8e7FBa4",1)
print('###### set user type',result)
result = A.setUserType("0x9D14f2d9b3afAC6Dd20d1d70c27890B6BB27d778",1)
print('###### set user type',result)







 """


result = P.createProduct(3, 1, 1)
print('###### create product',result)

result = ProductContract.functions.isProductOwner(P.pub_key, 3).call()
print('###### is Product Owner',result)


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