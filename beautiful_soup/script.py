from bs4 import BeautifulSoup
import requests
 
req = requests.get("https://owasp.org/")
soup = BeautifulSoup(req.text, "html.parser")

#print(soup.prettify())

print(soup.head.parent.name)

print(soup.title)

print(soup.title.name)

print(soup.h1.string)

print(soup.body.attrs)

print(soup.body['class'])

soup.find(id="blocker")

for s in soup.find_all('img'):
    print(s['src'])

for link in soup.find_all('a'):
    print(link.get('href'))
