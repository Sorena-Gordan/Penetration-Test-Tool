import requests
from colorama import Fore
import time
import sys

def __start__():
    try:
        print(Fore.RED+" [!] Plase Enter Domain")
        target = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"OG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"CMS-Detect"+Fore.RED+"""]
    └──╼ """+Fore.WHITE+"卐 ")
        r = requests.get("https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey=at_GcmMQOutBKNrlIvxVotffMZXoioMA&domainName="+target+"&outputFormat=json&ipWhois=1").text
        print(Fore.BLUE+r)
    except:
        pass
    try:
        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
    except:
        print("")
