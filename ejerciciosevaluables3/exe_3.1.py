tupla=(1,1,2,3,4,1,1,1,1 )
numero=int(input("deme un numero"))
contador=0
for i in range(len(tupla)):
   # print(tupla[i])
    if(numero==tupla[i]):
        contador=contador +1
print(contador)
