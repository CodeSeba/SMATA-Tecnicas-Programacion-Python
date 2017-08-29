Funcion unNombre <- IngresarNombre
	Mostrar "Ingresar Nombre."
	Leer unNombre
FinFuncion

Funcion unaEdad <- IngresarEdad
	Mostrar "Ingresar Edad."
	Leer unaEdad
FinFuncion

Algoritmo Ejercicio1
	// Usando el mismo ejercio de 23Ago-ej10
	//
	// A. Ingresar el nombre y edad de una persona
	// Se pide imprimir el nombre si es o no mayor de edad
	// B. Ingresar por teclado los nombres y edades
	// de los alumnos de un curso, la carga termina
	// al ingresar 'pepe'
	// Se pide calcular la cantidad de alumnos mayores a 18
	// y la cantindad de alumnos con menos de 18
	// calcular el porcentaje de alumnos mayores de edad.
	// C. Nombre del alumno de mayor edad.
	// Nombre del alumno de menor edad.
	// D. Imprimir el promedio de todas las edades.
	// E. Indicar cuantos tienen edad mayor al promedio.
	
	// A.
	nombre = IngresarNombre
	edad = IngresarEdad
	
	Si ( edad >= 18 )
		Mostrar nombre," es mayor de edad."
	SiNo
		Mostrar nombre," es menor de edad."
	FinSi
	
	// B.
	
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
	
	nombre = IngresarNombre
	
	Mientras ( nombre <> 'pepe' )
		totalAlumnos = totalAlumnos + 1
		edad = IngresarEdad
		acumuladorEdades = acumuladorEdades + edad		// Ej. D.
		
		Si ( edad < 18 )
			
			menores = menores + 1
			
			Si ( edad < elMenor )		// Ej. C.
				elMenor = edad
				nombreMenor = nombre
			FinSi
			
		SiNo
			
			mayores = mayores + 1
			
			Si ( edad > elMayor )		//Ej. C.
				elMayor = edad
				nombreMayor = nombre
			FinSi
			
			Si ( edad == 18 )		// No se pide los de igual a 18
				igual18 = igual18 + 1
			FinSi
			
		FinSi
		
		nombre = IngresarNombre
	FinMientras
	
	
	porcentajeMayores18 = ( (mayores-igual18) / totalAlumnos) * 100
	promedio = acumuladorEdades / totalAlumnos
	
	Mostrar "Cantidad de Mayores de edad: ",mayores
	Mostrar "Cantidad de Menores de edad: ",menores
	Mostrar "Porcentaje de Mayoures: ",porcentajeMayores
	Mostrar "El alumno con menor edad es: ",nombreMenor
	Mostrar "El alumno con mayor edad es: ",nombreMayor
	Mostrar "El promedio de edad es: ",promedio
	
FinAlgoritmo