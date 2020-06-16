Flag_alfauser = False
user=input("ingrese user")
password=input("ingrese pass ")

if(len(user)<=6):
   print("El nombre de usuario debe contener al menos 6 caracteres")
   exit()

if (len(user) >= 12):
    print("El nombre de usuario no puede contener más de 12 caracteres")
    exit()

i=0
while(i<len(user)):
    Caracterazo=user[i]
    #print(f"comprobando el caracter{Caracterazo}")












    if user[i].isalnum() == False :
         print("El nombre de usuario puede contener solo letras y números")
         exit()
         #print("comprobando alfanumero")



    i = i + 1












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
    print("Usuario correcto")
    print("Su contraseña fuerte")
    exit()
else :
    print("Su contraseña debil")
    exit()









