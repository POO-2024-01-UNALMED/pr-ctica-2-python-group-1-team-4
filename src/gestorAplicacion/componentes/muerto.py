from typing import List

from gestorAplicacion.componentes.animal import Animal
from gestorAplicacion.componentes.cliente import Cliente

#DANIEL ALBERTO ZAPATA CASTAÑO
#OKY RUIZ DE LA ROSA
#SALOMÉ MURILLO GAVIRIA
#NICOLAS DAVID ZAMBRANO MURCIA
	
#DESCRIPCIÓN DE LA CLASE:
#Representa a los animales que han fallecido, almacenando información sobre el dueño, fecha de fallecimiento y mensajes de recuerdo.

class Muerto:

    # Constructor 

    def __init__(self, animal = None, fecha = "", mensaje = "", dueño = None, tiempo = "", tipo = ""):
        self._animal = animal
        self._fecha = fecha
        self._mensaje = mensaje
        self._dueño = dueño
        self._tiempo = tiempo
        self._tipo = tipo
        self._flores: List[str] = ["No hay flores aquí."]


#METODOS GET Y SET
    def setAnimal(self, animal):
        self._animal = animal
    
    def getAnimal(self):
        return self._animal
    
    def setFlores(self, flores):
        self._flores = flores

    def getFlores(self):
        return self._flores
    
    def setFecha(self, fecha):
        self._fecha = fecha

    def getFecha(self):
        return self._fecha
    
    def setMensaje(self, mensaje):
        self._mensaje = mensaje

    def getMensaje(self):
        return self._mensaje
    
    def setDueño(self, dueño):
        self._dueño = dueño

    def getDueño(self):
        return self._dueño
    
    def setTipo(self, tipo):
        self._tipo = tipo

    def getTipo(self):
        return self._tipo
    
    def setTiempo(self, tiempo):
        self._tiempo = tiempo

    def getTiempo(self):
        return self._tiempo
    
#VERIFICA SI LAS TUMBAS/OSARIOS TIENEN FLORES. SI HAY MENOS DE 5, LAS AGREGA.
    def ponerFlor(self, flor):
        if self._flores[0] == "No hay flores aquí.":
            self._flores.clear()
            self._flores.append(flor)
            return f"Pronto, un jardinero pondrá las flores: {flor}."
        elif len(self._flores) <= 5:
            self._flores.append(flor)
            return f"Pronto, un jardinero pondrá las flores: {flor}."
        else:
            return "Hay un límite de 5 tipos de flores."
        
#IMPRIME LAS FLORES QUE HAYAN
    def mostrarFlores(self):
        if self._flores[0] == "No hay flores aquí":
            return self._flores[0]
        elif len(self._flores) == 1:
            return f"Hay: {self._flores[0]}"
        else:
            acumulador = "Flores que hay: "
            for flor in self._flores:
                acumulador += f"{flor} "
            return acumulador.strip()
        
#toString
    def __str__(self):
        return f"{self._animal.getNombre()} {self._fecha} {self._mensaje} {self.mostrarFlores()}\n"