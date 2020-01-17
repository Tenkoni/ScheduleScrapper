import re

class Group:
	def __init__ (self, tipo, horario, dias, salon, clave = 0, grupo = 0, profesor = "", cupo = 0, vacantes = 0):
		self.clave = int(clave)
		self.grupo = int(grupo)
		self.profesor = profesor
		self.tipo = tipo
		self.salon = [salon]
		self.cupo = int(cupo)
		self.vacantes = int(vacantes)
		self.addHorario(horario)
		self.addDias(dias)
		self.labo_salon = None
		self.labo_horario= None
		self.labo_dias = None

	def printGroup(self):
		print("--------------------------")
		print ("Clave: " + str(self.clave))
		print ("Grupo: " + str(self.grupo))
		print ("Profesor: " + self.profesor)
		print ("Tipo: " + self.tipo)
		print ("Horario: " )
		print (self.horario)
		print ("Días: " )
		print (self.dias)
		print ("Salón: ")
		print (self.salon)
		print ("Cupo: " + str(self.cupo))
		print ("Vacantes: " + str(self.vacantes))
		if self.labo_horario != None:
			print("-------LAB+--------")
			print ("Horario_lab: " )
			print (self.labo_horario)
			print ("Días_lab: " )
			print (self.labo_dias)
			print ("Salón_lab: ")
			print (self.labo_salon)
		print("--------------------------")

	def addHorario(self, time_expr):
		time_list = time_expr.replace(':', '.')
		time_list = re.findall('\d*[.]\d+', time_list)
		try:
			#cast to float of each element in case self.horario already has a value
			self.horario += [float(i) for i in time_list]
		except:
			#cast in case there's no value for horario
			self.horario = [float(i) for i in time_list]
	
	def addDias(self, dias):
		day_list = dias.replace(',', '')
		day_list = day_list.split()
		numeric_days = []
		for day in day_list:
			if day == 'Lun':
				numeric_days.append(1)
			elif day == 'Mar':
				numeric_days.append(2)
			elif day == 'Mie':
				numeric_days.append(3)
			elif day == 'Jue':
				numeric_days.append(4)
			elif day == 'Vie':
				numeric_days.append(5)
			elif day == 'Sab':
				numeric_days.append(6)
		try:
			self.dias += numeric_days
		except:
			self.dias = numeric_days

	def addHorario_lab(self, time_expr):
		time_list = time_expr.replace(':', '.')
		time_list = re.findall('\d*[.]\d+', time_list)
		try:
			self.labo_horario += [float(i) for i in time_list]
		except:
			self.labo_horario = [float(i) for i in time_list]
	
	def addDias_lab(self, dias):
		day_list = dias.replace(',', '')
		day_list = day_list.split()
		numeric_days = []
		for day in day_list:
			if day == 'Lun':
				numeric_days.append(1)
			elif day == 'Mar':
				numeric_days.append(2)
			elif day == 'Mie':
				numeric_days.append(3)
			elif day == 'Jue':
				numeric_days.append(4)
			elif day == 'Vie':
				numeric_days.append(5)
			elif day == 'Sab':
				numeric_days.append(6)
		try:
			self.labo_dias += numeric_days
		except:
			self.labo_dias = numeric_days


