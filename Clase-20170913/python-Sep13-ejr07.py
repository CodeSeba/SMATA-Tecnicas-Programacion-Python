# Mostrar cuantos números multiplos de 3
# hay entre 1 y 12.

print("\nComienzo\n")

acum = 0

for i in range(1,13) :
	res = i % 3

	if ( res == 0 ) :
		acum += 1
		print( f"{i} es multiplo de 3." )

print( f"Total encontrados: {acum}" )

print("\nFin\n")