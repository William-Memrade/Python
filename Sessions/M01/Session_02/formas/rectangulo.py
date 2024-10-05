from .figura import Figura
from .color import Color


# en este caso como solo hay un super y se necesita herencia multiple se hace por nombre de clase
class Rectangulo(Figura, Color):
    def __init__(self, nombre, color, base, altura) -> None:
        # super().__init__(nombre)
        Figura.__init__(self, nombre)
        Color.__init__(self, color)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return (self.base + self.altura) * 2
