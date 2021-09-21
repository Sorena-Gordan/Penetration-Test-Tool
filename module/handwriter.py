import pywhatkit as kit
from colorama import Fore
import time
import sys

def __start__():
    print(Fore.RED + " [!] please enter your word (EXAMPLE : hello world)")
    word = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "ir.nofoz" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "other" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "whatsapp_sender" + Fore.RED + """]
    └──╼ """ + Fore.WHITE + "卐 ")
    time.sleep(0.1)
    print(Fore.BLUE + "please wait...")
    kit.text_to_handwriting(word,rgb=(0,0,255))
    time.sleep(0.1)
    print(Fore.BLUE + "finish :)")
    try:
        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
    except:
        print("")