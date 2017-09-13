# Dado un rango entre 1 y 100.
# Indicar si un número ingresado por teclado
# pertenece al rango.
# Indicar si es primo o no.

nro = int( input("Ingresar número\n") )

print("\nComienzo\n")

cont = 0
i = 1

if nro > 0 and nro < 101 :
	print(nro,"pertenece al rango.")

	while cont < 3 and i < (nro+1) :
		res = nro % i
		
		if res == 0 :
			cont += 1

		i += 1

	if cont < 3 :
		print(nro,"es primo.")
	else :
		print(nro,"no es primo.")

else :
	print(nro,"no pertenece al rango.")

print("\nFin\n")