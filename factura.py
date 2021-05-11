class Factura:
    def __init__(self,id_factura,fecha,dniEmisor,dniReceptor):
        self.id_factura=id_factura
        self.fecha=fecha
        self.dniEmisor=dniEmisor
        self.dniReceptor=dniReceptor
        self.pagada=False
        self.base=0.0
        self.iva=21
        self.total=0
        self.lineasFactura=[]


    def getIdFactura(self):
        return self.id_factura

    def getFecha(self):
        return self.fecha

    def getDniEmisor(self):
        return self.dniEmisor

    def getDniReceptor(self):
        return self.dniReceptor

    def getPagada(self):
        return self.pagada

    def getBase(self):
        return self.base

    def getIva(self):
        return self.iva

    def getTotal(self):
        return self.total

    def getLineasFactura(self):
        return self.lineasFactura


    def addLineaFactura(self,producto,cantidad,base):
        self.base+=base
        self.total=self.base+(self.base*(self.iva/100))
        self.lineasFactura.append((producto,cantidad,base))

    def mostrarLineasFactura(self):
        lineas=""
        for i in self.lineasFactura:
            lineas+="\t"+str(i[0])+"\t"+str(i[1])+"\t"+str(i[2])+"\n\t\t\t"

        return lineas


    def facturaPagada(self):
        self.pagada=True
            


    