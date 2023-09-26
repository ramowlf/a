import os

class Config:
    API_ID = int(os.environ.get("API_ID", "25114508")) #Karışmayın
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce") #Karışmayın
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") #Botunuzun Tokenini Girin .
    BOT_OWNER = os.environ.get("BOT_OWNER", "") #Bot Sahibi Kullanıcı Adı Girin .
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "") #Bot Kullanıcı Adı Girin .
    BOT_CHANNEL = os.environ.get("BOT_CHANNEL", "") #Kanal Kullanıcı Adı Girin .
    
