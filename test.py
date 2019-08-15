from scrapper import ScrapGroup


list_of_classes = ['1228','1322','1447','2068']
list_of_groups = []

for cla in list_of_classes:
	list_of_groups.append(ScrapGroup(cla))

try:
	print(len(list_of_groups))
	for cla in list_of_groups:
		for group in cla:
			group.printGroup()
except TypeError:
	print("Grupo inválido")