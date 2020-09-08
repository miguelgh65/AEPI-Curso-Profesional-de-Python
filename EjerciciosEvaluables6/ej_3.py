import math

class circulo:
    def __init__(self, x):
        self.radio = x

    def area(self):
        area_circulo = self.radio**2*math.pi
        return area_circulo
    def perimetro(self):
        perimetro = 2*math.pi*self.radio
        return perimetro

circulazo=circulo(5)
print(circulazo.perimetro())
print(circulazo.area())