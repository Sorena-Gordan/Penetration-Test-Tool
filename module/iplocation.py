import sys
import ipapi
from colorama import Fore


def __start__():
    print(Fore.RED + " [!] Plase Enter IP")
    target = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "ir.nofoz" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "IG" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "CMS-Detect" + Fore.RED + """]
 └──╼ """ + Fore.WHITE + "卐 ")
    result = ipapi.location(ip=target, key=None)
    try:
        print(Fore.BLUE+"[*] ip = " + result["ip"])
        print(Fore.BLUE + "[*] city = " + result["city"])
        print(Fore.BLUE + "[*] region_code = " + result["region_code"])
        print(Fore.BLUE + "[*] timezone = " + result["timezone"])
        print(Fore.BLUE + "[*] country_calling_code = " + result["country_calling_code"])
        print(Fore.BLUE + "[*] currency_name = " + result["currency_name"])
        print(Fore.BLUE + "[*] org = " + result["org"])
        print(Fore.BLUE + "[*] postal = " + result["postal"])
        print(Fore.BLUE + "[*] languages = " + result["languages"])
        try:
            input(Fore.GREEN + " [*] Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print(Fore.RED + " [!] please enter a ip")






