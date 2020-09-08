"""
Miguel Gonzalez Hernandez 13/5/2020
"""


def division(valor):



    try:
     return valor/0
    except ZeroDivisionError:
        raise ZeroDivisionError("El divisor no puede ser cero")








division(4)