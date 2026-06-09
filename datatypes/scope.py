
#LEGB Kuralı
# Local: Şu an içinde bulunduğun fonksiyonun kapsamı.
# Enclosing: Eğer iç içe fonksiyon varsa, bir üst (dış) fonksiyonun kapsamı.
# Global: Modül düzeyindeki değişkenler. 
# Built-int: Python'un hazır isimleri: len, print

def hesapla():
    sonuc = 42
    print("fonksiyon içinde sonuc değeri",sonuc)

hesapla()

#print(sonuc)
sayac = 0

def goster():
    print(sayac)

def arttir():
   global sayac
   sayac+= 1

arttir()
goster()
arttir()
goster()

def sayac_olustur():
    deger = 0

    def arttir():
        nonlocal deger #nonlocal keyword'u bu fonksiyona en yakın dış fonksiyonun
                       #local değişkenini yakalar.   
        deger += 1
        return deger
    
    def goster():
        print("Şu anki değer:",deger)

    return arttir, goster

fn_arttir, fn_goster = sayac_olustur()
fn_arttir()
fn_arttir()
fn_arttir()
fn_goster()

x = "global"
#x = 9


def dis():
    #x = "enclosing"

    def ic():
        #x = "local"
        print(x)
    
    ic()

dis()
