from factura import Factura

class Controlador:
    def __init__(self):
        self.listaFacturas={}
        self.productos={
                        'tornillo':5,
                        "tuerca":6,
                        "teclado":7,
                        "raton":8,
                        "pantalla":9,
                        "mesa":10,
                        "silla":11
                      }


    def numFacturas(self):
        return len(self.listaFacturas)

    def addFactura(self,factura):
        if factura.getIdFactura() not in self.listaFacturas:
            self.listaFacturas[factura.getIdFactura()]=factura
            return True

        return False

    def mostrarProductos(self):
        listaProductos=""
        for i in self.productos:
            listaProductos+=" - "+str(i)+"\n"

        return listaProductos


    def addLineaFactura(self,id_factura,producto,cantidad):
        if id_factura in self.listaFacturas:
            if producto in self.productos:

                base=self.productos[producto]*int(cantidad)
                self.listaFacturas[id_factura].addLineaFactura(producto,cantidad,base)
                return True
        return False



    def mostrarFacturas(self,estaPagada,opcion,dni=""):
        lista=[]
        for clave,valor in self.listaFacturas.items():
            if valor.getPagada()==estaPagada:
                if opcion==1 and valor.getDniEmisor()==dni:
                    lista.append("Id_Factura: "+clave+"\n\tFecha: "+valor.getFecha()+"\n\tDni Emisor: "+valor.getDniEmisor()+"\n\tDni Receptor: "+valor.getDniReceptor()+"\n\tLineas Factura: "+valor.mostrarLineasFactura()+"\n\tBase: "+str(valor.getBase())+"\n\tIva: "+str(valor.getIva())+"\n\tTotal: "+str(valor.getTotal()))
                if opcion==2 and valor.getDniReceptor()==dni:
                    lista.append("Id_Factura: "+clave+"\n\tFecha: "+valor.getFecha()+"\n\tDni Emisor: "+valor.getDniEmisor()+"\n\tDni Receptor: "+valor.getDniReceptor()+"\n\tLineas Factura: "+valor.mostrarLineasFactura()+"\n\tBase: "+str(valor.getBase())+"\n\tIva: "+str(valor.getIva())+"\n\tTotal: "+str(valor.getTotal()))
                if opcion==3:
                    lista.append("Id_Factura: "+clave+"\n\tFecha: "+valor.getFecha()+"\n\tDni Emisor: "+valor.getDniEmisor()+"\n\tDni Receptor: "+valor.getDniReceptor()+"\n\tLineas Factura: "+valor.mostrarLineasFactura()+"\n\tBase: "+str(valor.getBase())+"\n\tIva: "+str(valor.getIva())+"\n\tTotal: "+str(valor.getTotal()))

        return lista



    def facturaPagada(self,id_factura):
        if id_factura in self.listaFacturas:
            self.listaFacturas[id_factura].facturaPagada()
            return True

        return False

    