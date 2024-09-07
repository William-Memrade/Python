try:
    # w = input('Digite una palara: ')
    4/0
    # w+5
    # int(w)
except ZeroDivisionError:
    print("Ocurrio un error")
except TypeError:
    print("No se pueden sumar cadenas y numeros")
except Exception as e:
    print("Ocurrio un error" + str(e))
else:
    print("Sin errores")
finally:
    print("Errores o no aqui estoy")

print("Final del programa")
