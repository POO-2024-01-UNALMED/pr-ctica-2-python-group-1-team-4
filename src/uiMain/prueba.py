import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# IMPORTACIÓN ADMINISTRADORES
from gestorAplicacion.administracion.centroAdopcion import CentroAdopcion
from gestorAplicacion.administracion.centroAdopcion import TipoServicio
from gestorAplicacion.administracion.adopcion import Adopcion
from gestorAplicacion.administracion.cita import Cita
from gestorAplicacion.administracion.tienda import Tienda
from gestorAplicacion.administracion.funeraria import Funeraria
from gestorAplicacion.administracion.socializar import Socializar

# IMPORTACIÓN COMPONENTES
#from gestorAplicacion.componentes.persona import Persona
from gestorAplicacion.componentes.cliente import Cliente
from gestorAplicacion.componentes.animal import Animal
from gestorAplicacion.componentes.animal import EstadoSalud
from gestorAplicacion.componentes.cupo import Cupo
from gestorAplicacion.componentes.empleado import Empleado
from gestorAplicacion.componentes.muerto import Muerto
from gestorAplicacion.componentes.producto import Producto
from gestorAplicacion.componentes.empleado import Rol

#IMPORTACIÓN BASE DE DATOS
from baseDatos.deserializador import Deserializador
from baseDatos.serializador import Serializador

#IMPORTACIÓN DE EXCEPCIONES
from gestorExcepciones.ErrorAplicacion import ErrorAplicacion
from gestorExcepciones.ErrorAplicacion import ErrorFormularioVacio

# Lista donde se guardarán las sedes
sedes = []

# Creando las instancias de CentroAdopcion
sede1 = CentroAdopcion("SEDE BELLO", 25, TipoServicio.GUARDERIA)
sedes.append(sede1)
sede2 = CentroAdopcion("SEDE ITAGÜI", 20, TipoServicio.VETERINARIA)
sedes.append(sede2)
sede3 = CentroAdopcion("SEDE MEDELLÍN", 20, TipoServicio.PELUQUERIA)
sedes.append(sede3)

# Agregar animales a cada sede
# Sede 1
sede1.agregar_animal(Animal("Capitán", "Canario", 2, "Macho", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Nala", "Canario", 3, "Hembra", EstadoSalud.ENFERMO))
sede1.agregar_animal(Animal("Rocky", "Conejo", 2, "Macho", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Sky", "Conejo", 3, "Hembra", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Reina", "Gato", 3, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede1.agregar_animal(Animal("Rey", "Gato", 3, "Macho", EstadoSalud.ENFERMO))
sede1.agregar_animal(Animal("Rolly", "Hámster", 1, "Hembra", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Zuma", "Hámster", 2, "Macho", EstadoSalud.ENFERMO))
sede1.agregar_animal(Animal("Tobi", "Perro", 5, "Macho", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Dino", "Perro", 4, "Macho", EstadoSalud.ENTRATAMIENTO))

# Sede 2
sede2.agregar_animal(Animal("Golfo", "Conejo", 3, "Macho", EstadoSalud.ENFERMO))
sede2.agregar_animal(Animal("Luna", "Conejo", 3, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede2.agregar_animal(Animal("Frapee", "Canario", 2, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede2.agregar_animal(Animal("Luna", "Gato", 6, "Hembra", EstadoSalud.ENFERMO))
sede2.agregar_animal(Animal("Everest", "Gato", 4, "Hembra", EstadoSalud.SANO))
sede2.agregar_animal(Animal("Junior", "Hámster", 2, "Macho", EstadoSalud.SANO))
sede2.agregar_animal(Animal("Puppy", "Hámster", 3, "Hembra", EstadoSalud.ENTRATAMIENTO))

# Sede 3
sede3.agregar_animal(Animal("Thor", "Perro", 6, "Macho", EstadoSalud.SANO))
sede3.agregar_animal(Animal("Teo", "Perro", 7, "Macho", EstadoSalud.SANO))
sede3.agregar_animal(Animal("Mia", "Gato", 4, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede3.agregar_animal(Animal("Lola", "Gato", 6, "Hembra", EstadoSalud.ENFERMO))
sede3.agregar_animal(Animal("Sony", "Conejo", 3, "Macho", EstadoSalud.SANO))
sede3.agregar_animal(Animal("River", "Conejo", 4, "Macho", EstadoSalud.SANO))
sede3.agregar_animal(Animal("Kira", "Canario", 3, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede3.agregar_animal(Animal("Furry", "Canario", 4, "Macho", EstadoSalud.ENFERMO))
sede3.agregar_animal(Animal("Princea", "Hámster", 2, "Hembra", EstadoSalud.ENTRATAMIENTO))

# Agregar empleados a cada sede
# Sede 1 (Guardería)
sede1.agregar_empleado(Empleado("Juan Zapata", 25, 21491118, 313775896, "Carrera 30", Rol.CUIDADOR))
sede1.agregar_empleado(Empleado("Julieta Vanegas", 21, 58941118, 310789651, "Calle 96", Rol.CUIDADOR))
sede1.agregar_empleado(Empleado("Andres Garcia", 34, 10278056, 300845962, "Calle 80", Rol.CUIDADOR))
sede1.agregar_empleado(Empleado("Ana Restrepo", 28, 47889566, 315986487, "Carrera Septima", Rol.CUIDADOR))
sede1.agregar_empleado(Empleado("Wilson Jimenez", 36, 70925845, 313153964, "Carrera 72a", Rol.CUIDADOR))
sede1.agregar_empleado(Empleado("Mateo Munera", 25, 56892347, 311567832, "Carrera 68", Rol.CUIDADOR))

# Sede 2 (Veterinaria)
sede2.agregar_empleado(Empleado("Carlos Rivera", 23, 12307004, 328748995, "Carrera 30", Rol.VETERINARIO))
sede2.agregar_empleado(Empleado("Marta Puerta", 28, 66973892, 304236021, "Calle 90", Rol.VETERINARIO))
sede2.agregar_empleado(Empleado("Karen Diaz", 32, 11277768, 314943886, "Calle 86", Rol.VETERINARIO))
sede2.agregar_empleado(Empleado("Mario Martinez", 30, 79698181, 300564603, "Carrera 67b", Rol.VETERINARIO))

# Sede 3 (Peluquería)
sede3.agregar_empleado(Empleado("Natalia Fernandez", 26, 70233557, 318529646, "Calle 63", Rol.PELUQUERO))
sede3.agregar_empleado(Empleado("Jose Bueno", 39, 50270440, 306537090, "Calle 50", Rol.PELUQUERO))
sede3.agregar_empleado(Empleado("Diana Henao", 28, 69620661, 330175882, "Carrera Sexta", Rol.PELUQUERO))
sede3.agregar_empleado(Empleado("Julian Taborda", 36, 37664642, 332773881, "Carrera 72c", Rol.PELUQUERO))
sede3.agregar_empleado(Empleado("Andrea Higuita", 21, 55000283, 332697785, "Carrera 61", Rol.PELUQUERO))

# Crear cliente y agregar puntos
cliente1 = Cliente("Oky", 18, 1072253440, 3106762877, "Medellín")
cliente1.agregar_puntos(20)

for sede in sedes:
    print(sede)

print(cliente1)

print("-----------------------------------------------------------------")

# CLIENTES BY DEFAULT
c1 = Cliente("Miguel Cortés", 19, 1020349)
c2 = Cliente("Julian Sanchéz", 18, 234933)
c3 = Cliente("Catalina Salazar", 18, 666)
c4 = Cliente("Nico Murcia", 19, 3335632)
c5 = Cliente("Richard Pérez", 19, 339393)

# ANIMALES BY DEFAULT
b1 = Animal("Rocky", "Perro", 8, "Macho")
b2 = Animal("Zimba", "Gato", 13, "Macho")
b3 = Animal("Coco", "Pato", 15, "Hembra")
b4 = Animal("Lucero", "Vaca", 9, "Macho")
b5 = Animal("Milo", "Hamster", 16, "Hembra")

# MUERTOS BY DEFAULT
a1 = Muerto(b1, "18/08/2022", "Eres nuestro ángel de cuatro patas, siempre en nuestros corazones.", c1, "Permanente", "tumba")
a2 = Muerto(b2, "23/01/2023", "Tu lealtad y amor nunca serán olvidados.", c2, "4 años", "tumba")
a3 = Muerto(b3, "07/05/2022", "Eternamente en nuestros pensamientos.", c3, "Permanente", "Osario")
a4 = Muerto(b4, "21/07/2021", "Fuiste la vaca más bonita de mi rancho.", c4, "7 años", "tumba")
a5 = Muerto(b5, "18/08/2024", "Te queremos y te extrañamos.", c5, "6 años", "Osario")

# FLORES BY DEFAULT
a4.ponerFlor("Girasoles")
a3.ponerFlor("Margaritas")
a1.ponerFlor("Rosas")
a1.ponerFlor("Lirios")
a2.ponerFlor("Claveles")
a2.ponerFlor("Hortensias")

# TUMBAS Y CENIZAS BY DEFAULT
Funeraria.cenizas.append(a5)
Funeraria.tumbas.append(a4)
Funeraria.tumbas.append(a2)
Funeraria.cenizas.append(a3)
Funeraria.tumbas.append(a1)

cenizas = Funeraria.getCenizas()
tumbas = Funeraria.getTumbas()

for ceniza in cenizas:
    print(ceniza) 
print("------------------")
for tumba in tumbas:
    print(tumba)

print("--------------------------------------------------------------------------")

# PRODUCTOS INICIALES CON LOS QUE EMPIEZA LA TIENDA
Tienda.agregarProducto(Producto("Pack juguetes", 14000, 15, "perros"))
Tienda.agregarProducto(Producto("Huesos", 6000, 20, "perros"))
Tienda.agregarProducto(Producto("Correas", 25000, 10))
Tienda.agregarProducto(Producto("Pack juguetes", 18000, 10, "gatos"))
Tienda.agregarProducto(Producto("Rascadores", 40000, 5, "gatos"))
Tienda.agregarProducto(Producto("Comederos de acero", 20000, 25))
Tienda.agregarProducto(Producto("Comederos con formas", 30000, 10))
Tienda.agregarProducto(Producto("Shampoo", 60000, 20, "perros"))
Tienda.agregarProducto(Producto("Shampoo", 65000, 20, "gatos"))
Tienda.agregarProducto(Producto("Pienso generico", 30000, 30, "perros"))
Tienda.agregarProducto(Producto("Pienso generico", 35000, 20, "gatos"))
Tienda.agregarProducto(Producto("Alpiste", 12000, 20, "aves"))
Tienda.agregarProducto(Producto("Jaula", 50000, 6, "aves"))
Tienda.agregarProducto(Producto("Casa de madera", 100000, 2, "aves"))
Tienda.agregarProducto(Producto("Semillas y cereales", 15000, 20, "hamsters"))
Tienda.agregarProducto(Producto("Jaula", 30000, 10, "hamsters"))
Tienda.agregarProducto(Producto("Ruedas", 22000, 10, "hamsters"))
Tienda.agregarProducto(Producto("Heno", 23000, 20, "conejos"))
Tienda.agregarProducto(Producto("Corral metálico", 30000, 10, "conejos"))

productos = Tienda.getProductos()

for producto in productos:
    print(producto)

print("-----------------------------------------------------------------------")