import socket , requests
import sys
import time
from colorama import Fore

def __start__():
    print(Fore.RED+" [!] Plase Enter Domain")
    target = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"OG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"CMS-Detect"+Fore.RED+"""]
└──╼ """+Fore.WHITE+"卐 ")
    result = requests.get("https://www.whoisxmlapi.com/whoisserver/DNSService?apiKey=at_GcmMQOutBKNrlIvxVotffMZXoioMA&domainName="+target+"&type=_all&outputFormat=json").text
    print(Fore.BLUE+str(result))
    try:
        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()
