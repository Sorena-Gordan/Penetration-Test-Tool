import requests
import sys
import time
from colorama import Fore

list = ['robots.txt',
        'search/',
        'admin/',
        'login/',
        'sitemap.xml',
        'sitemap2.xml',
        'config.php',
        'wp-login.php',
        'log.txt',
        'update.php',
        'INSTALL.pgsql.txt',
        'user/login/',
        'INSTALL.txt',
        'profiles/',
        'scripts/',
        'LICENSE.txt',
        'CHANGELOG.txt',
        'themes/',
        'inculdes/',
        'misc/',
        'user/logout/',
        'user/register/',
        'cron.php',
        'filter/tips/',
        'comment/reply/',
        'xmlrpc.php',
        'modules/',
        'install.php',
        'MAINTAINERS.txt',
        'user/password/',
        'node/add/',
        'INSTALL.sqlite.txt',
        'UPGRADE.txt',
        'INSTALL.mysql.txt']


def __start__():
    print(Fore.RED + " [!] Plase Enter Domain")
    target = input(
        Fore.RED + " ┌─[" + Fore.LIGHTGREEN_EX + "ir.nofoz" + Fore.BLUE + "~" + Fore.WHITE + "@HOME" + Fore.RED + "/" + Fore.CYAN + "OG" + Fore.RED + "/" + Fore.LIGHTYELLOW_EX + "CMS-Detect" + Fore.RED + """]
└──╼ """ + Fore.WHITE + "卐 ")
    try:
        if "http://" in target:
            pass
        elif 'http://' != target:
            url = "http://" + target
        for i in list:
            time.sleep(0.2)
            ul = (url + "/" + i)
            result = requests.get(ul)
            if result.status_code == 200 or result.status_code == 405:
                print(Fore.GREEN + "[+]" + ul + " | " + "Found")
            else:
                print(Fore.RED + "[-]" + ul + " | " + "Notfound")
        try:
            input(Fore.GREEN + " [*] Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()
    except:
        print("")

