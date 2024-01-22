from pyrogram import Client, filters
from config import Config
import requests

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

allowed_user_id = 6698881784  # Sadece belirli bir kullanıcının dosya yüklemesine izin verecek ID'dir

def upload_file(message, upload_url):
    if message.from_user.id != allowed_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="Üzgünüm, dosya yüklemek için izniniz yok."
        )
        return

    if not message.document:
        bot.send_message(
            chat_id=message.chat.id,
            text="Lütfen yüklemek istediğiniz belgeyi ekleyin."
        )
        return

    bot.send_message(
        chat_id=message.chat.id,
        text="Dosya yükleme işlemi başlatılıyor..."
    )

    try:
        file_name = message.document.file_name
        file_path = bot.download_media(message, file_name='downloads/' + file_name)
        files = {'file': (file_name, open(file_path, 'rb'))}

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

@bot.on_message(filters.command("upload") & filters.private)
def trigger_upload(client, message):
    upload_url = "https://sngvip.fun/upload.php"
    upload_file(message, upload_url)

@bot.on_message(filters.command("upload2") & filters.private)
def trigger_upload2(client, message):
    upload_url = "https://sngvip.fun/upload2.php"
    upload_file(message, upload_url)

# Bot'u başlat
bot.run()
        
