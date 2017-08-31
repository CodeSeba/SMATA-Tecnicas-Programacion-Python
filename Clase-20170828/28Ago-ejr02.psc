Funcion unNombre <- IngresarNombre
	Imprimir "Ingresar Nombre."
	Leer unNombre
FinFuncion

Funcion unaEdad <- IngresarEdad
	Imprimir "Ingresar Edad."
	Leer unaEdad
FinFuncion

Algoritmo Ejercicio2
	
	Dimension arregloNombre[5]
	Dimension arregloEdad[5]
	
	// Recordar que los arreglos son en base cero.
	// La primera posicion es 0 y la ultima es N-1.
	// En este ejemplo los arreglos son de 5 posiciones
	// entonces la ultima posicion es 5-1 -> 4.
	
	Para i = 0 Hasta 4 Con Paso 1			// Carga de datos.
		
		arregloNombre[i] = IngresarNombre
		arregloEdad[i] = IngresarEdad
		
	FinPara
	
	Para j = 0 Hasta 4 Con Paso 1
		
		Imprimir arregloNombre[j],', ',arregloEdad[j],' años.'
		
	FinPara
	
FinAlgoritmo
