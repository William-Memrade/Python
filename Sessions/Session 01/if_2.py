# Programa para determinar si una persona es mayor de edad
# condiciones simples y anidadas

edad = int(input('Digite su edad: '))

if edad > 0 and edad < 18:
    print('No es adulto')
elif edad >= 18 and edad <= 60:
    print('Es adulto')
elif edad > 60 and edad <= 110:
    print('Es adulto de tercera edad')
else:
    print('Edad no valida')
