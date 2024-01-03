from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

bot = Client(
    'moonBot',
    bot_token='6756702590:AAEgJpC7qdmbg-5dYwpWLax0FqAh6bULkRc',
    api_id='23664317',
    api_hash='8c246b2d2b2455ff7bef02ae0178eefa'
)

# MERHABA KOMUTU
@bot.on_message(filters.text & ~filters.command)
def merhaba_command(client, message):
    if "merhaba" in message.text.lower():
        message.reply_text("Merhaba!")

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    helptext = f'**📥 Telegram Müzik & Video İndirme Botudur, Tamamen Ücretsizdir ...\n\n» /bul < müzik adı >\n    - Anında Müzik İndirir ...\n» /vbul < video adı >\n    - Anında Video İndirir ...**'
    message.reply_text(
        text=helptext,
        quote=False,
        reply_markup=InlineKeyboardMarkup(
            [[
                InlineKeyboardButton('💌 ʙᴇɴɪ ɢʀᴜʙᴀ ᴇᴋʟᴇ 💌', url=f'http://t.me/DenizzmusiccBot?startgroup=new'),
            ], [
                InlineKeyboardButton('📚 ᴋᴀɴᴀʟ', url=f'https://t.me/japonicd')
            ], [
                InlineKeyboardButton('👤 ᴏᴡɴᴇʀ', url=f'https://t.me/sakultah')
            ]
            ]
        )
    )

# Bot başlatıldığında uyarı mesajı
@bot.on_startup
def on_startup():
    print("Bot başlatıldı! Hazır durumda.")

bot.run()
