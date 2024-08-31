from enum import Enum
from multimethod import multimethod

# OKY RUIZ DE LA ROSA
# SALOMÉ MURILLO GAVIRIA
# NICOLAS DAVID ZAMBRANO MURCIA
#DANIEL ALBERTO ZAPATA CASTAÑO

#DESCRIPCIÓN DE LA CLASE:
#Representa a los animales disponibles para adopción, incluye atributos como nombre, tipo, edad, sexo y estado de salud, 
#de igual forma representa a las mascotas que un usuario registre para recibir un servicio o agendar una cita.

# Enumerado con los estados de salud posibles de un animal:
class EstadoSalud(Enum):
    SANO = "Sano"
    ENFERMO = "Enfermo"
    ENTRATAMIENTO = "En tratamiento"

class Animal:

    @multimethod
    def __init__(self, nombre: str, tipo: str, edad: int, sexo: str, estadoSalud : EstadoSalud):
        self._nombre = nombre
        self._tipo = tipo
        self._edad = edad  # Edad en meses
        self._sexo = sexo
        self._estadoSalud = estadoSalud

    @multimethod
    def __init__(self, nombre: str, tipo: str, edad: int, sexo: str):
        self._nombre = nombre
        self._tipo = tipo
        self._edad = edad  # Edad en meses
        self._estadoSalud = None
        self._sexo = sexo
     

    # Métodos setter y getter

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setEspecie(self, tipo):
        self._tipo = tipo

    def getEspecie(self):
        return self._tipo

    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad

    def setSexo(self, sexo):
        self._sexo = sexo

    def getSexo(self):
        return self._sexo

    def setEstadoSalud(self, estadoSalud):
        self._estadoSalud = estadoSalud

    def getEstadoSalud(self):
        return self._estadoSalud

    def __str__(self):
        if self._estadoSalud is not None:
            return (f"Nombre: {self.getNombre()}, Especie: {self.getEspecie()}, "
                    f"Edad (meses): {self.getEdad()}, Sexo: {self.getSexo()}, "
                    f"Estado de salud: {self.getEstadoSalud().value}")
        else:
            return (f"Nombre: {self.getNombre()}, Especie: {self.getEspecie()}, "
                    f"Edad (meses): {self.getEdad()}, Sexo: {self.getSexo()}")

