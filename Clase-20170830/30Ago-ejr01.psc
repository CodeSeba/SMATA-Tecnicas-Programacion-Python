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
	auxiliar = 0
	
	Para z = 0 Hasta 4 Con Paso 1			// Carga de datos
		
		vector[z] = IngresarValor
		
	FinPara
	
	
	Para pos = 0 Hasta 3 Con Paso 1
		
		Para sig = pos+1 Hasta 4 Con Paso 1
			
			Si ( vector[pos] < vector[sig] )
				
				auxiliar = vector[pos]
				vector[pos] = vector[sig]
				vector[sig] = auxiliar
				
			FinSi
			
		FinPara
		
	FinPara
	
	Para i =0 Hasta 4 Con Paso 1
		
		Imprimir vector[i]
		
	FinPara
	
FinAlgoritmo