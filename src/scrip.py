from gestorAplicacion.componentes.animal import Animal, EstadoSalud

from gestorAplicacion.componentes.cliente import Cliente

from gestorAplicacion.administracion.adopcion import Adopcion

from gestorAplicacion.componentes.producto import Producto


#CREACION DE LOS ANIMALES --------------

animal1 = Animal("Rex", "Perro", 24, "Masculino", EstadoSalud.SANO) #CONSTRUCTOR 1
animal2 = Animal("Mia", "Gato", 12, "Femenino") #CONSTRUCTOR 2

#CREACION DE LOS CLIENTES --------------

cliente1 = Cliente("Juan Pérez", 30, 123456789, 987654321, "Calle Falsa 123") #CONSTRUCTOR 1
cliente2= Cliente("María López", 25, 987654321) #CONSTRUCTOR 2


#CREACIÓN DE LAS ADOPCIONES ------------

adopcion1= Adopcion(animal1, cliente1)
adopcion2 = Adopcion(animal2, cliente2)

print("\nDETALLES DE LAS ADOPCIONES: \n")
print(adopcion1)
print()
print(adopcion2)

#CREACION DE PRODUCTOS -----------------

producto1 = Producto("Alimento para perros", 50.0, "Perros", 20)
producto2 = Producto("Juguete para gatos", 15.0, 10)

print("\nLOS PRODUCTOS SON: ")
print(producto1)
print(producto2)

