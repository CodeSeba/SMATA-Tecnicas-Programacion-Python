Funcion unValor <- ValorIngresado
	Mostrar "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio7
	// Dada una lista de nro positivos que finaliza al ingresar
	// un cero.  Se pide indicar cuantos nros ingresados son pares
	// y cuantos son impares.
	
	pares = 0
	impares = 0
	
	Hacer
		nro = ValorIngresado
		resto = nro % 2
		
		Si ( resto == 0 )
			pares = pares + 1
		SiNo
			impares = impares + 1
		FinSi
		
	Hasta Que nro == 0
	
	Mostrar "Cantidad Pares: ",pares
	Mostrar "Cantidad Impares: ",impares
	
FinAlgoritmo
