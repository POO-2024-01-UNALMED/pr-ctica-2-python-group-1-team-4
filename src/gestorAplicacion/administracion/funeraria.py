from typing import List

from gestorAplicacion.administracion.centroAdopcion import CentroAdopcion
from gestorAplicacion.componentes.muerto import Muerto

#DANIEL ALBERTO ZAPATA CASTAÑO
#OKY RUIZ DE LA ROSA
#SALOMÉ MURILLO GAVIRIA
#NICOLAS DAVID ZAMBRANO MURCIA
	
#DESCRIPCIÓN DE LA CLASE:
#Proporcionar servicios de cremación y entierro para mascotas fallecidas, gestionando la memoria de los animales.

class Funeraria: 

    ##Atributos
    tumbas: List['Muerto'] = []
    cenizas: List['Muerto'] = []

    ##Constructor ----------------------------------------------------------------------------
    def __init__(self, centro: CentroAdopcion):
        self._centro = centro

    ##Setter and Getter ----------------------------------------------------------------------
    def getCentro(self):
        return self._centro
    
    def setCentro(self, centro: CentroAdopcion):
        self._centro = centro

    def getNombre(self):
        return self._centro.getNombre()
    
    @classmethod
    def getTumbas(cls):
        return cls.tumbas
    
    @classmethod
    def getCenizas(cls):
        return cls.cenizas
    
    ##Métodos --------------------------------------------------------------------------------
    def espacioTumbas(self):
        if len(self.tumbas) <= 15:
            return True
        else: 
            return False
    
    def espacioCenizas(self):
        if len(self.cenizas) <= 25:
            return True
        else:
            return False
        
    def visita(self, tipo):
        resultado = ""
        #Se controla el tipo ingresado
        if (tipo=="tumbas"):
            indice = 0
            for i in self.tumbas:
                indice += 1
                resultado += str(indice)+". "+str(i)
            return resultado
        elif (tipo=="cenizas"):
            indice = 0
            for i in self.cenizas:
                indice += 1
                resultado += str(indice)+". "+str(i)
            return resultado

    def florCenizas(self, indice, flores):
        if 0 <= indice < len(self.cenizas):  # Verificar si el índice es válido (dentro de rango)
            return self.cenizas[indice].ponerFlor(flores)  # No restar 1 al índice
        else: 
            return "Índice inválido, no se pudo colocar las flores."
    
    def florTumbas(self, indice, flores):
        if 0 <= indice < len(self.tumbas):  # Verificar si el índice es válido
            return self.tumbas[indice].ponerFlor(flores)  # No restar 1 al índice
        else: 
            return "Índice inválido, no se pudo colocar las flores."
