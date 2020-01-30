##Recursive backtracking for automatic schedule
import itertools

def autoSchedule (list_of_group_objs):
	possible_schedules = []
	#sorting the lists of groups by number of groups, in this case
	#this might prune a bigger branch of invalid groups faster
	list_of_group_objs.sort(key = len)
	backtrackSchedule(list_of_group_objs, 0, possible_schedules, [])
	return possible_schedules


def backtrackSchedule (list_of_group_objs, location, possible_schedules, possible_classes):
	if location == len(list_of_group_objs):
		possible_schedules.append(possible_classes[:])
		#print("GET")
		return 
	for posgroup in range(len(list_of_group_objs[location])):
		if compatible_times(list_of_group_objs[location][posgroup], possible_classes):
			#print(list_of_group_objs[location][posgroup])
			possible_classes.append(list_of_group_objs[location][posgroup])
			#print(len(possible_classes))
			backtrackSchedule(list_of_group_objs,location+1,possible_schedules, possible_classes)
			possible_classes.pop()
	return

def compatible_times(candidate_group, possible_classes):
	if not possible_classes:
		return True
	for group in possible_classes:
		for dia_g in group.dias:
			for dia_c in candidate_group.dias:
				if dia_g == dia_c:
					if (candidate_group.horario[0] >= group.horario[0] and candidate_group.horario[0] <= group.horario[1]) or (candidate_group.horario[1] >= group.horario[0] and candidate_group.horario[1] <= group.horario[1]):
						return False
		if group.labo_horario != None:
			for dia_g in group.labo_dias:
				for dia_c in candidate_group.dias:
					if dia_g == dia_c:
						if (candidate_group.horario[0] >= group.labo_horario[0] and candidate_group.horario[0] <= group.labo_horario[1]) or (candidate_group.horario[1] >= group.labo_horario[0] and candidate_group.horario[1] <= group.labo_horario[1]):
							return False
		if candidate_group.labo_horario != None:
			for dia_g in group.dias:
				for dia_c in candidate_group.labo_dias:
					if dia_g == dia_c:
						if (candidate_group.labo_horario[0] >= group.horario[0] and candidate_group.labo_horario[0] <= group.horario[1]) or (candidate_group.labo_horario[1] >= group.horario[0] and candidate_group.labo_horario[1] <= group.horario[1]):
							return False
		if candidate_group.labo_horario != None and group.labo_horario != None:
			for dia_g in group.labo_dias:
				for dia_c in candidate_group.labo_dias:
					if dia_g == dia_c:
						if (candidate_group.labo_horario[0] >= group.labo_horario[0] and candidate_group.labo_horario[0] <= group.labo_horario[1]) or (candidate_group.labo_horario[1] >= group.labo_horario[0] and candidate_group.labo_horario[1] <= group.labo_horario[1]):
							return False
	return True

