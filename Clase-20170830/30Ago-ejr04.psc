Funcion unValor <- IngresarValor
	Imprimir "Ingresar Valor."
	Leer unValor
FinFuncion

Algoritmo Ejercicio4
	
	// Ingresar 5 valores enteros en el arreglo 'uno' y
	// otros 5 en el arreglo 'dos'.
	// Imprimir los valores de 'uno' que sean
	// distintos de 'dos'.
	
	
	Dimension uno[5],dos[5]
	encontrados = 0
	
	
	Para z = 0 Hasta 4 Con Paso 1			// Carga de datos
		
		Imprimir "Arreglo UNO, posicion ",z,"."
		uno[z] = IngresarValor
		
	FinPara
	
	Para z = 0 Hasta 4 Con Paso 1			// Carga de datos
		
		Imprimir "Arreglo DOS, posicion ",z,"."
		dos[z] = IngresarValor
		
	FinPara
	
	
	Para i = 0 Hasta 4 Con Paso 1
		
		encontrados = 0
		
		Para j = 0 Hasta 4 Con Paso 1
			
			Si ( uno[i] == dos[j] )
				
				encontrados = encontrados + 1
				
			FinSi
			
		FinPara
		
		Si ( encontrados == 0 )
			
			Imprimir "Valor distinto: ",uno[i]
			
		FinSi
		
	FinPara
	
FinAlgoritmo