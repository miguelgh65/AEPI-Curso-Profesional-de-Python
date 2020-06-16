"""
Miguel Gonzalez Hernandez 26/4/2020
"""



def pide_numero(numero):
    nombre = f"tabla{numero}.txt"
    f = open(file=nombre, mode="w")

    for numerazo in range(numero, 100):
        f.write(str(numerazo))

    f.close()
pide_numero(5)