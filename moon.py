import os
from pyrogram import Client, filters

bot = Client(
    'moonBot',
    bot_token='6756702590:AAEgJpC7qdmbg-5dYwpWLax0FqAh6bULkRc',
    api_id='23664317',
    api_hash='8c246b2d2b2455ff7bef02ae0178eefa'
)

# MERHABA KOMUTU
@bot.on_message(filters.text & ~filters.command)
def merhaba_command(client, message):
    message.reply_text("Merhaba!")

bot.run()
