from datetime import timedelta

from ..componentes.animal import Animal
from ..componentes.cliente import Cliente
from ..componentes.empleado import Empleado
from ..componentes.cupo import Cupo
from multimethod import multimethod 

#DANIEL ALBERTO ZAPATA CASTAÑO
#OKY RUIZ DE LA ROSA
#SALOMÉ MURILLO GAVIRIA
#NICOLAS DAVID ZAMBRANO MURCIA

#DESCRIPCIÓN DE LA CLASE:
#Almacena información sobre las citas agendadas para servicios como veterinaria, guardería o peluquería, incluyendo el animal, cliente, empleado y costo.


class Cita:
    @multimethod
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
    
    @multimethod
    def __init__(self, cliente: Cliente, animal: Animal, cliente2: Cliente, animal2: Animal, fecha):
        self._cliente = cliente
        self._cliente2 = cliente2
        self._animal=cliente.getMascota()
        self._animal2=cliente2.getMascota()
        self._fecha=fecha
        self._estado = "pendiente"
    @multimethod
    def __init__(self, cliente1, cliente2):
        self.cliente1 = cliente1
        self.cliente2 = cliente2

    
    def actualizar_estado(self, nuevo_estado):
        if nuevo_estado in ["aceptada", "rechazada", "aplazada"]:
            self.estado = nuevo_estado
            if nuevo_estado == "aplazada":
                # Aplazar la cita al día siguiente
                self.fecha += timedelta(days=1)
        else:
            print("Estado no válido")
    
    def aplicarDescuento(self):
        self._costo -= (self._costo * 0.1)

    def getAnimal(self):
        return self._animal
    
    def __str__(self):
        profesion = ""

        if self._empleado.getProfesion() == 'Veterinario':
            profesion = "Veterinario"
        elif self._empleado.getProfesion() == 'Cuidador':
            profesion = "Cuidador"
        elif self._empleado.getProfesion() == 'Peluquero':
            profesion = "Peluquero"

        return (f"Cliente: {self._cliente.getNombre()}\n"
                f"Mascota: {self._animal.getNombre()}\n"
                f"{profesion}: {self._empleado.getNombre()}\n"
                f"Costo cita: {self._costo} pesos \n"
                f"Fecha de la cita: {self._cupo.fechaFormateada()}\n"
                f"Hora: {self._cupo.getHoraInicio()} - {self._cupo.getHoraFin()}")