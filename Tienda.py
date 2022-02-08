from datetime import datetime
from tokenize import Double

class transaccion:

    venta = 1
    Abastecimiento = 2 #constantes

    def __init__(self,tipo: int , cantidad: int):
        self._tipo = tipo
        self._cantidad = cantidad
        self._fecha = datetime.now()

    @property
    def tipo(self):
        return self._tipo   

    @tipo.setter
    def tipo(self,valor):
        if valor == 1 or valor == 2:
            self._tipo=val



class libro:
    def __init__(self,isbn:str,titulo:str,pcompra:Double,pventa:Double,cantidad:Double) -> None:
        self.isbn = isbn    
        self.titulo = titulo
        self.pventa = pventa    
        self.pcompra = pcompra   
        self.cantidad = cantidad  
        self.transacciones = []       #list()

        
class tienda:
    def __init__(self) -> None:
        self.dinero_en_caja = 1000000
        self.catalogo = {}           #dict()

if __name__ == "__main__":
    trans1 = transaccion(transaccion.venta,5)
    trans2 = transaccion(transaccion.Abastecimiento,10)


    print(f"tipo t1: {trans1.tipo}")
    print(f"tipo t2: {trans2.tipo}")
    
    trans2.tipo=20
    print(f"tipo t1: {trans1.cantidad}")
    print(f"tipo t2: {trans2.cantidad}")
