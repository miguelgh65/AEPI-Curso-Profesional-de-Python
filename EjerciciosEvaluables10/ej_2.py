
"""
Miguel Gonzalez Hernandez 13/5/2020
"""






from peewee import *



#ojo se añaden más filas al usar esto, dará erroneo el resultado si se ejecuta el 1 primero y luego el 2, solo ejecutar el 2
#para evitar este error, comentar ciertas lineas del ej1 y se soluciona
from ej_1 import *

db = SqliteDatabase('Coches.db')




coches_total=0
coches_total_ford=0
coches_total_fiat=0
coche_mas_vendido=0
coche_mas_rentable=0
coches_total_peugeot=0
coches_total_citroen=0

#1)
for car in Car.select():
    coches_total+=car.numero_vendidos
#2)
for car in Car.select().where(Car.marca=='Ford'):

     coches_total_ford+=car.numero_vendidos

for car in Car.select().where(Car.marca=='Fiat'):

     coches_total_fiat+=car.numero_vendidos
for car in Car.select().where(Car.marca=='Peugeot'):

     coches_total_peugeot+=car.numero_vendidos

for car in Car.select().where(Car.marca=='Citroen'):

     coches_total_citroen+=car.numero_vendidos









#3)
for car in Car.select():
    if coche_mas_vendido<car.numero_vendidos:
        coche_mas_vendido=car.numero_vendidos
        modelo_mas_vendido=car.modelo


#4
for car in Car.select():
    if coche_mas_rentable<(car.numero_vendidos*car.precio):
        coche_mas_rentable=car.numero_vendidos
        modelo_mas_rentable=car.modelo
#5
print('coches los cuales son gama media')
for car in Car.select().where(Car.gama=='Media'):
    print(car.modelo)


print('-------------------------------------------------------')
#6

cars_ordered = Car.select().order_by(Car.precio)
print('Modelos de coches ordenados por precio')
for car in cars_ordered:
    print(car.modelo)

print('-------------------------------------------------------')

print(f'el numero total de coches vendidos es de {coches_total}')
print('-------------------------------------------------------')
print(f'numero de coches vendidos por Ford: {coches_total_ford}')
print('-------------------------------------------------------')
print(f'numero de coches vendidos por Fiat: {coches_total_fiat}')
print('-------------------------------------------------------')
print(f'numero de coches vendidos por Citroen: {coches_total_citroen}')
print('-------------------------------------------------------')
print(f'numero de coches vendidos por Peugeot: {coches_total_peugeot}')
print('-------------------------------------------------------')
print(f'el coche más vendido es el {modelo_mas_vendido}con un total de venntas de {coche_mas_vendido}')
print('-------------------------------------------------------')

print(f'el mejor coches es el {Car.select(Car.modelo).where(Car.modelo=="Multipla").scalar()}')
print('-------------------------------------------------------')



