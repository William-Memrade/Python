# programa para uso de funciones

# definicion de la funcion
def mi_primera_funcion():
    print('Esta es mi primera funcion')
    print('Esta es otra linea')


# invocar la funcion
mi_primera_funcion()


# funcion que retorna un valor
def suma(a, b):
    # c = a + b
    return a + b


print(suma(20, 5))
c = suma(10, 5)
print(f'suma: {c}')
