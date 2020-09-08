
"""
Miguel Gonzalez Hernandez 14/5/2020
"""


#ESTE EJERCICIO LO VOY A REALIZAR DE UNA MANERA COMPLETAMENTE DISTINA AL ANTERIOR, INSPIRANDOME EN EL DE CLASE DE LOS LIBROS
#NO ME QUEDBAN LOS RESULTADOS QUE QUERÍA, SAQUE LA IDEA DEL .SCALAR() DE UN FORO EN INTERNET







from peewee import *


#ejecutar mejor directamente el ejercicio 2 que ya ejecuta implicitamente este, si no el ej_2 da mal
#para evitar este error, comentar ciertas lineas del ej1 y se soluciona

db = SqliteDatabase('Concesionario.db')

class Concesionario(Model):
    """
    Book model. Definimos el modelo datos que va a contener nuestra db
    """
    nombre = CharField()
    posicion = CharField()


    class Meta:
        database = db






#db = SqliteDatabase('Coches2.db')

class Car2(Model):
    """
    Book model. Definimos el modelo datos que va a contener nuestra db
    """
    marca = CharField()
    modelo = CharField()
    concesionario=ForeignKeyField(Concesionario)
    precio = IntegerField()
    numero_vendidos = IntegerField()
    gama = CharField()

    class Meta:
        database = db




db.connect()
db.create_tables([Car2, Concesionario])
#Relacciones


conces1=Concesionario.create(nombre='Pepito SL',posicion='Mostoles')
conces1.save()
conces2=Concesionario.create(nombre='Arriaga Vehiculos',posicion='Valencia')

conces2.save()

coche1=Car2.create(marca='Ford',modelo='Fiesta',precio=9000,numero_vendidos=1000,gama='baja',concesionario=conces1)
coche1.save()

coche2=Car2.create(marca='Ford',modelo='Focus',precio=14500,numero_vendidos=540,gama='Media',concesionario=conces1)
coche2.save()

coche3=Car2.create(marca='Ford',modelo='Mondeo',precio=28000,numero_vendidos=630,gama='Alta',concesionario=conces2)
coche3.save()

coche4=Car2.create(marca='Citroen',modelo='C3',precio=9500,numero_vendidos=780,gama='baja',concesionario=conces2)
coche4.save()

coche5=Car2.create(marca='Citroen',modelo='C4',precio=13500,numero_vendidos=340,gama='Media',concesionario=conces1)
coche5.save()

coche6=Car2.create(marca='Citroen',modelo='C5',precio=26000,numero_vendidos=120,gama='Alta',concesionario=conces2)
coche6.save()

coche7=Car2.create(marca='Peugeot',modelo='208',precio=9700,numero_vendidos=120,gama='baja',concesionario=conces2)
coche7.save()

coche9=Car2.create(marca='Peugeot',modelo='308',precio=16000,numero_vendidos=160,gama='Media',concesionario=conces1)
coche9.save()

coche10=Car2.create(marca='Peugeot',modelo='408',precio=27500,numero_vendidos=1760,gama='Alta',concesionario=conces2)
coche10.save()


#
# """
# Filtros / Ordenacion
# """
#
#
#
coches0=Car2.select(fn.SUM(Car2.numero_vendidos)).join(Concesionario).where(Concesionario.nombre=='Pepito SL').scalar()

print(f'Se han encontrado un total de {(coches0)} coches en el concesionario {conces1.nombre}')


coches=Car2.select(fn.SUM(Car2.numero_vendidos)).join(Concesionario).where(Concesionario.nombre=='Arriaga Vehiculos').scalar()

print(f'Se han encontrado un total de {(coches)} coches en el concesionario {conces2.nombre}')


result = Car2.select(fn.MAX(Car2.numero_vendidos)).join(Concesionario).where(Concesionario.nombre=='Arriaga Vehiculos').scalar()
modelo=Car2.select(Car2.modelo).join(Concesionario).where(conces2.nombre=='Arriaga Vehiculos',Car2.numero_vendidos==result).scalar()
marca=Car2.select(Car2.marca).join(Concesionario).where(conces2.nombre=='Arriaga Vehiculos',Car2.numero_vendidos==result).scalar()
print(f'se han vendido un total de  {result} {marca} {modelo} en el concesionario Arriaga Vehiculos')



result2 = Car2.select(fn.MAX(Car2.numero_vendidos)).join(Concesionario).where(Concesionario.nombre=='Pepito SL').scalar()
modelo2=Car2.select(Car2.modelo).join(Concesionario).where(conces1.nombre=='Pepito SL',Car2.numero_vendidos==result2).scalar()
marca2=Car2.select(Car2.marca).join(Concesionario).where(conces1.nombre=='Pepito SL',Car2.numero_vendidos==result2).scalar()
print(f'se han vendido un total de  {result2} {marca2} {modelo2} en el concesionario Pepito SL')