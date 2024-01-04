import requests
from datetime import datetime, timedelta
from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import Config

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# Web Sitesi URL'si
blocked_users_url = "http://sakultah.fun/a.txt"  # Gerçek URL'yi kendi ihtiyaçlarınıza göre değiştirin

# Dosyadan Engellenen Kullanıcıları Okuma Fonksiyonu
def read_blocked_users_from_web():
    try:
        response = requests.get(blocked_users_url)
        response.raise_for_status()  # Hatalı yanıtlar için HTTPError fırlatır (4xx veya 5xx)
        return set(int(line.strip()) for line in response.text.splitlines())
    except requests.exceptions.RequestException as e:
        print(f"Hata: {e}")
        return set()

# Engellenen Kullanıcılar
blocked_users = read_blocked_users_from_web()

# Kullanıcı Engelleme Filtresi
def is_user_blocked(_, __, msg):
    user_id = msg.from_user.id
    return user_id in blocked_users

# START KOMUTU
@bot.on_message(filters.command(["start"]) & ~is_user_blocked)
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
@bot.on_message(filters.command(["key"]) & ~is_user_blocked)
def key_command(client, message):
    # Eğer kullanıcı engellenmişse işlem yapma
    if message.from_user.id in blocked_users:
        bot.send_message(
            chat_id=message.chat.id,
            text="Üzgünüm, ancak size izin verilmiyor. Engellenen bir kullanıcısınız."
        )
        return
    
    # Key alma işlemleri
    php_url = 'http://sakultah.fun/hbXAii2byXnvgAEF4M9tG33u/Sjajajajajaj.php'
    user_id = message.from_user.id

    # Check if user's last key retrieval time is available
    # ...

    # Retrieve and send the key
    key_content = get_key_from_php(php_url)
    bot.send_message(
        chat_id=message.chat.id,
        text=key_content
    )

    # Update user's last key retrieval time
    # ...

bot.run()
    
