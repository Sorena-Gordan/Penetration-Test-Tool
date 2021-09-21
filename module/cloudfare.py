import socket
import sys
import time
from colorama import Fore

def __start__():
    print(Fore.WHITE+"""
        [▶] be bakhsh bypass cloudfare khosh amadid
        
        [▶] url site target ra vared konid
    """)
    domin = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', 'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', 'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', 'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', 'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', 'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

    url_target = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"ir.nofoz"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"OG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Bypass-CloudFlare"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"→ ")
    if url_target == "":
        try:
            print(Fore.RED+" [!!] "+Fore.BLUE+"url site target ra vared konid \n")
            time.sleep(5)
            sys.exit()
        except :
            return
    for sub in domin:
        try:
            host=str(sub)+"."+str(url_target)
            result = socket.gethostbyname(str(host))
            print (Fore.GREEN+"[‼] ip :"+result+" | "+"url : "+host)
        except Exception:
            pass
    try:
        input(Fore.GREEN+" [*] Bargasht be Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()
