import pywhatkit as kit
from colorama import Fore
import time
import sys

def __start__():
    print(Fore.RED + " [!] please enter a your number")
    print(Fore.RED + " [!] please dont input your number 0")
    number = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "ir.nofoz" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "other" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "whatsapp_sender" + Fore.RED + """]
    └──╼ """ + Fore.WHITE + "卐 ")
    print(Fore.RED + " [!] please enter a pm")
    pm = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "ir.nofoz" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "other" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "whatsapp_sender" + Fore.RED + """]
    └──╼ """ + Fore.WHITE + "卐 ")
    kit.sendwhatmsg("+98" + str(number) , pm , time_hour=0,time_min=1)
    try:
        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
    except:
        print("")
