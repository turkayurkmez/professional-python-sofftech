import logging

#1. adım: Logging'i yapılandır.
logging.basicConfig(level=logging.DEBUG, 
                    format="%(asctime)s | %(levelname)s | %(message)s",
                    handlers=[
                        logging.StreamHandler(), # console'a yaz
                        logging.FileHandler("app.log") #dosyaya da yaz
                    ])   

logger = logging.getLogger(__name__)

def division(number1_str,number2_str):
    logger.info(f"division fonksiyonu çağrıldı. a={number1_str}, b={number2_str}")
    try:
        number1 = int(number1_str)
        number2 = int(number2_str)
        result = number1 // number2
       
    except ValueError:
       logger.error("Yalnızca sayı tipleri ile çalışır.")
    except ZeroDivisionError:
       logger.error("Sıfıra bölme hatası!!!")
    except Exception as ex:
        logger.error(f"Tespit edilemeyen hata: {ex}")
    else:
        print("hiç hata olmadı. Sonuç döndürülüyor.")
        return result
    finally:
        print("hata olsa da olmasa da çalışır!!!")









number1 = input("Lütfen bir sayı girin:")
number2 = input("Bir sayı daha girin:")
result = division(number1,number2)

print(result)
