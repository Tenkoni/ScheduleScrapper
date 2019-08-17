from bs4 import BeautifulSoup
from urlGenerator import generateURL
from htmlGenerator import extractHTML
from group import Group

def doubleJump(iterator):
	next(iterator)
	return iterator

def isInt(value):
	try: 
		int(value)
		return True 
	except TypeError:
		return False
	except ValueError:
		return False

def ScrapGroup(class_sel):
	try:
		url = generateURL(class_sel)
	except TypeError:
		sys.exit()
	if url == "Invalid class":
		return 
	status, plain_html = extractHTML(url)
	soup = BeautifulSoup(plain_html)
	tree_groups = soup.find_all("tr")
	group_list=[]
	tree_groups.pop(0) #remove 2 first branches of the tree
	tree_groups.pop(0) 
	for gr in tree_groups:
		group_iter = gr.descendants #create a generator containing all the branches of the tree
		group_content = next(doubleJump(gr.descendants))
		if group_content == 'L':
			tipo_t = next(doubleJump(group_iter))
			horario_t = next(doubleJump(group_iter))
			dias_t = next(doubleJump(group_iter))
			salon_t = next(doubleJump(group_iter))
			group_list[-1].addHorario_lab(horario_t)
			group_list[-1].addDias_lab(dias_t)
			group_list[-1].labo_salon = salon_t

		elif isInt(group_content):
			clave_t = next(doubleJump(group_iter))
			grupo_t = next(doubleJump(group_iter))
			profesor_t = next(doubleJump(group_iter))
			tipo_t = next(doubleJump(group_iter))
			horario_t = next(doubleJump(group_iter))
			dias_t = next(doubleJump(group_iter))
			salon_t = next(doubleJump(group_iter))
			cupo_t = next(doubleJump(group_iter))
			vacantes_t = next(doubleJump(group_iter))
			group_list.append(Group(clave = clave_t, grupo = grupo_t, profesor = profesor_t, tipo = tipo_t, horario = horario_t, dias = dias_t, salon = salon_t, cupo = cupo_t, vacantes = vacantes_t))

		elif len(list(gr.descendants))==6:
			horario_t = next(doubleJump(group_iter))
			dias_t = next(doubleJump(group_iter))
			salon_t = next(doubleJump(group_iter))
			group_list[-1].salon.append(salon_t)
			group_list[-1].addHorario(horario_t)
			group_list[-1].addDias(dias_t)

	return group_list



	
