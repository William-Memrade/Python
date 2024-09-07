import unicodedata

# Programa para uso de operadores de comparacion

a = 10
b = 3

print(a == b)  # True | False
print(a != b)
print(a < b)
print(a > b)
print(a <= b)
print(a >= b)

# cadenas
cad1 = 'hola'
cad2 = 'Hola'
print('cadenas:', cad1.lower() == cad2.lower())
print('cadenas:', cad1.lower() != cad2.lower())
cad3 = 'canción'
# cad3 = cad3.replace('ó', 'o')
print(unicodedata.normalize('NFD', cad3).encode('ASCII', 'ignore')
      .decode('UTF-8'))
