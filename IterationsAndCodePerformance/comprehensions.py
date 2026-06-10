#Amaç: 1-10'a kadar olan sayıların karelerini tutan bir liste oluşturmak:
squares = []
for x in range(10):
    squares.append(x ** 2)

print(squares)

squares_comp =  [x ** 2 for x in range(10)]
print(squares_comp)

squares_comp_even =  [x ** 2 for x in range(10) if x % 2 == 0]
print(squares_comp_even)

product_prices = {"elma":80, "armut":120, "muz":119}
#tek satırda, kdv'yi dahil ettiğiniz yeni bir dict üretiyorsunuz:
extra_kdv_prices = { product: price * 1.20 for product,price in product_prices.items() }
print(product_prices)
print(extra_kdv_prices)
for k,v in extra_kdv_prices.items():
    print(k,v)

unique_length = { len(word)  for word in ["python","go","spinoza","determinizm","probabilistik","c","C#","java"]}
print(unique_length)
    
upper_words = [ word.upper() for word in ["elma","armut","kavun","karpuz"]]
print(upper_words)

