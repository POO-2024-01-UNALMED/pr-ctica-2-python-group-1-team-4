from persona import Persona
from animal import Animal
from multimethod import multimethod

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

    def actualizar_datos(self, edad: int, telefono: int, direccion: str):
        self.setEdad(edad)
        self.setTelefono(telefono)
        self.setDireccion(direccion)

    def agregar_puntos(self, puntos: int):
        self._puntos += puntos

    def disminuir_puntos(self, puntos: int):
        self._puntos -= puntos

    def getPuntos(self) -> int:
        return self._puntos

    def setMascota(self, mascota: Animal):
        self._mascota = mascota

    def getMascota(self) -> Animal:
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

