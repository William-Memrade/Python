# uso de diccionarios
usuario = {
    'usuario': 'alicia',
    'correo': 'alicia@gmail.com',
    'clave': '123456',
    'edad': 20
}

# tamanio
print(len(usuario))

# son ordenados
print(usuario)

# los elementos se acceden por su llave
print(usuario['correo'])

# sus elementos son mutables
usuario['usuario'] = 'alicia2001'
print(usuario)

# anadir quitar elementos (son de tamanio dinamico)
usuario['telefono'] = '55555555'
usuario.pop('clave')
print(usuario)

# recorrer el diccionario
for valor in usuario.values():
    print(f'valor: {valor}')
for llave in usuario.keys():
    print(f'llave: {llave}')
for k, v in usuario.items():
    print(f'{k}: {v}')
