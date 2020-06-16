# """
# Miguel Gonzalez Hernandez
# 22/4/2020
# """
#
#
#
def arreglanotas(asignaturas):

    #asignaturas={'Mates':6,'Fisica':4,'Quimica':5}

    asignaturaMayusc= asignaturas.keys()
    asignaturaMayusc1= asignaturas.values()
    listamayu=[]
    listamayusc1=[]
    for i in asignaturaMayusc:
        #print(i)
        a=i.upper()
        #print(a)
        listamayu.append(a)




    #print(asignaturaMayusc)
    #print(listamayu)




    for i in asignaturaMayusc1:
    #print(i)
        a=i
        #print(a)
        listamayusc1.append(a)
    #print(listamayusc1)




    for i in range(len(listamayusc1)-1):
        if(listamayusc1[i]<5):
            del listamayusc1[i]
            del listamayu[i]


    #print(listamayusc1)
    #print(listamayu)

    dictionary = dict(zip(listamayu, listamayusc1))
    print(dictionary)


    return dictionary



#signaturas={'Mates':6,'Fisica':4,'Quimica':5}

#arreglanotas(signaturas)