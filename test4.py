from web3models.Farmer import Farmer
from web3models.AccessControl import AccessControl ,AccessControlContract 
from web3models.Product import Product ,ProductContract
from web3models.Offer import Offer ,OfferContract





A = AccessControl( "0x3114361C91A0647c0DbF9202c03197cdFf6c5152",  "0xb279d7e16d94de21c9a05434b8404c5482a6c5f75a3d91bef9a44c4800c596bb")
P = Product("0x52F7edC583AB01C1c8926fDd6B6533CC8a402D31",  "0xa3751db70dfe6eda5a4314d1f7b5c88fe489dc55150f95ced20f53f1a283df64")
P1  = Product('0x3617776C8EAC094584b41590497085f497Ba9579', '0x90d778d32c2db802f7434951528f3b195f234e9be360fed9043a9992d1dac082') 

""" result = P.createProduct(1, 2, 1)
print('###### create product',result) 
 """
""" result = P.createOffer(2, 1, 1, 1)
print('###### buy offer',result)  """

result = P1.buyOffer(2)
print('###### buy offer',result)

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