# Programa para calcular el promedio de notas

nota1 = float(input('Ingrese el valor de la primera nota: '))
nota2 = float(input('Ingrese el valor de la segunda nota: '))
nota3 = float(input('Ingrese el valor de la tercera nota: '))
nota4 = float(input('Ingrese el valor de la cuarta nota: '))

notas = [nota1, nota2, nota3, nota4]
print(f'Notas procesadas: {notas}')

notas.sort()
notas.pop(0)

sumNotas = 0
print(f'Notas para promedio: {notas}')

for nota in notas:
    sumNotas += nota

promedio = sumNotas / len(notas)
print(f'El promedio de notas es de: {promedio:.2f}')
