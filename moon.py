from pyrogram import Client, filters

bot = Client('moonBot', bot_token='BOT_TOKEN', api_id='API_ID', api_hash='API_HASH')

@bot.on_message(filters.text & filters.private & filters.regex(r'^\s*merhaba\s*$'))
def hello_command(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Merhaba!"
    )

# Bot'u başlat
bot.run()
