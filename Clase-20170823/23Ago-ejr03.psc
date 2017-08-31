Funcion unValor <- ValorIngresado
	Imprimir "Ingresar Valor"
	Leer unValor
FinFuncion

Algoritmo Ejercicio3
	
	nro1 = ValorIngresado
	nro2 = ValorIngresado
	
	Si ( nro1 > nro2 )
		
		resta = nro1 - nro2
		Imprimir  "Resta: ",resta
		
		Si ( nro2 <> 0 )
			
			cociente = nro1 / nro2
			Imprimir "Cociente: ",cociente
			
		FinSi
		
	FinSi
	
FinAlgoritmo
