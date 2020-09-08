
"""
Miguel Gonzalez Hernandez 13/5/2020
"""


from peewee import *


#ejecutar mejor directamente el ejercicio 2 que ya ejecuta implicitamente este, si no el ej_2 da mal
#para evitar este error, comentar ciertas lineas del ej1 y se soluciona

db = SqliteDatabase('Coches.db')

class Car(Model):
    """
    Book model. Definimos el modelo datos que va a contener nuestra db
    """
    marca = CharField()
    modelo = CharField()
    precio=IntegerField()
    numero_vendidos=IntegerField()
    gama=CharField()


    class Meta:
        database = db

# Conectamos con la base datos
db.connect()

# Creamos la tabla Book
db.create_tables([Car])


car=Car.create(marca='Ford',modelo='Fiesta',precio=9000,numero_vendidos=1000,gama='baja')
car=Car.create(marca='Ford',modelo='Focus',precio=14500,numero_vendidos=540,gama='Media')
car=Car.create(marca='Ford',modelo='Mondeo',precio=28000,numero_vendidos=630,gama='Alta')
car=Car.create(marca='Citroen',modelo='C3',precio=9500,numero_vendidos=780,gama='Baja')
car=Car.create(marca='Citroen',modelo='C4',precio=13500,numero_vendidos=340,gama='Media')
car=Car.create(marca='Citroen',modelo='C5',precio=26000,numero_vendidos=120,gama='Alta')
car=Car.create(marca='Peugeot',modelo='208',precio=9700,numero_vendidos=1250,gama='Baja')
car=Car.create(marca='Peugeot',modelo='308',precio=16000,numero_vendidos=160,gama='Media')
car=Car.create(marca='Peugeot',modelo='408',precio=27500,numero_vendidos=1760,gama='Alta')
car=Car.create(marca='Fiat',modelo='Multipla',precio=150000,numero_vendidos=0,gama='UltraAlta')

