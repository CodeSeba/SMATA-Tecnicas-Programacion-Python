# Ingresar 2 numeros por teclado
# Indicar cual es el mayor y cual es el menor

n1 = int( input("Ingresar nro 1\n") )

n2 = int( input("Ingresar nro 2\n") )

if n1 == n2 :
	print( "ERROR, los numeros son iguales." )
else :
	if n1 < n2 :
		print( "El menor es",n1 )
		print( "El mayor es",n2 )
	else :
		print( "El menor es",n2 )
		print( "El mayor es",n1 )
		
# Usando un arreglo y .sort() que ordena de forma ascendente.
print( "\nUsando un Arreglo.\n" )

if n1 == n2 :
	print( "ERROR, los numeros son iguales." )
else :
	a = [n1,n2]
	a.sort()
	print( "El menor es",a[0] )
	print( "El mayor es",a[1] )
