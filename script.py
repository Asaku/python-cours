import requests, extract

def emailAction(url):
	print(url)

r = requests.get("https://www.tripadvisor.fr/Restaurant_Review-g187147-d699456-Reviews-Le_Cinq-Paris_Ile_de_France.html")
newEmail = extract.extract(r.content.decode('utf-8'))
print(newEmail)	

urls = extract.extractUrl(r.content.decode('utf-8'))

for url in urls:
	emailAction(url)


#print (r.status_code)
#print (r.headers)
#print (r.content)
