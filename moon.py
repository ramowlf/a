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

@bot.on_message(filters.private)
def process_private_commands(client, message):
    # Komutları kontrol et
    if message.text.startswith("/upload1"):
        upload_file(client, message, 'upload.php')
    elif message.text.startswith("/upload2"):
        upload_file(client, message, 'upload2.php')
    else:
        bot.send_message(
            chat_id=message.chat.id,
            text="Geçersiz komut. /upload1 veya /upload2 kullanın."
        )

def upload_file(client, message, php_script):
    if message.from_user.id != allowed_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="Üzgünüm, dosya yüklemek için izniniz yok."
        )
        return

    file_id = None
    file_path = None
    if message.document:
        file_id = message.document.file_id
        file_path = client.download_media(message, file_name=f'downloads/{message.document.file_name}')

    if file_id and file_path:
        upload_url = f"https://yourwebsite.com/{php_script}"
        files = {'file': (message.document.file_name, open(file_path, 'rb'))}

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

# Bot'u başlat
bot.run()
