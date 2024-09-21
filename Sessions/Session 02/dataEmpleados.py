# programa que captura n cantidad de empleados

option = 0
lista_empleados = []

while option != 3:
    print("/////////////////// MENU ///////////////////")
    print("1. Agregar empleado")
    print("2. Mostrar empleados")
    print("3. Salir")
    option = int(input('Seleccione la opcion deseada: '))

    if option == 1:
        print("////////////// Agregar empleado //////////////")
        name = str(input('Ingrese el nombre del empleado: '))
        cargo = str(input('Ingrese el cargo del empleado: '))
        sueldo = float(input('Ingrese el sueldo del empleado: '))

        empleado_data = {
            'nombre': name,
            'cargo': cargo,
            'sueldo': sueldo
        }
        lista_empleados.append(empleado_data)

        print("Empleado agregado con exito")
        continue
    elif option == 2:
        print("////////////// Mostrar empleados //////////////")
        print(lista_empleados)
        for item in lista_empleados:
            for k, v in item.items():
                print(f"{k}: {v}")
            print("\n")

        continue
    elif option == 3:
        print("Gracias por utilizar nuestros servicios")
        break

    else:
        print("Valor no valido")
        continue
