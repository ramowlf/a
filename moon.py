import sqlite3
from pyrogram import Client, filters

# Connect to SQLite database
conn = sqlite3.connect('your_database.db')  # Replace 'your_database.db' with your actual database file
cursor = conn.cursor()

# Create a table if not exists
cursor.execute('''
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY,
        chat_id INTEGER,
        key TEXT,
        value TEXT
    )
''')
conn.commit()

bot = Client(
    'moonBot',
    bot_token='6756702590:AAEgJpC7qdmbg-5dYwpWLax0FqAh6bULkRc',
    api_id='23664317',
    api_hash='8c246b2d2b2455ff7bef02ae0178eefa'
)

# MERHABA KOMUTU
@bot.on_message(filters.text)
def merhaba_command(client, message):
    if "key" in message.text.lower():
        # Example: Inserting data into the SQLite database
        chat_id = message.chat.id
        key = "example_key"
        value = "example_value"
        cursor.execute('INSERT INTO data (chat_id, key, value) VALUES (?, ?, ?)', (chat_id, key, value))
        conn.commit()

        # Example: Reading data from the SQLite database
        cursor.execute('SELECT * FROM data WHERE chat_id = ?', (chat_id,))
        rows = cursor.fetchall()
        for row in rows:
            message.reply_text(f"Data retrieved: {row}")

bot.run()
