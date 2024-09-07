from multimethod import multimethod
from ..componentes.animal import Animal
from .persona import Persona 
# con ".persona" le indicamos al scrip que Persona está en el mismo paquete de Cliente.

# OKY RUIZ DE LA ROSA
# SALOMÉ MURILLO GAVIRIA
# NICOLAS DAVID ZAMBRANO MURCIA
#DANIEL ALBERTO ZAPATA CASTAÑO

# DESCRIPCIÓN DE LA CLASE:
# Representa a los usuarios que se registran para adoptar animales, agendar citas para servicios
# y comprar productos en la tienda.

class Cliente(Persona):

    @multimethod
    def __init__(self, nombre: str, edad: int, cedula: int, telefono: int, direccion: str):
        super().__init__(nombre, edad, cedula, telefono, direccion)
        self._puntos = 0
        self._mascota = None
    
    @multimethod
    def __init__(self, nombre: str, edad: int, telefono: str, participar : bool, mascota: Animal):
        super().__init__(nombre, edad, telefono)
        self._participar=participar
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
    
    #DEFINIENDO EL MÉTODO ABSTRACTO DE PERSONA
    def __str__(self):
        mascota_info = f", Mascota: {self.getMascota()}" if self._mascota else ""

        return (f"Nombre: {self.getNombre()}, Edad: {self.getEdad()}, Cédula: {self.getCedula()}, "
                f"Teléfono: {self.getTelefono()}, Dirección: {self.getDireccion()}, "
                f"Puntos: {self.getPuntos()}{mascota_info}\n")


