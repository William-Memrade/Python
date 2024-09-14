# Operadores aritmeticos y conversion de tipos

a = 10
b = 3

print('Suma: ' + str(a+b))
print('Resta: ', (a-b))
print('Resta: ', (b-a))

c = '10'

print(a*b+int(c))
print(a/b)
print(a//b)
print(a % b)
print(a**b)

# precedencia, aplicamos asociaticidad por izquierda
# es decir toma del operador el que este mas a la izquierda
# en este caso a*b esta mas cerca de /
print(a*b/int(c))
