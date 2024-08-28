from enum import Enum
from multimethod import multimethod

class EstadoSalud(Enum):
    SANO = "Sano"
    ENFERMO = "Enfermo"
    ENTRATAMIENTO = "En tratamiento"

class Animal:
    @multimethod
    def __init__(self, nombre: str, tipo: str, edad: int, sexo: str, estado_salud = None):
        self._nombre = nombre
        self._tipo = tipo
        self._edad = edad  # Edad en meses
        self._sexo = sexo
        self._estadoSalud = estado_salud

 #   @multimethod
  #  def __init__(self, nombre: str, tipo: str, edad: int, sexo: str):
   #     self._nombre = nombre
    #    self._tipo = tipo
     #   self._edad = edad  # Edad en meses
      ## self._estadoSalud = None
        

    # Métodos setter y getter
    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre

    def setTipo(self, tipo):
        self._tipo = tipo

    def getTipo(self):
        return self._tipo

    def setEdad(self, edad):
        self._edad = edad

    def getEdad(self):
        return self._edad

    def setSexo(self, sexo):
        self._sexo = sexo

    def getSexo(self):
        return self._sexo

    def setEstadoSalud(self, estado_salud):
        self._estadoSalud = estado_salud

    def getEstadoSalud(self):
        return self._estadoSalud

    # Método para representar el objeto como cadena
    def __str__(self):
        if self._estadoSalud is not None:
            return (f"Nombre: {self.getNombre()}, Especie: {self.getTipo()}, "
                    f"Edad (meses): {self.getEdad()}, Sexo: {self.getSexo()}, "
                    f"Estado de salud: {self.getEstadoSalud().value}")
        else:
            return (f"Nombre: {self.getNombre()}, Especie: {self.getTipo()}, "
                    f"Edad (meses): {self.getEdad()}, Sexo: {self.getSexo()}")

# Ejemplo de uso
if __name__ == "__main__":
    animal1 = Animal("Rex", "Perro", 24, "Masculino", EstadoSalud.SANO)
    animal2 = Animal("Mia", "Gato", 12, "Femenino")

    print(animal1)
    print(animal2)