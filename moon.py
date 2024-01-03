import requests

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

# Function to get content from a text file on a website
def get_key_from_website(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Failed to fetch key. Error: {e}"

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    bot.send_message(
        chat_id=message.chat.id,
        text="AŞAĞIDAKİ KANAL KATILMADIĞINİZ TESPİT EDİLİRSE BAN YERSİNİZ",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url=f'https://t.me/japonicd')
              ]] 
        )
    )

# Key KOMUTU
@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    website_url = 'http://sakultah.fun/a.txt'  # Replace with your actual URL
    key_content = get_key_from_website(website_url)

    bot.send_message(
        chat_id=message.chat.id,
        text=key_content
    )

bot.run()
