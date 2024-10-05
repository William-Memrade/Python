class Persona_:
    pass


p = Persona_()
print(type(p))


class Persona:
    def __init__(self, nombres, apellidos, edad, dui) -> None:
        self.nombres = nombres # publico
        self._apellidos = apellidos # protegido
        self.__edad = edad # privado
        self.__dui = dui # privado

    def __es_adulto(self): # metodo privado
        return self.__edad >= 18
    
    def mostrar_datos(self): # metodo publico
        print(
            f'nombres: {self.nombres}\n'
            f'apellidos: {self._apellidos}\n'
            f'edad: {self.__edad}\n'
            f'adulto: {self.__es_adulto()}\n'
            f'dui: {self.__dui}\n'
        )
