#coding:utf-8
#!/usr/bin/python3

import MySQLdb, random, string

def insertEmail(newEmail):
	conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "aston")
	cursor = conn.cursor()

	try:
		cursor.execute ("INSERT INTO email(email) VALUE('"+newEmail+"')")
		conn.commit()
	except MySQLdb.IntegrityError:
		print ("Already in the database")

def findOneById(id):
	conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "aston")
	cursor = conn.cursor()
	cursor.execute ("SELECT * from email WHERE id = %s"%id)
	row = cursor.fetchone() 
	cursor.close()
	conn.close()
	return row
