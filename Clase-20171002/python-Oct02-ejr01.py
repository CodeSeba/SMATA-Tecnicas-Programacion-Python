# Dado un curso de alumnos.
# Se deben cargar los siguientes datos:
# -Nombre
# -Apellido
# -Nota 1
# -Nota 2
# -Nota 3
# -Genero
# La carga finaliza con el nombre "pepe".
#
# Se debe calcular el promedio,
# si el promedio < 4 entonces "Reprobado",
# si el promedio es >= 4 entonces "Aprobado",
# si aprobo los tres examenes con nota
# superior a 7 entonces "Promocionado".
#
# A. Indicar la cantidad de alumnos reprobados.
# B. Nombre, Apellido, Promedio de los alumnos promocionados.
# C. Cantidad de mujeres aprobadas.
# D. Cantidad de alumnos discriminado por genero.
# E. Cantidad de alumnos promocionados.
# F. Calcular Promedio General.
# G. Calcular Porcentaje de Alumnos Reprobados.
# H. Nombre y Apellido de los alumnos cuyo promedio
#    sea mayor al promedio general.
# I. Cantidad de alumnos con promedio igual al
#    promedio general.
# J. Listado (nombre y apellido) de los alumnos aprobados
#    con mas de 7 en el primer parcial.
# K. Cantidad de alumnos que reprobaron en el segundo parcial.
# L. Nombre de los alumnos con la tercera nota mayor a 4 y menor a 7.


# Nombre de los indices
nombre = 0
apellido = 1
nota1 = 2
nota2 = 3
nota3 = 4
genero = 5
promedio = 6
estado = 7

lista_alumnos = []
datos_alumno = []


# Datos cargados para pruebas
lista_alumnos.append( ["Jose","Saraza",6,6,6,"Masc"] )
lista_alumnos.append( ["Ana","Salsa",9,9,8,"Feme"] )
lista_alumnos.append( ["Pablo","Martillo",7,6,4,"Masc"] )
lista_alumnos.append( ["Pepa","Pitt",2,3,3,"Feme"] )
lista_alumnos.append( ["Tomas","Tomate",2,2,2,"Masc"] )
lista_alumnos.append( ["Ariadna","Menendez",10,10,10,"Feme"] )

for alumno in lista_alumnos :

	calc_promedio = ( alumno[nota1] + alumno[nota2] + alumno[nota3] ) // 3
	alumno.append(calc_promedio)

	alumno_estado = "Reprobado" if calc_promedio < 4 else "Aprobado"
	alumno_estado = "Promocionado" if alumno[nota1] > 7 and alumno[nota2] > 7 and alumno[nota3] > 7 else alumno_estado

	alumno.append(alumno_estado)


'''
# Carga de datos mediante input
cant_alumnos = 0
print("Ingresar los datos del alumno",cant_alumnos+1)
input_nombre = input("Ingresar Nombre\n")

while input_nombre != "pepe" :

	input_apellido = input("Ingresar Apellido\n")
	input_nota1 = int( input("Ingresar Nota 1\n") )
	input_nota2 = int( input("Ingresar Nota 2\n") )
	input_nota3 = int( input("Ingresar Nota 3\n") )
	input_genero = input("Ingresar Genero\n")

	datos_alumno.append(input_nombre)
	datos_alumno.append(input_apellido)
	datos_alumno.append(input_nota1)
	datos_alumno.append(input_nota2)
	datos_alumno.append(input_nota3)
	datos_alumno.append(input_genero)

	calc_promedio = ( datos_alumno[nota1] + datos_alumno[nota2] + datos_alumno[nota3] ) / 3
	datos_alumno.append(calc_promedio)

	alumno_estado = "Reprobado" if calc_promedio < 4 else "Aprobado"
	alumno_estado = "Promocionado" if datos_alumno[nota1] > 7 and datos_alumno[nota2] > 7 and datos_alumno[nota3] > 7 else alumno_estado
	datos_alumno.append(alumno_estado)

	lista_alumnos.append(datos_alumno)

	cant_alumnos += 1
	del datos_alumno

	print("Ingresar los datos del alumno",cant_alumnos+1)
	input_nombre = input("Ingresar Nombre\n")
'''


# A.
cant_reprobados = len( [ alumno for alumno in lista_alumnos if alumno[estado] == "Reprobado" ] )

# B.
lista_promocionados = [ [ alumno[nombre], alumno[apellido], round(alumno[promedio],2) ] for alumno in lista_alumnos if alumno[estado] == "Promocionado" ]

# C.
cant_mujeresAprobadas = len( [ alumno for alumno in lista_alumnos if alumno[genero] == "Feme" and ( alumno[estado] == "Aprobado" or alumno[estado] == "Promocionado" ) ] )

# D.
cant_feme = len( [ alumno for alumno in lista_alumnos if alumno[genero] == "Feme" ] )
cant_masc = len( [ alumno for alumno in lista_alumnos if alumno[genero] == "Masc" ] )

# E.
cant_promocionados = len( lista_promocionados )

# F.
cant_alumnos = len( lista_alumnos )
acum_promedio = sum( [ alumno[promedio] for alumno in lista_alumnos ] )
promedioGeneral = acum_promedio // cant_alumnos

# G.
porcetajeReprobados = cant_reprobados * 100 // cant_alumnos

# H.
lista_mayorPromedioGral = [ [ alumno[nombre], alumno[apellido] ] for alumno in lista_alumnos if alumno[promedio] > promedioGeneral ]

# I.
cant_igualPromedioGral = len( [ alumno for alumno in lista_alumnos if alumno[promedio] == promedioGeneral ] )

# J.
lista_aprobaron1erParcial = [ [ alumno[nombre], alumno[apellido] ] for alumno in lista_alumnos if alumno[nota1] > 7 ]

# K.
cant_reprobados2doParcial = len( [ alumno for alumno in lista_alumnos if alumno[nota2] < 4 ] )

# L.
lista_aprobaron3erParcial = [ alumno[nombre] for alumno in lista_alumnos if alumno[nota1] in range(4,8) ]


# Impresion de todos los resultados
tab = " " * 4
print("Cantidad de alumnos reprobados:",cant_reprobados,"\n")

print("Lista de alumnos promocionados\n" + "-" * 50)
for alumno in lista_promocionados :
	print( "Nombre: " + alumno[0] + tab + "Apellido: " + alumno[1] + tab + "Promedio:",alumno[2] )

print("\nCantidad de mujeres aprobadas:",cant_mujeresAprobadas,"\n")
print("Cantidad de mujeres:",cant_feme,"\n")
print("Cantidad de hombre:",cant_masc,"\n")
print("Cantidad de alumnos promocionados:",cant_promocionados,"\n")
print("Promedio General:",promedioGeneral,"\n")
print("Porcentaje de Reprobados:",porcetajeReprobados,"%\n")

print("Lista de alumnos con mayor promedio general\n" + "-" * 50)
for alumno in lista_mayorPromedioGral :
	print( "Nombre: " + alumno[0] + tab + "Apellido: " + alumno[1] + tab )

print("\nCantidad de alumnos con igual promedio que el promedio general:",cant_igualPromedioGral,"\n")

print("Lista de alumnos que aprobaron el 1er parcial\n" + "-" * 50)
for alumno in lista_aprobaron1erParcial :
	print( "Nombre: " + alumno[0] + tab + "Apellido: " + alumno[1] + tab )

print("\nCantidad de alumnos que reprobaron el 2do parcial:",cant_reprobados2doParcial,"\n")

print("Lista de alumnos que aprobaron el 3er parcial entre 4 y 7\n" + "-" * 50)
for unNombre in lista_aprobaron3erParcial :
	print( "Nombre: " + unNombre )