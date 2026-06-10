def division(number1_str,number2_str):
    try:
        number1 = int(number1_str)
        number2 = int(number2_str)
        result = number1 // number2
       
    except ValueError:
        print("Değerler int tipinde olmalı")
    except ZeroDivisionError:
        print("Tam sayılar, 0'a bölünemez!!")
    except Exception:
        print("Tespit edilemeyen bir hata oluştu")
    else:
        print("hiç hata olmadı. Sonuç döndürülüyor.")
        return result
    finally:
        print("hata olsa da olmasa da çalışır!!!")









number1 = input("Lütfen bir sayı girin:")
number2 = input("Bir sayı daha girin:")
result = division(number1,number2)

print(result)
