"""
Copyright (C) 2023 - 2024 Latip176
DILARANG KERAS MERUBAH NAMA AUTHOR
"""

import requests, re
from bs4 import BeautifulSoup


def get_all_platforms(url = "https://user-agents.net"):
	no = 0
	r = BeautifulSoup(requests.get(url+"/platforms",headers={"user-agent":"chrome"}).text, "html.parser")
	data = {}
	for x in r.find("ul",{"class":"compact_list"}).findAll("li"):
		no += 1
		data.update(
			{
				str(no):{
					"nama":x.find("a").string,
					"href":x.find("a").get("href")
				}
			}
		)
	return data
	
def getUaList(v, url = "https://user-agents.net"):
	no = 0
	r = BeautifulSoup(requests.get(url+str(v),headers={"user-agent":"chrome"}).text, "html.parser") 
	data = {}
	for x in r.find("ul",{"class":"compact_list"}).findAll("li"):
		if "/browser" in x.find("a").get("href"):
			no += 1
			data.update(
				{
					str(no):{
						"nama":x.find("a").string,
						"href":x.find("a").get("href")
					}
				}
			)
	return data

def getUa(data, url = "https://user-agents.net"):
	no = 0
	print("===== INFORMASI =====")
	print(f" >= Nama: {data['nama']}\n >= Href: {data['href']}")
	print("===== BROWSER =====")
	menu = getUaList(data['href'])
	for k in menu:
		print(f"{k}. {menu[k]['nama']}")
	chose = input("\n > Pilih Browser: ")
	try:
		ua = BeautifulSoup(requests.get(url+menu[chose]['href'], headers={"user-agent":"chrome"}).text, "html.parser")
		print("===== UA LIST =====")
		for x in ua.find("ul", {"class":"agents_list"}).findAll("li"):
			no += 1
			print(f"{no}. {x.string}")
			open(menu[chose]['nama']+".txt", "a").write(x.string+"\n")
	except IndexError:
		exit(" Pilihan Tidak Tersedia!")
	exit(f"\n Berhasil Tersimpan di File: {menu[chose]['nama']+'.txt'}\n Thanks You! ")
	
if __name__=="__main__":
	print("""
	Get UserAgent all Platforms!
		Coded by: Latip176
	""")
	
	print("===== PLATFORMS =====")
	menu = get_all_platforms()
	for k in menu:
		print(f"{k}. {menu[k]['nama']}")
	
	try:
		chose = input('\n > Pilih Ua: ')
		getUa(menu[chose])
	except IndexError:
		exit(" Pilihan Tidak Tersedia!")