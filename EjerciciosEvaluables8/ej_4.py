import json


with open('poblacion.json','r') as fichero:

    contenido=json.load(fichero)

    biggest_population=0
    smallest_population=99999999999999999999999999
    small=0


    for poblacion in contenido:
        #print(biggest_population)
        if(biggest_population<poblacion.get("poblacion_empadronada")):
            biggest_population = poblacion.get("poblacion_empadronada")
            big=poblacion.get("rango_edad")

        if ( poblacion.get("poblacion_empadronada")<smallest_population ):
            smallest_population = poblacion.get("poblacion_empadronada")
            small=poblacion.get("rango_edad")





print((f'rango { big} en el barrio con más habitantes'))
print((f'rango { small} en el barrio con menos habitantes que tiene una cantidad de habitantes de {smallest_population}'))


