# Programa para calcular el promedio de notas

horas = int(input('Ingrese la cantidad de horas: '))
minutos = int(input('Ingrese la cantidad de minutos: '))

# Variables fijas
costo = 1.50
minuto = 60

minutosExtra = minutos - minuto
print("minutosExtra", minutosExtra)

while minutosExtra >= 0:
    horas += 1
    minutosExtra -= minuto
    print("minutosExtraWhile", minutosExtra)

print("horas", horas)

# totalCancelar = horas * costo
# print(f'Monto total a cancelar {totalCancelar}')
