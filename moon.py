import requests
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config  # Assuming this file contains your configuration

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# Function to get banned IDs from a file
def get_banned_ids_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            banned_ids = [int(line.strip()) for line in file if line.strip()]
        return banned_ids
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return []

# Function to get banned IDs from a web page
def get_banned_ids_from_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        banned_ids = [int(line.strip()) for line in response.text.split('\n') if line.strip()]
        return banned_ids
    except requests.exceptions.RequestException as e:
        print(f"Hata oluştu: {e}")
        return []

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

# List to store banned user IDs
banned_user_ids_url = 'http://sakultah.fun/a.txt'  # Replace with the actual URL
banned_user_ids = get_banned_ids_from_website(banned_user_ids_url)

# Log dosyasına yazan işlev
def write_to_log(log_message):
    admin_user_id = 6698881784  # Yönetici kullanıcının ID'sini buraya ekleyin
    
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

# Komutlara cevap verme fonksiyonu
def respond_to_commands(client, message):
    user_id = message.from_user.id

    # Check if user is banned
    if user_id in banned_user_ids:
        # Eğer kullanıcı banlı ise mesaj atmasına izin verme
        bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=user_id
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=f"{user_id} numaralı kullanıcı banlı olduğu için atıldı."
        )
        return

    # Diğer komutlara devam et
    # ...

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    user_id = message.from_user.id

    # Check if user is banned
    if user_id in banned_user_ids:
        bot.send_message(
            chat_id=message.chat.id,
            text="Banlısınız! ❌"
        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE BAN YERSİNİZ VE İSTEMEDİĞİM KİŞİLERİ BANLARI\nKEY ALMAK İÇİN /key YAZMANIZ YETERLİ KÜFÜR YAZAN BAN YER",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url=f'https://t.me/rawzhack')
                ]] 
            )
        )

# KEY KOMUTU
@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    respond_to_commands(client, message)

# Check if a user is banned when joining the chat
@bot.on_message(filters.chat(chats='your_chat_id') & filters.new_chat_members)
def on_new_chat_members(client, message):
    user_id = message.new_chat_members[0].id

    if user_id in banned_user_ids:
        bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=user_id
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=f"{user_id} numaralı kullanıcı banlı olduğu için atıldı."
        )

bot.run()
