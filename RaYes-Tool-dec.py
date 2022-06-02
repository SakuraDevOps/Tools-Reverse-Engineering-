#DECOMPILE BY: SakuraDevOps
import os, sys, time, mechanize, itertools, datetime, random, hashlib, re, threading, json, getpass, urllib, cookielib, requests
from multiprocessing.pool import ThreadPool
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m'
O = '\x1b[1;96m'
my_color = [
 P, M, H, K, B, U, O]
 
warna = random.choice(my_color)
warni = random.choice(my_color)
ip = requests.get('https://api.ipify.org').text.strip()
loc = requests.get('https://ipapi.com/ip_api.php?ip=' + ip, headers = {
    'Referer': 'https://ip-api.com/',
    'Content-Type': 'application/json; charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36' }).json()['country_name'].upper()
def pkgs():
    uuid = str(os.geteuid()) + str(os.getlogin())
    id = ('-').join(uuid)
    print logo
    print '\x1b[37;1mYour ID : ' + id
    try:
        httpCaht = requests.get('https://github.com/KhalidH3cker2977/RaYes-Tool/blob/main/public.txt').text
        if id in httpCaht:
            print '\x1b[37;1mYOUR ID IS ACTIVE.........'
            msg = str(os.geteuid())
            time.sleep(1)
        else:
            print '\x1b[37;1mYOUR ID IS NOT ACTIVE.........'
            print '\x1b[37;1m Send Your Id To Admin.........'
            time.sleep(1)
            sys.exit()
        try:
            open('.login.txt', 'r')
            b_menu()
        except IOError:
            animate()

    except:
        sys.exit()
        if name == '__main__':
            pkgs()


try:
    import mechanize
except ImportError:
    os.system('pip2 install mechanize')

try:
    import requests
except ImportError:
    os.system('pip2 install requests')
    os.system('python2 Cloning.py')

from requests.exceptions import ConnectionError
from mechanize import Browser
from datetime import datetime
reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]
os.system('clear')
done = False

def animate():
    for c in itertools.cycle(['\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa110%', '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa120%', '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa130%', '\x1b[1;94m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa140%', '\x1b[1;95m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa150%', '\x1b[1;96m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa160%', '\x1b[1;97m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa170%', '\x1b[1;92m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa180%', '\x1b[1;93m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa1\xe2\x96\xa190%', '\x1b[1;91m\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x96\xa0\xe2\x88\x9a100%']):
        if done:
            break
        sys.stdout.write('\r\x1b[1;93mLoading ' + c)
        sys.stdout.flush()
        time.sleep(0.25)


t = threading.Thread(target=animate)
t.start()
time.sleep(2.5)
done = True

def keluar():
    print '\x1b[1;97m{\x1b[1;91m!\x1b[1;97m} Back'
    os.sys.exit()


def acak(x):
    w = 'mhkbpcP'
    d = ''
    for i in x:
        d += '!' + w[random.randint(0, len(w) - 1)] + i

    return cetak(d)


def cetak(x):
    w = 'mhkbpcP'
    for i in w:
        j = w.index(i)
        x = x.replace('!%s' % i, '%s;' % str(31 + j))

    x += ''
    x = x.replace('!0', '')
    sys.stdout.write(x + '\n')


def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(1e-05)


logo = ''
logoa1 = '\x1b[1;96m $$$$$$$$\\                                                    \n\\__$$  __|                                                   \n   $$ | $$$$$$\\   $$$$$$\\  $$$$$$\\$$$$\\  $$\\   $$\\ $$\\   $$\\ \n   $$ |$$  __$$\\ $$  __$$\\ $$  _$$  _$$\\ $$ |  $$ |\\$$\\ $$  |\n   $$ |$$$$$$$$ |$$ |  \\__|$$ / $$ / $$ |$$ |  $$ | \\$$$$  / \n   $$ |$$   ____|$$ |      $$ | $$ | $$ |$$ |  $$ | $$  $$<  \n   $$ |\\$$$$$$$\\ $$ |      $$ | $$ | $$ |\\$$$$$$  |$$  /\\$$\\ \n   \\__| \\_______|\\__|      \\__| \\__| \\__| \\______/ \\__/  \\__|\n                                                             \n                                                                             \n$$$\\    $$$ |                      $$ |                        \n$$$$\\  $$$$ | $$$$$$\\   $$$$$$$\\ $$$$$$\\    $$$$$$\\   $$$$$$\\  \n$$\\$$\\$$ $$ | \\____$$\\ $$  _____|\\_$$  _|  $$  __$$\\ $$  __$$\\ \n$$ \\$$$  $$ | $$$$$$$ |\\$$$$$$\\    $$ |    $$$$$$$$ |$$ |  \\__|\n$$ |\\$  /$$ |$$  __$$ | \\____$$\\   $$ |$$\\ $$   ____|$$ |      \n$$ | \\_/ $$ |\\$$$$$$$ |$$$$$$$  |  \\$$$$  |\\$$$$$$$\\ $$ |      \n\\__|     \\__| \\_______|\\_______/    \\____/  \\_______|\\__|  \n    \n           \xe2\x80\xa2\t\x1b[1;93m[\x1b[1;97m\x1b[1;43mRaYes Khalid \x1b[0m\x1b[1;93m]\n  \x1b[0m\x1b[1;93m\n\x1b[1;97m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2                             \n\x1b[1;91m\xe2\x9e\xa3 \x1b[1;92mAuthor   :   RaYes Khalid \n\x1b[1;91m\xe2\x9e\xa3 \x1b[1;92mGithub   :   https://github.com/KhalidH3cker2977 \n\x1b[1;91m\xe2\x9e\xa3 \x1b[1;92mVersion  :   0.1 RaYes Tool \x1b[0m\x1b[1;93m\n\x1b[1;97m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
Y = '\x1b[1;93m'
B = '\x1b[1;94m'
P = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'

def clear():
    os.system('clear')


def t():
    time.sleep(1)


def t1():
    time.sleep(0.01)


def love(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        t1()


def menu():
    os.system('clear')
    pkgs()
    os.system('clear')
    print logoa1
    os.system('clear')
    print '\n\033[1;94mYour Country :' +loc
    print '\n\033[1;95mYour IP : ' + ip
    os.system('echo -e "\n\n \n\x1b[1;91m\xe2\x9e\xa3 \x1b[1;92mAuthor   :   RaYes Khalid \n\x1b[1;91m\xe2\x9e\xa3 \x1b[1;92mGithub   :   https://github.com/KhalidH3cker2977 \n\x1b[1;91m\xe2\x9e\xa3 \x1b[1;92mVersion  :   0.1 RaYes Tool \x1b[0m\x1b[1;93m\n\x1b[1;97m\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2\xe2\x80\xa2" | lolcat ')
    os.system('echo  ------ My Best Friend is King Sharif-------\xe2\x97\x8f&&date  | lolcat -a -F 0.1')
    os.system('echo ----------------RaYes Khalid-----------------\xe2\x97\x8f| lolcat')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x97\xa2\xe2\x96\x87\xe2\x97\xa3\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88  RaYes| lolcat --animate')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88       khalid| lolcat --animate')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88| lolcat')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x96\x87\xe2\x96\x87\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88  Friends| lolcat --animate')
    os.system('echo  \xe2\x94\x88\xe2\x94\x88-\xcc\xb4\xcd\x97\xcd\x91\xcd\x8c\xcc\x83\xcd\x98\xcc\xbf\xcd\x97\xcc\x88\xcc\xbf\xcc\xbf\xcc\x8f\xcd\x97\xcc\x91\xcd\x80\xcd\x80\xcc\xac\xcd\x96\xcd\x87\xcc\x9f\xcc\x9f\xcc\xbc\xcc\xb1\xcd\x99\xcc\xa0\xcd\x89\xcc\x9f\xcc\xb9\xcc\x98\xcc\x96\xcc\xa5\xcd\x88\xcd\x96\xcc\xa7\xcd\x9a\xcc\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88-\xcc\xb4\xcd\x97\xcd\x91\xcd\x8c\xcc\x83\xcd\x98\xcc\xbf\xcd\x97\xcc\x88\xcc\xbf\xcc\xbf\xcc\x8f\xcd\x97\xcc\x91\xcd\x80\xcd\x80\xcc\xac\xcd\x96\xcd\x87\xcc\x9f\xcc\x9f\xcc\xbc\xcc\xb1\xcd\x99\xcc\xa0\xcd\x89\xcc\x9f\xcc\xb9\xcc\x98\xcc\x96\xcc\xa5\xcd\x88\xcd\x96\xcc\xa7\xcd\x9a\xcc\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88-\xcc\xb4\xcd\x97\xcd\x91\xcd\x8c\xcc\x83\xcd\x98\xcc\xbf\xcd\x97\xcc\x88\xcc\xbf\xcc\xbf\xcc\x8f\xcd\x97\xcc\x91\xcd\x80\xcd\x80\xcc\xac\xcd\x96\xcd\x87\xcc\x9f\xcc\x9f\xcc\xbc\xcc\xb1\xcd\x99\xcc\xa0\xcd\x89\xcc\x9f\xcc\xb9\xcc\x98\xcc\x96\xcc\xa5\xcd\x88\xcd\x96\xcc\xa7\xcd\x9a\xcc\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x97\xa5\xe2\x97\xa4\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88-\xcc\xb4\xcd\x97\xcd\x91\xcd\x8c\xcc\x83\xcd\x98\xcc\xbf\xcd\x97\xcc\x88\xcc\xbf\xcc\xbf\xcc\x8f\xcd\x97\xcc\x91\xcd\x80\xcd\x80\xcc\xac\xcd\x96\xcd\x87\xcc\x9f\xcc\x9f\xcc\xbc\xcc\xb1\xcd\x99\xcc\xa0\xcd\x89\xcc\x9f\xcc\xb9\xcc\x98\xcc\x96\xcc\xa5\xcd\x88\xcd\x96\xcc\xa7\xcd\x9a\xcc\xaf\xe2\x94\x88\xe2\x94\x88\xe2\x94\x88     Hack| lolcat --animate')
    os.system('echo -----------------RaYes Khalid----------------\xe2\x97\x8f| lolcat --animate')
    os.system('echo ---  To return to this menu from any Tool---\xe2\x97\x8f| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo -------- Stop Process Press. CTRL + z -----\xe2\x97\x8f| lolcat --animate')
    time.sleep(0.0005)
    os.system('echo ---------- Friends Hacking Team --------\xe2\x97\x8f| lolcat --animate')
    os.system('echo -----------------RaYes-Tools------------------\xe2\x97\x8f| lolcat --animate')
    time.sleep(0.0005)

    os.system('echo -e " [01] Afghanistan FB Cloning Commands V 0.1----\xe2\x97\x8f\n [02] Pakistan FB Cloning    Commands V 0.1----\xe2\x97\x8f\n [03] Bangladish FB Clonig Commands -----------\xe2\x97\x8f\n [04] (8)  Countries FB Cloning Commands-------\xe2\x97\x8f\n [05] Rang  FaceBook  Cloning  Commands--------\xe2\x97\x8f\n [06] Afghanistan FB Cloning Commands V 0.2----\xe2\x97\x8f\n [07] (30) Countries FB Cloning Commands-------\xe2\x97\x8f\n [08] Afghanistan FB Cloning Commands V 0.3----\xe2\x97\x8f\n [09] Afghanistan FB Cloning Commands V 0.4----\xe2\x97\x8f\n [10] Afghanistan FB Cloning Commands V 0.5----\xe2\x97\x8f\n [11] All Countries Cloning Commands  V 0.1----\xe2\x97\x8f\n [12] All Countries Cloning Commands  V 0.2----\xe2\x97\x8f\n [13] Pakistan FB Cloning Commands V 0.2-------\xe2\x97\x8f\n [14] Pakistan FB Cloning Commands V 0.3-------\xe2\x97\x8f\n [15] Pakistan FB Cloning Commands V 0.4-------\xe2\x97\x8f\n [16] India FB Cloning Commands    V 0.1-------\xe2\x97\x8f\n [17] Afghanistan FB Cloning Commands V 0.6----\xe2\x97\x8f\n [18] OLD ID Cloning Commands------------------\xe2\x97\x8f\n [19] Pakistan FB Cloning Commands V 0.5-------\xe2\x97\x8f\n [20] Followers File Cloning Commands----------\xe2\x97\x8f\n [21] Extract File For Followers Cloning-------\xe2\x97\x8f\n [22] Update RaYes Tool------------------------\xe2\x97\x8f\n [23] Exit RaYes Tool--------------------------\xe2\x97\x8f" | lolcat ')
    friends()


def friends():
    Rayes = raw_input('\x1b[1;91m  \xe2\x94\xba\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\x1b[1;97m\xe2\x94\x80\xe2\x94\x80\x1b[1;96m\xe2\x94\x80\xe2\x94\x80\x1b[1;95m\xe2\x94\x80\xe2\x94\x80\x1b[1;94m\xe2\x94\x80\xe2\x94\x80\x1b[1;92m\xe2\x94\x80\xe2\x94\x80\x1b[1;96m\xe2\x94\x80\xe2\x94\x80\xe2\x94\x81\x1b[1;93m\xe2\x9e\xa2\x1b[1;92m\xe2\x9e\xa3\x1b[1;91m\xe2\x9e\xa4\xe2\x9e\xa4\xe2\x9e\xa4\xe2\x9e\xa4\xe2\x9e\xa4')
    if Rayes == '  ':
        print ' Plz type write code '
        friends()
    elif Rayes == '1' or Rayes == '01':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Extantion')
        love('\x1b[1;93mTool User Name :\x1b[1;95m     afg ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     cloner ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/afg-cloner')
        os.system('cd $HOME/afg-cloner && python2 afgcrack.py')
    elif Rayes == '02' or Rayes == '2':
        clear()
        print logoa1
        os.system('rm -rf $HOME/RayesfriendsTool')
        love('\x1b[1;93mTool User Name :\x1b[1;95m    pak  ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m    cloner ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/pak-crack')
        os.system('cd $HOME/pak-crack && python2 pakcrack.py')
    elif Rayes == '3' or Rayes == '03':
        clear()
        print logoa1
        os.system('rm -rf $HOME/DdosAttack')
        love('\x1b[1;93mTool Password  :\x1b[1;95m    bangla ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/bangla')
        os.system('cd $HOME/bangla && python2 bangla.py')
    elif Rayes == '04' or Rayes == '4':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Rayesfriends-Server/')
        love('\x1b[1;93mTool Password  :\x1b[1;95m    8clone ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/Fast-clone')
        os.system('cd $HOME/Fast-clone && python2 fastclone.py')
    elif Rayes == '5' or Rayes == '05':
        clear()
        print logoa1
        os.system('rm -rf $HOME/CameraHack/')
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/sking')
        os.system('cd $HOME/sking && python2 Sking.py')
    elif Rayes == '6' or Rayes == '06':
        clear()
        print logoa1
        os.system('rm -rf $HOME/RayesfriendsA')
        love('\x1b[1;93mTool User Name :\x1b[1;95m   Rayes ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m   khalid ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/Afg-cracker')
        os.system('cd $HOME/Afg-cracker && python2 crack.py')
    elif Rayes == '7' or Rayes == '07':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Phishing')
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/allcountry')
        os.system('cd $HOME/allcountry && python2 country.py')
    elif Rayes == '8' or Rayes == '08':
        clear()
        print logoa1
        os.system('rm -rf $HOME/random')
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/fast-afg')
        os.system('cd $HOME/fast-afg && python2 Fast-afg.py')
    elif Rayes == '9' or Rayes == '09':
        clear()
        print logoa1
        os.system('rm -rf $HOME/email')
        love('\x1b[1;93mTool User Name :\x1b[1;95m     Friends ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     Hack ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/Afghan')
        os.system('cd $HOME/Afghan && python2 Crackafg.py')
    elif Rayes == '10' or Rayes == '10':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Password')
        love('\x1b[1;93mTool User Name :\x1b[1;95m     Afg ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     crack ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/Ask')
        os.system('cd $HOME/Ask && python2 Afgcr3k.py')
    elif Rayes == '11' or Rayes == 'd':
        clear()
        print logoa1
        os.system('rm -rf $HOME/lovehack')
        love('\x1b[1;93mTool User Name :\x1b[1;95m     Rayes ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     khalid ')
        time.sleep (5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/pro-tool')
        os.system('cd $HOME/pro-tool && python2 pro-tool.py')
    elif Rayes == '12' or Rayes == 'e':
        clear()
        print logoa1
        os.system('rm -rf $HOME/402')
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/pro-cloner')
        os.system('cd $HOME/pro-cloner && python2  pro-cloner.py')
    elif Rayes == '13' or Rayes == 'f':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Rayeshole')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     paktool ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/pak-tool')
        os.system('cd $HOME/pak-tool && python2 pak-tool.py')
    elif Rayes == '14' or Rayes == 'g':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Spider')
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/pakistan-V1')
        os.system('cd $HOME/pakistan-V1 && python2 pakistan.py')
    elif Rayes == '15' or Rayes == 'h':
        clear()
        print logoa1
        os.system('rm -rf $HOME/KaliIndia')
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/pakistan-V2')
        os.system('cd $HOME/pakistan-V2 && python2 pakistan-v2.py')
    elif Rayes == '16' or Rayes == 'i':
        clear()
        print logoa1
        os.system('rm -rf $HOME/RayesHat')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/India-V2')
        os.system('cd $HOME/India-V2 && python2 india-v1.py')
    elif Rayes == '17' or Rayes == 'j':
        clear()
        print logoa1
        os.system('rm -rf $HOME/RedMoonNew')
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/allsim')
        os.system('cd $HOME/allsim && python2 allsim.py')
    elif Rayes == '18' or Rayes == 'k':
        clear()
        print logoa1
        os.system('rm -rf $HOME/lov3Hak3r')
        love('\x1b[1;93mTool User Name :\x1b[1;95m     OLD ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     CLONE ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/old')
        os.system('cd $HOME/old && python2 lovehacker.py')
    elif Rayes == '19' or Rayes == 'l':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Cobra')
        love('\x1b[1;93mTool User Name :\x1b[1;95m     pakistan ')
        love('\x1b[1;93mTool Password  :\x1b[1;95m     clone ')
        time.sleep(5)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/pakistan-V3')
        os.system('cd $HOME/pakistan-V3 && python2 pakistan-v3.py')
    elif Rayes == '20' or Rayes == 'm':
        clear()
        print logoa1
        os.system('rm -rf $HOME/Dragon')
        
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/Followers_Clone')
        os.system('cd $HOME/Followers_Clone && python2 Followers_clone.py')
    elif Rayes == '21' or Rayes == 'n':
        clear()
        print logoa1
        os.system('rm -rf $HOME/NetHunting')
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/Followers_Clone')
        os.system('cd $HOME/Followers_Clone && python2 extract_file.py')
    elif Rayes == '22' or Rayes == 'y':
        clear()
        print logoa1
        os.system('rm -rf $HOME/RaYes-Tool')
        love('\x1b[1;96mTurn on Mobile Date And Wait . RaYes Tool Updating automaticly')
        time.sleep(3)
        os.system('cd $HOME && git clone https://github.com/KhalidH3cker2977/RaYes-Tool')
        os.system('cd $HOME/RaYes-Tool && RaYes-Tool.py')
    elif Rayes == '23' or Rayes == 'z':
        print logoa1
        os.system('exit')


if __name__ == '__main__':
    menu()

