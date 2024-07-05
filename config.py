import os

class Config:
    TELEGRAM_API_ID = int(os.environ.get("TELEGRAM_API_ID", "16088758")) #Karışmayın
    TELEGRAM_API_HASH = os.environ.get("TELEGRAM_API_HASH", "7c959970fc76db9846339b79b7bd8aae") #Karışmayın
    TELEGRAM_PHONE_NUMBER = os.environ.get("TELEGRAM_PHONE_NUMBER", "6958129929") #Botunuzun Tokenini Girin .  

