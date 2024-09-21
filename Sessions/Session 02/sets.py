# uso de set
equipos = {'Real Madrid', 'Barcelona', 'Manchester City', 'Liverpool', 1,
           (1, 2), frozenset({1, 2})}

# longitud
print('La longitud es de: ', {len(equipos)})

# son desordenados
print(equipos)

# no son indexadas
# print(equipos[2])

# son de tamanio dinamico
equipos.add('Arsenal')
print(equipos)
equipos.discard('Liverpool')
print(equipos)
equipos.add('Real Madrid')
print(equipos)

# recorrer un set
for equipo in equipos:
    print(f'equipo: {equipo}')
