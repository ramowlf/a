import os
import wget
from pyrogram import Client, filters

bot = Client(
    'moonBot',
    bot_token='6756702590:AAEgJpC7qdmbg-5dYwpWLax0FqAh6bULkRc',
    api_id='23664317',
    api_hash='8c246b2d2b2455ff7bef02ae0178eefa'
)

# MERHABA KOMUTU
@bot.on_message(filters.text)
def merhaba_command(client, message):
    if "merhaba" in message.text.lower():
        file_url = "http://sakultah.fun/s.php"  # Replace with the actual file URL
        file_path = wget.download(file_url)
        message.reply_document(document=file_path, caption="Merhaba! Dosyanızı gönderiyorum.")

        # Remove the downloaded file after sending
        os.remove(file_path)

bot.run()
