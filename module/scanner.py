import requests
from colorama import Fore
import time
import sys


def __start__():
    print(Fore.RED + " [!] Plase ip/Domin")
    target = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "ir.nofoz" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "OG" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "CMS-Detect" + Fore.RED + """]
└──╼ """ + Fore.WHITE + "卐 ")
    r = requests.get('https://hackertarget.com/nmap/?q=' + target)
    print(Fore.BLUE + str(r))
    try:
        input(Fore.GREEN+" [*] Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()

