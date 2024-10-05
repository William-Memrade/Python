# Programa de determinar si un numero es positivo, negativo o cero
numero = float(input('Digite un numero: '))

if numero > 0:
    print("El numero es positivo")
elif numero < 0:
    print("El numero es negativo")
else:
    print("El numero es igual a 0")

a = 1000
b = 30
c = 500

if a > b and a > c:
    print('a es mayor que b y c')
