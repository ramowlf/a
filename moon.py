import telebot
import requests
from datetime import datetime, timedelta

TOKEN = '7012512707:AAFc3gLNJdzxvmNfRv7cqAjqlCInSy_9qEE'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    
    welcome_message = f"*TSG Key Botuna Hoşgeldin {first_name} \n/key yazarak keyini alabilirsin.\n\n! Spam yaparsan bottan banlanırsın.*"
    
    bot.reply_to(message, welcome_message, parse_mode="Markdown")

def is_user_in_channel(chat_id, channel_username):
    try:
        chat_member = bot.get_chat_member(channel_username, chat_id)
        return chat_member.status != "left"
    except telebot.apihelper.ApiException as e:
        print(f"API Hatası")
        return False

last_key_time = {}

def is_user_allowed_to_get_key(user_id):
    if user_id in last_key_time:
        last_retrieval_time = last_key_time[user_id]
        time_since_last_retrieval = datetime.now() - last_retrieval_time
        
        if time_since_last_retrieval < timedelta(hours=24):
            return False
    return True

@bot.message_handler(commands=['key'])
def send_key(message):
    try:
        user_id = message.from_user.id
        
        channel_username = '@TSGxMODS'
        if not is_user_in_channel(user_id, channel_username):
            bot.reply_to(message, "Anahtar alabilmek için önce @TSGxMODS kanalımıza katılmanız gerekmektedir.", parse_mode="Markdown")
            return
               
        if not is_user_allowed_to_get_key(user_id):
            bot.reply_to(message, "24 saat içinde bir kez anahtar alabilirsiniz.")
            return

        response = requests.get("https://tsgmods.com.tr/2SyAmh0ND7ZMKjPamk.php")
        
        if response.status_code == 200:
            user_key = response.text.strip()
        else:
            bot.reply_to(message, f"Anahtar alınırken bir hata oluştu")
            return

        last_key_time[user_id] = datetime.now()

        bot.reply_to(message, f"Anahtarınız: `{user_key}`", parse_mode="MarkdownV2")
        
        log_message = f"Yeni Anahtar Atıldı!\n" \
                      f"Anahtar: {user_key}\n" \
                      f"Atayan ID: {message.from_user.id}\n" \
                      f"Atayan Adı: {message.from_user.first_name}\n" \
                      f"Atayan K. Adı: @{message.from_user.username}\n" \
                      f"Tarih ve Saat: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        bot.send_message(-1002079991334, log_message)  

    except Exception as e:
        bot.reply_to(message, f"Hata oluştu")

bot.polling()
