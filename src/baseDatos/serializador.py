import os
import pickle

from gestorAplicacion.administracion.centroAdopcion import CentroAdopcion
from gestorAplicacion.administracion.funeraria import Funeraria
from gestorAplicacion.administracion.tienda import Tienda
from gestorAplicacion.componentes.muerto import Muerto


class Serializador:

    @staticmethod
    def serializar(lista, nombre):
        try:
            # Obtener la ruta absoluta y crear el directorio si no existe
            base_path = os.path.abspath('')
            path = os.path.join(base_path, 'src/baseDatos/temp', f'{nombre}.txt')

            os.makedirs(os.path.dirname(path), exist_ok=True)

            # Serializar la lista
            with open(path, 'wb') as file:
                pickle.dump(lista, file)

        except FileNotFoundError:
            print("No se encuentra el archivo ingresado")
        except IOError:
            print("Error en el flujo de inicialización")

    @staticmethod
    def serializarListas():
        from uiMain.prueba import Prueba
        # Métodos estáticos
        Serializador.serializar(Prueba.sedes, "Sedes")
        Serializador.serializar(CentroAdopcion.getClientes(), "Clientes")
        Serializador.serializar(Funeraria.getTumbas(), "Tumbas")
        Serializador.serializar(Funeraria.getCenizas(), "Cenizas")
        Serializador.serializar(Tienda.getProductos(), "Productos")
        Serializador.serializar(Tienda.getEmpleados(), "Empleados_Tienda") #lista de empleados debería ser de clase

        #probar
        #Serializador.serializar(Muerto.getFlores(), "Flores")

        # Métodos no estáticos
        m = Muerto()
        Serializador.serializar(m.getFlores(), "Flores")
