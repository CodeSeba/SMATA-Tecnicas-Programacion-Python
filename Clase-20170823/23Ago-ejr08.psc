Funcion unValor <- ValorIngresado
	Imprimir "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio8
	
	// Dada una lista de nro positivos que finaliza al ingresar un cero.
	// Se pide mostrar:
	// Cantidad de positivos
	// Cantidad de negativos
	// Cantidad de pares
	// Cantidad de impares
	
	pares = 0
	impares = 0
	positivos = 0
	negativos = 0
	
	Hacer
		
		nro = ValorIngresado
		resto = nro % 2
		
		Si ( resto == 0 )
			
			pares = pares + 1
			
		SiNo
			
			impares = impares + 1
			
		FinSi
		
		Si ( nro > 0)
			
			positivos = positivos + 1
			
		SiNo
			
			negativos = negativos + 1
			
		FinSi
		
	Hasta Que nro == 0
	
	Imprimir "Cantidad Positivos: ",positivos
	Imprimir "Cantidad Negativos: ",negativos
	Imprimir "Cantidad Pares: ",pares
	Imprimir "Cantidad Impares: ",impares
	
FinAlgoritmo
