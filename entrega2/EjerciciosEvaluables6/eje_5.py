
"""
Miguel Gonzalez Hernandez 26/4/2020
"""




class Producto:
    nombre=""
    precio=0.0

    def __init__(self,nombre,precio):
        self.precio=precio
        self.nombre=nombre

class Yogur(Producto):

    def get_price(self):
        return (self.precio*1.21)

# nombre=input("ingrese nombre de yogur ")
# precio=int(input("ingrese precio "))
# Yougurlado=Yogur(nombre,precio)
# print(Yougurlado.get_price())