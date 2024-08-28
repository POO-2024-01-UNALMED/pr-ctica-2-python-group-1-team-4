from datetime import date, timedelta
from babel.dates import format_date # Para darle formato

class Cupo:
    def __init__(self, dia: date, horaInicio: str, horaFin: str, disponible: bool):
        self._dia = dia
        self._horaInicio = horaInicio
        self._horaFin = horaFin
        self._disponible = disponible

#METODOS GET Y SET
    def getDia(self):
        return self._dia
    
    def getHoraInicio(self):
        return self._horaInicio
    
    def getHoraFin(self):
        return self._horaFin
    
    def isDisponible(self):
        return self._disponible
    
    def setDisponible(self, booleano: bool):
        self._disponible = booleano
    
#OTROS METODOS
    
    def __str__(self) -> str:
        # Mostrar la franja horaria del cupo
        return f"De {self._horaInicio} a {self._horaFin}"

    
    def fechaFormateada(self) -> str:
        # Formatear la fecha en español
        return format_date(self._dia, format='long', locale='es_ES')
    

if __name__ == "__main__":

    print()
    hoy = date.today() 
    cupo = Cupo(hoy, "10:00", "12:00", True)

    # Mostrar la fecha actual
    print("Fecha actual:", cupo.getDia())  # Muestra la fecha de hoy

    # Aumentar 2 días a la fecha actual
    nueva_fecha = cupo.getDia() + timedelta(days=2)

    # Mostrar la nueva fecha
    print("Nueva fecha (2 días después):", nueva_fecha)

    # Actualizar la fecha en el objeto Cupo
    cupo._dia = nueva_fecha

    # Mostrar la fecha actualizada en el objeto Cupo
    print("Fecha actualizada en el objeto Cupo:", cupo.getDia())  # Muestra la nueva fecha

    print()

    print(cupo.fechaFormateada())
    print(cupo)