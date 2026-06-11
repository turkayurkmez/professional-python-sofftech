from custom_exception import NegativeAmountException

import inventory
 
test = inventory.Inventory() 
try:
    stock = test.update_stock(5)
except NegativeAmountException as na:
    print(na.amount," değeri negatif olduğundan hata oluşuyor.")
else:
    print(stock)

