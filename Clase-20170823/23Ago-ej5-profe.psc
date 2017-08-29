// Ingresar 3 valores numericos distintos.
// Calcular
// Si A es mayor: el promedio
// Si B es mayor: el cociente entre B y C
// Si C es mayor: mostrar el menor.

Funcion nro <- valorIngresado
FinFuncion

Algoritmo Ejercicio5
	A = valorIngresado
	B = valorIngresado
	C = valorIngresado
	
	Si ( A > B )
			Si ( A > C )
				promedio = (A + B + C) / 3
				Mostrar "Promedio: ",promedio
			SiNo
				Mostrar "Menor es B"
				Mostrar "Mayor es C"
			FinSi
		SiNo
			Si ( B > C )
				Si ( C <> 0 )
					cociente = B / C
					Mostrar "Cociente: ",cociente
				SiNo
					Mostrar "ERROR"
				FinSi
			SiNo
				Mostrar "Menor es A"
				Mostrar "Mayor es C"
			FinSi
	FinSi
	
FinAlgoritmo
