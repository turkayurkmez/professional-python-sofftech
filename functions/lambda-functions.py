from typing import Callable # bunu ekledim çünkü lambda func'un parametresin, bir tipe zorlamak istiyorum:
from functools  import  reduce



def add_tax_normal(price: float):
    return price * 1.20

print(add_tax_normal(100))

add_tax = lambda price: price * 1.20
apply_discount = lambda price,rate: price * (1-rate)
shipping_feed = lambda amount: 0 if amount >=3 else 100

#Callable[[float],float] ifadesi parametre olarak ne alır ve geriye ne döner sorusuna net cevap verir. 
add_tax_alt : Callable[[float], float] = lambda price: price *1.20 

print(add_tax(150))
print(add_tax_alt(150))
print(shipping_feed(1))
print(shipping_feed(3))


product_prices = [85,1200,50,575,750]
product_with_taxes = list(map(lambda p: p*1.20, product_prices))
product_with_taxes_2 = list(map(add_tax, product_prices))

print(product_prices)
print(product_with_taxes)

expensive_products = list(filter(lambda p: p>700,product_with_taxes))
print("700 TL üzerindeki ürünler:",expensive_products)

print(product_with_taxes_2)

total_price = reduce(lambda total,price: total+price,product_with_taxes)
print("Toplam fiyat:",total_price)


## iç içe fonksiyon:
def discount_factory(rate: float):
    def apply_discount(price: float):
        return price * (1-rate)
    
    def discount_for_amount(amount: int, price:float):
        if amount > 2:
            price * (1-0.4)

       

    return apply_discount, discount_for_amount

standard_discount = discount_factory(0.05)
silver_discount = discount_factory(0.1)
gold_discount = discount_factory(0.2)

(companyDiscount, sample_discount) = discount_factory(0.20)


print(standard_discount(200))
print(silver_discount(500))
print(gold_discount(1000))
print(sample_discount(3,1000))