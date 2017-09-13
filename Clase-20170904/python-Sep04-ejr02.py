# Ingresar 2 numeros por teclado
# Indicar si la division es exacta o no (resto igual cero)

n1 = int( input("Ingresar nro 1\n") )

n2 = int( input("Ingresar nro 2\n") )

if n2 == 0:
	print( "ERROR" )
else:
	res =  n1 % n2

if res == 0:
	print( "La devision es exacta" )
else:
	print( "La division no es exacta" )