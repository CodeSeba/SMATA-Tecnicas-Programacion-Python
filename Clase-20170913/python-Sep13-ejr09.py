# Teniendo un rango de valores entre 3 y 8 inclusive.
# Calcular el valor acumulado.

print("\nComienzo\n")

suma = 0

for i in range(3,9) :
	suma += i

print( f"El acumulado es {suma}." )

print("---\nUsando un vector y sum()\n---")

vec = range(3,9)

print( f"El acumulado es {sum(vec)}" )

print("\nFin\n")