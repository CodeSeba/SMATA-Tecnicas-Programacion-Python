# Se realiza la inscripcion de socios en un club.
# La carga de datos finaliza cuando se ingresa
# como nombre "pepe".
#
# Los datos a ingresar son:
# -Nombre
# -Apellido
# -Edad
# -Sexo
# -Deporte
#
# Los deportes son:
# -Futbol
# -Hockey
# -Handball
# -Tenis
# -Natacion
#
# Para calcular la Categoria se usa
# la siguiente tabla:
# -Menor - 0 a 3 años.
# -Infantil - 3 a 6 años.
# -PreMini - 6 a 9 años.
# -Mini - 9 a 12 años.
# -Cadete - 12 a 15 años.
# -Juvenil - 15 a 18 años.
# -Activo - 18 a 60 años.
# -Vitalicio - Mayores a 60 años.
#
# 1. Imprimir Nombre, Categoria y Deporte.

# (Ejercicios Agregados el 23 de Oct.)
# 2. Total de socios con categoria "Activo".
# 3. Total de socios con categoria "Juvenil" y sexo "Femenino".
# 4. Total de socios con categoria "Mini", sexo "Masculino" y
#    deporte "Futbol".
# 5. Promedio de mujeres inscriptos en "Hockey".
# 6. Total de socios con sexo "Femenino" y deporte "Hockey".
# 7. Total de socios con categoria "Mini" y deporte "Tenis".
# 8. Total de socios que practican "Natacion".
# 9. Pocentaje de socios que practican "Natacion".
# 10. Pocentaje de socios con sexo "Femenino".
# 11. Total de socios discriminados por:
#     -Genero
#     -Deporte
#     -Categoria


# Nombre de los indices
nombre = 0
apellido = 1
edad = 2
sexo = 3
deporte = 4
categoria = 5

'''
# Carga de datos mediante input
datos_socio = []
lista_socios = []
cant_socios = 0

print("Ingresar los datos del socio",cant_socios+1)
input_nombre = input("Ingresar Nombre\n")

while input_nombre != "pepe" :

	input_apellido = input("Ingresar Apellido\n")
	input_edad = int(input("Ingresar Edad\n"))
	input_sexo = input("Ingresar Genero\n")
	input_deporte = input("Ingresar Deporte\n")

	datos_socio.append(input_nombre)
	datos_socio.append(input_apellido)
	datos_socio.append(input_edad)
	datos_socio.append(input_sexo)
	datos_socio.append(input_deporte)
	
	lista_socios.append(datos_socio)

	datos_socio = []
	cant_socios += 1
	print("-"*50)

	print("Ingresar los datos del socio",cant_socios+1)
	input_nombre = input("Ingresar Nombre\n")
'''

# Carga de datos para pruebas
lista_socios = \
	[
		["Gregoire","Kropach",3,"Masculino","Hockey"],
		["Braden","MacDavitt",5,"Masculino","Futbol"],
		["Giorgia","Oattes",7,"Femenino","Futbol"],
		["Skippy","Gullefant",10,"Masculino","Hockey"],
		["Vito","Titterell",15,"Masculino","Natacion"],
		["Braden","Griston",16,"Masculino","Hockey"],
		["Rupert","Rutley",20,"Masculino","Hockey"],
		["Niles","Dobey",66,"Masculino","Futbol"],
		["Stanleigh","Oluwatoyin",2,"Masculino","Hockey"],
		["Lena","Kift",17,"Femenino","Handball"],
		["Raoul","DeZuani",20,"Masculino","Natacion"],
		["Brooky","Espinheira",9,"Femenino","Tenis"]
	]

for unSocio in lista_socios :
	
	if unSocio[edad] in range(0,3) :
		unaCategoria = "Menor"
	elif unSocio[edad] in range(3,6) :
		unaCategoria = "Infantil"
	elif unSocio[edad] in range(6,9) :
		unaCategoria = "PreMini"
	elif unSocio[edad] in range(9,12) :
		unaCategoria = "Mini"
	elif unSocio[edad] in range(12,15) :
		unaCategoria = "Cadete"
	elif unSocio[edad] in range(15,18) :
		unaCategoria = "Juvenil"
	elif unSocio[edad] in range(18,60) :
		unaCategoria = "Activo"
	elif unSocio[edad] >= 60 :
		unaCategoria = "Vitalicio"

	unSocio.append(unaCategoria)


print("Lista de socios")
print("="*50)
print("")

# 2.
lista_activos = [ unSocio for unSocio in lista_socios
	if unSocio[categoria] == "Activo" ]

# 3.
lista_juv_fem = [ unSocio for unSocio in lista_socios
	if unSocio[categoria] == "Juvenil" and unSocio[sexo] == "Femenino" ]

# 4.
lista_min_mas_fut = [ unSocio for unSocio in lista_socios
	if unSocio[categoria] == "Mini" and unSocio[sexo] == "Masculino" and unSocio[deporte] == "Futbol" ]

# 5.
cant_femeninos = len([unSocio for unSocio in lista_socios
	if unSocio[sexo] == "Femenino"])
# 6.
cant_fem_hoc = len([unSocio for unSocio in lista_socios
	if unSocio[sexo] == "Femenino" and unSocio[deporte] == "Hockey"])

#promedio_fem_hoc = 

# 7.
cant_min_ten = len([unSocio for unSocio in lista_socios
	if unSocio[categoria] == "Mini" and unSocio[deporte] == "Tenis"])

# 8.
cant_natacion = len([unSocio for unSocio in lista_socios
	if unSocio[deporte] == "Natacion"])

# 9.
cant_socios = len(lista_socios)
print("Cantidad Natacion:",cant_natacion)
print("Cantidad Socios:",cant_socios)
porcentaje_natacion = cant_natacion *100 // cant_socios
print("Porcentaje natacion:",porcentaje_natacion)

# 10.
cant_femeninos = len([unSocio for unSocio in lista_socios
	if unSocio[sexo] == "Femenino"])

porcentaje_femeninos = cant_femeninos * 100 // cant_socios

# 11.
dicc_genero = {}
dicc_deporte = {}
dicc_categoria = {}

for unSocio in lista_socios :
	dicc_genero[unSocio[sexo]] = dicc_genero.get(unSocio[sexo],0) + 1
	dicc_deporte[unSocio[deporte]] = dicc_deporte.get(unSocio[deporte],0) + 1
	dicc_categoria[unSocio[categoria]] = dicc_categoria.get(unSocio[categoria],0) + 1

# 1.
for unSocio in lista_socios :
	print("Nombre: " + unSocio[nombre])
	print("Categoria: " + unSocio[categoria])
	print("Deporte: " + unSocio[deporte])
	print("-"*50)

print("\nLista de socios Activos")
print("="*50)
for unSocio in lista_activos :
	print("Nombre: " + unSocio[nombre])
	print("Apellido: " + unSocio[apellido])


print("\nLista con categoria Juvenil y genero Femenino")
print("="*50)
for unSocio in lista_juv_fem :
	print("Nombre: " + unSocio[nombre])
	print("Apellido: " + unSocio[apellido])


print("\nLista con categoria Mini, genero Masculino y deporte Futbol")
print("="*50)
for unSocio in lista_min_mas_fut :
	print("Nombre: " + unSocio[nombre])
	print("Apellido: " + unSocio[apellido])


print("\nTotal de socios con genero Femenino y deporte Hockey:", cant_fem_hoc)
print("\nTotal de socios con categoria Mini y deporte Tenis:", cant_min_ten)
print("\nTotal de socios con deporte Natacion:", cant_natacion)
print("\nPorcentaje de socios con deporte Natacion:", porcentaje_natacion)
print("\nPorcentaje de socios con genero Femenino:", porcentaje_femeninos)


print("\nTotal de socios por Genero")
print("="*50)
for key, valor in dicc_genero.items():
	print(key,":",valor)

print("\nTotal de socios por Deporte")
print("="*50)
for key, valor in dicc_deporte.items():
	print(key,":",valor)

print("\nTotal de socios por Categoria")
print("="*50)
for key, valor in dicc_categoria.items():
	print(key,":",valor)