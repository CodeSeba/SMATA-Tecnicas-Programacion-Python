# Ingresar numeros por teclado, el ingreso
# termina cuando se ingresa un cero.
# Indicar cuantos pares e impares se ingresaron.

print( "Cuantos pares e impares" )

# Se debe inicializar nro, pares e impares porque
# estas variables son consultadas en operadores.
# Si no tienen asignado ningun valor antes de ser
# consultados se generan errores de sintaxis.

nro = 1
pares = 0
impares = 0

while nro != 0 :
	nro = int( input("Ingresar un numero\n") )

	resto = nro % 2

	if resto == 0 :
		pares += 1
	else :
		impares += 1

print( "---" )
print( "Pares:",pares,"Impares:",impares )