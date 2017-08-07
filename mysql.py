import MySQLdb, random, string

conn = MySQLdb.connect(host = "localhost", user = "root", passwd = "", db = "aston")
cursor = conn.cursor()

newEmail = ''.join((random.choice(string.ascii_lowercase)) for x in range(10))

print (newEmail)

try:
	cursor.execute ("INSERT INTO email(email) VALUE('"+newEmail+"@email.fr')")
	conn.commit()
except MySQLdb.IntegrityError:
	print ("existe deja")

cursor.execute ("SELECT * from email")
row = cursor.fetchall()
#row = cursor.fetchone()
print (row)
cursor.close()
conn.close()



#INSERT INTO table (nom_colonne_1, nom_colonne_2, ... VALUES ('valeur 1', 'valeur 2', ...)