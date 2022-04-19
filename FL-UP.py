import re
from requests import get,post
print("""
███████╗██╗         ██╗   ██╗██████╗ 
██╔════╝██║         ██║   ██║██╔══██╗
█████╗  ██║  █████╗ ██║   ██║██████╔╝
██╔══╝  ██║  ╚════╝ ██║   ██║██╔═══╝ 
██║     ███████╗    ╚██████╔╝██║     
╚═╝     ╚══════╝     ╚═════╝ ╚═╝     
<\> @TweakPY""")                      
print('-'*30)
file_name=input("[+] Set a File Name: ")
context=input("[+] The File Context:\n")
print('-'*30)
h={'Host': 'files.fm','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Referer': 'https://files.fm/','Te': 'trailers'}
req=get("https://files.fm/server_scripts/get_upload_id.php?show_add_key=1",headers=h).text
id=str(req.split(',')[0])
key=str(req.split(',')[2])
h2={'Host': 'free.files.fm','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': '*/*','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','X-File-Upload': 'uploadingfiles','Content-Type': 'multipart/form-data; boundary=---------------------------20104982571991613403268587895','Content-Length': '1705','Origin': 'https://files.fm','Referer': 'https://files.fm/','Te': 'trailers','Connection': 'close'}
d='''
-----------------------------20104982571991613403268587895
Content-Disposition: form-data; name="APC_UPLOAD_PROGRESS"

e536cf4b-5f15-90e2-6f74-ab9bd9ed33b6
-----------------------------20104982571991613403268587895
Content-Disposition: form-data; name="PHP_SESSION_UPLOAD_PROGRESS"

e536cf4b-5f15-90e2-6f74-ab9bd9ed33b6
-----------------------------20104982571991613403268587895
Content-Disposition: form-data; name="UPLOAD_IDENTIFIER"

e536cf4b-5f15-90e2-6f74-ab9bd9ed33b6
-----------------------------20104982571991613403268587895
Content-Disposition: form-data; name="Filedata"; filename="'''+file_name+'''"
Content-Type: application/x-desktop

'''+context+'''

-----------------------------20104982571991613403268587895
Content-Disposition: form-data; name="ModDate"

Thu Apr 14 2022 18:21:49 GMT-0400 (British Summer Time)

-----------------------------20104982571991613403268587895
Content-Disposition: form-data; name="UserAgent"

{"doNotTrack":"unspecified","maxTouchPoints":0,"oscpu":"Linux x86_64","vendor":"","vendorSub":"","productSub":"20100101","cookieEnabled":true,"buildID":"20181001000000","webdriver":false,"hardwareConcurrency":2,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (X11)","platform":"Linux x86_64","userAgent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0","product":"Gecko","language":"ar","onLine":true}
-----------------------------20104982571991613403268587895--'''
req2=post(f"https://free.files.fm/save_file.php?PHPSESSID=&up_id={id}&ignore_user_abort=1&skip_update=1&key={key}&v=1630913502868",headers=h2,data=d).text
h3={'Host': 'free.files.fm','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Origin': 'https://files.fm','Referer': 'https://files.fm/','Te': 'trailers','Connection': 'close'}
req3=get(f"https://free.files.fm/finish_upload.php?upload_hash={id}",headers=h3).text
req4=get(f'https://files.fm/u/{id}').text
if '"status":"ok"' in req3:
  date_delete=re.findall('<div class="upload_info__delete_warning">(.*?)</div>',req4)[0]
  print(f"[!] Done uploading File '{file_name}'...")
  print(f'[+] Your Link To Mange The File: https://files.fm/u/{id}')
  print('')
  print(f'[\] Your File Will Be Deleted On:\n{date_delete}')  
else:print('Talk to tool dev to solve this: ',req3)
