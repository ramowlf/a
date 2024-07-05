import os
import asyncio
from telethon import TelegramClient, events

sakso = 6958129929

asik_oldun = os.environ.get('TELEGRAM_API_ID')
sik_kafali = os.environ.get('TELEGRAM_API_HASH')
phone = os.environ.get('TELEGRAM_PHONE_NUMBER')

telethon_client = TelegramClient("telethon.session", int(asik_oldun), sik_kafali)

BotAltyapi = """**Merhaba first.**
**👩🏻‍💻Ben Sahibim'in Sekreteriyim.**
**❎Üzgünüm, Sahibim sizi onaylamamış.**
**🔃Onaylayana kadar bu mesajı tekrar tekrar atacağım.**
**✔️Yakında sizi onaylar.**
**📜Mesajınızı görmesi ve sizi onaylaması için sizi listeye alıyorum..**

`📜Listeye alma işlemi başlatıldı....`
`🗃Bilgiler alınıyor....`
`✅Bilgiler alındı....`

**👉🏻Adınız: first**
**👉🏻Kullanıcı adınız: username**

`📜Listeye alındınız.`
@BotAltyapi ve @ramowlfbio kanalına katılmayı unutma"""

pmpermit = False

BotAltyapi_ramowlf = []

@telethon_client.on(events.NewMessage)
async def dalyarak(event):
    sender = await event.get_sender()
    if event.is_private and pmpermit and sender.id != sakso:
        if event.sender_id not in BotAltyapi_ramowlf:
            me = await telethon_client.get_me()
            if sender.id != me.id:
                return await event.respond(BotAltyapi.replace("first", sender.first_name).replace("username", "@" + sender.username))

@telethon_client.on(events.NewMessage(pattern=r"\.pm"))
async def botaltyapi(event):
    global pmpermit
    sender = event.sender_id
    if sender == sakso:
        cmd = event.message.text.split()
        if len(cmd) > 1 and len(cmd) < 3:
            if cmd[1] == "on":
                pmpermit = True
                return await event.edit("Aktif")
            elif cmd[1] == "off":
                pmpermit = False
                return await event.edit("Aktif değil")
        else:
            return await event.respond("on/off bu ikisinden birini seç on aktif eder off kapatır")
    else:
        return await event.respond("oc sen ben misin")

@telethon_client.on(events.NewMessage(pattern=r"\.approve"))
async def Bot_Altyapi(event):
    global BotAltyapi_ramowlf
    sender = event.sender_id
    if sender == sakso:
        splt = event.message.text.split()
        if len(splt) > 1 and splt[1].isdigit():
            chat_id = int(splt[1])
            if chat_id not in BotAltyapi_ramowlf:
                BotAltyapi_ramowlf.append(chat_id)
                await event.edit("Onaylandı")
            else:
                await event.edit("Zaten onaylandı")
        else:
            await event.edit("Kullanım: .approve <user_id>")

@telethon_client.on(events.NewMessage(pattern=r"\.disapprove"))
async def yarrak(event):
    global BotAltyapi_ramowlf
    sender = event.sender_id
    if sender == sakso:
        splt = event.message.text.split()
        if len(splt) > 1 and splt[1].isdigit():
            chat_id = int(splt[1])
            if chat_id in BotAltyapi_ramowlf:
                BotAltyapi_ramowlf.remove(chat_id)
                await event.edit("Onay kaldırıldı")
            else:
                await event.edit("onaylı değil zaten")
        else:
            await event.edit("Kullanım: .disapprove <user_id>")

@telethon_client.on(events.NewMessage(pattern=r"\.id"))
async def oclardiyari(event):
    sender = await event.get_reply_message()
    if sender:
        await event.respond(f"karşı tarafın idsi: {sender.sender_id}")
    else:
        await event.respond("adama yanıt at")

if __name__ == "__main__":
    telethon_client.start(phone=lambda: phone)
    telethon_client.run_until_disconnected()
    
