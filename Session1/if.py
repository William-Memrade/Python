edad = int(input('Digite su edad: '))

if edad > 18:
    print('Es adulto')
    print('Porque tiene mas de 18')
    if edad > 60:
        print('Y es adulto de la tercera edad')
else:
    print('No es adulto')

print('Afuera del if')
