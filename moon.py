import requests
from datetime import datetime, timedelta
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
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

# Her kullanıcının son anahtar alma zamanını saklamak için sözlük
last_key_time = {}

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE BAN YERSİNİZ VE İSTEMEDİĞİM KİŞİLERİ BANLARI\nKEY ALMAK İÇİN /key YAZMANIZ YETERLİ KÜFÜR YAZAN BAN YER",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url=f'https://t.me/rawzhack')
            ]] 
        )
    )

# Key KOMUTU
@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    php_url = 'http://sakultah.fun/hbXAii2byXnvgAEF4M9tG33u/Sjajajajajaj.php'  # Gerçek PHP dosya URL'nizi buraya ekleyin
    user_id = message.from_user.id

    # Kullanıcının son anahtar alma zamanı mevcut mu diye kontrol edin
    if user_id in last_key_time:
        last_retrieval_time = last_key_time[user_id]
        time_since_last_retrieval = datetime.now() - last_retrieval_time

        # Son alma zamanından bu yana 6 saatten az bir süre geçtiyse, kullanıcıyı bilgilendirin
        if time_since_last_retrieval < timedelta(hours=24):
            bot.send_message(
                chat_id=message.chat.id,
                text="GÜNDE 1 KERE KEY ALABİLİRSİNİZ STOK YAPAMAZSINIZ❗"
            )
            return

    # Anahtarı alın ve gönderin
    key_content = get_key_from_php(php_url)

    # Gönderilen mesajı DM olarak size gönderin
    sender_name = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    dm_text = f"Mesaj Gönderen: {sender_name}\nMesaj: {message.text}"
    bot.send_message(
        chat_id=6698881784,  # Gerçek Telegram DM sohbet kimliğinizi buraya ekleyin
        text=dm_text
    )

    # Kullanıcının son anahtar alma zamanını güncelleyin
    last_key_time[user_id] = datetime.now()

# ... (Kodun geri kalanı)

bot.run()
        
