# Programa para calcular factoriales
# 5! = 5 * 4 * 3 * 2 * 1

n = int(input('Digite un numero: '))

f = 1

for n in range(2, n+1):
    f *= n

print(f'El factorial de {n} es: {f}')