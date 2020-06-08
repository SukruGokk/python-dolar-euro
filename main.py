#
#@author: SukruGokk
#

import requests
from bs4 import BeautifulSoup as BS

euroURL = "http://tr.investing.com/currencies/eur-try"
dolarURL = "http://tr.investing.com/currencies/usd-try"

def get_euro():
	# CREATES A SESSION
	with requests.Session() as euroSes:

		# PAGE CONTENT
		cnt = euroSes.get(euroURL, headers={"User-Agent": "Mozilla"}).content
		cnt = BS(cnt, features = "lxml")

		# EURO VALUE
		euro = cnt.find('span', id="last_last").string

		return euro

def get_dolar():
	# CREATES A SESSION
	with requests.Session() as dolarSes:

		# PAGE CONTENT
		cnt = dolarSes.get(dolarURL, headers={"User-Agent": "Mozilla"}).content
		cnt = BS(cnt, features = "lxml")
		
		# DOLAR VALUE
		dolar = cnt.find('span', id="last_last").string

		return dolar
