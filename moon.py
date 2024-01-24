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

@bot.on_message(filters.document & filters.private)
def upload_document(client, message):
    if message.from_user.id != allowed_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="SİKTİR GİT YARAM SAKULTAH SİKER ANANI İKİLE "
        )
        return

    file_id = message.document.file_id
    file_name = message.document.file_name  # Dosyanın orijinal adını al

    file_path = client.download_media(message, file_name=f'downloads/{message.command[0]}_{file_name}')

    upload_url = f"https://sngvip.fun/upload{message.command[0]}.php"
    files = {'file': (file_name, open(file_path, 'rb'))}  # Dosyanın adını kullan

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

@bot.on_message(filters.command(["upload1", "upload2", "upload3", "upload4", "upload5"]))
def trigger_upload(client, message):
    # Add any conditions or additional checks here if needed
    # Trigger the upload process by sending a document
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Dosya yüklemek için bir belge gönderin. Kullanabileceğiniz PHP endpoint: https://sngvip.fun/upload{message.command[0]}.php"
    )

# Bot'u başlat
bot.run()
