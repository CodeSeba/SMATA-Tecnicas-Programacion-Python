Algoritmo Ejercicio6
	
	// Usando el operador % resto
	nro1 = valorIngresado
	resto = nro1 % 2
	
	Si ( resto == 0 )
		Mostrar "Nro1 es Par"
	SiNo
		Mostrar "Nro1 es Impar"
	FinSi
	
	// Usando el operador // entero
	nro1 = valorIngresado
	parteEntera = nro1 - (nro1 % 2) // es igual a parteEntera = nro1 // 2
	cociente = nro1 / 2
	
	Si ( parteEntera == cociente )
		Mostrar "Nro1 es Par"
	SiNo
		Mostrar "Nro1 es Impar"
	FinSi
	
FinAlgoritmo
