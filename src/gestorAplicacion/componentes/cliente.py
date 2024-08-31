#from persona import Persona
from abc import ABC, abstractmethod
from multimethod import multimethod

#from persona import Persona

# CLASE PADRE - CLASE ABSTRACTA
class Persona(ABC):
    
    @multimethod
    def __init__(self, nombre: str, edad: int, cedula: int, telefono: int, direccion: str):
        self._nombre = nombre
        self._edad = edad
        self._cedula = cedula
        self._telefono = telefono
        self._direccion = direccion

    @multimethod
    def __init__(self, nombre: str, edad: int, cedula: int):
        self.__init__(nombre, edad, cedula, 0, "No aplica")

    # Métodos setter y getter
    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad

    def setCedula(self, cedula):
        self._cedula = cedula

    def getCedula(self):
        return self._cedula

    def setDireccion(self, direccion):
        self._direccion = direccion

    def getDireccion(self):
        return self._direccion

    def setTelefono(self, telefono):
        self._telefono = telefono

    def getTelefono(self):
        return self._telefono

    # Método abstracto
    @abstractmethod
    def __str__(self):
        pass

# -----------------------------------------

class Cliente(Persona):

    @multimethod
    def __init__(self, nombre: str, edad: int, cedula: int, telefono: int, direccion: str):
        super().__init__(nombre, edad, cedula, telefono, direccion)
        self._puntos = 0
        self._mascota = None
    
    @multimethod
    def __init__(self, nombre: str, edad: int, cedula: int):
        super().__init__(nombre, edad, cedula)
        self._puntos = 0
        self._mascota = None

    def actualizar_datos(self, edad, telefono, direccion):
        self.setEdad(edad)
        self.setTelefono(telefono)
        self.setDireccion(direccion)

    def agregar_puntos(self, puntos):
        self._puntos += puntos

    def disminuir_puntos(self, puntos):
        self._puntos -= puntos

    def getPuntos(self):
        return self._puntos

    def setMascota(self, mascota):
        self._mascota = mascota

    def getMascota(self):
        return self._mascota

    def __str__(self):
        mascota_info = f", Mascota: {self.getMascota()}" if self._mascota else ""

        
        return (f"Nombre: {self.getNombre()}, Edad: {self.getEdad()}, Cédula: {self.getCedula()}, "
                f"Teléfono: {self.getTelefono()}, Dirección: {self.getDireccion()}, "
                f"Puntos: {self.getPuntos()}{mascota_info}\n")


# Ejemplo de uso
if __name__ == "__main__":
    cliente1 = Cliente("Juan Pérez", 30, 123456789, 987654321, "Calle Falsa 123")
    cliente1.agregar_puntos(10)
    
    cliente2 = Cliente("María López", 25, 987654321)
    cliente2.agregar_puntos(5)

    # Imprimir información de los clientes
    print()
    print(cliente1)
    print(cliente2)

    print("La sobrecarga de constructores funciona correctamente. ")

