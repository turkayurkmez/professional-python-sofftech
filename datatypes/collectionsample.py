from collections import defaultdict, namedtuple, Counter

kume1 = {1,2,3,4,5}
kume2 = {1,2,6,7,9}

print('küme1',kume1)
print('kesişim:',kume1.intersection(kume2))
print('küme1 FARK küme2:', kume1.difference(kume2))
print('birleşim:',kume1.union(kume2))

#frozenset: Donmuş - değiştirilemez küme
permitted_roles = frozenset({"admin","editor","viewer"})
user_role = "viewer"
print(user_role in permitted_roles) #True
role_permission = {
    frozenset({"admin","editor"}): "write",
    frozenset({"viewer"}):"read"
}

print(role_permission)

#defaultdict: Normalde bir dictionary içinde olmayan bir key aradığınızda "KeyError" hatası fırlar. 
# Defaultdict ise hata fırlatmak yerine varsayılan bir dictionary oluşturur.

employees = [
    ("Türkay","Engineering"),
    ("Cansu","Development"),
    ("Gizem","HR"),
    ("Oktay","Engineering")  

]

department_map = defaultdict(list)
for name,dept in employees:
    department_map[dept].append(name)

print(department_map)
print(dict(department_map))
print(department_map.get('İK'))

log_entries = [
    "ConnectionError","TimeoutError","ValueError",
    "ValueError","ConnectionError","RuntimeError",
    "ValueError","ConnectionError","TimeoutError"
]

error_counts = Counter(log_entries)
print(error_counts)
print(error_counts.most_common(1))

more_logs = Counter({"ConnectionError":2, "MemoryError":4})
combined = error_counts + more_logs
print(combined, 'toplam hata:', combined.total())

sample_tuple = (10.3, 6, 8, 12)
info = ('Duolingo',4.7,'Freemium')
print(info, type(info))

Point = namedtuple("Point",["x","y","z"])

p1 = Point(10,20,30)
print(p1.x, p1.y, p1.z)

Employee = namedtuple("Employee",["id","name","department","salary"])
emp1 = Employee(101,"Türkay","IT",100_000)
print(f"{emp1.name} isimli çalışan, {emp1.department} departmanında ve maaşı {emp1.salary} TL")