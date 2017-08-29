Funcion unNombre <- IngresarNombre
	Imprimir "Ingresar Nombre."
	Leer unNombre
FinFuncion

Funcion unaNota <- IngresarNota
	Imprimir "Ingresar Nota."
	Leer unaNota
FinFuncion

Algoritmo Ejercicio3
	// Dada una comision de 5 alumnos ingresar
	// nombre y las 2 notas obtenidas.
	// Calcular
	// A. El promedio de cada alumno.
	// B. El promedio general.
	// D. El promedio mas alto.
	// E. El promedio mas bajo.
	// Imprimir
	// C. El nombre de todos los alumnos cuyo
	// 		promedio sea superior al promedio general
	// D. El nombre del promedio mas alto junto al nombre.
	// E. Lo mismo para el menor promedio.
	// F. Los nombres ordenados en forma descendente
	//		por promedio.
	
	Dimension nombreAlumno[5]
	Dimension nota1[5]
	Dimension nota2[5]
	Dimension promedioAlumno[5]
	acumuladoPromedio = 0
	acumuladoTotal = 0
	promedioGeneral = 0
	promedioMasAlto = 0
	promedioMasBajo = 99
	nombreMax = 99
	nombreMin = 99
	auxiliarPromedio = 0
	auxiliarNombre = ""
	
		
	
	Para i = 1 Hasta 5 Con Paso 1		// Carga de datos
		nombreAlumno[i] = IngresarNombre
		nota1[i] = IngresarNota
		nota2[i] = IngresarNota
	FinPara
	
	
	
	Para j = 1 Hasta 5 Con Paso 1
		
		promedioAlumno[j] = ( nota1[j] + nota2[j] ) / 2				// Ejr. A.
		acumuladoPromedio = acumuladoPromedio + promedioAlumno[j]
		
		Imprimir "Nombre: ",nombreAlumno[j],", Promedio: ",promedioAlumno[j]
		
	FinPara
	
	
	
	promedioGeneral = acumuladoPromedio / 5							//Ejr. B.
	
	Imprimir "Promedio General: ",promedioGeneral
	
	
	
	Para k = 1 Hasta 5 Con Paso 1
		
		Si ( promedioAlumno[k] > promedioGeneral )					// Ejr. C
			Imprimir "El alumno ",nombreAlumno[k]," supera el promedio general."
		FinSi
		
		Si ( promedioAlumno[k] > promedioMasAlto )					// Ejr. D
			promedioMasAlto = promedioAlumno[k]
			nombreMax = k
		SiNo
			Si ( promedioAlumno[k] < promedioMasBajo )				// Ejr. E
				promedioMasBajo = promedioAlumno[k]
				nombreMin = k
			FinSi
		FinSi
		
	FinPara
	
	Imprimir "El alumno ",nombreAlumno[nombreMax]," tiene el promedio mas alto con ",promedioMasAlto
	Imprimir "El alumno ",nombreAlumno[nombreMin]," tiene el promedio mas bajo con ",promedioMasBajo
	
	
	
	Para z = 4 Hasta 1 Con Paso -1									// Ejr. F
		
		Para t = 1 Hasta z-1 Con Paso 1
			
			Si ( promedioAlumno[t] < promedioAlumno[t+1] )
				
				auxiliarPromedio = promedioAlumno[t]
				auxiliarNombre = nombreAlumno[t]
				
				promedioAlumno[t] = promedioAlumno[t+1]
				nombreAlumno[t] = nombreAlumno[t+1]
				
				promedioAlumno[t+1] = auxiliarPromedio
				nombreAlumno[t+1] = auxiliarNombre
				
			FinSi
		FinPara
	FinPara
	
	Para ord = 1 Hasta 5 Con Paso 1
		Imprimir promedioAlumno[ord]," - ",nombreAlumno[ord]
	FinPara
	
	
	
FinAlgoritmo