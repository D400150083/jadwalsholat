#!system/bin/python
#author KANG-NEWBIE
#Open Source

import requests, json, os, sys, time
os.system('clear')
R=('\033[1;31m')
C=('\033[1;36m')
G=('\033[1;32m')
def slow(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.02)
def slow1(s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(0.1)
banner=('''%s
───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───		%sJADWAL SHOLAT%s
───█▒▒░░░░░░░░░▒▒█───
────█░░█░░░░░█░░█────	%sAuthor : KANG-NEWBIE%s
─▄▄──█░░░▀█▀░░░█──▄▄─	%sContact: t.me/kang_nuubi%s
█░░█─▀▄░░░░░░░▄▀─█░░█	%sGithub : github.com/KANG-NEWBIE%s
█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█	%sTEAM   : CRABS (t.me/CRABS_ID)%s
█░░╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗░░█
█░░║║║╠─║─║─║║║║║╠─░░█
█░░╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝░░█	"Sholatlah Kalian Sebelum
█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█	Kalian Disholatkan"
'''%(G,C,G,R,G,R,G,R,G,R,G))
print(banner)
kota=str(input('Masukan Nama Kota => '))
while True:
	try:
		r=requests.get('https://time.siswadi.com/pray/'+kota)
		js=json.loads(r.text)
		a=js['data']
		b=js['time']
		slow('''
Sekarang Tgl : {}
sekarang Jam : {}

Waktu Sholat di kota %s
	SUBUH		: {}
	SUNRISE		: {}
	DZUHUR		: {}
	ASHAR		: {}
	MAGRIB		: {}
	ISHA		: {}
	SPERTIGA MLM	: {}
	TENGAH MLM	: {}
	DUAPERTIGA MLM	: {}
'''.format(b['date'],b['time'],a['Fajr'],a['Sunrise'],a['Dhuhr'],a['Asr'],a['Maghrib'],a['Isha'],a['SepertigaMalam'],a['TengahMalam'],a['DuapertigaMalam'])%(kota))
		slow1("'dengan kembali bertaubat kepada-Nya dan bertakwalah kepada-Nya serta dirikanlah shalat dan janganlah kamu termasuk orang-orang yang mempersekutukan Allah'\n[QS. Ar-Rum [30] : 31]")
		time.sleep(7)
		os.system('clear')

	except:
		ngulang = sys.executable
		os.execl(ngulang, ngulang, *sys.argv)

