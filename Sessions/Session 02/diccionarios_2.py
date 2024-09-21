# uso de diccionarios
u1 = {
    'id': '1',
    'usuario': 'alicia',
    'correo': 'alicia@gmail.com',
    'rol': {1: 'gerente', 2: 'admin'}
}
u2 = {
    'id': '2',
    'usuario': 'beto',
    'correo': 'beto@gmail.com',
    'rol': {3: 'ventas', 4: 'users', 5: 'rrhh'}
}

lista_usuarios = []
lista_usuarios.append(u1)
lista_usuarios.append(u2)
print(lista_usuarios)

# como imprimir el correo de beto?
print(lista_usuarios[1]['correo'])

# como imprimir el rol 2 de alicia?
print(lista_usuarios[0]['rol'][2])

# como imprimir los roles de beto (llave: valor)?
for k, v in lista_usuarios[1]['rol'].items():
    print(f"{k}: {v}")
