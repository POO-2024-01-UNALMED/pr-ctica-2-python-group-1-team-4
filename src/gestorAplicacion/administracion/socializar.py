
from gestorAplicacion.administracion.cita import Cita
from gestorAplicacion.componentes.animal import Animal
from gestorAplicacion.componentes.cliente import Cliente

class Socializar:
 def __init__(self):
        self.clientes = []  # Lista para albergar clientes participantes
        self.citas = []

def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f"Cliente {cliente.nombre} registrado con éxito.")

def buscar_posibles_matches(self, cliente):
        posibles_matches = []
        for otro_cliente in self.clientes:
            if otro_cliente != cliente and self.comparar_caracteristicas(cliente.mascota, otro_cliente.mascota):
                posibles_matches.append(otro_cliente)
        return posibles_matches

def comparar_caracteristicas(self, animal1, animal2):
        return len(set(animal1.caracteristicas).intersection(set(animal2.caracteristicas))) > 0

def seleccionar_y_hacer_match(self, cliente):
        posibles_matches = self.buscar_posibles_matches(cliente)
        
        if posibles_matches:
            print(f"Posibles coincidencias para {cliente.nombre} y su mascota {cliente.mascota.nombre}:")
            for idx, match in enumerate(posibles_matches):
                print(f"{idx + 1}. {match.nombre} con la mascota {match.mascota.nombre}")

            seleccion = int(input("Seleccione el número del cliente con el que desea hacer match: ")) - 1

            if 0 <= seleccion < len(posibles_matches):
                cliente_seleccionado = posibles_matches[seleccion]
                nueva_cita = Cita(cliente, cliente_seleccionado)
                self.citas.append(nueva_cita)
                print(f"¡Match exitoso! {nueva_cita}")
            else:
                print("Selección no válida.")
        else:
            print("No se encontraron posibles coincidencias para su mascota.")

def eliminar_cliente(self, cliente):
        if cliente in self.clientes:
            self.clientes.remove(cliente)
            print(f"Cliente {cliente.nombre} ha sido eliminado del programa.")
        else:
            print("Cliente no encontrado.")

