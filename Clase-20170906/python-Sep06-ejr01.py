# Ingresar por teclado el año actual y otro año cualquiera.
# Imprmir la cantidad de años transcurridos o la 
# cantidad de años que faltan.
# Si ambos son iguales indicarlo tambien.

print( "Calculo de la diferencia entre dos años" )

año1 = int( input("Ingresar año 1\n") )
año2 = int( input("Ingresar año 2\n") )

resultado = año1 - año2

if resultado == 0:
	print( "Los años son iguales" )
elif resultado > 0:
	print( "En",año1,"trasncurrieron",resultado,"años desde",año2 )
else:
	resultado = resultado * -1
	print( "Desde",año1,"faltan",resultado,"años hasta",año2 )