# 1. Ingresar por teclado los valores de
#    los lados de un rectangulo.
#    Calcular:
#    - Perimetro [ 2 * (l1 + l2) ]
#    - Area [ l1 * l2 ]

'''
# Carga de datos mediante input
L1 = int ( input("Ingresar L1\n") )
L2 = int ( input("Ingresar L2\n") )
'''

# Datos cargados para pruebas
L1 = 4
L2 = 6

perimetro = 2 * ( L1 + L2 )
area = L1 * L2

print("Perimetro de un rectangulo:",perimetro)
print("Area de un rectangulo:",round(area,2))