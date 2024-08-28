from datetime import date

from componentes.animal import Animal
from componentes.cliente import Cliente

class Adopcion:
    def __init__(self, animal: Animal, cliente: Cliente):
        fechaActual = date.today()
        self._animal = animal
        self._cliente = cliente
        self._fechaAdopcion = fechaActual

    @staticmethod
    def preguntasEncuesta(pregunta: int):
        preguntas = {
            1: "\n1. ¿Tiene experiencia en el cuidado de mascotas?",
            2: "\n2. ¿Cuánto tiempo puede dedicar diariamente a la atención y el cuidado de la mascota?",
            3: "\n3. ¿Con qué frecuencia planea viajar en los próximos meses?",
            4: "\n4. ¿Tiene un espacio adecuado en su hogar para la mascota, tanto en interiores como en exteriores?",
            5: "\n5. ¿Ha considerado los requisitos específicos de ejercicio y cuidados para la raza/tipo de mascota?",
            6: "\n6. ¿Está dispuesto a someter a la mascota a chequeos veterinarios regulares?",
            7: "\n7. ¿Está dispuesto a recibir visitas por parte de AdoptaLove para enterarnos del estado de la mascota?"
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
    
    def setFechaAdopcion(self, fecha: date):
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