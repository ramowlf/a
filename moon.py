from pyrogram import Client, filters
from config import Config
import requests

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

@bot.on_message(filters.document & filters.private)
def upload_document(client, message):
    file_id = message.document.file_id
    file_path = client.download_media(message, file_name='downloads/')

    upload_url = "https://sngvip.fun/upload.php"
    files = {'file': ('filename', open(file_path, 'rb'))}

    try:
        response = requests.post(upload_url, files=files)

        # If upload is successful
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
