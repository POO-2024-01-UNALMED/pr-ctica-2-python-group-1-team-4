from gestorAplicacion.componentes.animal import Animal, EstadoSalud
from gestorAplicacion.componentes.cliente import Cliente
from gestorAplicacion.administracion.adopcion import Adopcion

#CREACION DE LOS CLIENTES --------------

cliente1 = Cliente("Juan Pérez", 30, 123456789, 987654321, "Calle Falsa 123") #CONSTRUCTOR 1
cliente2= Cliente("María López", 25, 987654321) #CONSTRUCTOR 2

print("")

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





