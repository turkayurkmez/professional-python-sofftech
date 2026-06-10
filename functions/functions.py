def create_order(customer_name:str, *products):
    print(customer_name, " müşterisinin siparişeri")
    print("Toplam ürün:",len(products)) 
    for product in products:
        print(product)


create_order("Ahmet","Klavye","Mouse")
create_order("Ayşe","Panko","Lahana Bebek","Tamogachi")
create_order("Mehmet")

def advanced_create_order(customer_name:str, *products, **settings):
    print(customer_name, " müşterisinin siparişeri")
    print("Ürünler:", ', '.join(products))
    if settings:
        print("Müşteri Tercihleri")
        for key,value in settings.items():
            print(key,value)

advanced_create_order("Yasemin",
                      "Lego","Puzzle",
                      teslimat="hızlı", 
                      not_ ="Kapıya bırakabilirsiniz",
                      adres="Odunpazarı, Eskişehir")
