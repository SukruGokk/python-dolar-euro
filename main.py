#
#@author: SukruGokk
#

import bs4
import requests

euroURL = "http://tr.investing.com/currencies/eur-try"
dolarURL = "http://tr.investing.com/currencies/usd-try"

def get_euro():
	# CREATES A SESSION
	with requests.Session() as euroSes:

		# PAGE CONTENT
		cnt = euroSes.get(euroURL, headers={"User-Agent": "Mozilla"}).content
		cnt = BS(cnt, "html5lib")

		# EURO VALUE
		euro = cnt.find('span', id="last_last").string

		return euro

def get_dolar():
	# CREATES A SESSION
	with requests.Session() as dolarSes:

		# PAGE CONTENT
		cnt = dolarSes.get(euroURL, headers={"User-Agent": "Mozilla"}).content
		cnt = BS(cnt, "html5lib")

		# DOLAR VALUE
		dolar = cnt.find('span', id="last_last").string

		return dolar
