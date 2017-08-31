Funcion unValor <- ValorIngresado
	Imprimir "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio6
	
	// Usando el operador % resto
	nro1 = ValorIngresado
	resto = nro1 % 2
	
	Si ( resto == 0 )
		
		Imprimir "Nro1 es Par"
		
	SiNo
		
		Imprimir "Nro1 es Impar"
		
	FinSi
	
	// Usando el operador // entero
	nro1 = ValorIngresado
	parteEntera = Trunc( nro1 / 2 ) // es igual a parteEntera = nro1 // 2
	cociente = nro1 / 2
	
	Si ( parteEntera == cociente )
		
		Imprimir "Nro1 es Par"
		
	SiNo
		
		Imprimir "Nro1 es Impar"
	FinSi
	
FinAlgoritmo