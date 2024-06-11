import telebot , requests , json ; from telebot import types
token = "7470061611:AAFqRu0bBmxE7wGAQcbEoqvB5LR_zEwH9pg"# token 
bot = telebot.TeleBot(token)#input('- Enter Token : '))
my_ch = '-1002017794930'#معرف قناتك داخل الاقواس
@bot.message_handler(commands=['start'])
def start(message):
	id  = message.from_user.id
	url = requests.get(f"https://api.telegram.org/bot{token}/getchatmember?chat_id={my_ch}&user_id={id}").text
	if "member" in url or "creator" in url or "administartor" in url:
		start = types.InlineKeyboardButton(text='-Video İndirmeو',callback_data='start')
		Ronaldo = types.InlineKeyboardMarkup(row_width=2) ; Ronaldo.add(start)
		bot.send_message(message.chat.id,text='TikTok Video indirme botuna hoş geldiniz l, aşağıdaki düğmeler arasından seçim yapın.',reply_markup=Ronaldo)
	else:
		bot.send_message(message.chat.id,'''
🚸| Üzgünüm canım
🔰| Kullanabilmek için bot kanalına abone olmanız gerekmektedir.



️| Abone ol ve gönder /start'''.format(my_ch))
@bot.callback_query_handler(func=lambda call:True)
def start2(call):
	if call.data=='start':
		ji = bot.send_message(call.message.chat.id,text='- Hoş geldin canım, hemen linki gönder.')
		bot.register_next_step_handler(ji,dow)
def dow(message):
		url = message.text
		headers = {"referer":"https://lovetik.com/sa/video/","origin":"https://lovetik.com","user-agent":"Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/113.0"}
		payload = {"query":url}
		url =requests.post("https://lovetik.com/api/ajax/search",headers = headers,data=payload).json()
		try:
			respones=json.loads('{"ok":"true","Video":{"authorUser":"'+url['author']+'","authorName":"'+url['author_name']+'","authorImage":"'+url['author_a']+'","cover":"'+url['cover']+'","vidID":"'+url['vid']+'","desc":"'+url["desc"]+'","link":"'+url['links'][4]['a']+'","audioName":"'+url['links'][5]['s']+'","audioLink":"'+url['links'][5]['a']+'"}}') 
		except:
			bot.send_message(message.chat.id,'- Üzgünüm canım, bağlantı geçersiz! !')
		bot.send_video(message.chat.id,respones['Video']['link'],caption='- Video Başarıyla İndirildi @TSGChecker.')
if __name__=="__main__":
	bot.infinity_polling()
