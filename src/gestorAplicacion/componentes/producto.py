

class Producto:
    def _init__(self, nombre: str, precio: float, tipoAnimal: str, cantidadUnidades: int):
        self._nombre = nombre
        self._precio = precio
        self._tipoAnimal = tipoAnimal
        self._cantidadUnidades = cantidadUnidades

    #otro constructor

#METODOS GET Y SET
    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre
    
    def setPrecio(self, precio):
        self._precio = precio

    def getPrecio(self):
        return self._precio
    
    def setTipoAnimal(self, tipoAnimal):
        self._tipoAnimal = tipoAnimal

    def getTipoAnimal(self):
        return self._tipoAnimal
    
    def setCantidadUnidades(self, cantidadUnidades):
        self._cantidadUnidades = cantidadUnidades

    def getCantidadUnidades(self):
        return self._cantidadUnidades
    
#toString
    def __str__(self):
        return f"\nProducto: {self.getNombre()}\nPrecio: {self.getPrecio()}\nDirigido a: {self.getTipoAnimal()}\nCantidad unidades: {self.getCantidadUnidades()}\n"