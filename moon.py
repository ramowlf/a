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

# Log dosyasına yazan işlev
def write_to_log(message):
    log_file_path = "message_log.txt"  # Log dosyasının adı ve yolu
    with open(log_file_path, "a", encoding="utf-8") as log_file:
        log_file.write(message + "\n")

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

    # Hedef kullanıcıya DM olarak mesajı gönder
    user_message = f"Yeni Mesaj:\n{message_text}\n\nGönderen:\n{user_name}\n(@{user_username})\n\nChat ID: {user_chat_id}"
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

    # Anahtarın logunu oluştur
    user_name = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    key_log_message = f"Anahtar alındı - Kullanıcı: {user_name} - Tarih: {datetime.now()}"
    write_to_log(key_log_message)

bot.run()
