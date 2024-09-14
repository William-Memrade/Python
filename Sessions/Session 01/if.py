# Programa para determinar si una persona es mayor de edad
# condiciones simples y anidadas

edad = int(input('Digite su edad: '))

if edad > 18:
    print('Es adulto')
    print('Porque tiene mas de 18')
    if edad > 60:
        print('Y es adulto de la tercera edad')
else:
    print('No es adulto')

print('Afuera del if')

# Aunque permite espacios, en practica solo tab
if edad < 5:
    print('Es infante')
