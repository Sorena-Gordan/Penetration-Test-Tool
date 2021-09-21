from module.helpf import help
import os
import sys
import time
from module import brotforce,DNSlookup,finder,handwriter,iplocation,revirceadress,scanner,seetec,sendwhatsapp,verifyemail,whois,wordpress,cloudfare



try :
    from colorama import Fore
except :
    print(" [Erorr] pakage color bayad nasb shavad")
    os.system("pip install colorama")
#------------------------------------------------
try :
    import requests
except :
    print(" [Erorr] pakage requests bayad nasb shavad")
    os.system("pip install requests")
#--------------------------------------------------
try :
    import builtwith
except :
    print(" [Erorr] pakage builwith bayad nasb shavad")
    os.system("pip install builtwith")
#---------------------------------------------------------------------------------
while True:
    try:
        help.info1()
        number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"→ ").lower()
    except:
        print("\n God Lock :) ")
        sys.exit()
        ############################
    if number == '5':
        print
        sys.exit()
        ############################
    elif number == "":
        print(Fore.RED+" [!]"+Fore.BLUE+" Please Enter Number :))))")
        input("")
        time.sleep(3)
        sys.exit()
        ############################
    elif number == "3":
        help.develioper()
        ############################
    #------------------------------------------------------------------------------
    #OG
    elif number == "1":
        try:
            help.info2()
            infor = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@OG"+Fore.RED+"""]
            └──╼ """+Fore.WHITE+"→ ").lower()
            if infor == "1":
                help.banner()
                cloudfare.__start__()
            elif infor == "2":
                help.banner()
                seetec.__start__()
            elif infor == "3":
                help.banner()
                scanner.__start__()
            elif infor == "4":
                help.banner()
                iplocation.__start__()
            elif infor == "5":
                help.banner()
                whois.__start__()
            elif infor == "6":
                help.banner()
                DNSlookup.__start__()
            elif infor == "7":
                help.banner()
                brotforce.__start__()
            elif infor == "8":
                help.banner()
                finder.__start__()
            elif infor == "9":
                input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
            elif infor == "10":
                sys.exit()
        except KeyboardInterrupt:
            print("")
            sys.exit()
#-----------------------------------------------------------------------
    elif number == "2" :
        try:
            help.infolist4()
            numcms = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@CPT"+Fore.RED+"""]
            └──╼ """+Fore.WHITE+"→ ").lower()
            if numcms == "1":
                help.wp()
                try:
                    numwp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@CPT"+Fore.RED+"""]
            └──╼ """+Fore.WHITE+"→ ").lower()
                except:      
                    print("")
                    sys.exit()
                if numwp == "1" :
                    help.banner() 
                    wordpress.wpplug()
                elif numwp == "2":
                    help.banner()
                    wordpress.user()
                elif numwp == "3":
                    try:
                        help.banner()
                        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
                    except :
                        print("")
                        sys.exit()                    
        except:
            print("")
            sys.exit()
#-------------------------------------------------------------------------------
    elif number == "4":
        try:
            help.other()
            ot = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@CPT"+Fore.RED+"""]
            └──╼ """+Fore.WHITE+"→ ").lower()
            if ot == "1":
                help.banner()
                handwriter.__start__()
            elif ot == "2":
                help.banner()
                verifyemail.__start__()
            elif ot == "3":
                help.banner()
                sendwhatsapp.__start__()
            elif ot == "4":
                try:
                    help.banner()
                    input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")
                except :
                    print("")
                    sys.exit()   
        except :
            print("")
            sys.exit()
    elif numcms == None or False:
        input(Fore.RED+" [!] "+Fore.GREEN+"Back To Menu (Press Enter...) ")





    


    

    
