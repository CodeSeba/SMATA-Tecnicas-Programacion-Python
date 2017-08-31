Funcion unValor <- IngresarValor
	Imprimir "Ingresar Valor."
	Leer unValor
FinFuncion

Algoritmo Ejercicio2
	
	// Cargar 5 valores en un arreglo 'num' y
	// otros 5 en el arreglo 'valor'.
	// Deben imprimir el arreglo 'suma' con la suma
	// de cada posicion de los arreglos.
	
	Dimension aValor[5],num[5],suma[5]		// Valor es una palabra reservada de PSeInt,
											// se utiliza entonces aValor.
	
	Para z = 0 Hasta 4 Con Paso 1			// Carga de datos
		
		Imprimir "Arreglo VALOR, posicion ",z,"."
		aValor[z] = IngresarValor
		
	FinPara
	
	Para z = 0 Hasta 4 Con Paso 1			// Carga de datos
		
		Imprimir "Arreglo NUM, posicion ",z,"."
		num[z] = IngresarValor
		
	FinPara
	
	Para z = 0 Hasta 4 Con Paso 1			// Carga de datos
		
		Imprimir "Arreglo SUMA, posicion ",z,"."
		suma[z] = IngresarValor
		
	FinPara
	
	
	Para i = 0 Hasta 4 Con Paso 1
		
		suma[i] = aValor[i] + num[i]
		Imprimir suma[i]
		
	FinPara
	
FinAlgoritmo