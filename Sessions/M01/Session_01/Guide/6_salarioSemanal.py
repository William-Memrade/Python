# Programa para calcular el sueldo o salario semanal de una persona

name = str(input('Ingrese el nombre del empleado: '))
dui = int(input('Ingrese el DUI (sin guiones): '))
horas = int(input('Ingrese la cantidad de horas trabajadas: '))

# variables fijas
jornada = 40
valorHora = 10.00
extras = horas - jornada
valorHoraExtra = valorHora * 2

if horas <= jornada:
    salario = valorHora * horas
else:
    salario = jornada * valorHora
    salario += (extras * valorHoraExtra)

print(f'El salario a devengar por el empleado {name} con DUI {dui}'
      + f'es de $: {salario}')
