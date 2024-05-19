import telebot
import json
import requests
import urllib
import telebot
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import requests


TOKEN = ("7031439985:AAFFmmRhEmzsJh0Q-ZSLwAww_eQHoklWVF8")


bot = telebot.TeleBot(TOKEN)

print("BOT AKTİF EDİLDİ...")


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    response = f"🍀 Merhaba {user_name}, ({user_id})!\n\n📚 Tsg Oyun Botuna Hoş Geldin. Bu bot, Oyun İndirme Botudur Tamamen ücretsizdir\n\n📮 Sorgular Ücretsiz Olduğu İçin @TSGChecker Katılmak Zorunludur."

    

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("📢 Tsg Kanal", url="https://t.me/TSGChecker"),
        telebot.types.InlineKeyboardButton("💭 Tsg Sohbet", url="https://t.me/TSGCheckerChat"),
        telebot.types.InlineKeyboardButton("👨🏼‍💻 İletişim", url="tg://user?id=6782067807"),
        telebot.types.InlineKeyboardButton("🔍 Komutlar", callback_data="commands")
    )

    bot.send_message(message.chat.id, response, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "commands")
def commands(call):
    response = "👨🏼‍💻 Komutlar Menüsü :"

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(
        telebot.types.InlineKeyboardButton("Ad Soyad", callback_data="sorgu"),
        telebot.types.InlineKeyboardButton("Ad Soyad İl", callback_data="sorgu1"),
        telebot.types.InlineKeyboardButton("TC Sorgu", callback_data="tc"),
        telebot.types.InlineKeyboardButton("TC Plus", callback_data="tc_plus"),
        telebot.types.InlineKeyboardButton("TC Gsm", callback_data="tc_gsm"),
        telebot.types.InlineKeyboardButton("Aile", callback_data="aile"),
        telebot.types.InlineKeyboardButton("Iban Sorgu", callback_data="iban_sorgu"),
        
        telebot.types.InlineKeyboardButton("Yazi", callback_data="yazi"),
        
        telebot.types.InlineKeyboardButton("⬅️ Geri", callback_data="back")
    )

    bot.edit_message_text(response, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    start(call.message)

@bot.callback_query_handler(func=lambda call: call.data in ["sorgu", "tc", "tc_gsm", "aile", "tc_plus", "yazi", "iban_sorgu","yazi"])
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

@bot.message_handler(commands=["tc"])
def tc_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = (f"Merhaba {user_name}, ({user_id})!\n\n"
                    "Sorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\n"
                    "Kanal: @TSGChecker\nChat: @TSGCheckerChat")
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
                        
                        response_text = (f"╭━━━━━━━━━━━━━╮\n"
                                         f"┃➥ @TSGChecker\n"
                                         f"╰━━━━━━━━━━━━━╯\n"
                                         f"╭━━━━━━━━━━━━━━\n"
                                         f"┃➥ 𝖳𝖢: {tc}\n"
                                         f"┃➥ 𝖠𝖣𝖨: {adi}\n"
                                         f"┃➥ 𝖲𝖮𝖸 𝖠𝖣𝖨: {soyadi}\n"
                                         f"┃➥ 𝖣𝖮𝖦̆𝖴𝖬 𝖳𝖠𝖱𝖨𝖧𝖨: {dogum_tarihi}\n"
                                         f"┃➥ 𝖭𝖴𝖥𝖴𝖲𝖨𝖫: {nufus_il}\n"
                                         f"┃➥ 𝖭𝖴𝖥𝖴𝖲𝖨𝖫𝖢𝖤: {nufus_ilce}\n"
                                         f"┃➥ 𝖠𝖭𝖭𝖤 𝖠𝖣: {anne_adi}\n"
                                         f"┃➥ 𝖠𝖭𝖭𝖤 𝖳𝖢: {anne_tc}\n"
                                         f"┃➥ 𝖡𝖠𝖡𝖠 𝖠𝖣: {baba_adi}\n"
                                         f"┃➥ 𝖡𝖠𝖡𝖠 𝖳𝖢: {baba_tc}\n"
                                         f"┃➥ Uyruk: {uyrugu}\n"
                                         f"╰━━━━━━━━━━━━━━\n")
                        
                        bot.send_message(message.chat.id, response_text)
                    else:
                        cevap = "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯"
                        bot.send_message(message.chat.id, cevap)
                else:
                    cevap = f"Api Hata Kodu: {response.status_code}"
                    bot.send_message(message.chat.id, cevap)
            except Exception as e:
                cevap = f"Hata oluştu: {str(e)}"
                bot.send_message(message.chat.id, cevap)
        else:
            cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tc <kurbanın tc>\n╰──────────────────────╯"
            bot.send_message(message.chat.id, cevap)
    else:
        cevap = "╭──────────────────────╮\n┃ 📛 𝖸𝖺𝗇𝗅ı𝗌̧ 𝖪𝗈𝗆𝗎𝗍 𝖪𝗎𝗅𝗅𝖺𝗇ı𝗆ı\n│ ✅ 𝖣𝗈𝗀̆𝗋𝗎 𝖥𝗈𝗋𝗆𝖺𝗍: /tc <kurbanın tc>\n╰──────────────────────╯"
        bot.send_message(message.chat.id, cevap)



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

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = (f"Merhaba {user_name}, ({user_id})!\n\n"
                    f"Sorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. "
                    f"Kanal ve chate katılıp tekrar deneyin.\n\n"
                    f"Kanal: @TSGChecker\nChat: @TSGChecker")
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

                    response_text = (f"""
╭━━━━━━━━━━━━━╮
┃➥ @TSGChecker
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



@bot.message_handler(commands=["aile"])
def aile_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    start_message = bot.send_message(message.chat.id, "İşleminiz Gerçekleştiriliyor, Lütfen Bekleyin...")

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
                    cevap = "╭━━━━━━━━━━━━━╮\n┃➥ @TSGChecker\n╰━━━━━━━━━━━━━╯\n"
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

                        info = f"""╭━━━━━━━━━━━━━━
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
╰━━━━━━━━━━━━━━"""
                        cevap += info

                    file_name = f"Sonuçlar.txt"
                    with open(file_name, 'w', encoding='utf-8') as file:
                        file.write(cevap)

                    with open(file_name, 'rb') as file:
                        bot.send_document(message.chat.id, file, caption=f"**", parse_mode="Markdown")
                    
                    bot.delete_message(message.chat.id, start_message.message_id)
                else:
                    bot.reply_to(message, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖽ı\n╰────────────╯")
            else:
                bot.reply_to(message, f"hata ({response.status_code}).")
        else:
            bot.reply_to(message, "╭──────────────────────╮\n┃ 📛 Yanlış Formatlı TC\n┃ Kodu düzeltip tekrar deneyin.")



@bot.message_handler(commands=["sorgu"])
def sorgu(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
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
    ilce = None

    for i in range(len(words)):
        if words[i] == "-isim" and i < len(words) - 1:
            isim = words[i + 1]
        elif words[i] == "-isim2" and i < len(words) - 1:
            isim2 = words[i + 1]
        elif words[i] == "-soyisim" and i < len(words) - 1:
            soyisim = words[i + 1]
        elif words[i] == "-il" and i < len(words) - 1:
            il = words[i + 1]
        elif words[i] == "-ilce" and i < len(words) - 1:
            ilce = words[i + 1]

    if not isim or not soyisim:
        bot.reply_to(message, "Yanlış Kullanım! Doğru format: /sorgu -isim <isim> -soyisim <soyisim> [-il <il>] [-ilce <ilce>]")
        return

    chat_id = message.chat.id

    log_message = f"Yeni Sorgu Atıldı!\n" \
                  f"Sorgulanan İsim: {isim}\n" \
                  f"Sorgulanan Soyisim: {soyisim}\n" \
                  f"Sorgulanan İl: {il}\n" \
                  f"Sorgulanan İlçe: {ilce}\n" \
                  f"Sorgulayan ID: {user_id}\n" \
                  f"Sorgulayan Adı: {user_name}\n" \
                  f"Kanal ID: {chat_id}"

    bot.send_message(-1002017751874, log_message)

    start_message = bot.send_message(chat_id, "İşleminiz Gerçekleştiriliyor, Lütfen Bekleyin...")

    if isim2:
        isim_birlestirmesi = urllib.parse.quote(f"{isim} {isim2}")
    else:
        isim_birlestirmesi = urllib.parse.quote(isim)

    if il and ilce:
        api_url = f"http://181.214.223.74/Kurdistan/Api/adsoyad.php?ad={isim_birlestirmesi}&soyad={soyisim}&il={il}&ilce={ilce}"
    elif il:
        api_url = f"http://181.214.223.74/Kurdistan/Api/adsoyad.php?ad={isim_birlestirmesi}&soyad={soyisim}&il={il}"
    else:
        api_url = f"http://181.214.223.74/Kurdistan/Api/adsoyad.php?ad={isim_birlestirmesi}&soyad={soyisim}"

    response = requests.get(api_url)
    data = response.json()

    if data["success"] == "true":
        number = data["number"]
        if number > 0:
            people = data["data"]
            info = ""
            for person in people:
                tc = person["TC"]
                ad = person["ADI"]
                soyad = person["SOYADI"]
                dogumtarihi = person["DOGUMTARIHI"]
                nufusil = person["NUFUSIL"]
                nufusilce = person["NUFUSILCE"]
                anneadi = person["ANNEADI"]
                annetc = person["ANNETC"]
                babaadi = person["BABAADI"]
                babatc = person["BABATC"]
                uyrugu = person["UYRUK"]

                info += f"""╭━━━━━━━━━━━━━╮
┃➥ @TSGChecker
╰━━━━━━━━━━━━━╯
╭━━━━━━━━━━━━━━╮
┃➥TC: {tc}
┃➥ ADI: {ad}
┃➥ SOYADI: {soyad}
┃➥ DOĞUM TARİHİ: {dogumtarihi}
┃➥ ANNE ADI: {anneadi}
┃➥ ANNE TC: {annetc}
┃➥ BABA ADI: {babaadi}
┃➥ BABA TC: {babatc}
┃➥ İL: {nufusil}
┃➥ İLÇE: {nufusilce}
┃➥ UYRUK: {uyrugu}
╰━━━━━━━━━━━━━━╯
"""


            file_name = f"Sonuçlar.txt"
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(info)

            with open(file_name, 'rb') as file:
                bot.send_document(message.chat.id, file)
                bot.delete_message(chat_id, start_message.message_id)
        else:
            bot.send_message(message.chat.id, "Veri Bulunamadı.")
            bot.delete_message(chat_id, start_message.message_id)
    else:
        bot.send_message(message.chat.id, "Data bulunamadı.")
        bot.delete_message(chat_id, start_message.message_id)


import requests

@bot.message_handler(commands=["tcgsm"])
def tcgsm_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    if len(message.text.split()) < 2:
        bot.send_message(message.chat.id, "Lütfen bir TC numarası girin.")
        return

    cevap = "╭━━━━━━━━━━━━━╮\n┃➥ @TSGChecker\n╰━━━━━━━━━━━━━╯"
    text = message.text.split()[1]  
    api_url = f"http://172.208.52.218/api/legaliapi/tcgsm.php?tc={text}"
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
        bot.send_message(-1002017751874, log_message)  
    else:
        bot.send_message(message.chat.id, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖬ı\n╰────────────╯")




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
import os

import requests

@bot.message_handler(commands=['iban'])
def iban_sorgula(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    chat_id = message.chat.id
    user_input = message.text.split(' ', 1)

    if len(user_input) != 2:
        bot.send_message(chat_id, "Lütfen geçerli bir IBAN girin.")
        return

    iban = user_input[1]
    api_url = f'http://172.208.52.218/api/legaliapi/iban.php?iban={iban}'

    response = requests.get(api_url)

    if response.status_code == 200:
        data = response.json()
        if 'Ad' in data and 'Kod' in data:
            banka_sube = {
                'Banka Adı': data['Ad'].strip('\"'),
                'Banka Kodu': data['Kod'].strip('\"'),
                'Swift': data['Swift'].strip('\"'),
                'Hesap No': data['Hesap No'].strip('\"'),
                'Şube Adı': data['Şube Adı'].strip('\"'),  
                'Şube Kodu': data['Şube Kodu'].strip('\"'),  
                'İl': data['İl'].strip('\"'),
                'İlçe': data['İlçe'].strip('\"'),
                'Tel': data['Tel'].strip('\"'),
                'Fax': data['Fax'].strip('\"')
            }

            response_message = (
                "╭━━━━━━━━━━━━━━━╮\n"
                "┃➥ Banka ve Şube Bilgileri\n"
                f"┃➥ Banka Adı: {banka_sube['Banka Adı']}\n"
                f"┃➥ Banka Kodu: {banka_sube['Banka Kodu']}\n"
                f"┃➥ Swift: {banka_sube['Swift']}\n"
                f"┃➥ Hesap No: {banka_sube['Hesap No']}\n"
                f"┃➥ Şube Adı: {banka_sube['Şube Adı']}\n"
                f"┃➥ Şube Kodu: {banka_sube['Şube Kodu']}\n"
                f"┃➥ İl: {banka_sube['İl']}\n"
                f"┃➥ İlçe: {banka_sube['İlçe']}\n"
                f"┃➥ Tel: {banka_sube['Tel']}\n"
                f"┃➥ Fax: {banka_sube['Fax']}\n"
                "╰━━━━━━━━━━━━━━━╯"
            )

            bot.send_message(chat_id, response_message)
            log_message = (
                f"Yeni IBAN Sorgu Atıldı!\n"
                f"Sorgulanan IBAN: {iban}\n"
                f"Sorgulayan ID: {user_id}\n"
                f"Sorgulayan Adı: {user_name}\n"
                f"Sorgulayan K. Adı: @{message.from_user.username}"
            )
            bot.send_message(-1002017751874, log_message)
        else:
            bot.send_message(chat_id, "╭─────📛─────╮\n│ Sonuç Bulunamadı\n╰────────────╯")
    else:
        bot.send_message(chat_id, "Veri alınırken bir hata oluştu.")


from fake_email import Email
from rich.console import Console

user_data = {}


@bot.message_handler(commands=["mail"])
def start_handler(message):
    user_id = message.from_user.id
    email_obj = Email() 
    email_bilgisi = email_obj.Mail()  
    user_data[user_id] = {
        "eposta": email_bilgisi["mail"],
        "session": email_bilgisi["session"]
    }
    eposta = user_data[user_id]["eposta"]
    gelen_mesajlar = Email(user_data[user_id]["session"]).inbox()
    
    bilgi = f"Eposta: {eposta}\nGelen Mesajlar: {gelen_mesajlar or 'Yeni mesaj yok'}"
    bot.send_message(message.chat.id, bilgi)

    
    if gelen_mesajlar:
        bot.send_message(message.chat.id, "Yeni bir e-posta geldi!")


@bot.message_handler(commands=['refresh'])
def refresh_handler(message):
    user_id = message.from_user.id
    if user_id in user_data:
        eposta = user_data[user_id]["eposta"]
        gelen_mesajlar = Email(user_data[user_id]["session"]).inbox()
        bilgi = f"Eposta: {eposta}\nGelen Mesajlar: {gelen_mesajlar or 'Yeni mesaj yok'}"
        bot.send_message(message.chat.id, bilgi)
    else:
        bot.send_message(message.chat.id, "Önce /start komutunu kullanarak başlamalısınız.")

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

    channel_id = -1002048770700
    group_id = -1002088355655

    # is_user_member fonksiyonunu tanımlayın ve kullanıcının üyelik durumunu kontrol edin
    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return
    
    text = message.text.replace('/meme ', '')  
    url = "https://tsgmods.com.tr/oba.jpg"  

    try:
        response = requests.get(url)
        response.raise_for_status()  # Eğer istekte bir hata varsa burada hata yükseltilecek

        # BytesIO nesnesini kullanmadan doğrudan resmi PIL kütüphanesi ile açıyoruz
        image = Image.open(BytesIO(response.content))

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

        # Buffer kullanmadan doğrudan resmi göndermek mümkün değil, dolayısıyla resmi kaydedip gönderiyoruz
        buffered = BytesIO()
        blurred_image.save(buffered, format="JPEG")  # JPEG formatında kaydediyoruz, çünkü Telegram JPEG formatını daha iyi destekliyor
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: {e}")

# Botu çalıştır


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Hata: {e} ")
