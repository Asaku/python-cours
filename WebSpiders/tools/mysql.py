#coding:utf-8
#!/usr/bin/python3

import sqlite3

class Mysql:
	def __init__(self):
		try:
			self.mysql = sqlite3.connect(host = "localhost", user = "root", passwd = "root")
		except:
			print "ERROR"

	def insertEmail(self, newEmail):
		cursor = self.mysql.cursor()
		try:
			cursor.execute("INSERT INTO email(email) VALUE('"+newEmail+"')")
			self.mysql.commit()
		except sqlite3.IntegrityError:
			print ("Already in the database")

	def findOneById(self, id):
		conn = self.mysql.connect(host = "localhost", user = "root", passwd = "", db = "aston")
		cursor = conn.cursor()
		cursor.execute("SELECT * from email WHERE id = %s" % id)
		row = cursor.fetchone()
		cursor.close()
		conn.close()
		return row