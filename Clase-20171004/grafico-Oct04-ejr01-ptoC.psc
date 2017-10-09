Algoritmo sin_titulo
	Dimension libro[5]
	Dimension lista_libros[10]
	
	Para Cada libro De lista_libros
		Si libro[paraPrestar] - libro[prestados] == 0 Entonces
			Imprimir libro[autor]
			Imprimir libro[titulo]
		FinSi
	FinPara
	
FinAlgoritmo
