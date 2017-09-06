# Ingresar por teclado el annio actual y otro annio cualquiera.
# Imprmir la cantidad de annios transcurridos o la 
# cantidad de annios que faltan.
# Si ambos son iguales indicarlo tambien.

print( "Calculo de la diferencia entre dos annios" )

annio1 = int( input("Ingresar annio 1\n") )
annio2 = int( input("Ingresar annio 2\n") )

resultado = annio1 - annio2

if resultado == 0:
	print( "Los annios son iguales" )
elif resultado > 0:
	print( "Trasncurrieron",resultado,"annios desde",annio2 )
else:
	resultado = resultado * -1
	print( "Faltan",resultado,"annios para",annio2 )
