# Los datos se manejar en una biblioteca
# tienen los siguientes datos:
# -Codigo de libro
# -Titulo
# -Autor
# -Editorial
# -Edicion
# -Tipo de Encuadernacion
# -Cantidad de total de ejemplares
#  para prestar
# -Cantidad de ejemplares prestados
# -Genero
#
# A. Cargar todos los libros
# B. Imprimir la cantidad de libros
#    discriminados por:
#    1. Autor
#    2. Editorial
#    3. Genero
# C. Autor y Titulo de todos los aquellos
#    libros que tengan todos sus
#	 sus libros prestados.
# D. Cantidad de libros que no tengan
#    ejemplares para prestar.
# E. Editoriales (nombres) que tienen
#    encuadernacion rustica.
# F. Autores que tienen libros de primera
#    edicion y genero de Terror.

# Nombres de los indices de biblioteca
libros = 0
prestados = 1
noprestados = 2

# Nombres de los indices de los datos del libro
codigo = 0
titulo = 1
autor = 2
editorial = 3
edicion = 4
encuadernacion = 5
genero = 6
estado = 7

# biblioteca = [ [lista_libros], cant_prestados, cant_noprestados ]
biblioteca = []
lista_libros = []
datos_libro = []
cant_libros = 0

# Esto es para pruebas
lista_libros.append([1,"100 Años de Soledad","Marquez","Strada","primera","rustica","novela","no prestado"])
lista_libros.append([2,"Alef","Borges","Santillan","segunda","tapa dura","novela","prestado"])
lista_libros.append([3,"Sistemas de Informacion","Caseros","Fotocopiadora","unica","no tiene tapa","tecnica","prestado"])
cant_libros = 3
biblioteca.append(lista_libros)
lista_libros = []

'''
print("Ingresar los datos del libro",cant_libros+1)
input_titulo = input("Ingresar Titulo\n")

while input_titulo != "pepe" :

	input_codigo = int( input("Ingresar Codigo\n") )
	input_autor = input("Ingresar Autor\n")
	input_editorial = input("Ingresar Editorial\n")
	input_edicion = input("Ingresar Edicion\n")
	input_encuadernacion = input("Ingresar Encuadernacion\n")
	input_genero = input("Ingresar Genero\n")

	datos_libro.append(input_codigo)
	datos_libro.append(input_titulo)
	datos_libro.append(input_autor)
	datos_libro.append(input_editorial)
	datos_libro.append(input_edicion)
	datos_libro.append(input_encuadernacion)
	datos_libro.append(input_genero)

	biblioteca.append(datos_libro)
	cant_libros += 1
	datos_libro = []

	print("Ingresar los datos del libro",cant_libros+1)
	input_titulo = input("Ingresar Titulo\n")
'''

# A.
lista_libros = biblioteca[libros]
cant_prestados = 0
cant_noprestados = 0
# B.
lista_autores = []
lista_editoriales = []
lista_generos = []
cant_libros_autor = 0
cant_libros_editorial = 0
cant_libros_genero = 0

for libro in lista_libros :

	if libro[estado] == "prestado" :
		cant_prestados += 1
	else :
		cant_noprestados += 1

	if (libro[autor] in lista_autores) == 0 :
		lista_autores.append(libro[autor])

	if (libro[editorial] in lista_editoriales) == 0 :
		lista_editoriales.append(libro[editorial])

	if (libro[genero] in lista_generos) == 0 :
		lista_generos.append(libro[genero])


biblioteca.append(cant_prestados)
biblioteca.append(cant_noprestados)


for unAutor in lista_autores :

	for libro in lista_libros :

		if libro[autor] == unAutor :
			cant_libros_autor += 1

	print("Cantidad de libros por autor " + unAutor + ": " + str(cant_libros_autor))
	cant_libros_autor = 0

for unaEditorial in lista_editoriales :

	for libro in lista_libros :

		if libro[editorial] == unaEditorial :
			cant_libros_editorial += 1

	print("Cantidad de libros por editorial " + unaEditorial + ": " + str(cant_libros_editorial))
	cant_libros_editorial = 0

for unGenero in lista_generos :

	for libro in lista_libros :

		if libro[genero] == unGenero :
			cant_libros_genero += 1

	print("Cantidad de libros por genero " + unGenero + ": " + str(cant_libros_genero))
	cant_libros_genero = 0
# C.
lista_libros_prestados = []

