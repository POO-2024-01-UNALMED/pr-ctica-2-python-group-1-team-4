from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from multimethod import multimethod

if TYPE_CHECKING:
    from gestorAplicacion.componentes.animal import Animal, EstadoSalud
    from gestorAplicacion.componentes.cliente import Cliente
    from gestorAplicacion.componentes.empleado import Empleado
    from .adopcion import Adopcion
    from .cita import Cita
    from gestorAplicacion.administracion.tienda import Tienda


#DANIEL ALBERTO ZAPATA CASTAÑO
#OKY RUIZ DE LA ROSA
#SALOMÉ MURILLO GAVIRIA
#NICOLAS DAVID ZAMBRANO MURCIA

#DESCRIPCIÓN DE LA CLASE:
#La clase CentroAdopcion hace referencia a las sedes, gestiona la operación del centro de adopción, incluyendo clientes, empleados, animales, citas y adopciones. 
#Facilita el proceso de adopción y la prestación de servicios relacionados.


class TipoServicio(Enum):
    VETERINARIA = "Veterinaria"
    GUARDERIA = "Guardería"
    PELUQUERIA = "Peluquería"

class CentroAdopcion:
    clientes_AdoptaLove: List['Cliente'] = []

# SOBRECARGA CONSTRUCTORES
    @multimethod
    def __init__(self, nombre: str, espacios: int, servicio: TipoServicio, tienda: Tienda):
        self._nombre = nombre
        self._espaciosDisponibles = espacios
        self._servicio = servicio
        self._tienda = tienda
        self._empleados: List['Empleado'] = []
        self._animales: List['Animal'] = []
        self._adopciones: List['Adopcion'] = []
        self._citas_agendadas: List['Cita'] = []

    @multimethod
    def __init__(self, nombre: str, espacios: int, servicio: TipoServicio):
        self.__init__(nombre, espacios, servicio, None)
    
#SOBRECARGA DE MÉTODOS
    @multimethod
    def animales_disponibles(self):
        disponibles = []
        for mascota in self._animales:
            if mascota.getEstadoSalud() != EstadoSalud.ENFERMO:
                disponibles.append(mascota)
        return disponibles

    @multimethod
    def animales_disponibles(self, tipo: str):
        disponibles = []
        for mascota in self._animales:
            if mascota.getEstadoSalud() != EstadoSalud.ENFERMO:
                if tipo is None or mascota.getEspecie().lower() == tipo.lower():
                    disponibles.append(mascota)
        return disponibles
    
#MÉTODO DE CLASE
    @classmethod
    def is_cliente(cls, cliente: Cliente):
        cliente_adoptaLove = next((existe for existe in cls.clientes_AdoptaLove if existe.getCedula() == cliente.getCedula()), None)
        if cliente_adoptaLove is None:
            cliente_adoptaLove = cliente
            cls.clientes_AdoptaLove.append(cliente_adoptaLove)
        else:
            cliente_adoptaLove.actualizar_datos(cliente.getEdad(), cliente.getTelefono(), cliente.getDireccion())
        return cliente_adoptaLove
    
#OTROS METODOS
    def tiene_mascotas(self):
        for mascota in self._animales:
            if mascota.getEstadoSalud() != EstadoSalud.ENFERMO:
                return True
        return False

    def registrar_adopciones(self, mascotas: List['Animal'], cliente: Cliente):
        adopciones_realizadas = []
        cliente_adoptaLove = self.is_cliente(cliente)
        for mascota in mascotas:
            if mascota:
                nueva_adopcion = Adopcion(mascota, cliente_adoptaLove)
                self._adopciones.append(nueva_adopcion)
                nueva_adopcion.getCliente().agregar_puntos(5)
                adopciones_realizadas.append(nueva_adopcion)
        return adopciones_realizadas

    def borrar_animal(self, animal: Animal):
        if animal in self._animales:
            self._animales.remove(animal)
            self._espaciosDisponibles += 1

    def agregar_animal(self, animal: Animal):
        if self._espaciosDisponibles > 0:
            self._animales.append(animal)
            self._espaciosDisponibles -= 1

    def tiene_empleados(self):
        emp_Disponibles = []
        for empleado in self._empleados:
            if empleado.tiene_cupos():
                emp_Disponibles.append(empleado)
        return emp_Disponibles
    
    def agregar_empleado(self, empleado: Empleado):
        self._empleados.append(empleado)

#MÉTODOS GET Y SET
    def getNombre(self):
        return self._nombre

    def setNombre(self, nombre: str):
        self._nombre = nombre

    def getEspacios(self):
        return self._espaciosDisponibles

    def setEspacios(self, espacios: int):
        self._espaciosDisponibles = espacios

    def setServicio(self, servicio: 'CentroAdopcion.TipoServicio'):
        self._servicio = servicio

    def getServicio(self):
        return self._servicio

    def getTienda(self):
        return self._tienda

    def setTienda(self, tienda: Tienda):
        self._tienda = tienda

    def getAdopciones(self):
        return self._adopciones

    def getEmpleados(self):
        return self._empleados

    def getAnimales(self):
        return self._animales

    @classmethod
    def getClientes(cls):
        return cls.clientes_AdoptaLove

    def getCitas(self):
        return self._citas_agendadas

#MÉTODO toString
    def __str__(self):
        if self._tienda != None:
            return f"Nombre: {self.getNombre()}, Espacios Disponibles: {self.getEspacios()}, Servicio: {self.getServicio().value}, tienda: si"
        else:
            return f"Nombre: {self.getNombre()}, Espacios Disponibles: {self.getEspacios()}, Servicio: {self.getServicio().value}, tienda: no"    
        
