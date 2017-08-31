Funcion unValor <- ValorIngresado
	Imprimir "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio5
	
	// Ingresar 3 valores numericos distintos.
	// Calcular
	// Si A es mayor: el promedio
	// Si B es mayor: el cociente entre B y C
	// Si C es mayor: imprimir el menor.
	
	A = ValorIngresado
	B = ValorIngresado
	C = ValorIngresado
	
	Si ( A > B )
		
		Si ( A > C )
			
			promedio = (A + B + C) / 3
			Imprimir "Promedio: ",promedio
			
		SiNo
			
			Imprimir "Menor es B"
			Imprimir "Mayor es C"
			
		FinSi
		
	SiNo
		
		Si ( B > C )
			
			Si ( C <> 0 )
				
				cociente = B / C
				Imprimir "Cociente: ",cociente
				
			SiNo
				Imprimir "ERROR"
				
			FinSi
			
		SiNo
			
			Imprimir "Menor es A"
			Imprimir "Mayor es C"
			
		FinSi
		
	FinSi
	
FinAlgoritmo
