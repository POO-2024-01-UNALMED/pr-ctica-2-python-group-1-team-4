from datetime import date, timedelta
from enum import Enum
from persona import Persona
from cupo import Cupo

# Enumeración para los roles de empleado
class Rol(Enum):
    VETERINARIO = "Veterinario"
    PELUQUERO = "Peluquero"
    CUIDADOR = "Cuidador"
    TENDERO = "Tendero"

class Empleado(Persona):

    def __init__(self, nombre: str, edad: int, cedula: int, telefono: int, direccion: str, profesion: Rol):
        super().__init__(nombre, edad, cedula, telefono, direccion)
        self.profesion = profesion
        self.agenda_dias = []  # Lista de listas para la agenda

        if self.profesion != Rol.TENDERO:  # El tendero no ofrece citas.
            self.llenar_agenda()

    
    def llenar_agenda(self):
        ciclos = [6, 5, 4, 3, 2, 1]
        fecha_actual = date.today()
        dia_semana = fecha_actual.weekday()  # Número del día de la semana (0=lunes, 6=domingo)

        if dia_semana == 6:  # Si es domingo
            fecha_actual += timedelta(days=1)  # Omitir el domingo

            for _ in range(6):
                cupos_dia = []
                cupos_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                cupos_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                cupos_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                cupos_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))
                
                self.agenda_dias.append(cupos_dia)
                fecha_actual += timedelta(days=1)  # Pasar al siguiente día.

        else:
            for i in range(ciclos[dia_semana]):
                cupos_dia = []
                cupos_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                cupos_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                cupos_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                cupos_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))

                self.agenda_dias.append(cupos_dia)
                fecha_actual += timedelta(days=1)  # Pasar al siguiente día.

            if dia_semana != 0 and dia_semana != 6:  # Omitir el domingo
                fecha_actual += timedelta(days=1)  # Omitir el domingo

                for j in range(dia_semana):
                    cupos_dia = []
                    cupos_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                    cupos_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                    cupos_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                    cupos_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))

                    self.agenda_dias.append(cupos_dia)
                    fecha_actual += timedelta(days=1)  # Pasar al siguiente día.