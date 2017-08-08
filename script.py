import requests, mysql, extract

r = requests.get("https://www.google.fr")
newEmail = extract.extract(r.content.decode('utf-8'))

mysql.insertEmail(newEmail)

#print (r.status_code)
#print (r.headers)
#print (r.content)
