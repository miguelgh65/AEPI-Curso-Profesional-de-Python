





password=input("ingrese pass ")

Flag_total = False

Flag_minuscula = False
Flag_mayuscula = False
Flag_espacio = True
Flag_numeros = False
Flag_alfa = False

if(len(password)<8):
   print("contraseña debil")
   exit()


i=0
while(i<len(password)):
    Caracterazo=password[i]
    #print(f"comprobando el caracter{Caracterazo}")
    flag_total=Flag_espacio and Flag_numeros and Flag_alfa and Flag_minuscula and Flag_mayuscula






    if password[i].isspace() == True and Flag_espacio == True:
        Flag_espacio = False
       # print("comprobando espacios")
        flag_total = Flag_espacio and Flag_numeros and Flag_alfa and Flag_minuscula and Flag_mayuscula



    if password[i].isdigit() == True and Flag_numeros == False:
         Flag_numeros = True
         #print("comprobando numeros")
    flag_total = Flag_espacio and Flag_numeros and Flag_alfa and Flag_minuscula and Flag_mayuscula



    if password[i].isalnum() == False and Flag_alfa== False:
         Flag_alfa = True
         #print("comprobando alfanumero")
    flag_total = Flag_espacio and Flag_numeros and Flag_alfa and Flag_minuscula and Flag_mayuscula


    if password[i].islower() == True and Flag_minuscula == False:
        Flag_minuscula = True
       #print("comprobando minusculas")
        flag_total = Flag_espacio and Flag_numeros and Flag_alfa and Flag_minuscula and Flag_mayuscula


    if password[i].isupper() == True and Flag_mayuscula == False:
        Flag_mayuscula = True
       # print("comprobando mayusculas")
        flag_total = Flag_espacio and Flag_numeros and Flag_alfa and Flag_minuscula and Flag_mayuscula



    i = i + 1


if (flag_total):
    print("Su contraseña fuerte")
    exit()
else :
    print("Su contraseña debil")
    exit()