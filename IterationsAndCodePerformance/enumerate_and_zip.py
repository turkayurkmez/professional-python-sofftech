products = ["A","B","C","D"]
print(products[0])

#Yöntem 1: index yönetimi manüel. 
index = 0

for p in products:
    print(index,p)
    index += 1

# Yöntem 2: Daha dinamik. len hesapla range ile hesaplanan değere kadar index üret
for i in range(len(products)):
    print(i, products[i])
# Yöntem 3: enumerate ile item'ları "numaralandırın"
for inx, p in enumerate(products):
    print(inx,p)

students = ["Merih","Dilan Ezgi","Türkay"]
scores = [85,92,78]

print(dict(zip(students,scores)))

for order, (ogrenci, not_) in enumerate(zip(students,scores),start=1):
    print(order,ogrenci,not_)


inventory = [
    {"name":"Laptop", "category":"elektronik", "price":70000},
    {"name":"Masa", "category":"mobilya", "price":7500},
    {"name":"Bateri", "category":"elektronik", "price":5000},
    {"name":"Kitaplık", "category":"mobilya", "price":3000},
    {"name":"Sandalye", "category":"mobilya", "price":13000}
]

#1. yalnızca elektronik kategorisindeki ürünleri getir (comprehension kullan)
electronics = [ product for product in inventory if product["category"]=="elektronik"]
#2. Fiyatı 5000 ya da fazla olanları %10 azaltarak dictionary'ye dönüştür.
most_expensive = {p["name"]: round(p["price"] * 0.9,2) for p in electronics if p["price"]>=5000}


#most_expensive = {p["name"]: round(p["price"] * 0.9,2)} for p in electronics if p["price"]>=5000}
print("----------------------------------------------")

def price_tag(prices:dict):
    for name,price  in prices.items():
        if price > 10000:
            tag = "Premium"
        elif price >= 5000:
            tag = "Medium"
        else:
            tag = "Economic"
        yield name,price,tag

for order,(name,price,tag) in enumerate(price_tag(most_expensive),start=1):
    print(f"{order}. {name:<12} | {price:> 10.2f} TL | {tag}")


