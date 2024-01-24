from pyrogram import Client, filters
from config import Config
import requests

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

allowed_user_id = 6698881784  # Bu, sadece belirli bir kullanıcının dosya yüklemesine izin verecek ID'dir

def upload_file(client, message, upload_url):
    if message.from_user.id != allowed_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="Üzgünüm, dosya yüklemek için izniniz yok."
        )
        return

    file_id = message.document.file_id
    file_name = message.document.file_name

    file_path = client.download_media(message, file_name='downloads/' + file_name)

    files = {'file': (file_name, open(file_path, 'rb'))}

    try:
        response = requests.post(upload_url, files=files)

        if response.status_code == 200:
            bot.send_message(
                chat_id=message.chat.id,
                text="Dosya başarıyla yüklendi!"
            )
        else:
            bot.send_message(
                chat_id=message.chat.id,
                text="Dosya yüklenirken bir hata oluştu."
            )
    except Exception as e:
        print(f"Hata: {e}")
        bot.send_message(
            chat_id=message.chat.id,
            text="Dosya yüklenirken bir hata oluştu."
        )

@bot.on_message(filters.document & filters.private)
def upload_document1(client, message):
    upload_file(client, message, "https://sngvip.fun/upload.php")

@bot.on_message(filters.command("upload"))
def trigger_upload1(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Dosya yüklemek için bir belge gönderin."
    )

@bot.on_message(filters.document & filters.private)
def upload_document2(client, message):
    upload_file(client, message, "https://sngvip.fun/upload2.php")

@bot.on_message(filters.command("upload2"))
def trigger_upload2(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Dosya yüklemek için bir belge gönderin."
    )

# Bot'u başlat
bot.run()
