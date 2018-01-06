#coding:utf-8
#!/usr/bin/python3

import requests, param
from tools import extract as extract
from time import *

if param.db == "mysql":
	from tools import mysql as orm
elif param.db == "mongo":
	from tools import mongo as orm

orm = orm.Db()
count = 0
while True:
	r = requests.get("https://www.tripadvisor.fr/RestaurantSearch?Action=PAGE&geo=187147&ajax=1&cat=10659&itags=10591&sortOrder=relevance&availSearchEnabled=true&eaterydate=2018_01_05&date=2018-01-06&time=20%3A00%3A00&people=2&o=a"+str(count))
	count = count + 30
	if r.status_code != 200:
		break
	urls = extract.extractUrl(r.content.decode('utf-8'))

	for url in set(urls):	
		if "media-cdn" not in url:
			sleep(2)
			req = requests.get("https://www.tripadvisor.fr/"+url)
			newEmail = extract.extractEmail(req.content.decode('utf-8'))
			print newEmail
			if newEmail:
				orm.insertEmail(newEmail)

