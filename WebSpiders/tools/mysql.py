#coding:utf-8
#!/usr/bin/python3

import MySQLdb as mysql
import warnings

warnings.filterwarnings('error')

class Mysql:
	def __init__(self):
		try:
			self.bdd = MySQLdb.connect(host = "localhost", user = "root", passwd = "root")
		except:
			print "ERROR"

		cursor = self.bdd.cursor()
		try:
			cursor.execute("create database IF NOT EXISTS spider")
		except:
			print "BDD already exist"

		cursor.execute('use spider')
		try:
			cursor.execute('create table IF NOT EXISTS victime (id INT(6) PRIMARY KEY AUTO_INCREMENT, email varchar(255) NOT NULL, UNIQUE (email))')
		except:
			print "table already exist"

		self.bdd.commit()

	def insertEmail(self, newEmail):
		cursor = self.bdd.cursor()
		cursor.execute("use spider")
		try:
			cursor.execute("INSERT INTO email(email) VALUE('"+newEmail+"')")
			self.mysql.commit()
		except:
			print ("Already in the database")
