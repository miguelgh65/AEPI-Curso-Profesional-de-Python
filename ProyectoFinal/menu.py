from datetime import datetime

from peewee import DoesNotExist


from manage_data import *
import threading
"""
Miguel Gonzalez Hernandez 23/5/2020 PFINAL AEPI PYTHON
"""


"""
Muestra un menú interactivo
"""

def mostrar_menu():
    print('\n')
    print("Bienvenido al sistema de Recambios Los Santos Custom".center(200))
    print('\n')
    print('Opciones disponibles:'.center(200))
    print('busca_pieza'.center(200))
    print('busca_fabricante'.center(200))
    print('generar_informe'.center(200))





entrada = ''
while entrada != 'exit':

    mostrar_menu()

    entrada = input('>>')

    """
    Genera el informe json y añade la lista de la compra a la tabla ordenes de la base de datos si no tienes nada en 
    lista_de_la_compra (funciona como carrito) no hace nada y te avisa de que debes comprar algo
    """

    if(entrada=="generar_informe"):
        print("usted ha comprado los siguientes materiales")
        print(lista_de_la_compra)

        ordenes(lista_de_la_compra)
        print("hasta otra")
        exit()

    """
     Te muestra o bien el catálogo general de la tienda o la posibilidad de buscar una pieza en particular
     """

    if entrada == 'busca_pieza':
        print(f'El número total de piezas es: {contador_piezas()}')
        print(f'Desea buscar una pieza en particular? si o no , si desea buscar/comprar una pieza esciba si'
              f' si solo desea ojear el catalogo pulse no ')
        entrada = input('>>>')

        """
         Muestra el catalgo entero solo para ojear, en futuras mejorar miraría el poder comprar directamente de ahí
         """

        if entrada == 'no':

            muestra_catalogo(False)

        """ 
        Para mas informacion ver comentarios en manage_data
                Buscador de piezas, te muestra las piezas que empiezan por lo que has escrito, si pones 'cil' aparecera la palabra
                'cilindro'
                
                Te permite modificar una pieza del catalogo a tu antojo, por ejemplo cambiar de nombre  un articulo, los numeros de registro 
                vuelven a crear de una manera aleatoria
                
                Te permite eliminar una pieza del catalogo
                
                Te permite crear una pieza, el fabricante de dicha pieza será 'nuestro taller'
                
                Te permite ver los detalles de una pieza en particular
                
                Y obviamente te permite comprar una piza, no es comprar como tal sino que lo añade al carrito y luego se compra como tal en 
                generar informe
                
                
                
                
                
                 """

        if entrada == 'si':
            print('ok')
            nombrepieza = input("Diga que pieza busca")
            print("se han encontrado las siguientes piezas a su busqueda,"
                  "si desea informacion de alguna pieza, ponga el numero de la pieza para ello, "
                  "si no está su pieza y desea encargar una nueva escriba crear pieza")
            print("si desea modificar su pieza escriba modificar ")
            print("si desea eliminar una pieza escriba eliminar ")
            print("si desea comprar alguna pieza escriba comprar)")

            resultado=buscapieza(nombrepieza)
            entrada=input('>>>>')
            if entrada=='crear pieza':
                    parametros=[]

                    a=input("introduzca el nombre de la pieza que quiere")

                    now = datetime.datetime.now()
                    b = now.strftime("%d/%m/%Y %H:%M:%S")
                    c = input("introduzca el numero de piezas que quiere añadir al stock")
                    creapieza(a,b,c)

            elif entrada == 'modificar':
                parametros = []

                a = input("introduzca el nombre de la pieza que quiere modificar")

                now = datetime.datetime.now()
                b = now.strftime("%d/%m/%Y %H:%M:%S")
                d = input("introduzca el numero de piezas que quiere")
                c = input("introduzca la nueva pieza que quiere")
                try:
                    modificaPieza(a, b,c,d)
                except:
                    sqlite3.OperationalError
                    print("pieza modificada")
            elif entrada == 'eliminar':
                parametros = []

                a = input("introduzca el nombre de la pieza que quiere eliminar")



                try:
                    eliminapieza(a)
                except:
                    sqlite3.OperationalError
                    print("pieza eliminada")


            elif entrada == 'comprar':


                nombrepiezaacomprar=input("el nombre exacto de la pieza que quiere comprar")
                resultado=comprapieza(nombrepiezaacomprar,True)


            else:

                n=0
                for numero in resultado:
                    if(n==int(entrada)):
                        print("olala")
                        print(numero)
                        temporal=buscainfromacionpieza(numero)
                        print(f'Numero de registro : {temporal[1]}')
                        print(f'Fecha de Fabricacion : {temporal[2]}')
                        print(f'Localidad Fabricacion : {temporal[3]}')
                        print(f'Precio : {temporal[4]}')
                        print(f'Numero de Piezas vendidas: {temporal[5]}')
                        break
                    n=n+1



        else:
            print("ok")

            """
            Para mas informacion ver comentarios en manage_data
                            El resto del programa, te permite buscar fabricantes de la base de datos,  ya sa mostrando todo el catalgo o en particularm, una vez has visto un
                            fabricante te deja ver las piezas que posee este fabricante para comprar una directamente, para comprar 
                            una pieza de una determinada marca es la única manera pues de la otra manera te asigna una pieza de marca cualesquiera
                            
                            Te permite eliminar fabricante y crear un fabricante nuevo


                             """










    elif entrada == 'busca_fabricante':
        print(f'El número total de fabricantes disponibles en stock  es de : {contador_fabricantes()}')
        print(f'Desea buscar un fabricante en particular? si o no ')
        entrada = input('>>>')
        if entrada == 'no':
            muestra_catalogo(True)


        if entrada == 'si':
            print('ok')
            nombrefabricante = input("Diga que fabricante busca ")
            print(
                "se han encontrado las siguientes fabricantes a su busqueda, desea informacion de algun fabricante, ponga el numero del fabricante para ello, si no está su fabricante y desea encargar un fabricante escriba crear fabricante")
            print("si desea modificar su fabricante escriba modificar ")
            print("si desea eliminar su fabricante escriba eliminar ")
            print("si desea ver las piezas de un fabricante escriba ver piezas")


            resultado = buscafabricante(nombrefabricante)

            entrada = input('>>>>')
            if entrada == 'crear fabricante':
                parametros = []

                a = input("introduzca el nombre del fabricante que quiere crear")

                # now = datetime.datetime.now()
                # b = now.strftime("%d/%m/%Y %H:%M:%S")
                b = input("introduzca el CIF del fabricante a crear")
                creafabricante(a,b)

            elif entrada == 'modificar':
                parametros = []

                a = input("introduzca el nombre del fabricante que quiere modificar")

                # now = datetime.datetime.now()
                # b = now.strftime("%d/%m/%Y %H:%M:%S")
                # d = input("introduzca el numero de piezas que quiere")
                b= input("introduzca el nuevo nombre del fabricante")
                c = input("introduzca el nuevo nombre CIF")

                try:
                    modificafabricante(a, b,c)
                except:
                    sqlite3.OperationalError
                    print("fabricante modificado")
            elif entrada == 'eliminar':
                parametros = []

                a = input("introduzca el nombre de la pieza que quiere eliminar")

                try:
                    eliminafabricante(a)
                except:
                    sqlite3.OperationalError
                    print("fabricante eliminado")

            elif entrada == 'ver piezas':

                nombreexactofabricante=input("introduzca el nombre exacto del fabricante")
                verpiezasfabricante(nombreexactofabricante,True)

                entradacompra=input("desea comprar esa pieza ? si asi lo desea escriba el numero que aparece al principio de la frase, si no pulse no")
                if(entradacompra=="no"):
                    print("ok")


                elif(int(entradacompra)==0):

                      piezazasa=verpiezasfabricante(nombreexactofabricante,False)[1][0]

                      try:
                        comprapiezaporfabricante(nombreexactofabricante,piezazasa,False)
                      except:
                          print("Ha petado, pon el nombre bien")
                      print(f"wubalubadubdub, su pieza ha sido comprada")
                      print(lista_de_la_compra)

                elif(entradacompra.isdigit() and int(entradacompra)!=0):
                   piezazita=verpiezasfabricante(nombreexactofabricante,False)[2*int(entradacompra)+1][2*int(entradacompra)]
                   comprapiezaporfabricante(nombreexactofabricante,piezazita,False)
                   print(f"wubalubadubdub, su pieza ha sido añadida a la lista de la compra, para pagar vaya a generar infrome")


            else:

                n = 0
                for numero in resultado:
                    if (n == int(entrada)):
                        print("olala")
                        print(numero)
                        temporal = buscainfromacionfabricante(numero)
                        print(f'Numero de registro : {temporal[1]}')
                        print(f'ID : {temporal[0]}')
                        print(f'CIF : {temporal[2]}')
                        break
                    n = n + 1







    else:
        print('Ha introducido mal el comando')

print('El programa ha finalizado')