import logging
class logGenerator:

   
    def __init__(self):
        #1. adım: Logging'i yapılandır.
        logging.basicConfig(level=logging.DEBUG, 
                            format="%(asctime)s | %(levelname)s | %(message)s",
                            handlers=[
                            logging.StreamHandler(), # console'a yaz
                            logging.FileHandler("app.log") #dosyaya da yaz
                            ])   
        self.logger = logging.getLogger(__name__)

    

    def get_logger(self):
       return self.logger 
        


   