Funcion unValor <- IngresarValor
	Imprimir "Ingresar Valor."
	Leer unValor
FinFuncion

Algoritmo Ejercicio3
	
	// Ingresar 5 valores enteros en el arreglo 'uno' y
	// otros 5 en el arreglo 'dos'.
	// Imprimir los valores encontrados en ambos arreglos.
	
	Dimension uno[5]
	Dimension dos[5]
		
	Para z = 1 Hasta 5 Con Paso 1			// Carga de datos
		Imprimir "Arreglo uno."
		uno[z] = IngresarValor
		Imprimir "Arreglo dos."
		dos[z] = IngresarValor
	FinPara
	
	Para i = 1 Hasta 4 Con Paso 1
		
		Para j = i Hasta 5 Con Paso 1
			
			Si ( uno[i] == dos[j] )
				
				Imprimir "Repetido: ",uno[i]
				
			FinSi
		FinPara
	FinPara
	
FinAlgoritmo
	