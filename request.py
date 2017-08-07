import requests, mysql

r = requests.get("https://www.google.fr")

#print (r.status_code)
#print (r.headers)
#print (r.content)

print (mysql.findOneById(11))