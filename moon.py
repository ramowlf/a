from pyrogram.handlers import MessageHandler
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import Config  # Assuming this file contains your configuration

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="Merhaba!",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('💌 ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ 💌', url=f'http://t.me/DenizzmusiccBot?startgroup=new'),
              ], [
                InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url=f'https://t.me/japonicd')
              ], [
                InlineKeyboardButton('👤 ᴏᴡɴᴇʀ', url=f'https://t.me/sakultahbey')
              ]
            ]
        )
    )

bot.run()
