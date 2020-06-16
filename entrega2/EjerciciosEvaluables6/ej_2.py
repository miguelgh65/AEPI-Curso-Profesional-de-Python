
"""
Miguel Gonzalez Hernandez 26/4/2020
"""



class rectangulo:
    def __init__(self, x, y):
        self.base = x
        self.altura = y

    def area(self):
        area_rectangulo = self.altura * self.base
        return area_rectangulo


rectangulazo = rectangulo(50, 20)
print(rectangulazo.area())

