# Los datos se manejar en una biblioteca
# tienen los siguientes datos:
# -Codigo de libro
# -Titulo
# -Autor
# -Editorial
# -Edicion
# -Tipo de Encuadernacion
# -Cantidad de total de ejemplares para prestar
# -Cantidad de ejemplares prestados
# -Genero
#
# A. Cargar todos los libros.
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

# Nombres de los indices de los datos del libro
codigo = 0
titulo = 1
autor = 2
editorial = 3
edicion = 4
encuadernacion = 5
paraPrestar = 6
prestados = 7
genero = 8

# biblioteca = [ [lista_libros], total_prestados, total_noprestados ]
datos_libro = []
lista_libros = []
biblioteca = []


# Esto es para pruebas
datos_libro = [1,"100 Años de Soledad","Marquez","Strada","primera","rustica",10,1,"novela"]
lista_libros.append(datos_libro)
datos_libro = [2,"Alef","Borges","Santillan","segunda","tapa dura",20,1,"novela"]
lista_libros.append(datos_libro)
datos_libro = [3,"Sistemas de Informacion","Caseros","Fotocopiadora","unica","no tiene tapa",30,1,"tecnica"]
lista_libros.append(datos_libro)
datos_libro = [4,"Alef, segunda parte","Borges","Santillan","segunda","tapa dura",40,1,"novela"]
lista_libros.append(datos_libro)
datos_libro = [5,"Alef, tercera parte","Borges","Santillan","segunda","tapa dura",10,10,"novela"]
lista_libros.append(datos_libro)
datos_libro = [6,"Libro6","Autor6","Editorial6","primera","tapa dura",5,4,"terror"]
lista_libros.append(datos_libro)

biblioteca.append(lista_libros)

del datos_libro
del lista_libros

'''
cant_libros = 0
print("Ingresar los datos del libro",cant_libros+1)
input_titulo = input("Ingresar Titulo\n")

while input_titulo != "pepe" :

	input_codigo = int( input("Ingresar Codigo\n") )
	input_autor = input("Ingresar Autor\n")
	input_editorial = input("Ingresar Editorial\n")
	input_edicion = input("Ingresar Edicion\n")
	input_encuadernacion = input("Ingresar Encuadernacion\n")
	input_paraPrestar = int( input("Ingresar cantidad para Prestar\n") )
	input_prestados = int( input("Ingresar cantidad de Prestador\n") )
	input_genero = input("Ingresar Genero\n")

	datos_libro.append(input_codigo)
	datos_libro.append(input_titulo)
	datos_libro.append(input_autor)
	datos_libro.append(input_editorial)
	datos_libro.append(input_edicion)
	datos_libro.append(input_encuadernacion)
	datos_libro.append(input_genero)

	biblioteca.append(datos_libro)
	del datos_libro
	cant_libros += 1

	print("Ingresar los datos del libro",cant_libros+1)
	input_titulo = input("Ingresar Titulo\n")
'''


lista_libros = biblioteca[libros]


# A.
total_prestados = sum( libro[prestados] for libro in lista_libros )
total_noprestados = sum( libro[paraPrestar] - libro[prestados] for libro in lista_libros )

biblioteca.append(total_prestados)
biblioteca.append(total_noprestados)


# B.
lista_autores = [ libro[autor] for libro in lista_libros ]
dicc_autores =  { unAutor : lista_autores.count(unAutor) for unAutor in lista_autores }

lista_editoriales = [ libro[editorial] for libro in lista_libros ]
dicc_editoriales =  { unaEditorial : lista_editoriales.count(unaEditorial) for unaEditorial in lista_editoriales }

lista_generos = [ libro[genero] for libro in lista_libros ]
dicc_generos =  { unGenero : lista_generos.count(unGenero) for unGenero in lista_generos }

lista_diccs = { "Autor" : dicc_autores, "Editorial" : dicc_editoriales, "Genero" : dicc_generos }

print("Cantidad de Libros por:\n" + "=" * 50)

for unDicc in lista_diccs :
	print( unDicc + "\n" + "-" * 50 )
	for key, valor in lista_diccs[unDicc].items() :
		print( key,":",valor )
	print("\n")


# C.
lista_agotados = [ libro for libro in lista_libros if libro[paraPrestar] - libro[prestados] == 0 ]
print("Libros que estan todos prestados\n" + "=" * 50)
for libro in lista_agotados : print( libro[autor] + ", \"" + libro[titulo] + "\"" )


# D.
print("\n" + "=" * 50)
print( "Cantidad de libros no disponibles:",len(lista_agotados) )
print("=" * 50)


# E.
lista_rusticos = [ libro[editorial] for libro in lista_libros if libro[encuadernacion] == "rustica" ]
print("\nLista de Editoriales con tapa rustica" + "\n" + "-" * 50)
for unaEditorial in lista_rusticos : print(unaEditorial)


# F.
lista_autores_1eraTerror = [ libro[autor] for libro in lista_libros if libro[edicion] == "primera" and libro[genero] == "terror" ]
print("\nLista de Autores de Terror con primera edicion" + "\n" + "-" * 50)
for unAutor in lista_autores_1eraTerror : print(unAutor)