from datetime import datetime

#localDate de dia.
class Cita:
    def __init__(self, dia: datetime, horaInicio: str, horaFin: str, disponible: bool):
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
    def fechaFormateada(self):
        return self._dia.strftime('%d %B %Y')
    
    def __str__(self):
        return f"De {self._horaInicio} a {self._horaFin}"