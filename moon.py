import sqlite3
import random
import string
from datetime import datetime, timedelta
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# SQLite veritabanı dosyasının adı
db_file = "vpanel.db"

bot = Client(
    'moonBot',
    bot_token=Config.BOT_TOKEN,
    api_id=Config.API_ID,
    api_hash=Config.API_HASH
)

def generate_random_string(length=12):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def is_username_unique(username, cursor):
    query = "SELECT COUNT(*) FROM vpanel WHERE username = ?"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    return result[0] == 0

def get_latest_username():
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        query = "SELECT username FROM vpanel ORDER BY expDate DESC LIMIT 1"
        cursor.execute(query)
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result[0] if result else None
    except Exception as e:
        print(f"Error: {e}")
        return None

def insert_data_to_sqlite():
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        # Generate a random username and ensure it's unique
        username = generate_random_string()
        while not is_username_unique(username, cursor):
            username = generate_random_string()

        # Generate a random password
        password = generate_random_string()

        # Calculate expDate to be 1 day from the current date and time
        exp_date = datetime.now() + timedelta(days=1)

        # Replace the INSERT query with your actual query to insert data into SQLite
        query = "INSERT INTO vpanel (username, password, uuid, expDate, expType, userType) VALUES (?, ?, ?, ?, ?, ?)"
        
        # Example data, you should replace these values with your actual data
        data = (username, password, 'bd73bd2db75956fe', exp_date, '1 day', 'membership')

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

# START KOMUTU
@bot.on_message(filters.command(["start"]))
def start_command(client, message):
    # ... (kodunuz aynı kalabilir)

# KEY KOMUTU
@bot.on_message(filters.command(["key"]))
def key_command(client, message):
    latest_username = get_latest_username()

    if latest_username:
        response_text = f"Son eklenen kullanıcı adı: {latest_username}"
    else:
        response_text = "Henüz hiç kullanıcı eklenmemiş."

    bot.send_message(chat_id=message.chat.id, text=response_text)

bot.run()
