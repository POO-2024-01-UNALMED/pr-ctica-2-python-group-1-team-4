from multimethod import multimethod

#DANIEL ALBERTO ZAPATA CASTAÑO
#OKY RUIZ DE LA ROSA
#SALOMÉ MURILLO GAVIRIA
#NICOLAS DAVID ZAMBRANO MURCIA

#DESCRIPCIÓN DE LA CLASE:
#Representa los artículos en venta en la tienda, incluyendo nombre, precio, tipo de animal y cantidad disponible. 


class Producto:
    @multimethod
    def __init__(self, nombre: str, precio: float, tipoAnimal: str, cantidadUnidades: int):
        self._nombre = nombre
        self._precio = precio
        self._tipoAnimal = tipoAnimal
        self._cantidadUnidades = cantidadUnidades

    @multimethod
    def __init__(self, nombre: str, precio: float, cantidadUnidades: int):
        self._nombre = nombre
        self._precio = precio
        self._tipoAnimal = "Uso general"
        self._cantidadUnidades = cantidadUnidades

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
    
if __name__ == "__main__":
    #PRUEBAS
    producto1 = Producto("Alimento para perros", 50.0, "Perros", 20)
    producto2 = Producto("Juguete para gatos", 15.0, 10)
    
    print(producto1)
    print(producto2)