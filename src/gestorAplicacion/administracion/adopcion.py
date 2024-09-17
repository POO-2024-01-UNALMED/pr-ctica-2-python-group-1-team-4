from datetime import date

# OKY RUIZ DE LA ROSA
# SALOMÉ MURILLO GAVIRIA
# NICOLAS DAVID ZAMBRANO MURCIA
#DANIEL ALBERTO ZAPATA CASTAÑO

# DESCRIPCIÓN DE LA CLASE:
# Registra información sobre el proceso de adopción, incluyendo el animal adoptado,
# el adoptante y la fecha de adopción.

class Adopcion:
    def __init__(self, animal, cliente):
        fechaActual = date.today()
        self._animal = animal
        self._cliente = cliente
        self._fechaAdopcion = fechaActual

    @staticmethod
    def preguntasEncuesta(pregunta: int):
        preguntas = {
            1: "1. ¿Tiene experiencia en el cuidado de mascotas?",
            2: "2. ¿Cuánto tiempo puede dedicar diariamente a la atención y el cuidado de la mascota?",
            3: "3. ¿Tiene un espacio adecuado en su hogar para la mascota, tanto en interiores como en exteriores?",
            4: "4. ¿Ha considerado los requisitos específicos de ejercicio y cuidados para eltipo de mascota?",
            5: "5. ¿Está dispuesto a someter a la mascota a chequeos veterinarios regulares?",
            6: "6. ¿Está dispuesto a recibir visitas por parte de AdoptaLove para enterarnos del estado de la mascota?"
        }
        return preguntas.get(pregunta, " ")
    
#METODOS GET Y SET
    def setAnimal(self, animal):
        self._animal = animal

    def getAnimal(self):
        return self._animal
    
    def setCliente(self, cliente):
        self._cliente = cliente

    def getCliente(self):
        return self._cliente
    
    def setFechaAdopcion(self, fecha):
        self._fechaAdopcion = fecha

    def getFechaAdopcion(self):
        return self._fechaAdopcion
    
#toString
    def __str__(self):
        return (f"- Adoptante: {self._cliente.getNombre()}"
                f"\n- CC: {self._cliente.getCedula()}"
                f"\n- Mascota: {self._animal.getNombre()}"
                f"\n- Tipo: {self._animal.getEspecie()}"
                f"\n- Fecha: {self._fechaAdopcion}")
    

    
