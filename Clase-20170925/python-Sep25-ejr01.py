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
ingresarNombre = "Ingresar el nombre del empleado "
ingresarSexo = "Ingresar el sexo del empleado "
ingresarHoras = "Ingresar la cant. de horas trabajadas del empleado "
ingresarEstadoCivil = "Ingresar el estado civil del empleado "
ingresarHijos = "Ingresar la cant. de hijos del empleado "

#lista_empleados = [ [Nombre,Sexo,Horas,EstadoCivil,Hijos] ]
lista_empleados = []
datos_empleado = []


#Datos cargados para pruebas
lista_empleados.append( ["Pablo","M",170,"C",6] )
lista_empleados.append( ["Ana","F",200,"S",0] )
lista_empleados.append( ["Jose","M",160,"D",2] )
lista_empleados.append( ["Maria","F",320,"V",3] )
lista_empleados.append( ["Tomas","M",250,"P",1] )

'''
#Datos cargados mediante input
for i in range(0,5) :
	nro = str( i+1 )
	datos_empleado.append( input(ingresarNombre + nro + "\n") )
	datos_empleado.append( input(ingresarSexo + nro + "\n") )
	datos_empleado.append( int(input(ingresarHoras + nro + "\n")) )
	datos_empleado.append( input(ingresarEstadoCivil + nro + "\n") )
	datos_empleado.append( int(input(ingresarHijos + nro + "\n")) )
	print("-" * 50)

	lista_empleados.append( datos_empleado )
	datos_empleado[:] = []
'''


# formato_moneda() es un metodo que da formato a un nro a formato moneda
def formato_moneda(unNro) :
	unNro = format(unNro,",.2f")
	unNro = unNro.replace(".",",")
	unNro = unNro.replace(",",".",unNro.count(",")-1)
	unNro = unNro.replace(",00",",-")
	unNro = "$ " + unNro
	return unNro


print("\nLista de empleados de la empresa")
print("=" * 50)

# Por cada empleado de la lista lista_empleados
for empleado in lista_empleados :
	
	horasExtras = 0
	totalHorasExtras = 0
	cantidadHijos = 0
	asignacion = 0

	sueldoBasico = 0
	sueldoFamiliar = 0
	sueldoBruto = 0

	# A.
	print( "Nombre: " + empleado[nombre] )
	print( "Genero: " + empleado[sexo] )
	print( "Horas trabajadas: ", empleado[horas] )

	# B.
	sueldoBasico = empleado[horas] * valorHora
	print( "Sueldo basico: " + formato_moneda(sueldoBasico) )

	# C.
	horasExtras = empleado[horas] - horarioNormal
	print( "Horas extras:",horasExtras )

	# D.
	totalHorasExtras = horasExtras * valorHora * indice_HoraExtra
	print( "Sueldo basico mas horas extras: " + formato_moneda(sueldoBasico + totalHorasExtras) )

	# E.
	if empleado[estadoCivil] == "C" :
		sueldoFamiliar += conyuge

	# F.
	for cantidadHijos in range( 1, empleado[hijos] + 1 ) :

		if cantidadHijos < familiaNumerosa :
			asignacion = asignacionPorHijo
		else :
			asignacion = asignacion * indice_familiaNumerosa

		sueldoFamiliar += asignacion

	# G.
	print( "Sueldo familiar: " + formato_moneda(sueldoFamiliar) )

	sueldoBruto = sueldoBasico + totalHorasExtras + sueldoFamiliar
	print( "Sueldo bruto: " + formato_moneda(sueldoBruto) )

	print("-" * 50)