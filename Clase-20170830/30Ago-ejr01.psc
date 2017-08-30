Funcion unValor <- IngresarValor
	Imprimir "Ingresar Valor."
	Leer unValor
FinFuncion

Algoritmo Ejercicio1
	
	// Ingresar por teclado 5 nurmeros enteros,
	// almacenarlos en un vector e
	// imprimir el vector ordenado en forma desc.
	// Ingresar al menos un valor negativo.
	
	Dimension vector[5]
	
	Para z = 1 Hasta 5 Con Paso 1			// Carga de datos
		vector[z] = IngresarValor
	FinPara
	
	
	
	Para i = 1 Hasta 4 Con Paso 1
		
		Para j = i+1 Hasta 5 Con Paso 1
			
			Si ( vector[i] < vector[j] )
				
				auxiliar = vector[i]
				vector[i] = vector[j]
				vector[j] = auxiliar
				
			FinSi
		FinPara
	FinPara
	
	Para i =1 Hasta 5 Con Paso 1
		Imprimir vector[i]
	FinPara
	
FinAlgoritmo
	