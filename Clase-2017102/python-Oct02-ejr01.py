# Dado un curso de alumnos. Se deben
# cargar las siguientes datos:
# Nombre
# Apellido
# Nota 1
# Nota 2
# Nota 3
# Genero
# La carga finaliza con el nombre "pepe"
#
# Se debe calcular el promedio
# si promedio < 4 entonces "Reprobado"
# si promedio es >= 4 entonces "Aprobado"
# si aprobo los tres examenes con nota
# superior a 7 entonces "Promocionado"
#
# A. Indicar la cantidad de alumnos "Reprobados"
# B. Nombre, Apellido, Promedio de los alumnos "Promocionados"
# C. Cantidad de mujeres "Aprobadas".
# D. Cantidad de alumnos discriminado por genero.
# E. Cantidad de alumnos promocionados.
# F. Promedio general.
# G. Porcentaje de alumnos reprobados.
# H. Nombre y Apellido de los almunos cuyo promedio
# sea mayor al promedio general.
# I. Cantidad de alumnos con promedio igual al
# promedio general.
# J. Listado (nombre y apellido) de los alumnos aprobados
# con mas de 7 en el primer parcial.
# K. Cantidad de alumnos que reprobaron en el segundo parcial.
# L. Nombre de los alumnos con la tercera nota mayor a 4 y menor a 7.

lista_alumnos = []
carga_alumno = []
cont_alumnos = 0
nombre = 0
apellido = 1
nota1 = 2
nota2 = 3
nota3 = 4
genero = 5
promedio = 6
estado = 7

lista_alumnos = [["Jose","Saraza",2,2,2,"Masc"],["Ana","Salsa",9,9,8,"Feme"],["Pablo","Martillo",7,6,4,"Masc"],["Pepa","Pitt",2,3,3,"Feme"]]
cont_alumnos = 4
'''
input_nombre = input("Ingresar Nombre\n")

while input_nombre != "pepe" :
	input_apellido = input("Ingresar Apellido\n")
	input_nota1 = int( input("Ingresar Nota 1\n") )
	input_nota2 = int( input("Ingresar Nota 2\n") )
	input_nota3 = int( input("Ingresar Nota 3\n") )
	input_genero = input("Ingresar Genero\n")

	carga_alumno.append(input_nombre)
	carga_alumno.append(input_apellido)
	carga_alumno.append(input_nota1)
	carga_alumno.append(input_nota2)
	carga_alumno.append(input_nota3)
	carga_alumno.append(input_genero)

	lista_alumnos.append(carga_alumno)
	cont_alumnos += 1
	carga_alumno = []

	input_nombre = input("Ingresar Nombre\n")

#print(lista_alumnos)
'''
for alumno in lista_alumnos :
	calc_promedio = ( alumno[nota1] + alumno[nota2] + alumno[nota3] ) / 3
	alumno.append(calc_promedio)

	if calc_promedio < 4 :
		alumno_estado = "Reprobado"
	else :
		alumno_estado = "Aprobado"

	if alumno[nota1] > 7 :
		if alumno[nota2] > 7 :
			if alumno[nota3] > 7 :
				alumno_estado = "Promocionado"

	alumno.append(alumno_estado)

cont_reprobados = 0
cont_mujeresAprobadas = 0

print("Lista de Alumnos Promocionados:\n")

for alumno in lista_alumnos :
	
	if alumno[estado] == "Reprobado" :
		cont_reprobados += 1
	
	if alumno[estado] == "Promocionado" :
		print("Nombre:",alumno[nombre])
		print("Apellido:",alumno[apellido])
		print("Promedio:",alumno[promedio])
		print("\n")

	if alumno[genero] == "Feme" :
		if alumno[estado] == "Aprobado" or alumno[estado] == "Promocionado" :
			cont_mujeresAprobadas += 1


print("Cantidad de Reprebados:",cont_reprobados)
print("Cantidad de Mujeres Aprobados:",cont_mujeresAprobadas)

cont_feme = 0
cont_masc = 0
cont_promo = 0
acum_promedio = 0

for alumno in lista_alumnos :
	
	if alumno[genero] == "Feme" :
		cont_feme += 1

	if alumno[genero] == "Masc" :
		cont_masc += 1

	if alumno[estado] == "Promocionado":
		cont_promo += 1

	acum_promedio += alumno[promedio]

promedioGeneral = acum_promedio / cont_alumnos

porcetajeReprobados = cont_reprobados * 100 / cont_alumnos

print("Cantidad de Alumnos Mujeres:",cont_feme)
print("Cantidad de Alumnos Hombres:",cont_masc)
print("Cantidad de Alumnos promocionados:",cont_promo)
print("Promedio General:",promedioGeneral)
print("Porcentaje Reprobados:",porcetajeReprobados)
