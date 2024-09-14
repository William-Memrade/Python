# Programa para determinar si un a;o es biciesto

anio = int(input('Digite el año a evaluar: '))

if anio % 4 == 0:
    if anio % 100 == 0:
        if anio % 400 == 0:
            print(f"El año {anio} es bisiesto")
        else:
            print(f"El año {anio} NO es bisiesto")
    else:
        print(f"El año {anio} es bisiesto")
else:
    print(f"El año {anio} NO es bisiesto")
