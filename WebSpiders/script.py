#coding:utf-8
#!/usr/bin/python3

import requests
from tools import extract as extract
from tools import mysql as mysql
from time import *

def sleep():
	print "haha"

sleep(10)

mysql = mysql.Mysql()
count = 0
while True:
	r = requests.get("https://www.tripadvisor.fr/Restaurant_Review-g187147-d699456-Reviews-Le_Cinq-Paris_Ile_de_France.html")
	count = count + 30
	if r.status_code != 200:
		break
	urls = extract.extractUrl(r.content.decode('utf-8'))

	for url in urls:
		if "tripadvisor" in url and "media-cdn" not in url:
			req = requests.get("https://www.tripadvisor.fr/"+url)

			newEmail = extract.extractEmail(req.content.decode('utf-8'))
			if newEmail:
				mysql.insertEmail(newEmail)

