# Ingresar 2 numeros por teclado
# Devolver el cociente entre ambos

n1 = int( input("Ingresar nro 1\n") )

n2 = int( input("Ingresar nro 2\n") )

if n2 == 0:
	print( "ERROR" )
else:
	print( n1 / n2 )