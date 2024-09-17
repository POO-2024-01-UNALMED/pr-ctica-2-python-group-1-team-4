from enum import Enum
from multimethod import multimethod 

# Enumerado con los estados de salud posibles de un animal.
class EstadoSalud(Enum):
    SANO = "Sano"
    ENFERMO = "Enfermo"
    ENTRATAMIENTO = "En tratamiento"

class Animal:

    @multimethod
    def __init__(self, nombre = None, tipo = None, edad = 0, sexo = None, estadoSalud = None):
        self._nombre = nombre
        self._tipo = tipo
        self._edad = edad  # Edad en meses
        self._sexo = sexo
        self._estadoSalud = estadoSalud
    
    @multimethod
    def __init__(self, nombre: str, edad: int, caracteristicas: str):
        self._nombre = nombre
        self._edad = edad  # Edad en meses
        self.caracteristicas= [carac.strip() for carac in caracteristicas.split(',')]
    #    self.puntaje= 100

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

    # Método para representar el objeto como cadena
    def __str__(self):
        if self._estadoSalud is not None:
            return (f"Nombre: {self.getNombre()}, Especie: {self.getEspecie()}, "
                    f"Edad (meses): {self.getEdad()}, Sexo: {self.getSexo()}, "
                    f"Estado de salud: {self.getEstadoSalud().value}")
        else:
            return (f"Nombre: {self.getNombre()}, Especie: {self.getEspecie()}, "
                    f"Edad (meses): {self.getEdad()}, Sexo: {self.getSexo()}")

# Ejemplo de uso
if __name__ == "__main__":
    animal1 = Animal("Rex", "Perro", 24, "Masculino", EstadoSalud.SANO) #CONSTRUCTOR 1
    animal2 = Animal("Mia", "Gato", 12, "Femenino") #CONSTRUCTOR 2

    print()
    print(animal1)
    print(animal2)
    print("La  sobrecarga de constructores funciona correctamente, ya está todo lo de JAVA\n")

