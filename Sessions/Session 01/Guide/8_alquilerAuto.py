# Programa para calcular el costo del alquiler de un vehiculo

km = float(input('Ingrese la cantidad de km recorridos: '))

# variables fijas
iva = 0.13
montoFijo = 30.00
montoAdicional = 0.25
montoAdicionalExtra = 0.50

kmFijo = 300
kmFijoMax = 1000
kmAdicional = km - kmFijo
kmAdicionalExtra = km - kmFijoMax

if km <= kmFijo:
    alquiler = montoFijo
elif km > kmFijo and km <= kmFijoMax:
    alquiler = montoFijo
    alquiler += kmAdicional * montoAdicional
else:
    alquiler = montoFijo
    alquiler += kmAdicional * montoAdicional
    alquiler += kmAdicionalExtra * montoAdicionalExtra
    alquiler -= kmAdicionalExtra * montoAdicional

montoIva = alquiler * iva
print(f'El monto total de alquiler es {alquiler:.2f}'
      + f' monto incluido de IVA {montoIva:.2f}')
