Funcion unValor <- ValorIngresado
	Imprimir "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio4
	
	nro1 = ValorIngresado
	nro2 = ValorIngresado
	nro3 = ValorIngresado
	
	nroMayor = nro1
	
	Si ( nro2 > nroMayor )
		
		nroMayor = nro2
		
	FinSi
	
	Si	( nro3 > nroMayor )
		
		nromayor = nro3
		
	FinSi
	
	Imprimir "El mayor es: ", nroMayor
	
FinAlgoritmo
