# Ingresar el nombre de un alumno y sus tres notas por teclado.
# Generar los metodos que:
# -Carguen los datos.
# -Imprimir los datos.
# -Calcular el promedio.
# -Imprimir nombre, promedio y si aprobo o no.


# Inicio de clase Alumno
class Alumno:
	
	def __init__(self):
		self.nombre = ""
		self.notas = []
		self.promedio = 0

	def cargarDatos(self):
		self.nombre = input("Ingresar Nombre:\n")
		
		for i in range(3):
			self.notas.append( int(input("Ingresar Nota "+str(i+1)+":\n")) )

		print("")

	def imprimirDatos(self):
		print("Nombre:", self.nombre)
		print("Notas: ",end="")

		for unaNota in self.notas: print(unaNota,end=", ")

		print("\n")

	def calcularPromedio(self):
		cant_notas = len(self.notas)

		for unaNota in self.notas: self.promedio += unaNota

		self.promedio /= cant_notas

	def imprimirInforme(self):
		print("Alumno:", self.nombre)
		print("Promedio:", round(self.promedio,2))

		estado = "Aprobado" if self.promedio > 4 else "A Marzo"

		print("Estado:",estado)

# Fin de clase Alumno

# Main
unAlumno = Alumno()

unAlumno.cargarDatos()
unAlumno.imprimirDatos()
unAlumno.calcularPromedio()
unAlumno.imprimirInforme()