# Ingresar un nurmero por teclado e
# indicar si es par, impar o cero.

print( "Indicar si es para o impar" )

nro = int( input("Ingresar un numero\n") )

if nro == 0 :
	print( "El numero es cero." )
else :
	resto = nro % 2
	if resto == 0 :
		print( nro,"es par." )
	else :
		print( nro,"es impar." )