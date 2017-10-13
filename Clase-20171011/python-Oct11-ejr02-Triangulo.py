# 1. Ingresar por teclado los valores de
#    los lados de un triangulo.
#    Calcular:
#    - Perimetro [ l1 + l2 + l3 ]
#    - Area [ ( s * (s - l1) * (s - l2) * (s - l3) ) ** (1/2) ]
#    Nota: s = semisuma = perimetro / 2

'''
# Carga de datos mediante input
L1 = int ( input("Ingresar L1\n") )
L2 = int ( input("Ingresar L2\n") )
L3 = int ( input("Ingresar L3\n") )
'''

# Datos cargados para pruebas
L1 = 4
L2 = 6
L3 = 8

perimetro = L1 + L2 + L3
# Semisuma
s = perimetro / 2	
area = ( s * (s - L1) * (s - L2) * (s - L3) ) ** (1/2)

print("Perimetro de un triangulo:",perimetro)
print("Area de un triangulo:",round(area,2))