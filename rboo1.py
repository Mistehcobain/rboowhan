# rboowhan
# codink utf-8
import sys
import os
import getpass
import re
import random

os.system("clear")

print ("\033[0;36m================JORME===============")
print ("FUTUMENTAL       [+]      ANTIMEANSTREAM")
print ("\033[0;37m_________///______///______///_____///")
print ("[+] Author : Gusti Restu Firmansyah")
print ("")
print ("[+] Tools : Jorme in the jarvis")
print ("")
print ("\033[0;36m================\-\033[0;31m●\033[0;36m-/===============")
print ("DARK NIGHT       [+]      Rboo1_LC2")
print ("\033[0;37m_________///______///______///_____///")
print ("\033[0;37m[\033[0;37m+\033[0;37m] Script : Advanced Technology")
print ("")
print ("[+] Tools : Jorme in the netherland")
print ("________________________________________________")
print ("")
	
sapaan = ["iyah hai juga", "iyah halo gimana baik-baik ajakan", "iyah halo juga"]

nama_program = ["owh hehhe namaku jorme, aku sebuah pemograman ai", "owh namaku jorme", "hai perkenalkan namaku jorme", "aku sebuah robot yang sudah dirancang"]

jenis = ["iyah aku sebuah robot ai", "hehhehe iyah aku sebuah maklhuk yang diprogram", "iyah aku program yang dibuat dan diberi jiwa hehhehehe", "aku ai yang diberi perasaan sama kayak kamu"]

balas_iya = ["iyah", "hehhe iya", "Oke"]

tempat_jorme = ["owh hehhe aku tinggalnya di hatimu", "rumah aku disini di layar hehe..", "aku sebuah program jadi aku tinggal dimana aja, tempatnya doraemon bisa"]

funy_moments = ["hahaha", "Wkwkwk", "wkwkwk", "hohhoho"]

panggilan = ["owh iyah ada apa", "iyah ada apa bang", "owh iyah ada apa, maaf lagi berak dalam layar"]

makanan_favorit = ["makanan favorit aku kari ayam sama kari sapi", "hehhe makanan favorit aku asal enak kok", "aku suka semua makanan asal enak", "apalagi ayam rica"]

balas_owh = ["Sip", "Iyah begitulah", "Terimakasih mau ngobrol sama aku ><)"]

keluar = ["baik tuan kembali lagi nanti ya >_<", "baik jangan lama-lama keluarnya tuan", "semoga tuan sehat selalu, serta dipanjangkan umurnya"]
while True:
	x = (input("User\t:"))
	io = x
	if re.findall(r"hai|halo", x):
		print ("Bot\t:", random.choice(sapaan))
		
	elif re.findall(r"nama kamu siapa|siapa nama kamu|nama kamu|kamu siapa|siapa kamu", x):
		print ("Bot\t:", random.choice(nama_program))
		
	elif re.findall(r"kamu robotkah|kamu sebuah pemogramankah|apakah kamu robot|apakah kamu sebuah pemograman|apakah kamu sebuah ai|kamu ai|kamu pemograman|kamu robot|kamu pemograman", x):
		print ("Bot\t:", random.choice(jenis))
		
	elif re.findall(r"iyah|iya|iyah jorme|Iya|Iyah|Ya|ya|Iyah jorme|iyah jorme|iya jorme|Iya jorme", x):
		print ("Bot\t:",random.choice(balas_iya))
		
	elif re.findall(r"kamu tinggal dimana|dimana kamu tinggal|tinggal dimana kamu|rumah kamu dimana|kamu rumahnya dimana|dimana rumah kamu|dimana tempat tinggalmu|tempat tinggalmu dimana|kamu rumahnya dimana|kamu tinggalnya dimana", x):
		print ("Bot\t:", random.choice(tempat_jorme))
		
	elif re.findall(r"Hahaha|hahaha|Wkwkwk|wkwkwk|hahhaha|hahahha|Hahhaha|hahaha|wkwkwk|kamu lucu jorme|Kamu lucu jorme", x):
		print ("Bot\t:", random.choice(funy_moments))
		
	elif re.findall(r"jorme|Jorme|bro|Bro|bang|Bang|mas|Mas|bre|Bre|tes|Tes", x):
		print ("Bot\t:", random.choice(panggilan))
		
	elif re.findall(r"kamu suka makan apa jorme|makanan kesukaan kamu apa jorme|kamu suka makan apa|makanan kesukaan kamu apa|Kamu suka makan apa|Makanan kesukaan kamu apa|makanan favorit kamu apa|Makanan favorit kamu apa|makanan favorit apa", x):
		print ("Bot\t:", random.choice(makanan_favorit))
		
	elif re.findall(r"owh|oh|oke|Oke|okey|Okey|Oh|oh", x):
		print ("Bot\t:", random.choice(balas_owh))
		
	elif re.findall(r"aku keluar dulu|Aku pamit dulu|aku pamit dulu|Aku mau keluar dulu|pergi dulu|Aku pergi dulu|jorme aku pergi dulu ya|Jorme aku pergi dulu ya|jorme aku pergi dulu|jorme aku keluar|aku keluar dulu jorme|Aku keluar dulu jorme|Aku pergi dulu jorme|aku pergi dulu jorme|aku keluar jorme|Aku keluar jorme", x):
		print ("Bot\t:",random.choice(keluar))
		
	else:
		tanya = (input("Bot\t: siapa nama kamu ?"))
		print ("Bot\t: owh hai", tanya,"salam kenal aku ya")
	


		
