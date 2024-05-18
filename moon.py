import telebot
import json
import requests
import urllib


TOKEN = ("7031439985:AAFFmmRhEmzsJh0Q-ZSLwAww_eQHoklWVF8")


bot = telebot.TeleBot(TOKEN)

print("BOT AKTİF EDİLDİ...")




@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = 7187410709
    group_id =-1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    response = f"🍀 Merhaba {user_name}, ({user_id})!\n\n📚 Tsg Oyun Botuna Hoş Geldin. Bu bot, Oyun İndirme Botudur Tamamen ücretsizdir\n\n📮 Sorgular Ücretsiz Olduğu İçin @TSGChecker Katılmak Zorunludur."

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("📢 Tsg Kanal", url="https://t.me/TSGChecker"),
        telebot.types.InlineKeyboardButton("💭 Tsg Sohbet", url="https://t.me/TSGCheckerChat"),
        telebot.types.InlineKeyboardButton("👨🏼‍💻 İletişim", url="tg://user?id=6782067807")
    )
    markup.add(
        telebot.types.InlineKeyboardButton("🔍 Komutlar", callback_data="commands")
    )

    bot.send_message(message.chat.id, response, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "commands")
def commands(call):
    response = "👨🏼‍💻 Komutlar Menüsü :"

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("Ad Soyad", callback_data="sorgu"),
       telebot.types.InlineKeyboardButton("Ad Soyad İl", callback_data="sorgu1") 
    )
    markup.add(
        telebot.types.InlineKeyboardButton("TC Sorgu", callback_data="tc"),
        telebot.types.InlineKeyboardButton("TC Plus", callback_data="tc_plus")
        
    )
    markup.add(
    telebot.types.InlineKeyboardButton("TC Gsm", callback_data="tc_gsm"),
        telebot.types.InlineKeyboardButton("Aile", callback_data="aile")
        
    )
    markup.add(
        telebot.types.InlineKeyboardButton("Iban Sorgu", callback_data="iban_sorgu"),
        
        telebot.types.InlineKeyboardButton("Yazi", callback_data="yazi")
    )
    
    markup.add(
        
        telebot.types.InlineKeyboardButton("⬅️ Geri", callback_data="back")
    )

    bot.edit_message_text(response, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    start(call.message)

@bot.callback_query_handler(func=lambda call: call.data in ["sorgu", "sorgu1", "tc", "tc_gsm", "aile", "tc_plus", "yazi", "iban_sorgu"])
def other_commands(call):
    if call.data == "sorgu":
        response = "Ad Soyad Sorgu Yardım:\n\n/sorgu -isim <kurbanın adı> -soyisim <kurbanın soy adı> \n\nİki isimli Sorgulama için -isim2 kullanabilirsiniz örnek:\n/sorgu -isim betül -isim2 berra -soyisim kapancı"
    elif call.data == "tc":
        response = "TC Sorgu Yardım:\n\n/tc <kurbanın tc>\n\nYardım İçin Sohbet Grubumuza Gelebilirsin. @TSGChecker"
    elif call.data == "sorgu1":
        response = "Ad Soyad Sorgu Yardım:\n\n/sorgu1 -isim <kurbanın adı> -soyisim <kurbanın soy adı> -il <kurbanın il>\n\nİki isimli Sorgulama için -isim2 kullanabilirsiniz örnek:\n/sorgu -isim betül -isim2 berra -soyisim kapancı -il istanbul"
    elif call.data == "tc_gsm":
        response = "TC Gsm Yardım:\n\n/tcgsm <kurbanın tc>\n\nÇekinmeden Sohbet Edebileceğin Sohbet Grubumuza Katıl @TSGChecker."
    elif call.data == "aile":
        response = "Aile Sorgu Yardım:\n\n/aile <kurbanın tc>\n\nHer Gün Çok Güzel Paylaşımlar Olan Kanalımıza Katıl. @TSGChecker"
    elif call.data == "tc_plus":
        response = "TC Plus Sorgu Yardım:\n\n/tcplus <kurbanın tc>\n\nSohbet Grubumuza Katılmaya Ne Dersin?"
    elif call.data == "yazi":
        response = "Yazi Yardım:\n\n/yaz - Yazılan Metini Deftere Yazar"
    elif call.data == "iban_sorgu":
        response = "İban Sorgu Yardım:\n\n/iban <kurbanın iban>\n\nkurbanın ibanı birleşik girin örnek TR317377373722"

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("⬅️ Geri", callback_data="commands")
    )

    bot.edit_message_text(response, call.message.chat.id, call.message.message_id, reply_markup=markup)


def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(str(e))
        return False

import requests

@bot.message_handler(commands=["tc"])
def tc_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = 7187410709
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        
        bot.send_message(message.chat.id, response)
        return

    mesaj = message.text
    if mesaj.startswith("/tc"):
        tc = mesaj.replace("/tc", "").strip()
        if tc.isdigit() and len(tc) == 11:
            api_url = f"http://172.208.52.218/api/legaliapi/tc.php?tc={tc}"
            try:
                response = requests.get(api_url)
                if response.status_code == 200:
                    json_data = response.json()
                    if json_data.get("success", False):
                        data = json_data.get("data", {})
                        adi = data.get("ADI", "")
                        soyadi = data.get("SOYADI", "")
                        dogum_tarihi = data.get("DOGUMTARIHI", "")
                        nufus_il = data.get("NUFUSIL", "")
                        nufus_ilce = data.get("NUFUSILCE", "")
                        anne_adi = data.get("ANNEADI", "")
                        anne_tc = data.get("ANNETC", "")
                        baba_adi = data.get("BABAADI", "")
                        baba_tc = data.get("BABATC", "")
                        uyrugu = data.get("UYRUK", "Bilinmiyor")
                        cevap = f"""
╭━━━━━━━━━━━━━╮
┃➥ @TSGChecker
╰━━━━━━━━━━━━━╯
╭━━━━━━━━━━━━━━
┃➥ 𝖳𝖢: {tc}
┃➥ 𝖠𝖣𝖨: {adi}
┃➥ 𝖲𝖮𝖸 𝖠𝖣𝖨: {soyadi}
┃➥ 𝖣𝖮𝖦̆𝖴𝖬 𝖳𝖠𝖱𝖨𝖧𝖨: {dogum_tarihi}
┃➥ 𝖭𝖴𝖥𝖴𝖲𝖨𝖫: {nufus_il}
┃➥ 𝖭𝖴𝖥𝖴𝖲𝖨𝖫𝖢𝖤: {nufus_ilce}
┃➥ 𝖠𝖭𝖭𝖤 𝖠𝖣: {anne_adi}
┃➥ 𝖠𝖭𝖭𝖤 𝖳𝖢: {anne_tc}
┃➥ 𝖡𝖠𝖡𝖠 𝖠𝖣: {baba_adi}
┃➥ 𝖡𝖠𝖡𝖠 𝖳𝖢: {baba_tc}
┃➥ Uyruk: {uyrugu}
╰━━━━━━━━━━━━━━
"""
                    else:
                        cevap = "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯"
                else:
                    cevap = f"Api Hata Kodu: {response.status_code}"
            except Exception as e:
                cevap = f"Hata oluştu: {str(e)}"
        else:
            cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝖴 𝖥𝗈𝗋𝗆𝖺𝗍: /tc <kurbanın tc>\n╰──────────────────────╯"
    else:
        cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝖴 𝖥𝗈𝗋𝗆𝖺𝗍: /tc <kurbanın tc>\n╰──────────────────────╯"
    bot.send_message(message.chat.id, cevap)

def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ["member", "administrator", "creator"]
    except Exception as e:
        print(str(e))
        return False



@bot.message_handler(commands=["tcplus"])
def tcplus_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    log_message = f"Yeni TC Plus Sorgu Atıldı!\n" \
                  f"Sorgulanan TC: {message.text.split(' ')[1]}\n" \
                  f"Sorgulayan ID: {user_id}\n" \
                  f"Sorgulayan Adı: {user_name}\n" \
                  f"Sorgulayan K. Adı: @{message.from_user.username}"
    bot.send_message(-1002017751874, log_message)

    channel_id = 7187410709
    group_id =-1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGChecker"
        bot.send_message(message.chat.id, response)
        return

    mesaj = message.text

    if mesaj.startswith("/tcplus"):
        tc = mesaj.replace("/tcplus", "").strip()

        if tc:
            api_url = f"http://172.208.52.218/api/legaliapi/tcpro.php?tc={tc}"

            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()

                if json_data.get("success") and "data" in json_data:
                    data = json_data["data"]
                    adi = data.get("ADI", "")
                    soyadi = data.get("SOYADI", "")
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

                    cevap = f"""
╭━━━━━━━━━━━━━╮
┃➥ @TSGChecker
╰━━━━━━━━━━━━━╯
╭━━━━━━━━━━━━━━
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
{gsm_mesaj}╰━━━━━━━━━━━━━━
"""
                else:
                    cevap = "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯"
            else:
                cevap = f"api hata kod: ({response.status_code}): {response.text}"
        else:
            cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tcplus <kurbanın tc>\n╰──────────────────────╯"
    else:
        cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tcplus <kurbanın tc>\n╰──────────────────────╯"
    bot.send_message(message.chat.id, cevap)


@bot.message_handler(commands=["sorgu"])
def sorgu(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = 7187410709
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        
        bot.send_message(message.chat.id, response)
        return

    
    text = message.text
    words = text.split()

    isim = None
    isim2 = None
    soyisim = None
    il = None

    for i in range(len(words)):
        if words[i] == "-isim" and i < len(words) - 1:
            isim = words[i + 1]
        elif words[i] == "-isim2" and i < len(words) - 1:
            isim2 = words[i + 1]
        elif words[i] == "-soyisim" and i < len(words) - 1:
            soyisim = words[i + 1]
        elif words[i] == "-il" and i < len(words) - 1:
            il = words[i + 1]

    if not isim or not soyisim:
        bot.reply_to(message, "╭───────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n┃✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /sorgu -isim ┃<kurbanın adı> -soyisim <kurbanın ┃soy adı>\n╰───────────────────╯")
        return

    
    log_message = f"Yeni Ad Soyad Sorgu Atıldı!\n" \
                  f"Sorgulanan Ad: {isim}\n" \
                  f"Sorgulanan Soyad: {soyisim}\n" \
                  f"Sorgulayan ID: {message.from_user.id}\n" \
                  f"Sorgulayan Adı: {message.from_user.first_name}\n" \
                  f"Sorgulayan K. Adı: @{message.from_user.username}"
    bot.send_message(-1002017751874, log_message) 

    if isim2:
        isim_encoded = urllib.parse.quote(f"{isim} {isim2}")
    else:
        isim_encoded = urllib.parse.quote(isim)

    api_url = f"http://172.208.52.218/api/legaliapi/adsoyad.php?ad={isim_encoded}&soyad={soyisim}"

    if il:
        api_url += f"&il={il}"

    response = requests.get(api_url)
    data = response.json()

    if data["status"] == "success":
        people = data["data"]

        for person in people:
            tc = person["TC"]
            adi = person["ADI"]
            soyadi = person["SOYADI"]
            dogumtarihi = person["DOGUMTARIHI"]
            anneadi = person["ANNEADI"]
            annetc = person["ANNETC"]
            babaadi = person["BABAADI"]
            babatc = person["BABATC"]
            nufusil = person["NUFUSIL"]
            nufusilce = person["NUFUSILCE"]

            info = f"""
╭━━━━━━━━━━━━━╮
┃➥ @TSGChecker
╰━━━━━━━━━━━━━╯

╭━━━━━━━━━━━━━━
┃➥TC: {tc}
┃➥ ADI: {adi}
┃➥ SOY ADI: {soyadi}
┃➥ DOĞUM TARİHİ: {dogumtarihi}
┃➥ ANNE ADI: {anneadi}
┃➥ ANNE TC: {annetc}
┃➥ BABA ADI: {babaadi}
┃➥ BABA TC: {babatc}
┃➥ İL: {nufusil}
┃➥ İLÇE: {nufusilce}
╰━━━━━━━━━━━━━━
"""
            bot.send_message(message.chat.id, info)
    else:
        bot.reply_to(message, "Veri Bulunamadı Ah Ah.")


import urllib.parse
import requests

@bot.message_handler(commands=["sorgu1"])
def sorgu(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = 7187410709
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        
        bot.send_message(message.chat.id, response)
        return

    text = message.text
    words = text.split()

    isim = None
    isim2 = None
    soyisim = None
    il = None

    for i in range(len(words)):
        if words[i] == "-isim" and i < len(words) - 1:
            isim = words[i + 1]
        elif words[i] == "-isim2" and i < len(words) - 1:
            isim2 = words[i + 1]
        elif words[i] == "-soyisim" and i < len(words) - 1:
            soyisim = words[i + 1]
        elif words[i] == "-il" and i < len(words) - 1:
            il = words[i + 1]

    if not isim or not soyisim:
        bot.reply_to(message,         
        "╭───────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n┃✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /sorgu1 -isim ┃<kurbanın adı> -soyisim <kurbanın ┃soy adı> -il <kurbanın il>\n╰───────────────────╯")
        return

    log_message = f"Yeni Ad Soyad Sorgu Atıldı!\n" \
                  f"Sorgulanan Ad: {isim}\n" \
                  f"Sorgulanan Soyad: {soyisim}\n" \
                  f"Sorgulayan ID: {message.from_user.id}\n" \
                  f"Sorgulayan Adı: {message.from_user.first_name}\n" \
                  f"Sorgulayan K. Adı: @{message.from_user.username}"
    bot.send_message(-1002017751874, log_message)

    if isim2:
        isim_encoded = urllib.parse.quote(f"{isim} {isim2}")
    else:
        isim_encoded = urllib.parse.quote(isim)

    api_url = f"http://172.208.52.218/api/legaliapi/adsoyadil.php?ad={isim_encoded}&soyad={soyisim}"

    if il:
        api_url += f"&il={il}"

    response = requests.get(api_url)
    data = response.json()

    if data["status"] == "success":
        people = data["data"]

        for person in people:
            tc = person["TC"]
            adi = person["ADI"]
            soyadi = person["SOYADI"]
            dogumtarihi = person["DOGUMTARIHI"]
            anneadi = person["ANNEADI"]
            annetc = person["ANNETC"]
            babaadi = person["BABAADI"]
            babatc = person["BABATC"]
            nufusil = person["NUFUSIL"]
            nufusilce = person["NUFUSILCE"]

            info = f"""
╭━━━━━━━━━━━━━╮
┃➥ @TSGChecker
╰━━━━━━━━━━━━━╯

╭━━━━━━━━━━━━━━╮
┃➥TC: {tc}
┃➥ ADI: {adi}
┃➥ SOYADI: {soyadi}
┃➥ DOĞUM TARİHİ: {dogumtarihi}
┃➥ ANNE ADI: {anneadi}
┃➥ ANNE TC: {annetc}
┃➥ BABA ADI: {babaadi}
┃➥ BABA TC: {babatc}
┃➥ İL: {nufusil}
┃➥ İLÇE: {nufusilce}
╰━━━━━━━━━━━━━━╯
"""
            bot.send_message(message.chat.id, info)
    else:
        bot.reply_to(message, "Veri Bulunamadı Ah Ah.")





@bot.message_handler(commands=["aile"])
def aile_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = 7187410709
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    log_message = f"Yeni Aile Sorgu Atıldı!\n" \
                  f"Sorgulanan TC: {message.text.replace('/aile', '').strip()}\n" \
                  f"Sorgulayan ID: {message.from_user.id}\n" \
                  f"Sorgulayan Adı: {message.from_user.first_name}\n" \
                  f"Sorgulayan K. Adı: @{message.from_user.username}"
    bot.send_message(-1002017751874, log_message)

    mesaj = message.text

    if mesaj.startswith("/aile"):
        tc = mesaj.replace("/aile", "").strip()

        if tc.isdigit() and len(tc) == 11:
            api_url = f"http://172.208.52.218/api/legaliapi/aile.php?tc={tc}"
            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()

                if json_data["success"] == True:
                    people = json_data["data"]
                    cevap = "╭━━━━━━━━━━━━━╮\n┃➥ @tekcrackarsiv\n╰━━━━━━━━━━━━━╯"
                    for person in people:
                        tc = person.get("TC", "-")
                        adi = person.get("ADI", "-")
                        soyadi = person.get("SOYADI", "-")
                        dogumtarihi = person.get("DOGUMTARIHI", "-")
                        nufusil = person.get("NUFUSIL", "-")
                        nufusilce = person.get("NUFUSILCE", "-")
                        anneadi = person.get("ANNEADI", "-")
                        annetc = person.get("ANNETC", "-")
                        babaadi = person.get("BABAADI", "-")
                        babatc = person.get("BABATC", "-")
                        uyruk = person.get("UYRUK", "-")
                        yakinlik = person.get("Yakınlık", "-")

                        info = f"""
╭━━━━━━━━━━━━━━
┃➥ TC: {tc}
┃➥ ADI: {adi}
┃➥ SOY ADI: {soyadi}
┃➥ DOĞUM TARİHİ: {dogumtarihi}
┃➥ İL: {nufusil}
┃➥ İLÇE: {nufusilce}
┃➥ ANNE ADI: {anneadi}
┃➥ ANNE TC: {annetc}
┃➥ BABA ADI: {babaadi}
┃➥ BABA TC: {babatc}
┃➥ UYRUK: {uyruk}
┃➥ YAKINLIK: {yakinlik}
╰━━━━━━━━━━━━━━
"""
                        cevap += info

                    bot.send_message(message.chat.id, cevap)
                else:
                    bot.reply_to(message, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯")
            else:
                bot.reply_to(message, f"hata ({response.status_code}).")
        else:
            bot.reply_to
