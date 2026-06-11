from log_generator import logGenerator

class InvalidAgeException(Exception):
    def __init__(self, age):
        super().__init__(f"Geçersiz yaş değeri: {age}")
        self.age = age
    

def is_valid_age(age):
    assert isinstance(age, int), "Yaş, tam sayı olmalı"
    assert age > 0, "Yaş negatif olamaz!" 
    if age>120:
        raise InvalidAgeException(age)
    return age

def create_user(name, age_str):
    generator = logGenerator()
    logger = generator.get_logger()
    logger.info(f"create_user fonksiyonu, name={name} ve age={age_str} argümanlarıyla başladı")
    try:
        age = int(age_str)
        is_valid_age(age)
    except ValueError:
        logger.error(f"Yaş int'e dönüştürülemedi. Girilen değer: {age_str} ")
        return False
    except InvalidAgeException as ex:
        logger.error(f"yaş doğrulanmadı. Sebebi:{ex}")
        return False
    except AssertionError as aex:
        logger.error(f"yaş doğrulanmadı. Sebebi:{aex}")
        return False
    else:
        logger.info("Kullanıcı başarıyla oluşturuldu")
        return True
    finally:
        logger.debug("create_user fonksiyonu tamamlandı!")
    

create_user("Türkay","46")
create_user("Derya","abc")
create_user("İlknur",-8)










