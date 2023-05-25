from web3models.Farmer import Farmer
from web3models.AccessControl import AccessControl  
from web3models.Product import Product ,ProductContract




A = AccessControl( "0xbBAF1Cf5aDec4670581B966dCaBaD1D925B3799b",  "0x1a6290b51064f75658a14d4c40304ebd29a6328a980c4c454dfca2d15a0f6e68")
P = Product("0x64a2566d47D0061AfE6C4ea18337570A9F7a1398",  "0xbe4e4789615dc1863056e869f902f0172e359258176ae5da72784ad3367819f6")

""" result = A.delUserType("0x64a2566d47D0061AfE6C4ea18337570A9F7a1398",1)
print('###### delete user type',result)

result = A.hasUserType("0xbBAF1Cf5aDec4670581B966dCaBaD1D925B3799b",1)
print('###### has user type',result)

result = A.setUserType("0x64a2566d47D0061AfE6C4ea18337570A9F7a1398",1)
print('###### set user type',result)

result = P.createProduct(1, 1, 1)
print('###### create product',result) """

result = ProductContract.functions.isProductOwner('0x625FDc8e408128dd3A404A388f76050Bb749B4D7', 1).call()
print('###### is Product Owner',result)
result = ProductContract.functions.updateProductQuantity(1, 2).call()
print('###### update Product Quantity',result)




"""





result = P.updateProduct(1, 3, 3)
print('###### update Product',result)


result = P.isProductOwner('0xdED0460c27694BBDACDc4a9aF89b3Ef0FE4cDe27', 1)
print('###### is Product Owner',result)


result = P.transferProduct('0xdED0460c27694BBDACDc4a9aF89b3Ef0FE4cDe27', 1,1)
print('###### transfer Product',result)

result = P.createOffer(1, 1, 1, 1)
print('###### create offer',result)

result = P.isOfferOwner("0xbBAF1Cf5aDec4670581B966dCaBaD1D925B3799b", 1)
print('###### is Offer Owner',result)



result = P.deleteProduct(1)
print('###### create product',result)

result = A.delUserType("0x64a2566d47D0061AfE6C4ea18337570A9F7a1398",1)
print('###### delete user type',result)
 """