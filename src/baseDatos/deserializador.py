import os
import pickle

from gestorAplicacion.administracion.centroAdopcion import CentroAdopcion
from gestorAplicacion.administracion.funeraria import Funeraria
from gestorAplicacion.administracion.tienda import Tienda
from gestorAplicacion.componentes.muerto import Muerto


class Deserializador:

    @staticmethod
    def deserializar(lista, nombre):
        try:
            # Obtener la ruta absoluta
            base_path = os.path.abspath('')
            path = os.path.join(base_path, 'src/baseDatos/temp', f'{nombre}.txt')

            # Si la lista es None, inicializarla como lista vacía
            if lista is None:
                lista = []

            # Deserializar la lista desde el archivo
            with open(path, 'rb') as file:
                lista.extend(pickle.load(file))

        except FileNotFoundError:
            print(f"No se encuentra el archivo {nombre}.txt")
        except IOError:
            print(f"Error en el flujo de lectura del archivo {nombre}.txt")
        except pickle.UnpicklingError:
            print("Error en la deserialización")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")

    @staticmethod
    def deserializarListas():
        # Métodos estáticos
        Deserializador.deserializar(CentroAdopcion.getSedes(), "Sedes")
        Deserializador.deserializar(CentroAdopcion.getClientes(), "Clientes")
        Deserializador.deserializar(Funeraria.getTumbas(), "Tumbas")
        Deserializador.deserializar(Funeraria.getCenizas(), "Cenizas")
        Deserializador.deserializar(Tienda.getProductos(), "Productos")

        # Métodos no estáticos
        m = Muerto()
        Deserializador.deserializar(m.getFlores(), "Flores")
        e = Tienda()
        Deserializador.deserializar(e.getEmpleados(), "Empleados_Tienda")