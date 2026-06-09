import copy


profile_template = {
    "name":"Varsayılan kullanıcı",
    "roles":["viewer"],
    "settings":{
        "theme":"light",
        "language":"tr"
    }
}

user_a = profile_template.copy() #shallow copy: nesnelerin tüm iç adreslerini kopyalar. Örneğin settings'in aynı referanslarını kullanır  
user_a["name"] ="Gizem"
user_a["roles"].append("editor")#bu nedenle burada değişiklik yaparsanız
print("kullanıcının rolleri:", user_a["roles"])
print("varsayılan roller:", profile_template["roles"]) #burası da etkilenir.

user_b =  copy.deepcopy(profile_template) #deepcopy ise sıfırdan yeni adresler oluşturarak kopyalarsınız. 
profile_template["roles"]=["viewer"]
user_b["name"] = "Alper"
user_b["roles"].append("admin") 
user_b["settings"]["theme"] = "dark" # bu nedenle bu değişiklik, orijinal nesneyi etkilemez!!!!

print("varsayılan roller:", profile_template["roles"])
print("user_b rolleri:",user_b["roles"])
print("varsayılan roller:", profile_template["roles"])
print("varsayılan tema:",profile_template["settings"]["theme"])
print("user-b tema:",user_b["settings"]["theme"])


