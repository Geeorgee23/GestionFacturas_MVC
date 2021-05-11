from factura import Factura
from controlador import Controlador
from datetime import datetime

controlador = Controlador()

while True:

    print("**********MENU**********")
    print("Actualmente hay ",controlador.numFacturas()," registradas")
    print("1.- Añadir Factura")
    print("2.- Listar Facturas Pendientes de Pago")
    print("3.- Listar Facturas Pagadas")
    print("4.- Pagar Factura")
    print("5.- Salir")

    while True:
        try:
            op=int(input("Introduce una opción: "))
            if op<=5 and op>=1:
                break
            else:
                print("Introduce un número del 1 al 5!")
        except ValueError:
            print("Introduce un valor numérico!")


    if op==5:
        print("Adiós, vuelve pronto!")
        break

    if op==1:
        print()

        
        print("Añadiendo Factura...")
        id_factura=input("Introduce el id de la factura: ")

        #fecha
        now = datetime.now()
        fecha_formateada = now.strftime("%d/%m/%Y %H:%M")

        dniEmisor=input("Introduce el dni del emisor: ")
        dniReceptor=input("Introduce el dni del receptor: ")

        #Crear Factura
        factura = Factura(id_factura,fecha_formateada,dniEmisor,dniReceptor)

        if controlador.addFactura(factura):
            print("Factura añadida correctamente!")
        else:
            print("Error al añadir la factura!")

        print()

        #añadir lineas factura
        while True:
            print("¿Qué productos quieres añadir?")
            #productos
            print(controlador.mostrarProductos())
            
            producto=input("Selecciona uno (si no quieres más introduce FIN): ")

            if producto=="FIN":
                break
            else:
                cantidad=input("¿Cuantos quieres? ")
                if controlador.addLineaFactura(id_factura,producto,cantidad):
                    print("Linea añadida correctamente!")
                    print()
                else:
                    print("Error al añadir la linea")
                    print()

        print()


    if op==2:
        print()
        print("*****Facturas Pendientes de Pago*****")
        print("-------------------------------------")
        print("Visualizar por: ")
        print("1.- Dni Emisor")
        print("2.- Dni Receptor")
        print("3.- Todas")

        while True:
            try:
                op=int(input("Introduce una opción: "))
                if op<=3 and op>=1:
                    break
                else:
                    print("Introduce un número del 1 al 3!")
            except ValueError:
                print("Introduce un valor numérico!")


        if op==1:
            dni=input("Introduce el dni del Emisor: ")
            for i in controlador.mostrarFacturas(False,1,dni):
                print(i)
            print()
            

        if op==2:
            dni=input("Introduce el dni del Receptor: ")
            for i in controlador.mostrarFacturas(False,2,dni):
                print(i)
            print()
            
        if op==3:
            for i in controlador.mostrarFacturas(False,3):
                print(i)
            print()
        continue


    if op==3:
        print()
        print("*****Facturas Pagadas*****")
        print("-------------------------------------")
        print("Visualizar por: ")
        print("1.- Dni Emisor")
        print("2.- Dni Receptor")
        print("3.- Todas")

        while True:
            try:
                op=int(input("Introduce una opción: "))
                if op<=3 and op>=1:
                    break
                else:
                    print("Introduce un número del 1 al 3!")
            except ValueError:
                print("Introduce un valor numérico!")


        if op==1:
            dni=input("Introduce el dni del Emisor: ")
            for i in controlador.mostrarFacturas(True,1,dni):
                print(i)
            print()

        if op==2:
            dni=input("Introduce el dni del Receptor: ")
            for i in controlador.mostrarFacturas(True,2,dni):
                print(i)
            print()

        if op==3:
            for i in controlador.mostrarFacturas(True,3):
                print(i)
            print()


    if op==4:
        id_factura=input("Introduce el id de la factura: ")

        if controlador.facturaPagada(id_factura):
            print("Factura Pagada!")
        else:
            print("Error al pagar la factura!")

        print()
            


        

