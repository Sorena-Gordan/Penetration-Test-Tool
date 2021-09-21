import requests
from colorama import Fore
import sys
import time

def __start__():
    try:
        print(Fore.RED+" [!] Plase Enter email")
        target = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"OG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"CMS-Detect"+Fore.RED+"""]
    └──╼ """+Fore.WHITE+"卐 ")
        r = requests.get("https://emailverification.whoisxmlapi.com/api/v1?apiKey=at_GcmMQOutBKNrlIvxVotffMZXoioMA&emailAddress="+target+"&outputFormat=json")
        if r.status_code == 200:
            print(Fore.BLUE + "[!] Email is Found ")
    except :
        print("Exit...")
        time.sleep(1)
        sys.exit()
    try:
        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()
