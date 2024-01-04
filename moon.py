from pyrogram import Client, filters
from datetime import datetime, timedelta
from config import Config  # Assuming this file contains your configuration
import requests

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# Yönetici kullanıcının ID'sini buraya ekleyin
admin_user_id = 6698881784

# Log dosyasına yazan işlev
def write_to_log(log_message):
    # Log mesajını yaz ve yöneticiye DM olarak gönder
    with open("message_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_message + "\n")

    try:
        bot.send_message(
            chat_id=admin_user_id,
            text=log_message
        )
    except Exception as e:
        print(f"Hata oluştu: {e}")

# Function to get content from a PHP file on a website
def get_key_from_php(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Lütfen Bekleyiniz 1 dk Sonra Tekrar Yazın"

# Dictionary to store the last key retrieval time for each user
last_key_time = {}

# Tüm mesajları yöneticiye ileten filtre
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

    # Log mesajını yaz ve yöneticiye DM olarak gönder
    write_to_log(log_message)

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
    php_url = 'http://sakultah.fun/hbXAii2byXnvgAEF4M9tG33u/Sjajajajajaj.php'  # Replace with your actual PHP file URL
    user_id = message.from_user.id

    # Check if user's last key retrieval time is available
    if user_id in last_key_time:
        last_retrieval_time = last_key_time[user_id]
        time_since_last_retrieval = datetime.now() - last_retrieval_time

        # If less than 6 hours have passed since the last retrieval, notify the user
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

    # Log the key retrieval
    user_name = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    log_message = f"Key retrieved - User: {user_name} - Date: {datetime.now()}"
    write_to_log(log_message)

bot.run()
