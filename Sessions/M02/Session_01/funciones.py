# Uso de listas y diccionarios
def saludo(nombre='Python'):
    print(f'Hola {nombre}')


saludo('Eva')
saludo()


def sumar(a, b, c=0, d=0):
    s = a+b+c+d
    return s


print(sumar(10, 20))
x = sumar(10, 20, 40)
print(x)
print(sumar(10, 20, 30, 40))
print(sumar(10, 20, d=100))


def numero(n):
    if n > 0:
        return 'positivo'
    elif n < 0:
        return 'negativo'
    else:
        return 'es cero'


print(numero(-0.1))
