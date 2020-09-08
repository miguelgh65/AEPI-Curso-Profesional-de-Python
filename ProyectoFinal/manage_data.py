








import datetime

from peewee import *
import random
import string
import sqlite3
import csv
import json


db = SqliteDatabase('fabricantes.db')


"""
Miguel Gonzalez Hernandez 23/5/2020 PFINAL AEPI PYTHON
"""

#variables

"""
Variables que se utilizan en el programa lista de la compra actua de carrito 
lista encontrada muestra los fabricantes que se han encontrado al buscarlo y lista numero es simplemente un indice para 
la anteriror lista
"""


lista_de_la_compra=[]
lista_encontrada_fabricante=[]
lista_numero_listaencontrada=[]

"""
Creacion de las bases de datos


No consideré el uso de foreingkey ya que vi que las bases de datos por defecto los fabricantes eran distintos y no vi la utilidad
de unificar las tablas de piezas y fabricantes
"""



class Ordenes(Model):
    """
    Book
    """
    id_compra = CharField()
    fecha_compra = DateField()
    vendedor = CharField()
    precio_total = FloatField()
    piezas = CharField()

    class Meta:
        database = db

class Fabricante(Model):
    """
    Book model. Definimos el modelo datos que va a contener nuestra db
    """
    numero_registro = CharField()
    nombre=CharField()
    CIF=CharField()

    class Meta:
        database = db

class Piezas(Model):
    """
    Book model. Definimos el modelo datos que va a contener nuestra db
    """
    nombre=CharField()
    numero_registro = CharField()
    fecha_fabricacion = DateField()
    fabricante=CharField()
    loc_fabricacion=CharField()
    prize=FloatField()
    Numer_piezasas=CharField()


    class Meta:
        database = db

db.connect()
db.create_tables([Piezas,Fabricante,Ordenes])



"""
Creacion de las bases de datos por defecto a partir de la lectura del csv, solo ejecutar una vez
"""




#Relacciones
#Creamos los fabricantes
#
# with open('fabricantes.csv')as f:
#   data = csv.reader(f)
#   contador=0
#   for row in data:
#
#
#
#     if contador==0:
#        fab0 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador==1:
#         fab1 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 2:
#         fab2 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 3:
#         fab3 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 4:
#         fab4 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 5:
#         fab5 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 6:
#         fab6 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 7:
#         fab7 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 8:
#         fab8 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 9:
#         fab9 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 10:
#         fab10 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 11:
#         fab11= Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 12:
#         fab12= Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 13:
#         fab13 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 14:
#         fab14 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 15:
#         fab15 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 16:
#         fab16 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#     elif contador == 17:
#         fab17 = Fabricante.create(nombre=row[1], numero_registro=row[0], CIF=row[3])
#
#     contador=contador+1
# """
# -----------------------------------------------------------------------------------------------------------------------
# """
# # # #Creamos ahora las piezas
# # #
# with open('Piezas.csv')as f:
#   data = csv.reader(f)
#   contador=0
#   for row in data:
#     print(row)
#
#     if contador==0:
#        piez0 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador==1:
#         piez1 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 2:
#         piez2 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 3:
#         piez3 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 4:
#         piez4 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 5:
#         piez5 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 6:
#         piez6 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 7:
#         piez7 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 8:
#         piez8 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 9:
#         piez9 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 10:
#         piez10 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 11:
#         piez11= Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 12:
#         piez12= Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 13:
#         piez13 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 14:
#         piez14 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 15:
#         piez15 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 16:
#         piez16 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#     elif contador == 17:
#         piez17 = Piezas.create(nombre=row[1], numero_registro=row[0], fabricante=row[3],loc_fabricacion=row[4],prize=row[5],Numer_piezasas=0,fecha_fabricacion=row[2])
#
#     contador=contador+1
"""
-----------------------------------------------------------------------------------------------------------------------
"""



#nos muestra el numero total de fabricantes
def contador_fabricantes():

    for fabrito in Fabricante.select():

        fab=fabrito.id

    print(fabrito.id)
    return fabrito.id
"""
-----------------------------------------------------------------------------------------------------------------------
"""
#nos muestra el numero total de piezas
def contador_piezas():

    for piecito in Piezas.select():

        fab=piecito.id

    print(piecito.id)
    return piecito.id
"""
-----------------------------------------------------------------------------------------------------------------------
"""

#metodo para buscar una pieza en la base de datos, si busco cil, apareceran cilindros etc etc

def buscapieza(namepieza):
    nombrepieza=namepieza
    lista_encontrada=[]

    Piezabuscada = Piezas.select(Piezas.nombre).where(Piezas.nombre.startswith(nombrepieza.capitalize())).scalar()
    numero = 0
    for piecito in Piezas.select():

        if piecito.nombre.startswith(nombrepieza.capitalize()):
            print(f'{numero} {piecito.nombre}')
            numero=numero+1
            lista_encontrada.append(piecito.nombre)


    return lista_encontrada

"""
-----------------------------------------------------------------------------------------------------------------------
"""

# me da mas informacion sobre una pieza en concreto, como su fabricante etc etc, me hubiese gustdo poder comprar desde aquí pero no hanía tiempo suficiente
def buscainfromacionpieza(nombrepieza):
    lista_encontrada = []

    Piezabuscada_id = Piezas.select(Piezas.id).where(Piezas.nombre==nombrepieza).scalar()
    lista_encontrada.append(Piezabuscada_id)
    Piezabuscada_numero_registro = Piezas.select(Piezas.numero_registro).where(Piezas.nombre == nombrepieza).scalar()
    lista_encontrada.append(Piezabuscada_numero_registro)
    Piezabuscada_fecha_fabricacion = Piezas.select(Piezas.fecha_fabricacion).where(Piezas.nombre == nombrepieza).scalar()
    lista_encontrada.append(Piezabuscada_fecha_fabricacion)
    Piezabuscada_fabricante = Piezas.select(Piezas.fabricante).where(Piezas.nombre == nombrepieza).scalar()
    lista_encontrada.append(Piezabuscada_fabricante)
    Piezabuscada_loc_fabricacion = Piezas.select(Piezas.loc_fabricacion).where(Piezas.nombre == nombrepieza).scalar()
    lista_encontrada.append(Piezabuscada_loc_fabricacion)
    Piezabuscada_prize = Piezas.select(Piezas.prize).where(Piezas.nombre == nombrepieza).scalar()
    lista_encontrada.append(Piezabuscada_prize)
    Piezabuscada_numero_piezas_vendidas = Piezas.select(Piezas.Numer_piezasas).where(Piezas.nombre == nombrepieza).scalar()
    lista_encontrada.append(Piezabuscada_numero_piezas_vendidas)
    return lista_encontrada

"""
-----------------------------------------------------------------------------------------------------------------------
"""

#generador de de numeros de registros con el mismo formato que los precios del csv
def randomString(stringLength=1):
    letters = string.ascii_uppercase
    letras=''.join(random.choice(letters) for i in range(stringLength))

    cifras=str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
    return letras+cifras
"""
-----------------------------------------------------------------------------------------------------------------------
"""


# crea una piez nueva
def creapieza(a,b,c):
    piez18 = Piezas.create(nombre=a, numero_registro=randomString(), fabricante="Nuestro Taller", loc_fabricacion="Madrid",
                           prize=random.randint(1,100), Numer_piezasas=c, fecha_fabricacion=b)

    return(f'Su pieza ha sido creada, el precio es de{piez18.prize}')

"""
-----------------------------------------------------------------------------------------------------------------------
"""
#modifcia una pieza existente
def modificaPieza(namepieza,fecha,nuevo_nombre,nueva_cantidad):
    Id_pieza_buscada = Piezas.select(Piezas.id).where(Piezas.nombre.startswith(namepieza.capitalize())).scalar()


    cursorObj = db.cursor()

    cursorObj.execute(f'UPDATE piezas SET nombre = "{nuevo_nombre}" where id = {Id_pieza_buscada}')
    cursorObj.execute(f'UPDATE piezas SET Numer_Piezasas = "{nueva_cantidad}" where id = {Id_pieza_buscada}')
    cursorObj.execute(f'UPDATE piezas SET Numer_Piezasas = "{nueva_cantidad}" where id = {Id_pieza_buscada}')
    cursorObj.execute(f'UPDATE piezas SET fecha_fabricacion = "{fecha}" where id = {Id_pieza_buscada}')
    cursorObj.execute(f'UPDATE piezas SET prize = "{random.randint(1,150)}" where id = {Id_pieza_buscada}')
    db.commit()
"""
-----------------------------------------------------------------------------------------------------------------------
"""
# elimina una pieza existente
def eliminapieza(nombrepieza):
    Id_pieza_buscada = Piezas.select(Piezas.id).where(Piezas.nombre.startswith(nombrepieza.capitalize())).scalar()

    Id_pieza_buscada = Piezas.delete_by_id(Id_pieza_buscada)


"""
-----------------------------------------------------------------------------------------------------------------------
"""


#te permite buscar un fabricante, funciona de manera análoga a buscapieza
def buscafabricante(nombrefabricante):

    lista_encontrada_fabricnate = []

    # FabricanteBuscado = Fabricante.select(Fabricante.nombre).where(Fabricante.nombre.startswith(nombrefabricante.upper())).scalar()
    numero = 0
    for fabrito in Fabricante.select():
        # print(fabrito.nombre)


        if fabrito.nombre.startswith(nombrefabricante.upper()):
            print(f'{numero} {fabrito.nombre}')
            numero = numero + 1
            lista_encontrada_fabricnate.append(fabrito.nombre)

    return lista_encontrada_fabricnate
"""
-----------------------------------------------------------------------------------------------------------------------
"""
#analogo a crea piezas
def creafabricante(nombrefab,cif):
    fab18 = Fabricante.create(nombre=nombrefab, numero_registro=randomString(), CIF=cif)
    print("Su fabricante ha sido añadido al catalogo")

"""
-----------------------------------------------------------------------------------------------------------------------
"""
#analogo a crea fabricante
def eliminafabricante(nombrefabricante):
    Id_fab_buscada = Fabricante.select(Fabricante.id).where(Fabricante.nombre.startswith(nombrefabricante.upper())).scalar()

    Id_fab_buscada = Fabricante.delete_by_id(Id_fab_buscada)

"""
 -----------------------------------------------------------------------------------------------------------------------
  """
#analogo al de buscainformacionpiezas

def buscainfromacionfabricante (nombrefabricante):
    lista_encontrada = []

    fabricante_buscado_id = Fabricante.select(Fabricante.id).where(Fabricante.nombre == nombrefabricante).scalar()
    lista_encontrada.append(fabricante_buscado_id)

    fabricante_buscado_registro = Fabricante.select(Fabricante.numero_registro).where(Fabricante.nombre == nombrefabricante).scalar()
    lista_encontrada.append(fabricante_buscado_registro)

    fabricante_buscado_CIF = Fabricante.select(Fabricante.CIF).where(Fabricante.nombre == nombrefabricante).scalar()
    lista_encontrada.append(fabricante_buscado_CIF)
    return lista_encontrada
"""
-----------------------------------------------------------------------------------------------------------------------
"""
#analogo a modifcapieza
def modificafabricante(nombrefabricante,nuevo_nombre,cif):
    fabricante_buscado_id = Fabricante.select(Fabricante.id).where(Fabricante.nombre == nombrefabricante).scalar()
    print(fabricante_buscado_id)
    cursorObj = db.cursor()

    cursorObj.execute(f'UPDATE fabricante SET nombre = "{nuevo_nombre}" where id = {fabricante_buscado_id}')
    cursorObj.execute(f'UPDATE fabricante SET CIF = "{cif}" where id = {fabricante_buscado_id}')
    cursorObj.execute(f'UPDATE fabricante SET numero_registro = "{randomString()}" where id = {fabricante_buscado_id}')
    db.commit()

"""
-----------------------------------------------------------------------------------------------------------------------
"""

#sirve para comprar o más bien añadir al carrito una pieza
def comprapieza(nombrepieza,mostrar):
    Piezabuscada_nombre = Piezas.select(Piezas.nombre).where(Piezas.nombre == nombrepieza).scalar()
    if(mostrar):
        print(f"Wubalubadubdub, usted ha comprado {Piezabuscada_nombre}, para proceder al pago vaya a generar informe")
    lista_de_la_compra.append(Piezabuscada_nombre)



"""
-----------------------------------------------------------------------------------------------------------------------
"""
#nos permite ver las piezas de una determinado fabricante
def verpiezasfabricante(nombreexactofabricante,mostrar):
    numero=0
    for piecito in Piezas.select():

        if piecito.fabricante==nombreexactofabricante:
            if(mostrar):
                print(f'{numero} {piecito.nombre}')
            lista_numero_listaencontrada.append(numero)
            numero=numero+1
            lista_encontrada_fabricante.append(piecito.nombre)

            lista_numero_listaencontrada.append(lista_encontrada_fabricante)

    return lista_numero_listaencontrada
"""
-----------------------------------------------------------------------------------------------------------------------
"""
#nos permite comprar una pieza de un fabricante, por ejemplo cilindros de marca x
def comprapiezaporfabricante(nombrefabricante,nombrepieza,mostrar):


    if Piezas.select(Piezas.nombre).where(Piezas.nombre==nombrepieza).scalar()!=nombrepieza:

        print("Su pieza no estab en nuestro catalgo de stock, no obstante se ha añadido a este catalogo como pieza a pedir")
        now = datetime.datetime.now()
        b = now.strftime("%d/%m/%Y %H:%M:%S")
        localizacion_Fabricante=Piezas.select(Piezas.loc_fabricacion).where(Piezas.fabricante==nombrefabricante).scalar()
        precioFabricante = Piezas.select(Piezas.prize).where(Piezas.fabricante == nombrefabricante).scalar()
        piez18 = Piezas.create(nombre=nombrepieza, numero_registro=randomString(), fabricante=nombrefabricante,
                               loc_fabricacion=localizacion_Fabricante,
                               prize=precioFabricante, Numer_piezasas=-1, fecha_fabricacion=b)



    comprapieza(nombrepieza, True)

"""
-----------------------------------------------------------------------------------------------------------------------
"""

#añade una compra al json cada vez que se realiza una compra para así mostrar un historico,
#para crear uan factura , sería simplemnente hacer un dump de lista_compra, pero solo mostraria la ultima compra
with open('registro.json', 'r') as f:
    hiperregistro=json.load(f)

def ordenes(lista):
    try:
        now = datetime.datetime.now()
        b = now.strftime("%d/%m/%Y %H:%M:%S")
        precio_total = 0
        for elementos in lista:
            Precioelemento = (Piezas.select(Piezas.prize).where(Piezas.nombre == elementos)).scalar()

            precio_total=precio_total+Precioelemento

        print(precio_total)


        for elementos in lista:
            print(elementos)

            Orde = Ordenes.create(nombre=elementos,id_compra=randomString() ,fecha_compra=b, vendedor="Miguel",precio_total=precio_total,piezas=tuple(lista))
            registrofinal={"elementos comprados":elementos,"precio total pagado":precio_total,"vendedor":"Miguel","fecha de compra":b}

        hiperregistro.append(registrofinal)





        with open('registro.json', 'w') as f:

            json.dump(hiperregistro, f)
    except:
        print("Debe comprar algo para generar su informe")




"""
-----------------------------------------------------------------------------------------------------------------------
"""

# muestra el catalogo completo, el parametro cual es para saber si es el de fabricntes o piezas, era eso o 2 metodos,
 #puse lineas para dar un mejor formato al print
def muestra_catalogo(cual):
    if cual:
        con = sqlite3.Connection('fabricantes.db')
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM piezas')

        for row in cur.fetchall():
            # can convert to dict if you want:
            print(dict(row))
            print("""
    ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    """)
    else:
        con = sqlite3.Connection('fabricantes.db')
        con.row_factory = sqlite3.Row

        cur = con.cursor()
        cur.execute('SELECT * FROM fabricante')

        for row in cur.fetchall():
            # can convert to dict if you want:
            print(dict(row))
            print("""
            ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
            """)

