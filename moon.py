import os
from pyrogram import Client, filters

bot = Client(
    'moonBot',
    bot_token='YOUR_BOT_TOKEN',
    api_id='YOUR_API_ID',
    api_hash='YOUR_API_HASH'
)

# MERHABA KOMUTU
@bot.on_message(filters.text & ~filters.command)
def merhaba_command(client, message):
    message.reply_text("Merhaba!")

bot.run()
