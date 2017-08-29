Funcion TomarCartaDe(Pila)
FinFuncion

Funcion DepositarEn(Pila)
FinFuncion

Funcion Incrementar(variable) // El PSeInt no permite ++
FinFuncion

Funcion Interrumpir // No existe Interrumpir en Segun..Hacer, o no lo encontre todavia.
FinFuncion




Algoritmo UltimoDelMiercoles
	
	//DEFINICION DE VARIABLES
	Definir CantB,CantC,CantE,CantO,MenorCant,MayorCant Como Entero // Para que no tire errores en PSeInt
	// Definir Fmenor,Fmayor Como Caracter; // Esto si queres usar manzanas! jajaja.
	
	CantB = 0		// Variable para contar la cantidad de BASTOS
	CbarB = 0		// Variable para contar la cantidad boca arriba de BASTOS
	CantC = 0		// Variable para contar la cantidad de COPAS
	CbarC = 0		// Variable para contar la cantidad boca arriba de COPAS
	CantO = 0		// Variable para contar la cantidad de OROS
	CbarO = 0		// Variable para contar la cantidad boca arriba de OROS
	CantE = 0		// Variable para contar la cantidad de ESPADAS
	CbarE = 0		// Variable para contar la cantidad boca arriba de ESPADAS
	MenorCant = 0	// Variable para evaluar la pila que tiene la Menor cantidad de cartas
	MayorCant = 0	// Variable para evaluar la pila que tiene la Mayor cantidad de cartas
	
	Fmenor = 0		// Variable (Flag), para identificar el Palo de la pila que tiene menor cantidad.
					// 1=Bastos \u2013 2=Copas \u2013 3=Oros \u2013 4=Espadas
					// Se utilizan al final del programa en los SEGUN XXX HACER
	Fmayor = 0		// Variable (Flag), para identificar el Palo de la pila que tiene mayor cantidad.
					// 1=Bastos \u2013 2=Copas \u2013 3=Oros \u2013 4=Espadas
					// Se utilizan al final del programa en los SEGUN XXX HACER
	
					// No, yo me lo sabía con manzanas !!
	// Fmenor='';	// En caso de no querer usar números, puedo usar letras
					// Variable para identificar el Palo de la pila que tiene menos Cartas
					// B=Bastos \u2013 C=Copas \u2013 O=Oros \u2013 E=Espadas
	// Fmayor='';	//Variable para identificar el Palo de la pila que tiene mas Cartas
					// B=Bastos , C=Copas , O=Oros , E=Espadas
	
	
	
	
	Mientras ( PilaB <> Vacio )		// Recorro la primer pila contando la Cantidad de bastos y la cantidad que están boca arriba.
		TomarCartaDe(PilaB)
		Incrementar(CantB)			// Cuenta la cantidad de cartas en la pila
		Si (Carta<>BocaAbajo)		// pregunto si no esta boca abajo
			Incrementar(CbarB)		// Cuenta la cantidad de cartas boca arriba
		FinSi
		DepositarEn(PilaX)
	FinMientras
	
	MenorCant = CantB		// Como es la primer pila que recorrí, asumo que tiene MenorCant cant. de cartas
	MayorCant = CantB		// Del mismo modo, asumo que es la que tiene Mayor cant. de cartas
	Fmenor = 1				// Diciendo que el palo con menos cartas es Bastos
	Fmayor = 1				// Y que también Bastos es el palo con mas cartas.
	
	
	
	
	Mientras ( PilaC <> Vacio )		// Recorro la segunda pila contando la Cantidad de copas y la cantidad que están boca arriba.
		TomarCartaDe(PilaC)
		Incrementar(CantC)			// Cuenta la cantidad de cartas en la pila
		Si (Carta<>BocaAbajo)		// pregunto si no esta boca abajo
			Incrementar(CbarC)		// Cuenta la cantidad de cartas boca arriba
		FinSi
		DepositarEn(PilaX)
	FinMientras
	
	Si ( CantC < MenorCant )	// Verifico si CantC es menor al MenorCant asignado antes
		MenorCant = CantC		// Si es así, asigno el nuevo menor al la variable MenorCant
		Fmenor = 2				// Y digo que el palo con menos cartas es 2 (Copas)
	FinSi						// Si no ocurre, el menor seguirá siendo el palo anterior
	Si ( CantC > MayorCant )	// Verifico si CantC es mayor al MayorCant asignado antes
		MayorCant = CantC 		// Si es así, asigno el nuevo mayor al la variable MayorCant
		Fmayor = 2 				// Y digo que el palo con más cartas es 2 (Copas)
	FinSi 						// Si no ocurre, el mayor seguirá siendo el palo anterior
	
	
	
	
	Mientras ( PilaO <> Vacio )		// Recorro la tercer pila contando la Cantidad de oros y la cantidad que están boca arriba.
		TomarCartaDe(PilaO)
		Incrementar(CantO)			// Cuenta la cantidad de cartas en la pila
		Si (Carta<>BocaAbajo)		// pregunto si no esta boca abajo
			Incrementar(CbarO)		// Cuenta la cantidad de cartas boca arriba
		FinSi
		DepositarEn(PilaX)
	FinMientras
	
	Si ( CantO < MenorCant )	// Verifico si CantO es menor al MenorCant encontrado antes
		MenorCant = CantO		// Si es así, asigno CantO al la variable MenorCant
		Fmenor = 3				// Y digo que el palo con menos cartas es 3 (Oros)
	FinSi						// Si no ocurre, el menor seguirá siendo el antes encontrado
	Si ( CantO > MayorCant )	// Verifico si CantO es mayor al MayorCant encontrado antes
		MayorCant = CantO		// Si es así, asigno CantO al la variable MayorCant
		Fmayor = 3				// Y digo que el palo con más cartas es 3 (Oros)
	FinSi						// Si no ocurre, el mayor seguirá siendo el antes encontrado
	
	
	
	
	Mientras ( PilaE <> Vacio )		// Recorro la última pila contando la Cantidad de espadas y la cantidad que están boca arriba.
		TomarCartaDe(PilaE)
		Incrementar(CantE)			// Cuenta la cantidad de cartas en la pila
		Si (Carta<>BocaAbajo)		// pregunto si no esta boca abajo
			Incrementar(CbarE)		// Cuenta la cantidad de cartas boca arriba
		FinSi
		DepositarEn(PilaX)
	FinMientras
	
	Si ( CantE < MenorCant )	// Verifico si CantE es menor al MenorCant encontrado antes
		MenorCant = CantE		// Si es así, asigno CantE al la variable MenorCant
		Fmenor = 4				// Y digo que el palo con menos cartas es 4 (Espadas)
	FinSi						// Si no ocurre, el menor seguirá siendo el antes encontrado
	Si ( CantE > MayorCant )	// Verifico si CantE es mayor al MayorCant encontrado antes
		MayorCant = CantE		// Si es así, asigno CantE al la variable MayorCant
		Fmayor = 4				// Y digo que el palo con más cartas es 4 (Espadas)
	FinSi						// Si no ocurre, el mayor seguirá siendo el antes encontrado
	
	
	
	
	// Punto a) Cantidad de cartas de cada palo
	Escribir 'La cantidad de Basto es: ' + CantB
	Escribir 'La cantidad de Copa es: ' + CantC
	Escribir 'La cantidad de Oros es: ' + CantO
	Escribir 'La cantidad de Espadas es: ' + CantE
	
	
	
	
	// Punto b) Pila con más cantidad de cartas.
	Segun Fmayor Hacer
		Caso 1:
			Escribir 'La pila de Bastos tiene más cartas ( ' + MayorCant + ' )'
			Interrumpir
		Caso 2:
			Escribir 'La pila de Copas tiene más cartas ( ' + MayorCant + ' )'
			Interrumpir
		Caso 3:
			Escribir 'La pila de Oros tiene más cartas ( ' + MayorCant + ' )'
			Interrumpir
		Caso 4:
			Escribir 'La pila de Espadas tiene más cartas ( ' + MayorCant + ' )'
			Interrumpir
		De Otro Modo: // Por defecto:
			Escribir 'Error'
	FinSegun
	
	
	
	
	// Punto c) Pila con menos cantidad de cartas.
	Segun Fmenor Hacer
		Caso 1:
			Escribir 'La pila de Bastos tiene menos cartas ( ' + MenorCant + ' )'
			Interrumpir
		Caso 2:
			Escribir 'La pila de Copas tiene menos cartas ( ' + MenorCant + ' )'
			Interrumpir
		Caso 3:
			Escribir 'La pila de Oros tiene menos cartas ( ' + MenorCant + ' )'
			Interrumpir
		Caso 4:
			Escribir 'La pila de Espadas tiene menos cartas ( ' + MenorCant + ' )'
			Interrumpir
		De Otro Modo: // Por defecto:
			Escribir 'Error'
	FinSegun
	
	
	
	
	// Punto d) Porcentaje de cartas boca arriba de cada pila.
	Escribir 'El porcentaje de Bastos boca arriba es: ' + (CbarB * 100 / CantB)
	Escribir 'El porcentaje de Copas boca arriba es: ' + (CbarC * 100 / CantC)
	Escribir 'El porcentaje de Oros boca arriba es: ' + (CbarO * 100 / CantO)
	Escribir 'El porcentaje de Espadas boca arriba es: ' + (CbarE * 100 / CantE)
	
FinAlgoritmo

