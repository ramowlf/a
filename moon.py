from pyrogram import Client, filters
from config import Config  # Assuming this file contains your configuration
bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)
@bot.on_message(filters.text & filters.private & filters.regex(r'^\s*merhaba\s*$'))
def hello_command(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Merhaba!"
    )

# Bot'u başlat
bot.run()
