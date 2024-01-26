import requests
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config  # Assuming this file contains your configuration

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

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
banned_user_ids_url = 'https://sngvip.fun/banned_users.php'  # Replace with the actual URL
banned_user_ids = get_banned_ids_from_website(banned_user_ids_url)

# Function to update banned user IDs from the website
def update_banned_user_ids():
    global banned_user_ids
    banned_user_ids = get_banned_ids_from_website(banned_user_ids_url)

# Initial update of banned user IDs
update_banned_user_ids()

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
        bot.send_message(
            chat_id=message.chat.id,
            text="Banlısınız! ❌"
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
            text=f"{message.from_user.first_name}, AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE BAN YERSİNİZ LÜTFEN KATILIN \nKEY ALMAK İÇİN /key YAZMANIZ YETERLİ KÜFÜR YAZAN BAN YER",
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url='https://t.me/rawzhack')
                ]] 
            )
        )

# KEY KOMUTU
@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    user_id = message.from_user.id

    # Check if user is banned
    if user_id in banned_user_ids:
        bot.send_message(
            chat_id=message.chat.id,
            text="Banlısınız! ❌"
        )
        return

    php_url = 'https://sngvip.fun/hbXAii2byXnvgAEF4M9tG33u/Sjajajajajaj.php'  # Replace with your actual PHP file URL

    # Check if user's last key retrieval time is available
    if user_id in last_key_time:
        last_retrieval_time = last_key_time[user_id]
        time_since_last_retrieval = datetime.now() - last_retrieval_time

        # If less than 6 hours have passed since the last retrieval, notify the user
        if time_since_last_retrieval < timedelta(hours=6):
            bot.send_message(
                chat_id=message.chat.id,
                text="6 SAATDE 1 KERE KEY ALABİLİRSİNİZ STOK YAPAMAZSINIZ❗"
            )
            return

    # Retrieve and send the key
    key_content = get_key_from_php(php_url)

    # Send the key to the user
    bot.send_message(
        chat_id=message.chat.id,
        text=f"{message.from_user.first_name}, işte senin key'in:\n{key_content}"
    )

    # Send the key to the admin
    admin_user_id = 6698881784  # Replace with your admin's user ID
    admin_user_name = "Admin"  # Replace with your admin's username
    admin_log_message = f"Key sent to {message.from_user.username} ({user_id}) by {admin_user_name} - Date: {datetime.now()}"
    write_to_log(admin_log_message)
    bot.send_message(
        chat_id=admin_user_id,
        text=f"{message.from_user.first_name}'in key'i:\n{key_content}"
    )

    # Update user's last key retrieval time
    last_key_time[user_id] = datetime.now()

# BAN KOMUTU
@bot.on_message(filters.command(["ban"]))
def ban_command(client, message):
    admin_user_id = 6698881784  # Yönetici kullanıcının ID'sini buraya ekleyin

    # Sadece yönetici kullanıcı bu komutu kullanabilir
    if message.from_user.id != admin_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="Bu komutu sadece yönetici kullanıcı kullanabilir! ❌"
        )
        return

    # Banlanacak kullanıcının ID'sini al
    banned_user_id = int(message.text.split(" ")[1])

    # Eğer yönetici kendi ID'sini banlamaya çalışıyorsa hata mesajı gönder
    if banned_user_id == admin_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="Kendinizi banlayamazsınız! ❌"
        )
        return

    # Banlanan kullanıcıyı listeye ekle
    banned_user_ids.append(banned_user_id)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Kullanıcı {banned_user_id} başarıyla banlandı! ❌"
    )

# UNBAN KOMUTU
@bot.on_message(filters.command(["unban"]))
def unban_command(client, message):
    admin_user_id = 6698881784  # Yönetici kullanıcının ID'sini buraya ekleyin

    # Sadece yönetici kullanıcı bu komutu kullanabilir
    if message.from_user.id != admin_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="Bu komutu sadece yönetici kullanıcı kullanabilir! ❌"
        )
        return

    # Unban yapılacak kullanıcının ID'sini al
    unbanned_user_id = int(message.text.split(" ")[1])

    # Eğer yönetici kendi ID'sini unbanlamaya çalışıyorsa hata mesajı gönder
    if unbanned_user_id == admin_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="Kendinizi unbanlayamazsınız! ❌"
        )
        return

    # Eğer kullanıcı banlı değilse hata mesajı gönder
    if unbanned_user_id not in banned_user_ids:
        bot.send_message(
            chat_id=message.chat.id,
            text="Bu kullanıcı zaten banlı değil! ❌"
        )
        return

    # Banlı kullanıcıyı listeden çıkar
    banned_user_ids.remove(unbanned_user_id)

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Kullanıcı {unbanned_user_id} başarıyla unbanned! ✅"
    )

# Bot'u başlat
bot.run()
