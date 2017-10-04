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
cant_alumnos = 0

# Esto es para pruebas
lista_alumnos.append(["Jose","Saraza",6,6,6,"Masc"])
lista_alumnos.append(["Ana","Salsa",9,9,8,"Feme"])
lista_alumnos.append(["Pablo","Martillo",7,6,4,"Masc"])
lista_alumnos.append(["Pepa","Pitt",2,3,3,"Feme"])
lista_alumnos.append(["Tomas","Tomate",2,2,2,"Masc"])
lista_alumnos.append(["Ariadna","Menendez",10,10,10,"Feme"])
cant_alumnos = 6

'''
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

	lista_alumnos.append(datos_alumno)
	cant_alumnos += 1
	datos_alumno = []

	print("Ingresar los datos del alumno",cant_alumnos+1)
	input_nombre = input("Ingresar Nombre\n")
'''

# A.
cant_reprobados = 0
acum_promedio = 0

for alumno in lista_alumnos :

	calc_promedio = ( alumno[nota1] + alumno[nota2] + alumno[nota3] ) / 3
	alumno.append(calc_promedio)
	acum_promedio += calc_promedio 

	if calc_promedio < 4 :
		alumno_estado = "Reprobado"
		cant_reprobados += 1
	else :
		alumno_estado = "Aprobado"

	if alumno[nota1] > 7 :
		if alumno[nota2] > 7 :
			if alumno[nota3] > 7 :
				alumno_estado = "Promocionado"

	alumno.append(alumno_estado)


# B.
lista_promocionados = ""
# C.
cant_mujeresAprobadas = 0
# D.
cant_feme = 0
cant_masc = 0
# E.
cant_promocionados = 0
# F.
promedioGeneral = acum_promedio / cant_alumnos
promedioGeneral = round(promedioGeneral,2)
# G.
porcetajeReprobados = cant_reprobados * 100 / cant_alumnos
porcetajeReprobados = round(porcetajeReprobados,2)
# H.
lista_mayorPromedioGral = ""
# I.
cant_igualPromedioGral = 0
# J.
lista_aprobaron1erParcial = ""
# K.
cant_reprobados2doParcial = 0
# L.
lista_aprobaron3erParcial = ""


for alumno in lista_alumnos :
	
	if alumno[estado] == "Promocionado" :
		lista_promocionados += "Nombre: " + alumno[nombre] + "\n"
		lista_promocionados += "Apellido: " + alumno[apellido] + "\n"
		lista_promocionados += "Promedio: " + str(round(alumno[promedio],2)) + "\n"
		lista_promocionados += "-" * 60 + "\n"
		cant_promocionados += 1
		

	if alumno[genero] == "Feme" :
		cant_feme += 1

		if alumno[estado] == "Aprobado" or alumno[estado] == "Promocionado" :
			cant_mujeresAprobadas += 1

	else :
		cant_masc += 1


	if alumno[promedio] > promedioGeneral :
		lista_mayorPromedioGral += "Nombre: " + alumno[nombre] + "\n"
		lista_mayorPromedioGral += "Apellido: " + alumno[apellido] + "\n"
		lista_mayorPromedioGral += "-" * 60 + "\n"

	elif alumno[promedio] == promedioGeneral :
		cant_igualPromedioGral += 1


	if alumno[nota1] > 7 :
		lista_aprobaron1erParcial += "Nombre: " + alumno[nombre] + "\n"
		lista_aprobaron1erParcial += "Apellido: " + alumno[apellido] + "\n"
		lista_aprobaron1erParcial += "-" * 60 + "\n"

	if alumno[nota2] < 4 :
		cant_reprobados2doParcial += 1

	if alumno[nota3] > 4 and alumno[nota3] < 7 :
		lista_aprobaron3erParcial += "Nombre: " + alumno[nombre] + "\n"
		lista_aprobaron3erParcial += "-" * 60 + "\n"


print("Lista de Alumnos Promocionados:\n" + lista_promocionados)

print("=" * 60)
print("Cantidad de Reprobados:",cant_reprobados)
print("Cantidad de Mujeres Aprobadas:",cant_mujeresAprobadas)
print("Cantidad de Alumnos Mujeres:",cant_feme)
print("Cantidad de Alumnos Hombres:",cant_masc)
print("Cantidad de Alumnos Promocionados:",cant_promocionados)
print("Promedio General:",promedioGeneral)
print("Porcentaje Reprobados:",porcetajeReprobados,"%")
print("=" * 60 + "\n")

print("Lista de Alumnos con mayor promedio general:\n" + lista_mayorPromedioGral)

print("=" * 60)
print("Cantidad de Alumnos con promedio igual al general:",cant_igualPromedioGral)
print("=" * 60 + "\n")

print("Lista de Alumnos que aprobaron con mas de 7 el 1er parcial:\n" + lista_aprobaron1erParcial)

print("=" * 60)
print("Cantidad de Alumnos que reprobaron el 2do parcial:",cant_reprobados2doParcial)
print("=" * 60 + "\n")

print("Lista de Alumnos que aprobaron el 3er parcial entre 4 y 7:\n" + lista_aprobaron3erParcial)
