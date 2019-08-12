import sys

def generateURL(assig_code):
	try:
		if assig_code in open("valid_class.miy").read():
			url = "https://ssa.ingenieria.unam.mx/hrsHtml/" + assig_code + '.html'
			return url
		return "Invalid class" #código usado para indicar un grupo inexistente
	except:
		SystemExit("The groups file is missing")
