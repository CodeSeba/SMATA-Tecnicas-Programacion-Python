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
#    libros que tengan todos sus libros
#    prestados.
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

# Datos cargados para pruebas
lista_libros = \
	[
		[1,"100 Años de Soledad","Gabriel García Márquez","Strada","primera","rustica",5,1,"novela"],
		[2,"Alef","Borges","Santillan","segunda","dura",4,2,"novela"],
		[3,"Aura","Carlos Fuentes","Norma","primera","blanda",3,3,"terror"],
		[4,"Don Quijote de La Mancha I","Miguel de Cervantes","Anaya","primera","rustica",2,1,"caballeresco"],
		[5,"Don Quijote de La Mancha II","Miguel de Cervantes","Anaya","segunda","rustica",1,1,"caballeresco"],
		[6,"Historias de Nueva Orleans","William Faulkner","Alfaguara","cuarta","blanda",5,2,"novela"],
		[7,"El principito","Antoine Saint-Exupery","Andina","primera","dura",4,3,"aventura"],
		[8,"El príncipe","Maquiavelo","S.M.","segunda","blanda",3,1,"político"],
		[9,"Diplomacia","Henry Kissinger","S.M.","tercera","dura",2,2,"político"],
		[10,"Doce cuentos peregrinos","Gabriel García Márquez","Debolsillo","primera","blanda",1,1,"terror"],
		[11,"El Último Emperador","Pu-Yi","Caralt","primera","rustica",5,3,"autobiografia"],
		[12,"Fortunata y Jacinta","Pérez Galdós","Plaza & Janés","sexta","blanda",4,4,"novela"]
	]

biblioteca.append(lista_libros)

'''
# Carga de datos mediante imput
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

	lista_libros.append(datos_libro)

	del datos_libro
	cant_libros += 1

	print("Ingresar los datos del libro",cant_libros+1)
	input_titulo = input("Ingresar Titulo\n")

biblioteca.append(lista_libros)
'''

del lista_libros

lista_libros = biblioteca[libros]


# A.
total_prestados = sum( libro[prestados] for libro in lista_libros )
total_noprestados = sum( libro[paraPrestar] - libro[prestados] for libro in lista_libros )

biblioteca.extend( [total_prestados,total_noprestados] )


# B.
lista_diccs = []

for item in [ autor, editorial, genero ] :
	lista_items = [ libro[item] for libro in lista_libros ]
	dicc_items  = { unItem : lista_items.count(unItem) for unItem in lista_items }
	lista_diccs.append(dicc_items)
	del dicc_items

items = ["Autor","Editorial","Genero"]

for i in range(0,3) :
	print( "\n" + "Libros por " + items[i] + "\n" + "-" * 50 )
	for key, valor in lista_diccs[i].items() : print( key,":",valor )


# C.
lista_agotados = [ libro for libro in lista_libros if libro[paraPrestar] - libro[prestados] == 0 ]
print( "\nLibros que estan todos prestados\n" + "=" * 50 )
for libro in lista_agotados : print( libro[autor] + ", \"" + libro[titulo] + "\"" )


# D.
print( "\nCantidad de libros no disponibles:",len(lista_agotados) )
print( "=" * 50 )


# E.
lista_rusticos = { libro[editorial] : "" for libro in lista_libros if libro[encuadernacion] == "rustica" }
print( "\nLista de Editoriales con tapa rustica\n" + "-" * 50 )
for unaEditorial in lista_rusticos : print(unaEditorial)


# F.
lista_autores_1eraTerror = [ libro[autor] for libro in lista_libros if libro[edicion] == "primera" and libro[genero] == "terror" ]
print("\nLista de Autores de Terror con primera edicion" + "\n" + "-" * 50)
for unAutor in lista_autores_1eraTerror : print(unAutor)