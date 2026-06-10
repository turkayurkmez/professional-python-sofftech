#Aşağıdaki kod, tüm listeyi bellekte tutuyor:
import sys


total_in_list = sum([x for x in range(1_000_000)])
print(total_in_list)
#Generator ile sadece bir sonrakini bellekte tutar ve talep anında üretir.
gen_total= sum((x for x in range(1_000_000)))
print(gen_total)

liste=[x for x in range(1_000_000)]
gen = (x for x in range(1_000_000))
print("Liste bellekte:",sys.getsizeof(liste)," byte")
print("generator bellekte:",sys.getsizeof(gen)," byte")

def get_errors_in_log(log_content):
    """Büyük bir log koleksiyonu içinden sadece ERROR satırlanı üretir"""
    for row in log_content:
        if "ERROR" in row:
            yield row.strip()

loglar = [
    "2026-06-10 INFO Uygulama basladi",
    "2026-06-10 ERROR db bağlantısı kesildi",
    "2026-06-10 INFO İstek alındı",
    "2026-06-10 ERROR enpoint TimeOut hatası verdi"
]

for err in get_errors_in_log(loglar):
    print("Hata: ",err)