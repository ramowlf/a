import telebot
import requests
import sqlite3
from datetime import datetime, timedelta

token = "7012512707:AAFc3gLNJdzxvmNfRv7cqAjqlCInSy_9qEE"
bot = telebot.TeleBot(token)

print("BOT AKTİF EDİLDİ")

def create_connection():
    return sqlite3.connect('user_data.db')

def create_users_table():
    conn = create_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (user_id INTEGER PRIMARY KEY, last_key_time TIMESTAMP)''')
    conn.commit()
    conn.close()

def handle_key_command(message):
    current_time = datetime.now()
    
    user_id = message.chat.id
    
    conn = create_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user_data = c.fetchone()
    
    if user_data:
        last_key_time = datetime.strptime(user_data[1], "%Y-%m-%d %H:%M:%S.%f")  
        time_passed = current_time - last_key_time

        if time_passed < timedelta(days=1):
            remaining_time = timedelta(days=1) - time_passed
            bot.reply_to(message, f"24 saat içinde sadece bir kez key komutunu kullanabilirsiniz.")
            conn.close()
            return
    
    try:
        new_key = requests.get("https://tsgmods.com.tr/a.php").text
        bot.reply_to(message, f"Keyiniz: {new_key}")
        
        if user_data:
            c.execute("UPDATE users SET last_key_time=? WHERE user_id=?", (current_time, user_id))
        else:
            c.execute("INSERT INTO users (user_id, last_key_time) VALUES (?, ?)", (user_id, current_time))
        conn.commit()
    except Exception as e:
        print(f"Hata: {e}")
        bot.reply_to(message, "Bir hata oluştu. Lütfen daha sonra tekrar deneyin.")
    finally:
        conn.close()  

@bot.message_handler(commands=['key'])
def handle_key_command_wrapper(message):
    handle_key_command(message)

# Botu başlatmadan önce veritabanı ve tablo oluşturma
create_users_table()

while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Hata: {e}")

print("BOT AKTİF EDİLDİ")
            
