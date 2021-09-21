import requests
import sys
import time
from colorama import Fore
import json

def __start__():
    print(Fore.RED+" [!] Plase Enter Domain")
    target = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"OG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"CMS-Detect"+Fore.RED+"""]
└──╼ """+Fore.WHITE+"卐 ")
    remote={"remoteAddress" : target}
    result = requests.post("https://domains.yougetsignal.com/domains.php",remote)
    
    result_ = json.loads(result.content)

    for data in result_["domainArray"]:
        print(" "+data[0]+"\n")
    try:
        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()
