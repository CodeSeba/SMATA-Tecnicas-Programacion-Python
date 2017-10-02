# Una empresa con 5 empleados, de ellos se carga:
# Nombre
# Sexo
# Cant. de horas trabajadas
# A.
# Se solicita imprimir los datos de cada empleado
# Sabemos que la cant. de horas a trabajar es 160
# y el valor de la hora es de 800
# Se desea saber del empleado:
# B.
# El sueldo basico (160 x 800)
# C.
# La cant. de horas extras.
# La hora extra es un 50% mas que la hora comun.
# D.
# Calcular el sueldo basico mas las horas extras.
# Se debe abonar salario familiar, para eso debemos
# cargar:
# Estado Civil
# Cantidad de hijos
# E.
# Si estado civil igual casado se paga por conyuge 200
# F.
# Por hijo se paga 1000 y por cada hijo a partir del 3ro
# se paga por hijo un 40% mas del valor del hijo anterior.
# Ejemplo: 1ro y 2do 1000 cada uno, el 3ro 1400
# el 4to 1960, el 5to 2744, etc...
# G.
# Imprimir salario familiar.


# Nombres de indices
nombre = 0
sexo = 1
horas = 2
estadoCivil = 3
hijos = 4

# Parametros (valores estaticos)
valorHora = 800
horarioNormal = 160
indice_HoraExtra = 1.5
conyuge = 200
asignacionPorHijo = 1000
familiaNumerosa = 3
indice_familiaNumerosa = 1.4

# Mensajes de ingresos
ingresarNombre = "Ingresar el nombre del empleado"
ingresarSexo = "Ingresar el sexo del empleado"
ingresarHoras = "Ingresar la cant. de horas trabajadas del empleado"
ingresarEstadoCivil = "Ingresar el estado civil del empleado"
ingresarHijos = "Ingresar la cant. de hijos del empleado"


lista_empleados = []
for i in range(0,5) :
	empleado = []
	empleado.append( input(f"{ingresarNombre} {i+1}\n") )
	empleado.append( input(f"{ingresarSexo} {i+1}\n") )
	empleado.append( int(input(f"{ingresarHoras} {i+1}\n")) )
	empleado.append( input(f"{ingresarEstadoCivil} {i+1}\n") )
	empleado.append( int(input(f"{ingresarHijos} {i+1}\n")) )
	lista_empleados.append( empleado )
	print("-" * 50)


print("\nLista de empleados de la empresa")
print("=" * 50)

# Como foreach en Java, seria "por cada empleado de la lista lista_empleados"
for empleado in lista_empleados :
	
	sueldoBasico = 0
	horasExtras = 0
	sueldoFamiliar = 0

	formato_sueldo = ''
	totalHorasExtras = 0
	asignacion = 0
	cantidadHijos = 0
	sueldoBruto = 0

	# A.
	print(f"Nombre: {empleado[nombre]}")
	print(f"Genero: {empleado[sexo]}")
	print(f"Horas trabajadas: {empleado[horas]}")

	# B.
	sueldoBasico = empleado[horas] * valorHora

	formato_sueldo = f"$ {sueldoBasico:,.2f}".replace(","," ").replace (".00",".-")
	print( f"Sueldo basico: {formato_sueldo}" )

	# C.
	horasExtras = empleado[horas] - horarioNormal

	print(f"Horas extras: {horasExtras}")

	# D.
	totalHorasExtras = horasExtras * valorHora * indice_HoraExtra
	
	formato_sueldo = f"$ {sueldoBasico + totalHorasExtras:,.2f}".replace(","," ").replace(".00",".-")
	print( f"Sueldo basico mas horas extras: {formato_sueldo}" )

	# E.
	if empleado[estadoCivil] == "C" :
		sueldoFamiliar += conyuge

	# F.
	for cantidadHijos in range(1,empleado[hijos]+1) :

		if cantidadHijos >= familiaNumerosa :
			asignacion = asignacion * indice_familiaNumerosa
		else :
			asignacion = asignacionPorHijo

		sueldoFamiliar += asignacion

	# G.
	formato_sueldo = f"$ {sueldoFamiliar:,.2f}".replace(","," ").replace(".00",".-")
	print( f"Sueldo familiar: {formato_sueldo}" )

	sueldoBruto = sueldoBasico + totalHorasExtras + sueldoFamiliar
	formato_sueldo = f"$ {sueldoBruto:,.2f}".replace(","," ").replace(".00",".-")
	print( f"Sueldo bruto: {formato_sueldo}" )

	print("-" * 50)