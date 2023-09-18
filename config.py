import os

class Config:
    API_ID = int(os.environ.get("API_ID", "25114508"))
    API_HASH = os.environ.get("API_HASH", "993ccdfe81548dade420e81bcd6807ce")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    BOT_OWNER = os.environ.get("BOT_OWNER", "")
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    BOT_CHANNEL = oe.environ.get("BOT_CHANNEL", "")
    
