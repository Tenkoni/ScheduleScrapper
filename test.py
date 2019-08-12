from scrapper import ScrapGroup

group_obj = ScrapGroup("1322")
print(len(group_obj))
for group in group_obj:
	group.printGroup()