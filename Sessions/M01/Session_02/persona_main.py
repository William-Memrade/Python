from persona import Persona

try:
    alicia = Persona('alicia', 'perez', 30, "060628923")
    beto = Persona('beto', 'perez', 20, "015923205")
    
    # miembros publicos
    print('Nombre: ', alicia.nombres)
    # miembros protegidos
    print('Nombre: ', alicia._apellidos)
    # # miembros privados
    # print('Nombre: ', alicia.__edad)

    print('-----------------------------------------------')
    beto.mostrar_datos()
except Exception as e:
    print(e)