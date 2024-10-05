# Uso de listas y diccionarios
personas = ['fran', 'eva', 'diego', 'luis']

print('La lista de personas tiene un tamano de: ', len(personas))
print(personas[1])

personas.append('diana')
personas.remove('fran')
personas.pop(0)
print(personas)

for p in personas:
    print(p)

alumno1 = {
    'nombre': 'alicia',
    'guia1': 9,
    'guia2': 10,
    'guia3': 9.5,
    'eval_teo': 10,
    'EF_Prac': 10
}

alumno2 = {
    'nombre': 'beto',
    'guia1': 10,
    'guia2': 9,
    'guia3': 8.5,
    'eval_teo': 9,
    'EF_Prac': 9
}

lista_alumnos = [alumno1, alumno2]
print('Evaluacion final de ', alumno1['nombre'], 'nota: ', alumno1['EF_Prac'])
print('Evaluacion final de ', alumno2['nombre'], 'nota: ', alumno2['EF_Prac'])
