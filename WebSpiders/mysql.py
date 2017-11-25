#coding:utf-8
#!/usr/bin/python3

import MySQLdb

class Mysql:
	def __init__(self):
		self.mysql = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "aston")

	def insertEmail(self, newEmail):
		cursor = self.mysql.cursor()
		try:
			cursor.execute("INSERT INTO email(email) VALUE('"+newEmail+"')")
			self.mysql.commit()
		except MySQLdb.IntegrityError:
			print ("Already in the database")

	def findOneById(self, id):
		conn = self.mysql.connect(host = "localhost", user = "root", passwd = "", db = "aston")
		cursor = conn.cursor()
		cursor.execute("SELECT * from email WHERE id = %s" % id)
		row = cursor.fetchone()
		cursor.close()
		conn.close()
		return row
