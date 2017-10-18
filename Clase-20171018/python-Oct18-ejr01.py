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
# Imprimir Nombre, Categoria y Deporte.


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

for unSocio in lista_socios :
	print("Nombre: " + unSocio[nombre])
	print("Categoria: " + unSocio[categoria])
	print("Deporte: " + unSocio[deporte])
	print("-"*50)