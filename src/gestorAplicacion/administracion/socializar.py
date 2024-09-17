
from gestorAplicacion.administracion.cita import Cita
from gestorAplicacion.componentes.animal import Animal
from gestorAplicacion.componentes.cliente import Cliente

#DANIEL ALBERTO ZAPATA CASTAÑO
#OKY RUIZ DE LA ROSA
#SALOMÉ MURILLO GAVIRIA
#NICOLAS DAVID ZAMBRANO MURCIA

#DESCRIPCIÓN DE LA CLASE:
#Contiene el proceso de búsqueda de matches y la realización de los mismos, permitiendo a los clientes encontrar al próximo amigo de su mascota, y porque no ,también de ellos.

#Inicializamos las listas de socializar.
class Socializar:
    def __init__(self):
        self.clientes = []  # Lista para albergar clientes participantes
        self.citas = []
    
    def registrar_cliente(self, cliente):#Se define un metodo para registrar un cliente.    
        self.clientes.append(cliente) #Se agrega el cliente a la lista de clientes que participan en socializar.
        print(f"Cliente {cliente._nombre} registrado con éxito.") #Se confirma el registro con exito.

    def buscar_posibles_matches(self, cliente): #Se define un metodo para buscar matches
        posibles_matches = [] #Se crea la lista posibles matches, donde se almacenan los clientes con los que hay un posible match.
        for otro_cliente in self.clientes: #Se aplica el metodo comparar caracteristicas, devuelve minimo una caracteristica en comun, se agregar el cliente a la lista.
            if otro_cliente != cliente and self.comparar_caracteristicas(cliente._mascota, otro_cliente._mascota):
                posibles_matches.append(otro_cliente)
        return posibles_matches

    def comparar_caracteristicas(self, animal1, animal2): #Se define el metodo para comparar las caracteristicas
        return len(set(animal1.caracteristicas).intersection(set(animal2.caracteristicas))) > 0 #Encuentra la(s) caracteristicas en comun.

    def seleccionar_y_hacer_match(self, cliente): #Se define la función para poder elegir un cliente y hacer match con este.
        posibles_matches = self.buscar_posibles_matches(cliente)
        
        if posibles_matches: #Muestra los clientes posibles para hacer match y le pide elgir uno.
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

    def eliminar_cliente(self, cliente): #cuando elige un cliente este se retira de la lista socializar.
        if cliente in self.clientes:
            self.clientes.remove(cliente)
            print(f"Cliente {cliente.nombre} ha sido eliminado del programa.")
        else:
            print("Cliente no encontrado.")