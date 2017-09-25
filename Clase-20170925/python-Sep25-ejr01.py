# Una empresa con 5 empleados, de ellos se carga:
# Nombre
# Sexo
# Cant. de horas trabajadas
# A. Se solicita imprimir los datos de cada empleado
# Sabemos que la cant. de horas a trabajar es 160
# y el valor de la hora es de 800
# Se desea saber del empleado:
# B. El sueldo bruto (160 x 800)
# C. La cant. de horas extras.
# La hora extra es un 50% mas que la hora comun.
# D. Calcular el sueldo bruto incluyendo las horas extras.
# E. Se debe abonar salario familiar, para eso debemos
# cargar:
# Estado Civil
# Cantidad de hijos
# F. Si estado civil igual casado se paga por conyuge 200
# G. Por hijo se paga 1000 y por cada hijo a partir del 3ro
# se paga un 40% mas (de los 1000) por cada hijo.
# Imprimir salario familiar.

#nombre = ["Pablo","Ana","Jose","Maria","Tomas"]
#sexo = ["M","F","M","F","M"]
#horas = [170,200,160,320,250]
#estcivil = ["","","","",""]
#hijos = [0,0,0,0,0]

empleado = []
empleados = []
nombre = 0
sexo = 1
horas = 2
estcivil = 3
hijos = 4
valorhora = 800
horarionormal = 160
indicehoraextra = 1.5

for i in range(0,5) :
	empleado.append( input(f"Ingresar el nombre del empleado {i+1}\n") )
	empleado.append( input(f"Ingresar el sexo del empleado {i+1}\n") )
	empleado.append( int(input(f"Ingresar la cant. de horas trabajadas del empleado {i+1}\n")) )
	empleado.append( input(f"Ingresar el estado civil del empleado {i+1}\n") )
	empleado.append( int(input(f"Ingresar la cant. de hijos del empleado {i+1}\n")) )
	empleados.append( empleado )
	empleado = []

for i in range(0,5) :
	sueldobruto = 0
	horasextras = 0
	sueldoneto = 0

	print(f"Nombre: {empleados[i][nombre]}")
	print(f"Genero: {empleados[i][sexo]}")
	print(f"Horas trabajadas: {empleados[i][horas]}")	# A.

	sueldobruto = empleados[i][horas] * valorhora
	print( f"Sueldo bruto: {sueldobruto:,.2f}".replace(","," ") )	# B.

	horasextras = empleados[i][horas] - horarionormal
	print(f"Horas extras: {horasextras}")	# C.

	sueldoneto = sueldobruto + horasextras * indicehoraextra
	print( f"Sueldo neto: {sueldoneto:,.2f}".replace(","," ") )		# D.
	print("----------")