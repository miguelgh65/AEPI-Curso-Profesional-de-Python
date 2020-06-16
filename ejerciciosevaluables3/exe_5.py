"""
Miguel Gonzalez Hernandez 21/4/2020
"""
asignatura={'Mates':6,'Fisica':4,'Quimica':5}

for key in asignatura:
    print (f"la asignatura {key}","tiene ",f"{asignatura[key]}  creditos")


a=sum(asignatura.values())
print(f"numero total de creditos : {a}")