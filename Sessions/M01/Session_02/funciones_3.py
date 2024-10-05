# multiples valores de retorno

def aritme(a, b):
    return a + b, a - b, a * b, a / b, a % b, a ** b, a // b


print(aritme(10, 5))


# retornos multiples
def dias_mes(mes):
    if mes == 12 or mes == 10:
        return 31
    elif mes == 6 or 11:
        return 30
    elif mes == 2:
        return 28
    else:
        return 0


print(dias_mes(12))


# valores por default
def suma(a, b, c=0, d=0):
    return a + b + c + d


print(suma(1, 3))
print(suma(1, 3, 5))
print(suma(1, 3, 5, 10))
