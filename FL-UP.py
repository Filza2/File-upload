import requests,re
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
h={'Host': 'files.fm','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','X-Requested-With': 'XMLHttpRequest','Referer': 'https://files.fm/','Te': 'trailers',}
req=requests.get("https://files.fm/server_scripts/get_upload_id.php?show_add_key=1",headers=h).text
id=str(req.split(',')[0])
key=str(req.split(',')[2])
h2={'Host': 'free.files.fm','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','X-File-Upload': 'uploadingfiles','Content-Type': 'multipart/form-data; boundary=---------------------------2064228528415751481379601863','Content-Length': '2668','Origin': 'https://files.fm','Referer': 'https://files.fm/','Te': 'trailers','Connection': 'close'}
d='''-----------------------------2064228528415751481379601863
Content-Disposition: form-data; name="APC_UPLOAD_PROGRESS"

6c2005da-e8fa-b2ae-8707-a5b7c5613900
-----------------------------2064228528415751481379601863
Content-Disposition: form-data; name="PHP_SESSION_UPLOAD_PROGRESS"

6c2005da-e8fa-b2ae-8707-a5b7c5613900
-----------------------------2064228528415751481379601863
Content-Disposition: form-data; name="UPLOAD_IDENTIFIER"

6c2005da-e8fa-b2ae-8707-a5b7c5613900
-----------------------------2064228528415751481379601863
Content-Disposition: form-data; name="Filedata"; filename="'''+f"{file_name}"+'''"
Content-Type: text/x-python

'''+f"{context}"+'''

-----------------------------2064228528415751481379601863
Content-Disposition: form-data; name="ModDate"

Sun Sep 05 2021 05:12:38 GMT+0100 (British Summer Time)
-----------------------------2064228528415751481379601863
Content-Disposition: form-data; name="UserAgent"

{"doNotTrack":"unspecified","maxTouchPoints":0,"oscpu":"Linux x86_64","vendor":"","vendorSub":"","productSub":"20100101","cookieEnabled":true,"buildID":"20181001000000","webdriver":false,"hardwareConcurrency":2,"appCodeName":"Mozilla","appName":"Netscape","appVersion":"5.0 (X11)","platform":"Linux x86_64","userAgent":"Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0","product":"Gecko","language":"en-US","onLine":true}
-----------------------------2064228528415751481379601863--'''
req2=requests.post(f"https://free.files.fm/save_file.php?PHPSESSID=&up_id={id}&ignore_user_abort=1&skip_update=1&key={key}&v=1630913502868",headers=h2,data=d).text
h3={'Host': 'free.files.fm','User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0','Accept': 'application/json, text/javascript, */*; q=0.01','Accept-Language': 'en-US,en;q=0.5','Accept-Encoding': 'gzip, deflate','Origin': 'https://files.fm','Referer': 'https://files.fm/','Te': 'trailers','Connection': 'close'}
req3=requests.get(f"https://free.files.fm/finish_upload.php?upload_hash={id}",headers=h3).text
req4=requests.get(f'https://files.fm/u/{id}').text
date_delete=re.findall('<div id="upload_info__delete_warning">Will be deleted: (.*?)</div>',req4)[0]
print("[!] Done UPLOAD...")
print(f'[+] Your Link To Mange The File: https://files.fm/u/{id}')
print('')
print(f'[\] Your File Will Be Deleted On:\n{date_delete}')
