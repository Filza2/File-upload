from requests import post
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
    try:r=post("https://api.anonfiles.com/upload",files={'file':open(input("- The File Name : "),"rb")});header()
    except FileNotFoundError:exit('- File Not Found ! \n')
    if "full" in r.text and 'short' in r.text and 'id' in r.text:print(f'- Done successfully, Your File at : {r.json()["data"]["file"]["url"]["short"]}\n')
    elif 'error' in r.text:
        try:exit(f"- Error, {r.json()['error']['message']}\n")
        except Exception as e:exit("- Error !\n")
    else:exit("- Error !\n")
    
    
    

header();File_uploader()
