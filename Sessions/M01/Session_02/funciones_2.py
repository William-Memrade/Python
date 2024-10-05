# paso por valor y referencia

# paso por copia
x = 5


def modificar_variable(y):
    y += 2
    return y


modificar_variable(x)
print(x)

# por direccion (listas, set, diccionario y tipos propios)
v = [3, 9, 5]


# se puede definirel tipo de dato, colocando : ejemplo
# : list, pero no es necesario y no es definicion solo ayuda
def modificar_vector(z: list):
    z.append(4)
    return z


modificar_vector(v)
print(v)
