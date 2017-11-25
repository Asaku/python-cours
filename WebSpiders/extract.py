import re

def extract(str):
	match = re.search(r'[\w\.-]+@[\w\.-]+', str)
	return match.group(0)

def extractUrl(str):
	urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', str)
	return urls
