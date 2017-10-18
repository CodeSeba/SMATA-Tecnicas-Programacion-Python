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
datos_inscripto = []
lista_inscriptos = []
cant_inscriptos = 0

print("Ingresar los datos del inscripto",cant_inscriptos+1)
input_nombre = input("Ingresar Nombre\n")

while input_nombre != "pepe" :

	input_apellido = input("Ingresar Apellido\n")
	input_edad = int(input("Ingresar Edad\n"))
	input_sexo = input("Ingresar Genero\n")
	input_deporte = input("Ingresar Deporte\n")

	datos_inscripto.append(input_nombre)
	datos_inscripto.append(input_apellido)
	datos_inscripto.append(input_edad)
	datos_inscripto.append(input_sexo)
	datos_inscripto.append(input_deporte)
	
	lista_inscriptos.append(datos_inscripto)

	datos_inscripto = []
	cant_inscriptos += 1
	print("-"*50)

	print("Ingresar los datos del inscripto",cant_inscriptos+1)
	input_nombre = input("Ingresar Nombre\n")
'''

# Carga de datos para pruebas
lista_inscriptos = \
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

for unInscripto in lista_inscriptos :
	
	if unInscripto[edad] in range(0,3) :
		unaCategoria = "Menor"
	elif unInscripto[edad] in range(3,6) :
		unaCategoria = "Infantil"
	elif unInscripto[edad] in range(6,9) :
		unaCategoria = "PreMini"
	elif unInscripto[edad] in range(9,12) :
		unaCategoria = "Mini"
	elif unInscripto[edad] in range(12,15) :
		unaCategoria = "Cadete"
	elif unInscripto[edad] in range(15,18) :
		unaCategoria = "Juvenil"
	elif unInscripto[edad] in range(18,60) :
		unaCategoria = "Activo"
	elif unInscripto[edad] >= 60 :
		unaCategoria = "Vitalicio"

	unInscripto.append(unaCategoria)


print("Lista de Inscriptos")
print("="*50)
print("")

for unInscripto in lista_inscriptos :
	print("Nombre: " + unInscripto[nombre])
	print("Categoria: " + unInscripto[categoria])
	print("Deporte: " + unInscripto[deporte])
	print("-"*50)
