"""
Miguel Gonzalez Hernandez 21/4/2020
"""
diccionario={'Euros':'€','Dollar':'$','Yen':'¥'}
dicho=input("que simbolo de divisa quiere ver : ")
if(dicho in diccionario):
    devuelto=diccionario.get(dicho)
    print(devuelto)

else:

    print("No está en el diccionario")