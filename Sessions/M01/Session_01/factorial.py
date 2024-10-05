# Programa para calcular factoriales
# 5! = 5 * 4 * 3 * 2 * 1

# for

n = int(input('Digite un numero: '))

f = 1

for i in range(2, n + 1):
    f *= i

print(f'El factorial de {n} es: {f}')

# while

f = 1
i = 2

while i < n + 1:
    f *= i
    i += 1

print(f'El factorial de {n} es: {f}')
