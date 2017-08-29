Funcion unNombre <- IngresarNombre
	Mostrar "Ingresar Nombre"
	Leer unNombre
FinFuncion

Funcion unaEdad <- IngresarEdad
	Mostrar "Ingresar Edad"
	Leer unaEdad
FinFuncion

Algoritmo Ejercicio10
	// A. Ingresar el nombre y edad de una persona.
	// 	Se pide imprimir el nombre si es o no mayor de edad.
	// B. Ingresar por teclado los nombres y edades
	// 	de los alumnos de un curso, la carga termina
	// 	al ingresar 'pepe'.
	// C. Se pide calcular la cantidad de alumnos mayores a 18
	// 	y la cantindad de alumnos con menos de 18.
	// D. Calcular el porcentaje de alumnos mayores de edad.
	
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
	
	nombre = IngresarNombre
  
  	Mientras ( nombre <> 'pepe' )

    		edad = IngresarEdad
		totalAlumnos = totalAlumnos + 1
		
		Si ( edad < 18 )          // C.
			menores = menores + 1
		SiNo
			Si ( edad == 18 )
				igual18 = igual18 + 1
			Sino
				mayores = mayores + 1
			FinSi
		FinSi
    
		nombre = IngresarNombre		
    
	FinMientras
	
	porcentajeMayores = ( mayores / totalAlumnos) * 100     // D.
	
	Mostrar "Cantidad de Mayores de edad: ",mayores
  	Mostrar "Cantidad de 18 años de edad: ",igual18         // No se solicita pero la profe lo puso igual.
	Mostrar "Cantidad de Menores de edad: ",menores
	Mostrar "Porcentaje de Mayores de edad: ",Trunc(porcentajeMayores),"%"

FinAlgoritmo
