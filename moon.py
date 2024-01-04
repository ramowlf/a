import requests
from datetime import datetime, timedelta
from pyrogram import Client, filters
from config import Config  # Konfigürasyon dosyanızın gerçek konumunu ekleyin

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# Bir web sitesindeki bir PHP dosyasından içerik almak için işlev
def get_key_from_php(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kötü yanıtlar için HTTPError oluştur
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Lütfen Bekleyiniz 1 dk Sonra Tekrar Yazın"

# Bota yazılan her mesajı belirli bir kullanıcıya DM olarak gönderen filtre
@bot.on_message(filters.private & ~filters.me)
def send_messages_to_user(client, message):
    user_id = 6698881784  # Hedef kullanıcının ID'sini buraya ekleyin
    user_message = f"Yeni Mesaj: {message.text}"
    
    try:
        bot.send_message(
            chat_id=user_id,
            text=user_message
        )
    except Exception as e:
        print(f"Hata oluştu: {e}")

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE BAN YERSİNİZ VE İSTEMEDİĞİM KİŞİLERİ BANLARI\nKEY ALMAK İÇİN /key YAZMANIZ YETERLİ KÜFÜR YAZAN BAN YER"
    )

# KEY KOMUTU
@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    php_url = 'http://sakultah.fun/hbXAii2byXnvgAEF4M9tG33u/Sjajajajajaj.php'  # Gerçek PHP dosya URL'nizi buraya ekleyin

    # Anahtarı alın ve gönderin
    key_content = get_key_from_php(php_url)
    bot.send_message(
        chat_id=message.chat.id,
        text=key_content
    )

bot.run()
