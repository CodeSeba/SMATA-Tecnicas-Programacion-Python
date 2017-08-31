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
	//    A. El promedio de cada alumno.
	//    B. El promedio general.
	//    D. El promedio mas alto.
	//    E. El promedio mas bajo.
	// Imprimir
	//    C. El nombre de todos los alumnos cuyo
	//       promedio sea superior al promedio general
	//    D. El nombre del promedio mas alto junto al nombre.
	//    E. Lo mismo para el menor promedio.
	//    F. Los nombres ordenados en forma descendente
	//		 por promedio.
	
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
	
	
	Para z = 0 Hasta 4 Con Paso 1			// Carga de datos
		
		nombreAlumno[z] = IngresarNombre
		nota1[z] = IngresarNota
		nota2[z] = IngresarNota
		
	FinPara
	
	
	Para t = 0 Hasta 4 Con Paso 1
		
		promedioAlumno[t] = ( nota1[t] + nota2[t] ) / 2				// Ejr. A.
		acumuladoPromedio = acumuladoPromedio + promedioAlumno[t]	// Ejr. B.
		
		Imprimir "Nombre: ",nombreAlumno[t],", Promedio: ",promedioAlumno[t]
		
	FinPara
	
	
	promedioGeneral = acumuladoPromedio / 5							//Ejr. B.
	Imprimir "Promedio General: ",promedioGeneral
	
	
	Para k = 0 Hasta 4 Con Paso 1
		
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
	
	
	Para pos = 0 Hasta 3 Con Paso 1									// Ejr. F
		
		Para sig = pos+1 Hasta 4 Con Paso 1
			
			Si ( promedioAlumno[pos] < promedioAlumno[sig] )
				
				auxiliarPromedio = promedioAlumno[pos]
				auxiliarNombre = nombreAlumno[pos]
				
				promedioAlumno[pos] = promedioAlumno[sig]
				nombreAlumno[pos] = nombreAlumno[sig]
				
				promedioAlumno[sig] = auxiliarPromedio
				nombreAlumno[sig] = auxiliarNombre
				
			FinSi
			
		FinPara
		
	FinPara
	
	Para i = 0 Hasta 4 Con Paso 1
		
		Imprimir promedioAlumno[i]," - ",nombreAlumno[i]
		
	FinPara
	
FinAlgoritmo