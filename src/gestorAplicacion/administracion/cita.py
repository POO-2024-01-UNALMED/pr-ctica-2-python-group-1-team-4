from componentes.animal import Animal
from componentes.cliente import Cliente
from componentes.empleado import Empleado
from componentes.cupo import Cupo

class Cita:
    def __init__(self, cliente: Cliente, animal: Animal, empleado: Empleado, cupo: Cupo, servicio: int):
        self._cliente = cliente
        self._animal = animal
        self._empleado = empleado
        cupo.setDisponible(False)
        self._cupo = cupo

        if servicio == 1:
            self._costo = 10000
            self._cliente.agregar_puntos(3)
        elif servicio == 2:
            self._costo = 20000
            self._cliente.agregar_puntos(5)
        elif servicio == 3:
            self._costo = 15000
            self._cliente.agregar_puntos(4)
        else:
            self._costo = 0

#METODO PARA APLICAR EL DESCUENTO
    def aplicarDescuento(self):
        self._costo -= (self._costo * 0.1)

#METODO GET
    def getAnimal(self):
        return self._animal
    
#toString
    def __str__(self):
        profesion = ""

        if self._empleado.getProfesion() == 'VETERINARIO':
            profesion = "Veterinario"
        elif self._empleado.getProfesion() == 'CUIDADOR':
            profesion = "Cuidador"
        elif self._empleado.getProfesion() == 'PELUQUERO':
            profesion = "Peluquero"

        return (f"Cliente: {self._cliente.getNombre()}\n"
                f"Mascota: {self._animal.getNombre()}\n"
                f"{profesion}: {self._empleado.getNombre()}\n"
                f"Costo cita: {self._costo} pesos \n"
                f"Fecha de la cita: {self._cupo.fechaFormateada()}\n"
                f"Hora: {self._cupo.getHoraInicio()} - {self._cupo.getHoraFin()}")