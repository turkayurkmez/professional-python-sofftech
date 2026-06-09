a = [1,2,3]
print(id(a))
b = a
print(id(b))
print(a is b)

x = 100
print('Öncesi',id(x))
x = x + 1
print('Sonrası',id(x))

s = "merhaba"
print(f"{s} -> {id(s)}")
s = s + " dünya"
print(f"{s} -> {id(s)}")

lst = [1,2,3]
print(f"{lst} -> {id(lst)}")
lst.append(5)
print(f"{lst} -> {id(lst)}")

#Mutable argüman riski
def add_item(collection:list, item:int):
    collection.append(item)
    return collection

numbers = [10,20,30]
new_list = add_item(numbers,80)
print("numbers değeri:",numbers)
print("new_list değeri:",new_list)

def add_item_safe(collection:list, item:int):
    new_collection = collection.copy()
    new_collection.append(item)
    return new_collection


numbers2 = [10,20,30]
new_list2 = add_item_safe(numbers2,80)
print("numbers2 değeri:",numbers2)
print("new_list2 değeri:",new_list2)