Funcion unValor <- ValorIngresado
	Mostrar "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio3
	nro1 = ValorIngresado
	nro2 = ValorIngresado
	
	Si (nro1 > nro2)
		resta = nro1 - nro2
		Mostrar "Resta: ",resta
		Si (nro2 <> 0)
			cociente = nro1 / nro2
			Mostrar "Cociente: ",cociente
		FinSi
	FinSi
FinAlgoritmo
