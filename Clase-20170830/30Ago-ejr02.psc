Funcion unValor <- IngresarValor
	Imprimir "Ingresar Valor."
	Leer unValor
FinFuncion

Algoritmo Ejercicio2
	
	// Cargar 5 valores en un arreglo 'num' y
	// otros 5 en el arreglo 'valor'.
	// Deben imprimir el arreglo 'suma' con la suma
	// de cada posicion de los arreglos.
	
	Dimension avalor[5]
	Dimension num[5]
	Dimension suma[5]
	
	Para z = 1 Hasta 5 Con Paso 1			// Carga de datos
		Imprimir "Arreglo valor."
		avalor[z] = IngresarValor
		Imprimir "Arreglo num."
		num[z] = IngresarValor
	FinPara
	
	
	
	Para i = 1 Hasta 5 Con Paso 1
		
		suma[i] = avalor[i] + num[i]
		
	FinPara
	
	Para j =1 Hasta 5 Con Paso 1
		
		Imprimir suma[j]
		
	FinPara
	
FinAlgoritmo