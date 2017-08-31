Funcion unValor <- ValorIngresado
	Imprimir "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio5
	
	// Ingresar 3 valores numericos distintos.
	// Calcular
	// Si A es mayor: el promedio
	// Si B es mayor: el cociente entre B y C
	// Si C es mayor: mostrar el menor.
	
	A = ValorIngresado
	B = ValorIngresado
	C = ValorIngresado
	
	Si ( A > B )
		
		Si ( A > C )
			
			promedio = (A + B + C) / 3
			Imprimir "Promedio: ",promedio
			
		FinSi
		
	FinSi
	
	Si ( B > A )
		
		Si ( B > C )
			
			Si ( C <> 0 )
				
				cociente = B / C
				Imprimir "Cociente: ",cociente
				
			FinSi
			
		FinSi
		
	FinSi
	
	
	Si ( C > A)
		
		Si ( C > B)
			
			Si ( A > B)
				
				Imprimir "Menor es B"
				
			SiNo
				
				Imprimir "Menor es A"
				
			FinSi
			
		FinSi
		
	FinSi
	
FinAlgoritmo
