from pyrogram import Client, filters
from config import Config
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import requests

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

allowed_user_id = 6698881784

@bot.on_message(filters.document & filters.private)
def upload_document(client, message):
    if message.from_user.id != allowed_user_id:
        bot.send_message(
            chat_id=message.chat.id,
            text="SİKTİR GİT YARAM SAKULTAH SİKER ANANI İKİLE "
        )
        return

    file_id = message.document.file_id
    file_name = message.document.file_name

    file_path = client.download_media(message, file_name='downloads/' + file_name)

    upload_url = "https://sngvip.fun/upload.php"
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

@bot.on_message(filters.command("upload"))
def trigger_upload(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Dosya yüklemek için bir belge gönderin."
    )

    bot.send_message(
        chat_id=message.chat.id,
        text=f"{message.from_user.first_name}, AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE BAN YERSİNİZ VE İSTEMEDİĞİM KİŞİLERİ BANLARI\nKEY ALMAK İÇİN /key YAZMANIZ YETERLİ KÜFÜR YAZAN BAN YER",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton('ᴋᴀɴᴀʟ1', callback_data='upload_1'),
                    InlineKeyboardButton('ᴋᴀɴᴀʟ2', callback_data='upload_2')
                ],
                [InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url='https://t.me/rawzhack')]
            ]
        )
    )

# Bot'u başlat
bot.run()
