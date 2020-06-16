user=input("ingrese user")



Flag_alfauser = False

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

print("Usuario correcto")