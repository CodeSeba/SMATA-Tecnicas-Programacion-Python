Funcion nombre <- IngresarNombre
FinFuncion

Funcion edad <- IngresarEdad
FinFuncion

Algoritmo Ejercicio7
	// A. Ingresar el nombre y edad de una persona
	// Se pide imprimir el nombre si es o no mayor de edad
	// B. Ingresar por teclado los nombres y edades
	// de los alumnos de un curso, la carga termina
	// al ingresar 'pepe'
	// Se pide calcular la cantidad de alumnos mayores a 18
	// y la cantindad de alumnos con menos de 18
	// calcular el porcentaje de alumnos mayores de edad.
	
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
	totalAlumnos = 0
	
	Hacer
		nombre = IngresarNombre
		edad = IngresarEdad
		totalAlumnos = totalAlumnos + 1
		
		Si ( edad < 18 )
			menores = menores + 1
		SiNo
			mayores = mayores + 1
		FinSi
		
	Hasta Que ( nombre == 'pepe' )
	
	porcentajeMayores = ( mayores / totalAlumnos) * 100
	
	Mostrar "Cantidad de Mayores de edad: ",mayores
	Mostrar "Cantidad de Menores de edad: ",menores
	Mostrar "Porcentaje de Mayoures: ",porcentajeMayores

FinAlgoritmo