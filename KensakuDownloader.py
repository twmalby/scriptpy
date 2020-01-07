import requests
import urllib.request
import time
import csv
from bs4 import BeautifulSoup

x = 2
url = 'https://www.ken-saku.jp/company_profile.php?id='


if True:
	while (x< 160000) :
	
		url = 'https://www.ken-saku.jp/company_profile.php?id=' + str(x)


		download_url = url

		print ('download:', download_url)

		urllib.request.urlretrieve(download_url, str(x) + '.html' )
		x=x+1
		time.sleep(30) # riposo 0.30 sec per evitare di venire bannato
