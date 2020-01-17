import requests

def getSite(url):
	siteres = requests.get(url)
	if siteres.status_code == 200:
		return True, siteres
	print(siteres.status_code)
	return False, None

def getPlainHTML(site):
	return site.content

def extractHTML(url):
	status, site = getSite(url)
	if status:
		return True, getPlainHTML(site)
	return False, None

