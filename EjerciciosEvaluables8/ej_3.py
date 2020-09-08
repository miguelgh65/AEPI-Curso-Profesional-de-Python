numero_1=input("Usuario 1 deme su numero de telefono ")
Usuario_1=input("Usuario 1 deme su nombre")
numero_2=input("Usuario 2 deme su numero de telefono ")
Usuario_2=input("Usuario 2 deme su nombre ")
numero_3=input("Usuario 3 deme su numero de telefono ")
Usuario_3=input("Usuario 3 deme su nombre ")



nombre = "listin-telefonico.txt"
f = open(file=nombre, mode="w")



diccionario = {Usuario_1 : numero_1, Usuario_2: numero_2, Usuario_3: numero_3 }


for key, value in diccionario.items():

   f.write(str((key)))
   f.write("-")
   f.write(str((value)))
   f.write("\n")





