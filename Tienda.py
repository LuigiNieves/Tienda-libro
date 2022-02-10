from datetime import datetime
from functools import reduce
from tokenize import Double

class transaccion:

    VENTA = 1
    ABASTECIMIENTO = 2 #constantes

    def __init__(self,tipo: int , cantidad: int):
        self._tipo = tipo
        self._cantidad = cantidad
        self._fecha = datetime.now()

    @property
    def tipo(self):
        return self._tipo   

    @property
    def cantidad(self):
            self._cantidad

    @property
    def fecha(self):
            self._fecha       



class libro:
    def __init__(self,isbn:str,titulo:str,pcompra:Double,pventa:Double,cantidad_actual:Double) -> None:
        self.isbn = isbn    
        self.titulo = titulo
        self.pventa = pventa    
        self.pcompra = pcompra   
        self._cantidad_actual = cantidad_actual 
        self.transacciones = []       #list()

    @property
    def cantidad_actual(sefl):
        return self._cantidad_actual

    @cantidad_actual.setter
    def cantidad_actual(self,nueva_cantidad):
        if nueva_cantidad < 0:
            raise Exception("la cantidad de un libro no puede ser negativa")

        self._cantidad_actual = nueva_cantidad  

    def vender(self,cantidad) -> bool:
        """
        Vende una cantidad dada de ejemplares del libro.Si no hay esa cantidad, no se 
        realiza la venta y retorna falso, si la venta se realiza la venta retorna true
        """
        if self._cantidad_actual>=cantidad):
            self.cantidad_actual-=cantidad
            Transacciones = transaccion(transaccion.VENTA,cantidad)
            self.transacciones.append(Transacciones)
            return True
        else:
            return False   


    def abastecer (self,cantidad):
        self.cantidad_actual += cantidad
        Transaccion=transaccion(transaccion.ABASTECIMIENTO,cantidad)
        self.transacciones.append(transaccion)


    def informar_ejemplares_ventidos(self):
        if len(self.transacciones) > 0: 
            # cantidades=[t.cantidad for t in self.transacciones if t.tipo == transaccion.VENTA] 
            # total_ejemplares = reduce(lambda x,y,:x + y, cantidades)
            # return total_ejemplares
            cantidad_ejemplares = 0
            for trans in self.transacciones:
                if trans.tipo == transaccion.VENTA:
                    cantidad_ejemplares += trans.cantidad
            return cantidad_ejemplares        
        else:
            return 0

    def __str__(self) -> str:
        return f"isbn: {self.isbn} \nTitulo: {self.titulo}" 
        
class tienda:
    def __init__(self) -> None:
        self.dinero_en_caja = 1000000
        self.catalogo = {}           #dict()

    def registrar_libro_en_catalogo(self, titulo, isbn ,pventa ,pcompra ,cantidad_actual):
        if isbn not in self.catalogo.keys():
            Libro=libro(self, titulo, isbn ,pventa ,pcompra ,cantidad_actual)
            self.catalogo[isbn] = Libro
        else:
            raise Exception(f"Ya existe el libro con  ISBN {isbn}") 

    def eliminar_libro_de_catalogo(self,isbn):
        if isbn in self.catalogo.keys()
            del self.catalogo[isbn]
        else:
            raise Exception(f"No existe el libro con ISBN {isbn}")         
       


Libro=libro(1234,"el principito" ,50000 ,60000, 10)
print(Libro)



   
