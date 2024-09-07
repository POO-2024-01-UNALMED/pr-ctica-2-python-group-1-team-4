from abc import ABC, abstractmethod
from multimethod import multimethod

# OKY RUIZ DE LA ROSA
# SALOMÉ MURILLO GAVIRIA
# NICOLAS DAVID ZAMBRANO MURCIA
#DANIEL ALBERTO ZAPATA CASTAÑO

#DESCRIPCIÓN DE LA CLASE:
#Representa a las personas relacionadas con el centro de adopción,
# almacena información personal básica en común de Clientes y Empleados.

#CLASE ABSTRACTA
class Persona(ABC):
    
    @multimethod
    def __init__(self, nombre: str, edad: int, cedula: int, telefono:str, direccion: str):
        self._nombre = nombre
        self._edad = edad
        self._cedula = cedula
        self._telefono = telefono
        self._direccion = direccion

    @multimethod
    def __init__(self, nombre:str, edad: int, cedula: int):
        self.__init__(nombre, edad, cedula, 0, "No aplica")
    
    @multimethod
    def __init__(self, nombre: str, edad: int, telefono:str):
        self._nombre = nombre
        self._edad = edad
        self._telefono = telefono


    # MÉTODOS SETTER Y GETTER ----

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

    # Método abstracto (necesario para que sea abstracta)
    @abstractmethod
    def __str__(self):
        pass

