Funcion unNombre <- IngresarNombre
	Imprimir "Ingresar Nombre."
	Leer unNombre
FinFuncion

Funcion unaEdad <- IngresarEdad
	Imprimir "Ingresar Edad."
	Leer unaEdad
FinFuncion

Algoritmo Ejercicio1
	
	// Usando el mismo ejercio de 23Ago-ej10
	//
	// A. Ingresar el nombre y edad de una persona.
	// 		Se pide imprimir el nombre si es o no mayor de edad
	// B. Ingresar por teclado los nombres y edades
	// 		de los alumnos de un curso, la carga termina
	// 		al ingresar 'pepe'.
	// C. Se pide calcular la cantidad de alumnos mayores a 18
	// 		y la cantindad de alumnos con menos de 18.
	// D. Calcular el porcentaje de alumnos mayores de edad.
	// E. Nombre del alumno de mayor edad.
	// 		Nombre del alumno de menor edad.
	// F. Imprimir el promedio de todas las edades.
	// G. Indicar cuantos tienen la edad mayor al promedio.
	
	// El ejercicio G no se puede resolver hasta este punto
	// donde la profe nos enseña el uso de arreglos (Dimension en PSeInt).
	// Ya que nombre solo se alamacena temporalmente en la variable pero
	// despues se sobreescribe con la siguiente iteracion del bucle Mientras.
	// Los arreglos permiten almacenar datos en memoria hasta el fin del algoritmo.
	
	// Ejr. A.
	nombre = IngresarNombre
	edad = IngresarEdad
	
	Si ( edad >= 18 )
		
		Imprimir nombre," es mayor de edad."
		
	SiNo
		
		Imprimir nombre," es menor de edad."
		
	FinSi
	
	mayores = 0
	menores = 0
	igual18 = 0
	totalAlumnos = 0
	elMenor = 9999		// No puede ser cero porque sino nunca funciona
	elMayor = 0
	nombreMenor = ''
	nombreMayor = ''
	acumuladorEdades = 0
	promedio = 0
	
	nombre = IngresarNombre								// Ejr. B
	
	Mientras ( nombre <> 'pepe' )
		
		totalAlumnos = totalAlumnos + 1
		edad = IngresarEdad
		acumuladorEdades = acumuladorEdades + edad		// Ejr. F.
		
		Si ( edad < 18 )
			
			menores = menores + 1						// Ejr. C.
			
			Si ( edad < elMenor )						// Ejr. E.
				
				elMenor = edad
				nombreMenor = nombre
				
			FinSi
			
		SiNo
			
			mayores = mayores + 1						// Ejr. C.
			
			Si ( edad > elMayor )						// Ejr. E.
				
				elMayor = edad
				nombreMayor = nombre
				
			FinSi
			
			Si ( edad == 18 )							// No se pide los de igual a 18 pero
														// la profe lo puso igual.
				igual18 = igual18 + 1
				
			FinSi
			
		FinSi
		
		nombre = IngresarNombre
		
	FinMientras
	
	
	
	porcentajeMayores18 = ( (mayores-igual18) / totalAlumnos) * 100		// Ejr. D.
	promedio = acumuladorEdades / totalAlumnos							// Ejr. F.
	
	Imprimir "Cantidad de Mayores de edad: ",mayores
	Imprimir "Cantidad de Menores de edad: ",menores
	Imprimir "Porcentaje de Mayores: ",porcentajeMayores
	Imprimir "El alumno con menor edad es: ",nombreMenor
	Imprimir "El alumno con mayor edad es: ",nombreMayor
	Imprimir "El promedio de edad es: ",promedio
	
FinAlgoritmo