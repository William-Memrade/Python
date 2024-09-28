# from formas.rectangulo import Rectangulo
# from formas.figura import Figura
from formas.circulo import Circulo

try:
    # f = Figura('indeterminado')
    # r = Rectangulo('Rectangulo', 'Verde', 10, 20)
    c = Circulo('circulo', 'rojo', 5)

    # f.mostrar_nombre()
    # r.mostrar_nombre()
    c.mostrar_nombre()

    # print("IMPRESIONES PARA RECTANGULO")
    # print(f'El area de {r.nombre} es: {r.calcular_area()}')
    # print(f'El perimetro de {r.nombre} es: {r.calcular_perimetro()}')
    # print(f'El color de {r.nombre} es: {r.color}')
    
    # print("IMPRESIONES PARA CIRCULO")
    print(f'La circunferencia de {c.nombre} es: {c.calcular_perimetro():.2f}')
    print(f'El diametro de {c.nombre} es: {c.calcular_diametro():.2f}')
    print(f'El area de {c.nombre} es: {c.calcular_area():.2f}')
    print(f'El color de {c.nombre} es: {c.color}')
except Exception as e:
    print(e)
