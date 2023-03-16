from requests import post
from uuid import uuid4
import os
def header():
    os.system("cls" if os.name=='nt' else "clear");print("""
███████╗██╗██╗     ███████╗    ██╗   ██╗██████╗ ██╗      ██████╗  █████╗ ██████╗ 
██╔════╝██║██║     ██╔════╝    ██║   ██║██╔══██╗██║     ██╔═══██╗██╔══██╗██╔══██╗
█████╗  ██║██║     █████╗█████╗██║   ██║██████╔╝██║     ██║   ██║███████║██║  ██║
██╔══╝  ██║██║     ██╔══╝╚════╝██║   ██║██╔═══╝ ██║     ██║   ██║██╔══██║██║  ██║
██║     ██║███████╗███████╗    ╚██████╔╝██║     ███████╗╚██████╔╝██║  ██║██████╔╝
╚═╝     ╚═╝╚══════╝╚══════╝     ╚═════╝ ╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝ 
                                                                                  
                            By @TweakPY - @vv1ck
""")
def File_uploader():
    content_file=input("- The File Name : ")
    file_name=uuid4()
    try:file_content=open(content_file,'r').read()
    except FileNotFoundError:exit('- File Not Found ! ')
    d=f'''-----------------------------240332332236763587692188904424
Content-Disposition: form-data; name="file"; filename="{file_name}"
Content-Type: application/octet-stream

{file_content}
-----------------------------240332332236763587692188904424--'''
    r=post('https://ttm.sh/',headers={'Host': 'ttm.sh','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8','Accept-Language': 'ar,en-US;q=0.7,en;q=0.3','Accept-Encoding': 'gzip, deflate','Content-Type': 'multipart/form-data; boundary=---------------------------240332332236763587692188904424'},data=d)
    if "https://ttm.sh/" in r.text:header();print(f"- Done successfully, Your File at : {r.text}")
    else:header();exit("- Error ! ")#print(r.text)
    
header();File_uploader()
