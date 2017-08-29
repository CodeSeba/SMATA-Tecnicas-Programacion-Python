Funcion unNombre <- IngresarNombre
	Mostrar "Ingresar Nombre."
	Leer unNombre
FinFuncion

Funcion unaEdad <- IngresarEdad
	Mostrar "Ingresar Edad."
	Leer unaEdad
FinFuncion

Algoritmo Ejercicio2
	
	Dimension arregloNombre[5]
	Dimension arregloEdad[5]
	
	Para i = 1 Hasta 5 Con Paso 1
		arregloNombre[i] = IngresarNombre
		arregloEdad[i] = IngresarEdad
	FinPara
	
	Para j = 1 Hasta 5 Con Paso 1
		Mostrar arregloNombre[j],', ',arregloEdad[j],' años.'
	FinPara
	
FinAlgoritmo
