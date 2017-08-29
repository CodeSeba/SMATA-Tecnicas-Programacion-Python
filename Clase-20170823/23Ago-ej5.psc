// Ingresar 3 valores numericos distintos.
// Calcular
// Si A es mayor: el promedio
// Si B es mayor: el cociente entre B y C
// Si C es mayor: mostrar el menor.

Funcion unValor <- ValorIngresado
	Mostrar "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio5
	A = ValorIngresado
	B = ValorIngresado
	C = ValorIngresado
	
	Si ( A > B )
		Si ( A > C )
			promedio = (A + B + C) / 3
			Mostrar "Promedio: ",promedio
		FinSi
	FinSi
	
	Si ( B > A )
		Si ( B > C )
			Si ( C <> 0 )
				cociente = B / C
				Mostrar "Cociente: ",cociente
			FinSi
		FinSi
	FinSi
	
	
	Si ( C > A)
		Si ( C > B)
			Si ( A > B)
				Mostrar "Menor es B"
			SiNo
				Mostrar "Menor es A"
			FinSi
		FinSi
	FinSi
	
FinAlgoritmo
