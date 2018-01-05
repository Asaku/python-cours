#coding:utf-8
#!/usr/bin/python3

import mysql as mysql
import warnings

'''
sudo apt-get install libmysqlclient-dev python-pip
pip install mysql-server
'''

warnings.filterwarnings('error')

class Db:
	def __init__(self):
		try:
			self.db = mysql.connect(host = "localhost", user = "root", passwd = "root")
		except:
			print "ERROR"

		cursor = self.db.cursor()
		try:
			cursor.execute("create database IF NOT EXISTS spider")
		except:
			print "db already exist"

		cursor.execute('use spider')
		try:
			cursor.execute('create table IF NOT EXISTS victime (id INT(6) PRIMARY KEY AUTO_INCREMENT, email varchar(255) NOT NULL, UNIQUE (email))')
		except:
			print "table already exist"

		self.db.commit()

	def insertEmail(self, newEmail):
		cursor = self.db.cursor()
		cursor.execute("use spider")
		try:
			cursor.execute("INSERT INTO email(email) VALUE('"+newEmail+"')")
			self.db.commit()
		except:
			print ("Already in the database")

