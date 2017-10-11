# 1. Ingresar por teclado los valores de
#    los lados de un rectangulo.
#    Calcular:
#    - Perimetro [ 2 * (l1 + l2) ]
#    - Area [ l1 * l2 ]
#
# 2. Idem 1 pero para un triangulo
#    - Perimetro [ l1 + l2 + l3 ]
#    - Area [ b * h / 2 ]

geometria = int( input("Ingresar 1 para rectangulo, 2 para triangulo.\n") )

'''
# Carga de datos mediante input
if  geometria == 1 :
	L1 = int ( input("Ingresar L1\n") )
	L2 = int ( input("Ingresar L2\n") )
elif geometria == 2 :
	L1 = int ( input("Ingresar L1\n") )
	L2 = int ( input("Ingresar L2\n") )
	L3 = int ( input("Ingresar L3\n") )
else :
	print("No es una opcion valida.")
'''
# Datos cargas para pruebas
L1 = 4
L2 = 6
L3 = 8

if  geometria == 1 :
	perimetro = 2 * ( L1 + L2 )
	area = L1 * L2

	print("Perimetro de un rectangulo:",perimetro)
	print("Area de un rectangulo:",round(area,2))

elif geometria == 2 :
	perimetro = L1 + L2 + L3
	area = (((L1 + L2 - L3) * (L1 - L2 + L3) * (-L1 + L2 +L3) * (L1 + L2 + L3)) ** (1/2)) / 4

	print("Perimetro de un triangulo:",perimetro)
	print("Area de un triangulo:",round(area,2))
else :
	print("No es una opcion valida.")

