from datetime import date, timedelta
from enum import Enum

from .persona import Persona # para indicar que se encuentra el mismo paquete
from .cupo import Cupo #para indicar que se encuentra en el mismo paqute

# OKY RUIZ DE LA ROSA
# SALOMÉ MURILLO GAVIRIA
# NICOLAS DAVID ZAMBRANO MURCIA
#DANIEL ALBERTO ZAPATA CASTAÑO

# DESCRIPCIÓN DE LA CLASE
# Representa al personal del centro, que puede ser veterinario, peluquero, cuidador o tendero.
# Cada empleado excepto los tenderos tienen citas (objetos de tipo Cupo) en sus agendas para atender a 
# los clientes y mascotas.

# Enumeración para los roles de empleado
class Rol(Enum):
    VETERINARIO = "Veterinario"
    PELUQUERO = "Peluquero" 
    CUIDADOR = "Cuidador"
    TENDERO = "Tendero"

class Empleado(Persona):

    def __init__(self, nombre, edad, cedula, telefono, direccion, profesion):
        super().__init__(nombre, edad, cedula, telefono, direccion)
        self._profesion = profesion
        self._agenda_dias = []  # Lista de listas para la agenda

        if self._profesion != Rol.TENDERO:  # El tendero no ofrece citas.
            self.llenar_agenda()

    
    def llenar_agenda(self):

        # cantidad de ciclos dependiendo del dia (lunes - sábado)
        ciclos = [6, 5, 4, 3, 2, 1]

        fecha_actual = date.today()
        dia_semana = fecha_actual.weekday()  # Número del día de la semana (0=lunes, 6=domingo)

        # llenar los dias restantes de la semana: 

        # si es domingo, se habilitan los cupos del lunes siguiente hasta el sábado.
        if dia_semana == 6: 
            fecha_actual += timedelta(days = 1)  # Omitir el domingo

            for j in range(6):
                cupos_dia = []
                cupos_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                cupos_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                cupos_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                cupos_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))
                
                self._agenda_dias.append(cupos_dia)
                fecha_actual += timedelta(days=1)  # Pasar al siguiente día.

        else:
            # cuando es un día diferente al domingo, se habilitan los cupos de los dias restantes de la semana
            for i in range(ciclos[dia_semana]):
                cupos_dia = []
                cupos_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                cupos_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                cupos_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                cupos_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))

                self._agenda_dias.append(cupos_dia)
                fecha_actual += timedelta(days=1)  # Pasar al siguiente día.
                # deja la fecha hasta el domingo.

            #--------------------------------
            # Llenar los dias que faltaron, es decir los anteriores, pero para la siguiente semana.

            #Como el domingo y lunes habilitaron todos los dias de la semana, no es necesario que estén aquí
            if dia_semana != 0 and dia_semana != 6: # por eso se omiten.

                fecha_actual += timedelta(days=1)  # Omitir el domingo

                for j in range(dia_semana):
                    cupos_dia = []
                    cupos_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                    cupos_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                    cupos_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                    cupos_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))

                    self._agenda_dias.append(cupos_dia)
                    fecha_actual += timedelta(days=1)  # Pasar al siguiente día.

    
    def actualizar_agenda(self):

        #recorremos la lista que contiene las listas de cupos por dia.
        for array_dia in self._agenda_dias:

            fecha_actual = date.today()  # La fecha de actualización
            
            #Comprobar si la fecha de los cupos es anterior a la actual.
            if array_dia[0].getDia() < fecha_actual:

                #si el dia (lunes, martes, miercoles..) coincide con el de actualización, entonces se habilitan
                #cupos para ese mismo día.
                if fecha_actual.weekday() == array_dia[0].getDia().weekday():
                    array_dia.clear()  # Limpiar la lista de ese día

                    #llenarlo con nuevos cupos
                    array_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                    array_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                    array_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                    array_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))

                else:

                    num_dia = array_dia[0].getDia().weekday()
                    continuar = True
                    
                    while continuar:
                        # si el dia (lunes, martes..) no coincide con el actual, entonces buscamos con el que
    				    #coincida en los próximos días.
                        fecha_actual += timedelta(days=1)  # Aumentamos al día siguiente

                        if fecha_actual.weekday() == num_dia:
                            array_dia.clear()  # Limpiar el array list de ese día.


                            array_dia.append(Cupo(fecha_actual, "8:00", "10:00", True))
                            array_dia.append(Cupo(fecha_actual, "10:00", "12:00", True))
                            array_dia.append(Cupo(fecha_actual, "14:00", "16:00", True))
                            array_dia.append(Cupo(fecha_actual, "16:00", "18:00", True))
                            continuar = True

    
    #COMPROBAR SI EL EMPLEADO TIENE CUPOS
    def tiene_cupos(self):
        self.actualizar_agenda()
        for cupos_por_dia in self._agenda_dias:
            for cupo in cupos_por_dia:
                if cupo.isDisponible():
                    return True
        return False
    

    #RETORNA LOS CUPOS DISPONIBLES DE UN EMPLEADO EN UN DÍA ESPECIFICO
    def cupos_disponibles(self, i):

        cupos_disponibles = []

        for array_dia in self._agenda_dias:
            if array_dia[0].getDia().weekday() == i:
                for cupo in array_dia:
                    if cupo.isDisponible():
                        cupos_disponibles.append(cupo)
                break
        return cupos_disponibles
    
    #MÉTODOS SET Y GET
    def getProfesion(self):
        return self._profesion.value

    def getCupo(self):
        return self._agenda_dias

    def __str__(self):
        return f"Nombre: {self.getNombre()}, Edad: {self.getEdad()} años, Celular: {self.getTelefono()}"
    
