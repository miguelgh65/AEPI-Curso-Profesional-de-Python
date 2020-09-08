"""
Miguel Gonzalez Hernandez 13/5/2020
"""


lista = [1,4,6,8]

try:
    print(lista[5])
except IndexError:
    raise IndexError("IndexError: la lista no llega a esa posición")

