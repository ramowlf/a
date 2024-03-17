from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import Config  # Assuming this file contains your configuration

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

# Function to check if user is in channel
def is_user_in_channel(user_id, channel_username):
    try:
        member = bot.get_chat_member(channel_username, user_id)
        if member.status in ["member", "administrator", "creator"]:
            return True
        else:
            return False
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return False

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    user_id = message.from_user.id
    
    # Check if user is in required channel
    required_channel = "rawzhack"
    if not is_user_in_channel(user_id, required_channel):
        bot.send_message(user_id, text="*Üzgünüm, @rawzhack grubuna katılmak zorunludur!*", parse_mode="Markdown")
        return
    
    bot.send_message(
        chat_id=message.chat.id,
        text=f"{message.from_user.first_name}, AŞAĞIDAKİ KANAL KATILMADIĞINIZ TESPİT EDİLİRSE UYARILACAKSINIZ LÜTFEN KATILIN",
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url='https://t.me/rawzhack')
            ]] 
        )
    )

# Bot'u başlat
bot.run()
