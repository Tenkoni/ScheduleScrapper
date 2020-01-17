from scrapper import ScrapGroup
from schedulebuilder import autoSchedule
import itertools

list_of_classes = ['2930', '406', '1858']
list_of_groups = []

for cla in list_of_classes:
	list_of_groups.append(ScrapGroup(cla))

# try:
# 	print(len(list_of_groups))
# 	for cla in list_of_groups:
# 		for group in cla:
# 			group.printGroup()
# except TypeError:
# 	print("Grupo inválido")

#automatic schedule generator
generated = autoSchedule(list_of_groups)

print(len(generated)) #total of schedules generated
for gp in generated:
	print (len(gp))
#	for grp in gp:
#		grp.printGroup() #print each schedule