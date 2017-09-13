# Mostrar cuantos números multiplos de 3
# hay entre 1 y 12.

print("Comienzo")

acum = 0

for i in range(1,13) :
	res = i % 3

	if ( res == 0 ) :
		acum += 1
		print(i,"es multiplo de 3.")

print("Total encontrados:",acum)

print("Fin")