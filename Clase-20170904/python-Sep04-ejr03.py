# Ingresar 2 numeros por teclado
# Indicar cual es el mayor y cual es el menor

n1 = int( input("Ingresar nro 1\n") )

n2 = int( input("Ingresar nro 2\n") )

if n1 == n2 :
	print( "ERROR" )
else :
	if n1 > n2 :
		print( n1,"es mayor que",n2)
	else :
		print( n2,"es mayor que",n1)