# Manejo de listas

nombres = ['alicia', 'beto', 'camila', 'diana', 1, True, [1, 2, 3]]

# obtener el tama;o de la lista
print(f'La lonfigtud de nombres es: {len(nombres)}')
print(nombres)

# Son indexadas
print(nombres[3])

# Modificar elementis
nombres[3] = 'Eva'
print(nombres)

# agregar y quitar nombres
nombres.append('Fran')
nombres.insert(0, 'Gaby')
nombres.remove('Eva')
print(nombres)

# Recorrer un array
for nombre in nombres:
    print(f'Nombre: {nombre}')
