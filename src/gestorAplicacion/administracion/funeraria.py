from centroAdopcion import CentroAdopcion

class Funeraria: 

    ##Atributos
    tumbas = []
    cenizas = []

    ##Constructor ----------------------------------------------------------------------------
    def __init__(self, centro: CentroAdopcion):
        _centro = centro

    ##Setter and Getter ----------------------------------------------------------------------
    def getCentro(self):
        return self._centro
    
    def setCentro(self, centro: CentroAdopcion):
        self._centro = centro

    def getNombre(self):
        return self._centro.getNombre()
    
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
        else:
            indice = 0
            for i in self.cenizas:
                indice += 1
                resultado += str(indice)+". "+str(i)

    def florCenizas(self, indice, flores):
        if indice <= len(self.cenizas):
            indice -= 1
            return self.cenizas[indice].ponerFlor(flores)
        else: 
            return "Índice inválido, no se pudo colocar las flores."
        
    def florTumbas(self, indice, flores):
        if indice <= len(self.tumbas):
            indice -= 1
            return self.tumbas[indice].ponerFlor(flores)
        else: 
            return "Índice inválido, no se pudo colocar las flores."