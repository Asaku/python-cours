import re

def extract(str):
	match = re.search(r'[\w\.-]+@[\w\.-]+', str)
	return match.group(0)