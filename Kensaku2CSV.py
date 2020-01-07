# −*− coding : utf−8 −*− #
import requests
import urllib.request
import time
import csv
from bs4 import BeautifulSoup
import os


x = 118320




with open('kensakuFullPart1.csv', 'w', newline='') as csvfile :
	spamwriter = csv.writer(csvfile,delimiter=',',quotechar='|',quoting=csv.QUOTE_MINIMAL)
	spamwriter.writerow(['nome','checkup','zip','tel','fax','web','comment','law','cash1','prpoint'])#

	while (x> 1) :
		url = '/home/albyx/kensakutf8/' + str(x) + '.html'    # setto  la cartella in cui scarico le pagine, nel mio caso c:\scrp\
		if os.path.isfile(url) :
			#url = '/home/cnc/kensaku/s0/converted/' + str(x) + '.html'    # setto  la cartella in cui scarico le pagine, nel mio caso c:\scrp\
			# inoltre i file li chiamo x.html (trasformo x in stringa con str(x) )

			print ('checkup for folder and file:', url)
			page = open(url,'r', encoding='utf-8', errors='ignore')
			pagex=page.read()
			soup = BeautifulSoup(pagex,"lxml")





			for tag in soup.find_all('div', {'id' : 'Description'}): # cerco i <DIV> con attributo "class" e classe con nome "detail-body"

				################################################ NOME
				if "解体" in pagex:
					try :
						nome = soup.select('body  h1')[0].get_text(strip=True)
					except ValueError:
						nome = "name not found"

				


				################################################ CONDIZIONE 1

					if True	:
						cond1_vende = '解体'

						if "住所" in pagex	:
							try:
								zip = soup.select('#outline  td')[0].get_text(strip=True) # cerco nel primo child <dd> di <dl>
							except ValueError :
								zip = "blank"
						else:
							zip = '0'

					################################################ ADDRESS

						if "電話番号" in pagex :
							try:
								tel = soup.select('#outline   td')[1].get_text(strip=True) # cerco nel secondo child <dd> di <dl>
							except ValueError:
								tel="not found"
						else:
							tel = '0'
					################################################ TEL

						if "FAX番号" in pagex :
							try:
								fax = soup.select('#outline   td')[2].get_text(strip=True)# cerco nel terzo child <dd> di <dl>
							except ValueError:
								fax = "none"
						else:
							fax = '0'




						if len(soup.select('#prPoint #Description'))>0:
							prpoint = soup.select('#prPoint #Description')[0].get_text(strip=True)  # cerco primo child <p> dei  <div> contenuti nel <div> con classe "goback"
						else :
							prpoint = 0

						print("> SCRP-file found")
						spamwriter.writerow([nome,str(x),zip,tel,fax,prpoint]) #scrivo su CSV
					else :
						cond1_vende = 'no'
						print("> SCRP-file not found!  Try again!")







					break

		x=x-1
