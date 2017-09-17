# Dado un rango entre 1 y 100.
# Indicar si un número ingresado por teclado
# pertenece al rango.
# Indicar si es primo o no.

nro = int( input("Ingresar número\n") )

print("\nComienzo\n")

cont = 0
i = 0

if nro > 0 and nro < 101 :
	print(f"{nro} pertenece al rango.")

	if nro == 1 :
		print(f"{nro} es primo.")

	else :

		while True :
			i += 1
			res = nro % i

			if res == 0 :
				cont += 1

			if cont == 2 :
				break

		if cont == 2 and i == nro :
			print(f"{nro} es primo.")

		else :
			print(f"{nro} no es primo.")

else :
	print(f"{nro} no pertenece al rango.")

print("\nFin\n")