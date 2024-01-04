from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config  # Konfigürasyon dosyanızın gerçek konumunu ekleyin
import requests

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# Dictionary to store the last key retrieval time for each user
last_key_time = {}

# Bir web sitesindeki bir PHP dosyasından içerik almak için işlev
def get_key_from_php(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Kötü yanıtlar için HTTPError oluştur
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Lütfen Bekleyiniz 1 dk Sonra Tekrar Yazın"

# Log dosyasına yazan işlev
def write_to_log(log_message):
    admin_user_id = 6698881784  # Yönetici kullanıcının ID'sini buraya ekleyin
    
    # Log mesajını yaz
    with open("message_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_message + "\n")

    # Yöneticiye DM olarak mesajı gönder
    try:
        bot.send_message(
            chat_id=admin_user_id,
            text=log_message
        )
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Mesajları detaylı log olarak atan filtre
@bot.on_message(filters.private & ~filters.me)
def log_messages(client, message):
    user_id = message.from_user.id
    user_name = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    user_username = message.from_user.username if message.from_user.username else "N/A"
    user_chat_id = message.chat.id
    message_text = message.text if message.text else "N/A"

    log_message = (
        f"Tarih: {datetime.now()}\n"
        f"Kullanıcı ID: {user_id}\n"
        f"Kullanıcı Adı: {user_name}\n"
        f"Kullanıcı Adı (@): {user_username}\n"
        f"Chat ID: {user_chat_id}\n"
        f"Mesaj: {message_text}\n"
    )

    # Log mesajını yaz ve DM olarak gönder
    write_to_log(log_message)

# START KOMUTU
@bot.on_message(filters.command("start") & filters.private)
def start_command(client, message):
    keyboard = [
        [InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url='https://t.me/rawzhack')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    bot.send_message(
        chat_id=message.chat.id,
        text="AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE BAN YERSİNİZ VE İSTEMEDİĞİM KİŞİLERİ BANLARI\nKEY ALMAK İÇİN /key YAZMANIZ YETERLİ KÜFÜR YAZAN BAN YER",
        reply_markup=reply_markup
    )

# KEY KOMUTU
@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    php_url = 'http://sakultah.fun/hbXAii2byXnvgAEF4M9tG33u/Sjajajajajaj.php'  # Gerçek PHP dosya URL'nizi buraya ekleyin
    user_id = message.from_user.id

    # Check if user's last key retrieval time is available
    if user_id in last_key_time:
        last_retrieval_time = last_key_time[user_id]
        time_since_last_retrieval = datetime.now() - last_retrieval_time

        # If less than 24 hours have passed since the last retrieval, notify the user
        if time_since_last_retrieval < timedelta(hours=24):
            bot.send_message(
                chat_id=message.chat.id,
                text="GÜNDE 1 KERE KEY ALABİLİRSİNİZ STOK YAPAMAZSINIZ❗"
            )
            return

    # Retrieve and send the key
    key_content = get_key_from_php(php_url)
    bot.send_message(
        chat_id=message.chat.id,
        text=key_content
    )

    # Update user's last key retrieval time
    last_key_time[user_id] = datetime.now()

    # Anahtarın logunu oluştur
    user_name = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    key_log_message = f"Anahtar alındı - Kullanıcı: {user_name} - Tarih: {datetime.now()}"
    write_to_log(key_log_message)

bot.run()
