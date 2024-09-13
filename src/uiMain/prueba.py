import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from gestorAplicacion.componentes.animal import Animal, EstadoSalud
from gestorAplicacion.componentes.cliente import Cliente
from gestorAplicacion.componentes.empleado import Empleado, Rol
from gestorAplicacion.administracion.adopcion import Adopcion
from gestorAplicacion.administracion.socializar import Socializar

print("")
#CREACION DE LOS CLIENTES --------------

cliente1 = Cliente("Juan Pérez", 30, 123456789, 987654321, "Calle Falsa 123") #CONSTRUCTOR 1
cliente2= Cliente("María López", 25, 987654321) #CONSTRUCTOR 2

# PROBAR MÉTODOS DE CLIENTE
print("Información del Cliente 1:")
print(cliente1)  # Usando el método __str__

print("Información del Cliente 2:")
print(cliente2)  # Usando el método __str__

# Actualizar datos del Cliente 1
cliente1.actualizar_datos(31, 123456789, "Avenida Siempre Viva 742")
print("Después de actualizar datos del Cliente 1:")
print(cliente1)

# Agregar y disminuir puntos
cliente1.agregar_puntos(50)
print("Puntos del Cliente 1 después de agregar 50 puntos:")
print(cliente1.getPuntos())

cliente1.disminuir_puntos(20)
print("Puntos del Cliente 1 después de disminuir 20 puntos:")
print(cliente1.getPuntos())

# Asignar una mascota al Cliente 1
cliente1.setMascota("Perro")
print("Información del Cliente 1 después de asignar una mascota:")
print(cliente1)

# Probar métodos del Cliente 2
cliente2.agregar_puntos(30)
print("Puntos del Cliente 2 después de agregar 30 puntos:")
print(cliente2.getPuntos())

cliente2.setMascota("Gato")
print("Información del Cliente 2 después de asignar una mascota:")
print(cliente2)

print("")

#CREACION DE LOS ANIMALES -------------------

animal1 = Animal("Rex", "Perro", 24, "Masculino", EstadoSalud.SANO) #CONSTRUCTOR 1
animal2 = Animal("Mia", "Gato", 12, "Femenino") #CONSTRUCTOR 2

print("")

# PROBAR MÉTODOS DE ANIMAL
print("Información del Animal 1:")
print(animal1)  # Usando el método __str__

print("\nInformación del Animal 2:")
print(animal2)  # Usando el método __str__

# Actualizar datos del Animal 1
animal1.setEdad(25)
animal1.setEstadoSalud(EstadoSalud.ENFERMO)
print("\nDespués de actualizar datos del Animal 1:")
print(animal1)

# Actualizar datos del Animal 2
animal2.setSexo("Macho")
animal2.setEstadoSalud(EstadoSalud.ENTRATAMIENTO)
print("\nDespués de actualizar datos del Animal 2:")
print(animal2)

print("")

#CREACIÓN DE LAS ADOPCIONES ------------

adopcion1= Adopcion(animal1, cliente1)
adopcion2 = Adopcion(animal2, cliente2)

print("\nDETALLES DE LAS ADOPCIONES: \n")
print(adopcion1)
print()
print(adopcion2)

#CREACIÓN DE EMPLEADO Y PRUEBA DE MÉTODOS --------------

empleado1 = Empleado("Juan Pérez", 30, 123456789, 987654321, "Calle Falsa 123", Rol.VETERINARIO)

print()
# Probar métodos
print(empleado1)  #Imprimir información del empleado

print()

print("Profesión:", empleado1.getProfesion().value)

print()

print("¿Tiene cupos disponibles?", empleado1.tiene_cupos())

# Mostrar cupos disponibles para el lunes (0)

print()
lunes_cupos = empleado1.cupos_disponibles(0)

print("Cupos disponibles el lunes:")

for cupo in lunes_cupos:
    print(cupo.getDia(), cupo, cupo.isDisponible())


# Actualizar agenda y mostrar resultados
empleado1.actualizar_agenda()
print("\nAgenda actualizada para el empleado 1, para la siguiente semana:\n")

for dia in empleado1.getCupo():
    for cupo in dia:
        print(cupo.fechaFormateada(),cupo, cupo.isDisponible())

    print()

if __name__ == "__main__":
    x=input("registrar o match")
    if x=="registrar":
        nombre=input("nombre")
        edad= int (input ("e"))
        celular=input("c")
        participar= bool (input("True/false"))
        print("mascota")
        nombrem=input("n")
        edadm= int(input("edadm"))
        caracteristicas= input("separa comas")
        mascota= Animal(nombrem,edadm,caracteristicas)
        socializar=Socializar()
        cliente = Cliente(nombre,edad,celular,participar,mascota)
        socializar.registrar_cliente(cliente) 
    elif x=="match":
        registro=input("si/no")
        socializar=Socializar()
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

print (cliente.getNombre())
print (mascota.getNombre())


