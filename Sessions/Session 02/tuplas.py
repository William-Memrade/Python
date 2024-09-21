# Manejo de tuplas
lenguajes = ('C++', 'Python', 'Java', 'JavaScript', 1, (2, 3))

# son ordenadas
print(lenguajes)

# son indexadas
print(lenguajes[1])

# las tuplas son inmutables, sus elementos no cambian
# lenguajes[2] = 'C#'

# las tuplas son de tamanio estatico
# lenguajes.index
lista = list(lenguajes)
print(type(lista), lista)

# recorrer una tupla
for lenguaje in lenguajes:
    print(f'lenguaje: {lenguaje}')
