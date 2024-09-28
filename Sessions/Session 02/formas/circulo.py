import math
from .figura import Figura
from .color import Color


# en este caso como solo hay un super y se necesita herencia multiple se hace por nombre de clase
class Circulo(Figura, Color):
    def __init__(self, nombre, color, radio) -> None:
        # super().__init__(nombre)
        Figura.__init__(self, nombre)
        Color.__init__(self, color)
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

    def calcular_diametro(self):
        return self.radio * 2
