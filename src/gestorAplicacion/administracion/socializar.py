from gestorAplicacion.administracion.cita import Cita
from gestorAplicacion.componentes.animal import Animal
from gestorAplicacion.componentes.cliente import Cliente

class socializar:
    def __init__(self):
        clientes=[] #Lista para albergar clientes participantes
        citas=[]

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
    
    def match(self):
        
        print("Buscando coincidencias para socializar...")
        # Filtrar los clientes con características de mascotas similares.
        for i in range(len(self.clientes)):
            for j in range(i + 1, len(self.clientes)):
                cliente1 = self.clientes[i]
                cliente2 = self.clientes[j]
                if self.comparar_caracteristicas(cliente1.mascota, cliente2.mascota):
                    # Crear cita si hay coincidencias
                    nueva_cita = Cita(cliente1, cliente2)
                    self.citas.append(nueva_cita)
                    print(f"Match encontrado: {nueva_cita}")

    def comparar_caracteristicas(self, animal1, animal2):
        # Comparar características de las mascotas.
        return len(set(animal1.caracteristicas).intersection(set(animal2.caracteristicas))) > 0

    def calificar_animal(self, animal, calificacion):
        animal.calificar(calificacion)

    def eliminar_cliente(self, cliente):
        self.clientes.remove(cliente)
        print(f"Cliente {cliente.nombre} ha sido eliminado del programa.")


if __name__ == "__main__":
    x=input("registrar o match")
    if x=="registrar":
        nombre=input("nombre")
        edad= int (input ("e"))
        celular=input("c")
        participar= bool (input("True/false"))
        socializar.clientes.append(Cliente)
        print("mascota")
        nombrem=input("n")
        edadm= int(input("edadm"))
        caracteristicas= input("separa comas")
        mascota= Animal(nombre,edad,caracteristicas)
        cliente = Cliente(nombre,edad,celular,participar,mascota)
    elif x=="match":
        registro=input("si/no")
        if registro=="si":
            print(socializar.clientes)
            socializar.match()

        elif registro=="no":
            nombre=input("nombre")
            edad= int (input ("e"))
            celular=input("c")
            participar= bool (input("True/false"))
            socializar.clientes.append(Cliente)
            print("mascota")
            nombrem=input("n")
            edadm= int(input("edadm"))
            caracteristicas= input("separa comas")
            mascota= Animal(nombre,edad,caracteristicas)
            cliente = Cliente(nombre,edad,celular,participar,mascota)
