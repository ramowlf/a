import telebot
import mysql.connector
import random
import string
from datetime import datetime, timedelta
import time

# MySQL veritabanı bağlantısı için gerekli bilgiler
DB_HOST = 'mysql6008.site4now.net'
DB_USER = 'aa7d17_apseta'
DB_PASSWORD = 'sSp6JdLyK6sE5Tee'
DB_DATABASE = 'db_aa7d17_apseta'

# Telegram botunuzun token'ını buraya ekleyin
TOKEN = '7078092516:AAEpH_4I6b6GF620GmgmwvHTDhDbP_mRqN8'

# Bot oluştur
bot = telebot.TeleBot(TOKEN)

# '/start' komutunu işle
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    # Hoşgeldin mesajı
    welcome_message = f"*TSG Key Botuna Hoşgeldin {first_name} \n/key yazarak keyini alabilirsin.\n\n! Spam yaparsan bottan banlanırsın.*"
    
    bot.reply_to(message, welcome_message, parse_mode="Markdown")





# Kullanıcının bir kanala katılıp katılmadığını kontrol etme fonksiyonu
def is_user_in_channel(chat_id, channel_username):
    try:
        chat_member = bot.get_chat_member(channel_username, chat_id)
        return chat_member.status != "left"
    except telebot.apihelper.ApiException as e:
        print(f"API Hatası: {e}")
        return False

# Anahtar oluşturma fonksiyonu
def generate_user_key(length=12):
    chars = string.ascii_letters + string.digits
    user_key = "TSGxMODS" + ''.join(random.choice(chars) for _ in range(length - 8))
    return user_key

# Kullanıcıların son anahtar alma zamanlarını takip etmek için bir sözlük
last_key_time = {}

# Kullanıcının son anahtar alma zamanını kontrol etme fonksiyonu
def is_user_allowed_to_get_key(user_id):
    if user_id in last_key_time:
        last_retrieval_time = last_key_time[user_id]
        time_since_last_retrieval = datetime.now() - last_retrieval_time
        # Eğer son alma zamanından 24 saat geçmediyse False döndür
        if time_since_last_retrieval < timedelta(hours=24):
            return False
    return True

# 'key' komutunu işle
@bot.message_handler(commands=['key'])
def send_key(message):
    try:
        user_id = message.from_user.id
        
        # Kullanıcının kanala katılıp katılmadığını kontrol et
        channel_username = '@snmskwkwmsmem'
        if not is_user_in_channel(user_id, channel_username):
            bot.reply_to(message, "Anahtar alabilmek için önce @rawzhack kanalımıza katılmanız gerekmektedir.")
            return

        # Kullanıcının son anahtar alma zamanını kontrol et
        if not is_user_allowed_to_get_key(user_id):
            bot.reply_to(message, "24 saat içinde bir kez anahtar alabilirsiniz.")
            return

        # MySQL veritabanına bağlan
        db_connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_DATABASE
        )

        # Bağlantı oluşturulduysa
        if db_connection.is_connected():
            cursor = db_connection.cursor()

            # Anahtar oluştur
            user_key = generate_user_key()
            duration = 1
            max_devices = 1
            created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            expired_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d %H:%M:%S')

            # Anahtarı veritabanına ekle
            sql_query = "INSERT INTO keys_code (user_key, duration, game, max_devices, registrator, created_at, expired_date) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (user_key, duration, 'PUBG', max_devices, 'AutoKeySistem', created_at, expired_date)
            cursor.execute(sql_query, values)

            # Veritabanına yapılan değişiklikleri kaydet
            db_connection.commit()

            # Kullanıcının son anahtar alma zamanını güncelle
            last_key_time[user_id] = datetime.now()

            # Anahtarı markdown formatında gönder
            bot.reply_to(message, f"Anahtarınız: `{user_key}`", parse_mode="MarkdownV2")

            # Bağlantıyı kapat
            cursor.close()
            db_connection.close()
        else:
            bot.reply_to(message, "Veritabanına bağlanılamadı.")
    except Exception as e:
        bot.reply_to(message, f"Hata oluştu: {e}")

# Botu çalıştır
bot.polling()
            
