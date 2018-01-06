import re

def extractUrl(str):
	#urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
	urls = re.findall(r'Restaurant[\w\.-]*html', str)
	return urls

def extractEmail(str):
	match = re.search(r'[0-9a-z]+@[a-z0-9\.]+', str)
	if match:
		return match.group(0)
	
	return None
