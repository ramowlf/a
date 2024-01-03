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
        text="AŞAĞIDAKİ KANAL KATILMADIĞINİZ TESPİT EDİLİRSE BAN YERSİNİZ",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url=f'https://t.me/japonicd')
              ] 
                              
            ]
        )
    )

bot.run()
