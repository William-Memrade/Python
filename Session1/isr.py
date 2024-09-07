# Programa para calculas el impuesto sobre la renta

sueldo = float(input('Digite el salario: '))

if sueldo <= 1000:
    isss = sueldo * 0.03
else:
    isss = 30

afp = sueldo * 0.0725
sg = sueldo - isss - afp

if sg >= 0.01 and sg <= 472:
    isr = 0
elif sg >= 472.01 and sg <= 895.24:
    isr = (sueldo - 472) * 0.1 + 17.67
elif sg >= 895.25 and sg <= 2038.10:
    isr = (sueldo - 895.24) * 0.2 + 60
elif sg >= 2038.11:
    isr = (sueldo - 2038.10) * 0.3 + 288.57

print(f'El impuesto sobre la renta es: ${isr:.2f}')
