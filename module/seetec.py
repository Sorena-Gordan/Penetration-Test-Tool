import requests, builtwith
from colorama import Fore
import sys

def __start__():
    print(Fore.RED+" [!] Plase Enter Domain")
    target = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"OG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"CMS-Detect"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    if not "https://" is target or not "http://" is target:
        url = "http://" + target
    else:
        url = target
    result = builtwith.parse(url)
    for name in result:
        value = ''
        for val in result[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val) 
        print(Fore.BLUE+"\n"+name+': '+value)
    try:
        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()

