Funcion resultado = Agregar (unaLista,unElemento)
		
FinFuncion

Algoritmo sin_titulo
	Inicio
	Reales: libros[]
	Dimension libro[5]
	Dimension imprimirLista[5]
	
	Para Cada libro De lista_libros
		
		Si libro[tapa] == "rustica" Entonces
			
			Si libro noesta en lista_libros Entonces
				
				Agregar(imprimirLista,libro) 
				
			FinSi
			
		FinSi
		
	FinPara
	
	Para cada libro De imprimirLista
		
		Imprimir libro
		
	FinPara

FinAlgoritmo
