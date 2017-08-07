#!/usr/bin/python3
import MySQLdb, random, string

conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "aston")
cursor = conn.cursor()

newEmail = ''.join((random.choice(string.ascii_lowercase)) for x in range(10))

print (newEmail)

try:
	cursor.execute ("INSERT INTO email(email) VALUE('"+newEmail+"@email.fr')")
	conn.commit()
except MySQLdb.IntegrityError:
	print ("Already in the database")

cursor.execute ("SELECT * from email")
row = cursor.fetchall()
#row = cursor.fetchone()
#print (row)
cursor.close()
conn.close()


def findOneById(id):
	conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "aston")
	cursor = conn.cursor()
	cursor.execute ("SELECT * from email WHERE id = %s"%id)
	row = cursor.fetchone() 
	cursor.close()
	conn.close()
	return row