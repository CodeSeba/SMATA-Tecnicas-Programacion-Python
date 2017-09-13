# Ingresar un número por teclado.
# Imprimir su tabla de multiplicar
# Hasta el 12.

nro = int( input("Ingresar número\n") )
print("---")

factor = 1

while factor < 13 :
	print(nro,"x",factor,"=",nro * factor)
	factor += 1

print("---")
print("Usando un FOR")
print("---")

# range(inicio,fin) incluye inicio pero no incluye fin.

for i in range(1,13) :
	print(nro,"x",i,"=",nro * i)
