"""
Miguel Gonzalez Hernandez 26/4/2020
"""




def devuelve_Tabla(numero):
    tabla=[]
    for i in range(0,11):
        tabla.append(numero*i)
    return tabla

tabla6=devuelve_Tabla(6)
tabla8=devuelve_Tabla(8)
tablafinal=tabla6+tabla8
print(tablafinal)


