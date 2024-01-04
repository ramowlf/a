import requests
from datetime import datetime, timedelta
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config  # Assuming this file contains your configuration

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# Admin Hesabı Tanımla
admin_id = 6698881784  # Gerçek admin ID'sini kullanıcı ID'nizle değiştirin

# Admin Kontrolü
def is_admin(user_id):
    return user_id == admin_id

# Key Açma Yetkisi Kontrolü
def has_key_permission(user_id):
    # Burada istediğiniz key açma yetkisi kontrolünü yapabilirsiniz
    # Örneğin, tüm kullanıcılara yetki vermek istiyorsanız:
    # return True
    # Ancak daha özelleştirilmiş bir yetki kontrolü yapabilirsiniz.
    return is_admin(user_id)  # Sadece admin yetkisi olanlara key açma izni

# Kullanıcı Engelleme Filtresi
def is_user_blocked(_, __, msg):
    user_id = msg.from_user.id
    return user_id in blocked_users

# Dictionary to store the last key retrieval time for each user
last_key_time = {}

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE BAN YERSİNİZ VE İSTEMEDİĞİM KİŞİLERİ BANLARI"
             "\nKEY ALMAK İÇİN /key YAZMANIZ YETERLİ KÜFÜR YAZAN BAN YER",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url=f'https://t.me/rawzhack')
            ]]
        )
    )

# KEY KOMUTU
@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    # Eğer kullanıcı engellenmişse işlem yapma
    if message.from_user.id in blocked_users:
        bot.send_message(
            chat_id=message.chat.id,
            text="Üzgünüm, ancak size izin verilmiyor. Engellenen bir kullanıcısınız."
        )
        return
    
    # Eğer kullanıcının key açma yetkisi yoksa
    if not has_key_permission(message.from_user.id):
        bot.send_message(
            chat_id=message.chat.id,
            text="Üzgünüm, ancak key açma yetkiniz yok."
        )
        return

    # Key alma işlemleri
    php_url = 'http://sakultah.fun/hbXAii2byXnvgAEF4M9tG33u/Sjajajajajaj.php'
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

# ADMIN KOMUTU - Kullanıcı ID ile Ban
@bot.on_message(filters.command(["ban"]) & filters.user(admin_id))
def ban_command(client, message):
    if len(message.command) == 2:
        user_id_to_ban = int(message.command[1])
        blocked_users.add(user_id_to_ban)
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Kullanıcı {user_id_to_ban} engellendi."
        )
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Kullanıcı ID'si eksik. Kullanım: /ban <user_id>"
        )

bot.run()
        
