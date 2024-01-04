import requests
from datetime import datetime, timedelta
from pyrogram import Client, filters
from config import Config  # Assuming this file contains your configuration

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

last_key_time = {}

def get_key_from_php(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return "Lütfen Bekleyiniz 1 dk Sonra Tekrar Yazın"

def write_to_log(log_message):
    admin_user_id = 6698881784

    with open("message_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(log_message + "\n")

    try:
        bot.send_message(
            chat_id=admin_user_id,
            text=log_message
        )
    except Exception as e:
        print(f"Hata oluştu: {e}")

@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE BAN YERSİNİZ VE İSTEMEDİĞİM KİŞİLERİ BANLARI\nKEY ALMAK İÇİN /key YAZMANIZ YETERLİ KÜFÜR YAZAN BAN YER"
    )

@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    php_url = 'http://sakultah.fun/hbXAii2byXnvgAEF4M9tG33u/Sjajajajajaj.php'
    user_id = message.from_user.id

    if user_id in last_key_time:
        last_retrieval_time = last_key_time[user_id]
        time_since_last_retrieval = datetime.now() - last_retrieval_time

        if time_since_last_retrieval < timedelta(hours=24):
            bot.send_message(
                chat_id=message.chat.id,
                text="GÜNDE 1 KERE KEY ALABİLİRSİNİZ STOK YAPAMAZSINIZ❗"
            )
            return

    key_content = get_key_from_php(php_url)
    bot.send_message(
        chat_id=message.chat.id,
        text=key_content
    )

    last_key_time[user_id] = datetime.now()

    user_name = f"{message.from_user.first_name} {message.from_user.last_name}" if message.from_user.last_name else message.from_user.first_name
    log_message = f"Key retrieved - User: {user_name} - Date: {datetime.now()}"
    write_to_log(log_message)

@bot.on_message(filters.command(["ban"]) & filters.user(Config.ADMIN_USER_ID))
def ban_command(client, message):
    if len(message.command) == 2:
        user_id_to_ban = int(message.command[1])
        ban_duration_hours = 24
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Kullanım: /ban [KULLANICI_ID]"
        )
        return

    try:
        bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=user_id_to_ban,
            until_date=datetime.now() + timedelta(hours=ban_duration_hours)
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Kullanıcı {user_id_to_ban} {ban_duration_hours} saat boyunca yasaklandı."
        )
    except Exception as e:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Hata oluştu: {e}"
        )

@bot.on_message(filters.command(["unban"]) & filters.user(Config.ADMIN_USER_ID))
def unban_command(client, message):
    if len(message.command) == 2:
        user_id_to_unban = int(message.command[1])
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Kullanım: /unban [KULLANICI_ID]"
        )
        return

    try:
        bot.unban_chat_member(
            chat_id=message.chat.id,
            user_id=user_id_to_unban
        )
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Kullanıcının yasağı kaldırıldı: {user_id_to_unban}"
        )
    except Exception as e:
        bot.send_message(
            chat_id=message.chat.id,
            text=f"Hata oluştu: {e}"
        )

bot.run()

