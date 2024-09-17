import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkinter import *

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
from gestorExcepciones.ErrorAplicacion import ErrorDigitos_Cel_CC
from gestorExcepciones.ErrorAplicacion import ErrorUsuarioMenor
from gestorExcepciones.ErrorAplicacion import ErrorFueraRango

# CREACIÓN DE OBJETOS BASE -----------------------------

#--------------------------------------SEDES, EMPLEADOS Y ANIMALES------------------------------
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
sede1.agregar_animal(Animal("Rocky", "Conejo", 2, "Macho", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Sky", "Conejo", 3, "Hembra", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Reina", "Gato", 3, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede1.agregar_animal(Animal("Rey", "Gato", 3, "Macho", EstadoSalud.ENFERMO))
sede1.agregar_animal(Animal("Rolly", "Hámster", 1, "Hembra", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Tobi", "Perro", 5, "Macho", EstadoSalud.SANO))
sede1.agregar_animal(Animal("Dino", "Perro", 4, "Macho", EstadoSalud.ENTRATAMIENTO))

# Sede 2
sede2.agregar_animal(Animal("Golfo", "Conejo", 3, "Macho", EstadoSalud.ENFERMO))
sede2.agregar_animal(Animal("Luna", "Conejo", 3, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede2.agregar_animal(Animal("Frapee", "Canario", 2, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede2.agregar_animal(Animal("emma", "Gato", 6, "Hembra", EstadoSalud.ENFERMO))
sede2.agregar_animal(Animal("Everest", "Gato", 4, "Hembra", EstadoSalud.SANO))
sede2.agregar_animal(Animal("Junior", "Hámster", 2, "Macho", EstadoSalud.SANO))
#sede2.agregar_animal(Animal("Puppy", "Hámster", 3, "Hembra", EstadoSalud.ENTRATAMIENTO))

# Sede 3
sede3.agregar_animal(Animal("Thor", "Perro", 6, "Macho", EstadoSalud.SANO))
sede3.agregar_animal(Animal("Teo", "Perro", 7, "Macho", EstadoSalud.SANO))
sede3.agregar_animal(Animal("Mia", "Gato", 4, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede3.agregar_animal(Animal("Lola", "Gato", 6, "Hembra", EstadoSalud.ENFERMO))
sede3.agregar_animal(Animal("Sony", "Conejo", 3, "Macho", EstadoSalud.SANO))
sede3.agregar_animal(Animal("River", "Conejo", 4, "Macho", EstadoSalud.SANO))
sede3.agregar_animal(Animal("Kira", "Canario", 3, "Hembra", EstadoSalud.ENTRATAMIENTO))
sede3.agregar_animal(Animal("Furry", "Canario", 4, "Macho", EstadoSalud.ENFERMO))
#sede3.agregar_animal(Animal("Princea", "Hámster", 2, "Hembra", EstadoSalud.ENTRATAMIENTO))

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

#-----------------------------------OBJETOS DE LA FUNERARIA-------------------------------------

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

#----------------------------PRODUCTOS DE LA TIENDA-------------------------------------------------------------
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

c1.agregar_puntos(30)
sede1.clientes_AdoptaLove.append(c1)
tienda1 = Tienda(Empleado("David", 24, 10456874576, 666777000, "Carlos E", Rol.TENDERO))
tienda1 = Tienda(sede1.getEmpleados()[0])

# FIELDFRAME -----------------------

class FieldFrame(Frame):
    
    # CONSTRUCTOR FIELDFRAME
    def __init__(self, frame_principal, titulo_campos, lista_criterios, titulo_entradas, lista_habilitados, tipos_esperados=None, Valores=None, combobox=None):
        # CONSTRUCTOR DEL FRAME PADRE
        super().__init__(frame_principal, bg="thistle1", highlightbackground="purple4", highlightthickness=2)
        self.titulo_campos = titulo_campos  # Título de criterios
        self.lista_criterios = lista_criterios # Nombres de cada criterio
        self.titulo_entradas = titulo_entradas # Título de las entradas
        self.lista_habilitados = lista_habilitados
        self.lista_valores = Valores # Lista de valores por defecto de las entradas
        self.combobox_items = combobox or {}

        self.tipos_esperados = tipos_esperados or {}  # Diccionario con los tipos esperados por campo
        self.lista_entradas = [] # Lista que guarda las Entrys o comboboxes

        # CREAR Y EMPAQUETAR LABELS DE LOS TITULOS
        Label_titulo_criterios = tk.Label(self, text=self.titulo_campos, font=("Times New Roman", 14, "bold", "underline"), fg="purple4", bg = "thistle1")
        Label_titulo_criterios.grid(row=0, column=0, padx=5, pady=10)
        
        Label_titulo_entradas = tk.Label(self, text=self.titulo_entradas, font=("Times New Roman", 14, "bold", "underline" ), fg="purple4", bg = "thistle1")
        Label_titulo_entradas.grid(row=0, column=1, padx=5, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        for i in range(len(self.lista_criterios)):
            # LABEL CRITERIOS
            label_criterio = tk.Label(self, text=self.lista_criterios[i], font=("Times New Roman", 12), bg="plum1", fg="purple4")
            label_criterio.grid(row=i+1, column=0, padx=5, pady=10)

            # CAMPOS DE TEXTO ENTRADAS
            if self.lista_criterios[i] in self.combobox_items:
                entradaValor = ttk.Combobox(self, values=self.combobox_items[self.lista_criterios[i]], state="readonly")
                entradaValor.grid(row=i+1, column=1, padx=5, pady=10)
                if self.lista_valores is not None:
                    entradaValor.set(self.lista_valores[i])
            else:
                entradaValor = tk.Entry(self)
                entradaValor.grid(row=i+1, column=1, padx=5, pady=10)
                if self.lista_valores is not None:
                    entradaValor.insert(0, self.lista_valores[i])

                if self.lista_habilitados is not None and not self.lista_habilitados[i]:
                    entradaValor.configure(state=tk.DISABLED)
            
            self.lista_entradas.append(entradaValor)

        # BOTÓN ACEPTAR 
        self.boton_aceptar = tk.Button(self, text="Aceptar", font=("Verdana", 10), bg="white", width=8, height=1)
        self.boton_aceptar.grid(row=len(self.lista_criterios)+1, column=1, padx=5, pady=2)

        # BOTÓN LIMPIAR
        self.boton_limpiar = tk.Button(self, text="Limpiar", font=("Verdana", 10), bg="white", width=6, height=1, command=self.funborrar)
        self.boton_limpiar.grid(row=len(self.lista_criterios)+1, column=0, padx=5, pady=2)

        self.grid_rowconfigure(len(self.lista_criterios)+1, weight=1)

    def funborrar(self):
        for entrada in self.lista_entradas:
            if isinstance(entrada, ttk.Combobox):  # SI ES UN COMBOBOX
                entrada.set('')  # RESTABLECER EL COMBOBOX
            else:
                entrada.delete("0", "end")  # BORRAR ENTRADAS NORMALES

    def funAceptar(self, funcion, texto = "Aceptar"):
        self.boton_aceptar.config(command=funcion, text=texto)

    def getValue(self, Criterio):
        index = self.lista_criterios.index(Criterio)
        return self.lista_entradas[index].get()
    
    def getEntradas(self):
        listaValores = []
        listaVacios = []
        for i in range(len(self.lista_criterios)):
            if self.lista_habilitados[i] == True:
                valor = self.getValue(self.lista_criterios[i])
                if valor == "":
                    listaVacios.append(self.lista_criterios[i])
                else:
                    # VALIDAR EL TIPO DE DATO ESPERADO
                    tipo_esperado = self.tipos_esperados.get(self.lista_criterios[i], str)

                    if not self.validar_tipo(valor, tipo_esperado):
                        messagebox.showerror("Error: Tipo de dato incorrecto", f"El campo {self.lista_criterios[i]} debe ser de tipo entero.")
                  
                        return False
                    listaValores.append(valor)

        if len(listaVacios) > 0:
            messagebox.showerror("Error",ErrorFormularioVacio(listaVacios))
            return False
        else:
            return listaValores
    
    def validar_tipo(self, valor, tipo_esperado):
        try:
            tipo_esperado(valor)
            return True
        
        except ValueError:
            return False
        
    def validar_cel_cc(self, celular, cedula):

        try:
            if len(celular) == 10 and celular.isdigit():
    
                if len(cedula) >= 7 and cedula.isdigit():
                    return True    
                     
                else:           
                    raise ErrorDigitos_Cel_CC("documento", " debe tener al menos 7 digitos")             
            else:
                raise ErrorDigitos_Cel_CC("celular", " debe tener 10 digitos")
                        
        except ErrorDigitos_Cel_CC as f:  
            f.mostrarMensaje()

    def validar_CC(self, cedula):

        try:
            if len(cedula)>=7 and cedula.isdigit():
                return True
            else:
                raise ErrorDigitos_Cel_CC("documento", " debe tener al menos 7 digitos" )
            
        except ErrorDigitos_Cel_CC as f:
            f.mostrarMensaje()


# -----------------------------------

def abrir_ventana(vent_inicio):

    # CREAR LA VENTANA PRINCIPAL (SECUNDARIA)
    vent_principal = tk.Toplevel(vent_inicio) 


    # ASIGNARLE EL NOMBRE. DIMENCIONES INICIALES Y COLOR DE FONDO
    vent_principal.title("AdoptaLove")
    vent_principal.geometry("1400x800")
    vent_principal.configure(bg='LightBlue1') 
    vent_principal.config(padx = 15, pady = 15)



    # ------ EVENTOS ------
    
    def descripcion_aplicacion():
         messagebox.showinfo("Aplicación","Sabemos que cada momento de tu compañero es importante, tanto su llegada, como su despedida; es por eso que creamos AdoptaLove, para acompañarte y ayudarte a encontrar o despedir a tu compañero de vida. Además te brindamos servicios para el bienestar de tu compañero; podrás agendar citas de peluqueria, veterinaria o guarderia; y, si quieres conocer nuevos amigos podrás socializar con nuestros clientes y sus mascotas; además, si deseas encontrar regalos para tu compañero, en nuestra tienda, encontrarás lo mejor para el.")

    def salir():
        vent_principal.destroy()  # Cerrar la ventana principal
        vent_inicio.deiconify()  # Mostrar nuevamente la ventana de inicio

    def info_desarrolladores():
        messagebox.showinfo("Autores de la aplicación","Oky Ruiz De La Rosa\nSalomé murillo Gaviria\nNicolas David Zambrano Murcia\nDaniel Alberto Zapata Castaño")

    # ------ FUNCIONALIDADES -------

    def clear_frame_bottom():
        for widget in frame_bottom.winfo_children():
            widget.destroy()

    def formato_frame_top(titulo, texto):
        titulo_1.config(text = titulo, font= ("Lucida Handwriting", 20, "bold"))

        descripcionFun.config(text = texto, font = ("Times New Roman", 14), fg= "purple")
       # descripcionFun.pack(side = "bottom", expand=True, fill = "both", pady =3)

    def adoptar_mascota():

        clear_frame_bottom()

        texto = "Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem Ipsum ha sido el texto de relleno estándar de las\n industrias desde el año 1500, cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de textos y los mezcló\nde tal manera que logró hacer un libro de textos especimen.\n "

        formato_frame_top("Funcionalidad adoptar Mascota", texto)
        
        # Creación de un objeto Field Frame
        listaCampos = ["Nombre", "Cédula", "Dirección","edad" ,"Sexo", "pregunta"]
        listaEditables = [True, True, False,True, True, True]
        listaValores = ["", "", "", "","", ""]
        dicTipos = {"Nombre": str, "Cédula": int, "Dirección": str,"edad": int, "Sexo": str, "pregunta":str}

        combobox_items = {"Sexo": ["Masculino", "Femenino", "Otro"], "pregunta":["Messi", "Cristiano"]}

        frame = FieldFrame(frame_bottom, "Persona" ,listaCampos, "Sus datos", listaEditables, dicTipos, listaValores, combobox_items)
        #frame.place(x =0, y = 0 , width=1236, height= 418)
        frame.pack(expand=True, fill="both")

        #---------

        def funcionAnimal():
            datos_cliente = frame.getEntradas()

            def mostrarCliente():
                 datos_animal = frame_Animal.getEntradas()

                 if datos_animal != False:

                    cliente = Cliente(datos_cliente[0], datos_cliente[2], datos_cliente[1])
                    CentroAdopcion.clientes_AdoptaLove.append(cliente)

                    for i in CentroAdopcion.clientes_AdoptaLove:
                        #messagebox.showinfo("DATOS CLIENTE", cliente.__str__())
                        print(i)

                    # Ocultar frame de datos del animal y volver al frame de cliente
                    frame_Animal.destroy()

                    frame.funborrar()
                    #frame.place(x=0, y=0, width=1236, height=418) 
                    frame.pack(expand=True, fill="both")

            if datos_cliente != False:

                frame.pack_forget()  # Ocultar el frame de Persona actual en lugar de destruirlo

                 #frame.destroy()
                listaAnimal = ["Nombre perro", "Sexo perro", "Edad perro"]
                listaEditables = [True, True, True]
                dicTipos = {"Nombre perro": str, "Sexo perro": str, "Edad perro": int}

                frame_Animal = FieldFrame(frame_bottom, "Animal", listaAnimal, "sus datos", listaEditables, dicTipos)
                #frame_Animal.place(x =0, y = 0, width=1236, height= 418)
                frame_Animal.pack(expand=True, fill="both")

                frame_Animal.funAceptar(mostrarCliente, "Finalizar")

        
        frame.funAceptar(funcionAnimal, "Continuar")

    def adoptarAnimal():

        # LIMPIAR EL FRAME_BOTTOM POR SI TIENE WIDGETS ADENTRO
        clear_frame_bottom()

        # ASIGNAR EL TIULO Y LA DESCRIPCIÓN DE LA FUNCIONALIDAD EN EL FRAME_TOP
        titulo = "Proceso de adopción"

        descripcion = "Mediante nuestros servicios de adopcion de mascotas puedes acceder de manera eficiente a la información sobre las mascotas disponibles para adopcion\nen cada una de nuestras sedes. Podras visualizar detalles de cada mascota como edad, tipo y condiciones de salud, así como gestionar el proceso de\n adopcion a través del sistema, seleccionando la mascota de tu preferencia y con la que mas hayas conectado."

        formato_frame_top(titulo, descripcion)

        # CREAR Y EMPAQUETAR EL FIELDFRAME PARA LA RECEPCIÓN DE LOS DATOS DEL CLIENTE (frame_datos_cliente)
    
        lista_datos = ["Nombre", "Edad", "N° Cédula", "Celular", "Dirección"] 
        lista_editables = [True, True, True, True, True]  
        valores_por_defecto = ["", "", "", "",""] 
        tipos_esperados = {"Nombre": str, "Edad": int, "N° Cédula": int, "Celular": int, "Dirección": str} 

        frame_datos_cliente = FieldFrame(frame_bottom, "Información Personal", lista_datos, "Datos requeridos", lista_editables, tipos_esperados,valores_por_defecto)

        frame_datos_cliente.pack(expand = True, fill = "both") 

        # EVENTO AL DAR CLICK EN EL BOTÓN CONTINUAR EN (frame_datos_cliente) ------
        def encuesta():

            datos_cliente = frame_datos_cliente.getEntradas() #LISTA CON LOS DATOS PERSONALES DEL CLIENTE

            # SI SE INGRESARON LOS DATOS CORRECTAMENTE
            if datos_cliente != False:

                # VERIFICAR SI EL USUARIO ES MENOR DE EDAD, SI LO ES, NO PODRÁ CONTINUAR EL PROCESO
                if int(datos_cliente[1]) < 18:
                    messagebox.showinfo("Usuario menor de edad", ErrorUsuarioMenor())
                    frame_datos_cliente.funborrar() #LIMPIAR LAS ENTRADAS PARA QUE PUEDA INGRESAR NUEVOS DATOS
                
                # SI ES MAYOR DE EDAD:
                else:
                    # VERIFICAR QUE EL CELULAR Y LA CÉDULA CUMPLA CON LOS REQUERIMIENTOS 
                    if frame_datos_cliente.validar_cel_cc(datos_cliente[3],datos_cliente[2]):

                        frame_datos_cliente.pack_forget() # OCULTAR EL FRAME DE DATOS DEL CLIENTE (NO BORRARLO)

                        #PREGUNTAS ENCUESTA
                        pregunta1 = Adopcion.preguntasEncuesta(1)
                        pregunta2 = Adopcion.preguntasEncuesta(2)
                        pregunta3 = Adopcion.preguntasEncuesta(3)
                        pregunta4 = Adopcion.preguntasEncuesta(4)
                        pregunta5 = Adopcion.preguntasEncuesta(5)
                        pregunta6 = Adopcion.preguntasEncuesta(6)

                        #CREAR Y EMPAQUETAR EL FIELDFRAME PARA LAS RESPUESTAS DEL CLIENTE A LA ENCUESTA (frame_encuesta)

                        lista_preguntas = [pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6] 
                        lista_editables = [True, True, True, True, True, True] 
                        valores_por_defecto = ["", "", "", "", "",""] 
                        tipos_esperados = {pregunta1 : int, pregunta2 : int, pregunta3 : int, pregunta4 : int, pregunta5: int, pregunta6:int}
                                                                                                        
                        rango= [1,2,3,4,5]  #RANGO RESPUESTAS
                        combobox_items = {pregunta1: rango, pregunta2 : rango, pregunta3 : rango, pregunta4 : rango, pregunta5: rango, pregunta6:rango}

                        frame_encuesta = FieldFrame(frame_bottom, "Preguntas" ,lista_preguntas, "Respuesta", lista_editables, tipos_esperados, valores_por_defecto, combobox_items)
     
                        frame_encuesta.pack(expand=True, fill="both") # EMPAQUETAR EL FIELDFRAME DE LA ENCUESTA EN FRAME BOTTOM

                        # INFORMACIÓN SOBRE LA ENCUESTA E INTRUCCIÓN DE COMO LLENARLA
                        messagebox.showinfo("Aviso", "La presente encuesta representa un instrumento necesario para verificar si usted cumple con los requisitos preestablecidos por AdoptaLove para ser admitido en calidad de adoptante.\n\nPor favor, responda a las preguntas en una escala de 1 a 5, siendo 1 la calificación más baja y 5 la más alta.")

                        # EVENTO AL DAR CLICK EN EL BOTÓN CONTINUAR EN (frame_encuesta) ------
                        def eleccion_sede():
                            respuestas_encuesta = frame_encuesta.getEntradas() #LISTA CON LAS RESPUESTAS DEL CLIENTE EN LA ENCUESTA

                            #SI SE RESPONDIERON TODOS LOS CAMPOS (PREGUNTAS) CORRECTAMENTE:
                            if respuestas_encuesta != False:
                                puntos = 0

                                # CALCULAR LOS PUNTOS OBTENIDOS POR EL CLIENTE
                                for i in respuestas_encuesta:
                                    puntos+= int (i)
                                
                                # SI NO CUMPLE CON LOS REQUERIDOS, SE LE MUESTRA UN AVISO INFORMANDO SOBRE ELLO Y QUE EL PROCESO NO PODRÁ CONTINUAR
                                if puntos<=18:
                                    messagebox.showinfo("Incumplimiento de reuisitos","Estimado " + datos_cliente[0] + ", lamentablemente no cumple con los requisitos necesarios para ser adoptante en AdoptaLove, \npor lo que no podemos continuar con el proceso de adopción." )
                                    
                                    # DESTRUIR EL FRAME DE LA ENCUESTA:
                                    frame_encuesta.destroy()

                                    #BORRAR LOS VALORES DE LAS ENTRADAS Y VOLVER A MOSTRAR EL FRAME DE LOS DATOS DEL CLIENTE 
                                    frame_datos_cliente.funborrar() 
                                    frame_datos_cliente.pack(expand=True, fill="both")
                                
                                # SI CUMPLE CON LOS PUNTOS REQUERIDOS
                                else:
                                    #DESTRUIR EL FRAME DE LA ENCUESTA:
                                    frame_encuesta.destroy()

                                    # CREAR EL FIELDFRAME PARA LA ELECCIÓN DE LA SEDE
                                    lista_datos = ["Sede"]
                                    lista_editables = [True]
                                    valores_por_defecto = [""]
                                    tipos_esperados = {"Sede": str}
                                    combobox_items = {"Sede": ["SEDE BELLO", "SEDE ITAGÜI","SEDE MEDELLÍN"]}

                                    frame_sede = FieldFrame(frame_bottom, "Centro de Adopcion", lista_datos, "seleccione una sede", lista_editables, tipos_esperados,valores_por_defecto,combobox_items)

                                    frame_sede.pack(expand= True, fill="both") # EMPAQUETAR EL FIELFRAME DE LA ELECCIÓN SEDE EN FRAME_BOTTOM


                                    # EVENTO AL DAR CLICK EN EL BOTÓN CONTINUAR EN (frame_sede) ------

                                    def eleccion_modovisualizar():
                                        
                                        respuesta = frame_sede.getEntradas()

                                        if respuesta!= False:
                                            respuesta_sede = respuesta[0]
                                            sede_seleccionada = None  # SEDE SELECCIONADA PARA LA ADOPCIÓN
                                            
                                            # BUSCAR CUAL ES LA SEDE QUE SE SELECCIONÓ
                                            for sede in sedes:
                                                if (sede.getNombre() ==  respuesta_sede):
                                                    sede_seleccionada = sede
            
                                                
                                            # SI LA SEDE SELECCIONADA NO TIENE MASCOTAS DISPONIBLES Y SE LE INFORMA DE ELLO     
                                            if (sede_seleccionada.tiene_mascotas()!= True):
                                                messagebox.showinfo("Falta de disponibilidad de mascotas", "Lo sentimos, en estos momentos esta sede no cuenta con mascotas disponibles para adopción.\nPuedes intentar en otras de nuestras sedes")

                                                frame_sede.funborrar() #SE BORRAN LAS ENTRADAS PARA QUE PUEDA INGRESAR NUEVOS DATOS

                                            # SI TIENE MASCOTAS DISPONIBLES
                                            else:
                                                #OCULTAMOS EL FRAME DE ELECCIÓN SE LA SEDE
                                                frame_sede.pack_forget()

                                                # CREAMOS EL FIELDFRAME PARA LA OPCIÓN DE VISUALIZACIÓN
                                                lista_datos = ["Modo visualización"]
                                                lista_editables = [True]
                                                valores_por_defecto = [""]
                                                tipos_esperados = {"Modo visualización": str}
                                                combobox_items = {"Modo visualización": ["Ver todos los animales", "filtrar por tipo"]}

                                                frame_modo_visualizacion = FieldFrame(frame_bottom, "Visualización Animales disponibles",lista_datos, "Seleccione",lista_editables, tipos_esperados, valores_por_defecto, combobox_items )

                                                frame_modo_visualizacion.pack(expand= True, fill="both")

                                                # EVENTO AL DAR CLICK EN EL BOTÓN CONTINUAR EN (frame_modo_visualización) ------

                                                def mostrar_animales_disponibles():
                                                    
                                                    eleccion_visualizacion = frame_modo_visualizacion.getEntradas()
                                                    mascotas_disponibles = [] #LISTA CON LAS MASCOTAS DISPONIBLES DE LA SEDE
                                                    
                                                    # COMPROBAMOS EL MODO DE VISUALIZACIÓN
                                                    if eleccion_visualizacion!=False:
                 
                                                        # SI ELIGIÓ VER TODOS, SE BUSCAN TODOS LOS ANIMALES DISPONIBLES DE SEDE                                        
                                                        if ((str(eleccion_visualizacion[0])) == "Ver todos los animales" ):

                                                            # LISTA CON LOS ANIMALES DISPONIBLES
                                                            mascotas_disponibles = sede_seleccionada.animales_disponibles() 

                                                            # DESTRUIR EL FRAME DE ELECCIÓN VISUALIZACIÓN
                                                            frame_modo_visualizacion.destroy()

                                                            # CONSTRUIR LOS FRAME DONDE SE VISUALIZARÁN LOS DATOS DE LAS MASCOTAS
                                                            frame_muestra_mascotas = tk.Frame(frame_bottom, highlightbackground="purple4", highlightthickness=2, bg = "thistle1")
                                                            frame_muestra_mascotas.pack(side = "top", expand = True,fill = "both")
                                                            frame_muestra_mascotas.pack_propagate(False)

                                                            # Configurar el frame para que las columnas se expandan de manera uniforme
                                                            #frame_mascotas.grid_columnconfigure(0, weight=1)
                                                            #frame_mascotas.grid_columnconfigure(1, weight=1)

                                                            #AGREGAR LOS LABEL DONDE SE MUESTRA CADA MASCOTA:

                                                            for i in range(len(mascotas_disponibles)):
                                                                # LABEL DEL NÚMERO DE LA MASCOTA
                                                                label_criterio = tk.Label(frame_muestra_mascotas, text=("Mascota " + str(i+1)),font= ("Times New Roman",10), bg = "plum1" )

                                                                label_criterio.grid(row = i, column = 0, padx=20, pady=8, sticky="e" )

                                                                # LABEL con __str__() DE LAS MASCOTAS
                                                                label_entrada = tk.Label(frame_muestra_mascotas, text=(mascotas_disponibles[i].__str__()),font= ("Times New Roman",10), bg = "plum1")
                                                                label_entrada.grid(row = i, column = 1, padx=20, pady=8, sticky="w")


                                                            # FIELDFRAME PARA LA ELECCIÓN DE LA MASCOTA 
                                                            lista_datos = ["Numero mascota"]
                                                            lista_editables = [True]
                                                            valores_por_defecto = [""]
                                                            tipos_esperados = {"Numero ascota": int}
                                                            combobox_items = {"Numero mascota": list(range(1,(len(mascotas_disponibles)+1)))}

                                                            frame_elegir_mascota = FieldFrame(frame_bottom, "Mascota", lista_datos, "Seleccione la mascota",lista_editables,tipos_esperados, valores_por_defecto, combobox_items)

                                                            frame_elegir_mascota.pack(side = "bottom", expand= True, fill = "both")


                                                            # EVENTO AL DAR CLICK EN EL BOTÓN CONTINUAR EN (frame_elegir_mascota) ------

                                                            def mostrar_resultados():
                                                                eleccion_mascota = frame_elegir_mascota.getEntradas()

                                                                if eleccion_mascota != False:

                                                                    num_mascota = int(eleccion_mascota[0]) 
               
                                                                    # MASCOTAS SELECCIONADA PARA SER ADOPTADA
                                                                    mascota_adoptada = mascotas_disponibles [(num_mascota)-1]

                                                                    #ADOPTANTE (CLIENTE)
                                                                    adoptador = Cliente(datos_cliente[0], int(datos_cliente[1]), int(datos_cliente[2]),int(datos_cliente[3]), datos_cliente[4])

                                                                    #VERIFICAR SI EL CLIENTE YA HA SIDO CLIENTE ANTERIORMENTE
                                                                    adoptador = sede_seleccionada.is_cliente(adoptador)

                                                                    # CREAR EL OBJETO ADOPCIÓN
                                                                    adopcion = Adopcion(mascota_adoptada,adoptador)
                        

                                                                    # REGISTRAMOS LA ADOPCIÓN ADOPCIÓN EN SU SEDE CORRESPONDIENTE
                                                                    sede_seleccionada.registrar_adopcion(adopcion)

                                                                    #ASIGNARLE 5 PUNTOS AL CLIENTE POR LA ADOPCIÓN
                                                                    adopcion.getCliente().agregar_puntos(5)

                                                                    messagebox.showinfo("Puntos canjeables", "Sr./Sra " + adoptador.getNombre() +  " usted ha ganado 5 puntos que serán agregados a su saldo de puntos. Estos puntos son canjeables para obtener descuentos en nuestros servicios y productos de nuestras tiendas.\nEn este momento tiene un total de " + str(adoptador.getPuntos()) + " puntos.")

                                                                    # MOTRAR LOS RESULTADOS POR PANTALLA 
                                                                    frame_elegir_mascota.destroy()
                                                                    frame_muestra_mascotas.destroy()

                                                                    frame_resultado_adopcion = Frame(frame_bottom, bg="thistle1", highlightbackground="purple4", highlightthickness=2 )                                                                                
                                                                    frame_resultado_adopcion.pack(expand=True, fill="both")
                                                                    # Label de factura1
                                                                    factura = tk.Label(frame_resultado_adopcion, text="----- DETALLES ADOPCIÓN -----", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                                    factura.pack(side="top", pady=30)
                                                                    # Label de factura2
                                                                    factura = tk.Label(frame_resultado_adopcion, text=adopcion.__str__(), font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                                    factura.pack(side="top")
                                                                    # Label de factura3
                                                                    factura = tk.Label(frame_resultado_adopcion, text=f"Gracias {adopcion.getCliente().getNombre()} por darle un hogar a {adopcion.getAnimal().getNombre()}", font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                                    factura.pack(side="top")
                                                                    # Label de factura4
                                                                    factura = tk.Label(frame_resultado_adopcion, text="-------------------------------", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                                    factura.pack(side="top")

                                                                    # botón final
                                                                    inicio = tk.Button(frame_resultado_adopcion, text="Salir", font=("Verdana", 10), bg="white", command=adoptarAnimal)
                                                                    inicio.pack(side="top")
       
                                                            frame_elegir_mascota.funAceptar(mostrar_resultados, "Adoptar")
                                                                

                                                        #SI ELIGIÓ FILTRAR POR TIPO
                                                        else:
                                                            frame_modo_visualizacion.destroy()

                                                            #CREAR EL FRAME PARA QUE SELECCIONE LA ESPECIE
                                                            lista_datos = ["Tipo"]
                                                            lista_editables = [True]
                                                            valores_por_defecto = [""]
                                                            tipos_esperados = {"Tipo": str}
                                                            combobox_items = {"Tipo": ["Perro", "Gato", "Canario", "Conejo", "Hámster"]}

                                                            frame_eleccion_tipo = FieldFrame (frame_bottom,"Especie mascota", lista_datos, "Seleccione el tipo",lista_editables, tipos_esperados, valores_por_defecto, combobox_items)

                                                            frame_eleccion_tipo.pack(expand=True, fill = "both")

                                                            # EVENTO AL DAR CLICK EN EL BOTÓN CONTINUAR EN (frame_modo_visualización) -----

                                                            def lista_filtro_tipo():
                                                                
                                                                tipo = frame_eleccion_tipo.getEntradas()

                                                                #SI SE SELECCIONÓ EL TIPO DE LA MASCOTA CORRECTAMENTE
                                                                if tipo != False:
                                                                    
                                                                    especie = tipo [0]
                                                                    
                                                                    #LISTA DE ANIMALES QUE COINCIDEN CON EL TIPO SOLICITADO
                                                                    mascotas_disponibles = sede_seleccionada.animales_disponibles(especie)

                                                                    # SI LA SEDE NO TIENE ANIMALES DE ESE TIPO, SE LE INFORMA DE ELLO Y LO DEVUELVE A ESCOGER SEDE                                 
                                                                    if (len(mascotas_disponibles) == 0):
                                                                        messagebox.showinfo("Falta de disponibilidad de mascotas", "Lo sentimos, en este momento en la sede no se encuentran mascotas de ese tipo disponibles para adopción.\nPuedes intentar en otra de nuestras sedes")

                                                                        frame_eleccion_tipo.destroy()
                                                                        frame_sede.funborrar()
                                                                        frame_sede.pack(expand=True,fill = "both") #PARA QUE VUELVA ESCOGER LA SEDE 

                                                                    # SI TIENE ANIMALES QUE COINCIDEN, ENTONCES EL USUARIO PODRÁ ESCOG
                                                                    else:
                                                                        frame_eleccion_tipo.destroy()
                                                                        
                                                                        frame_muestra_mascotas = tk.Frame(frame_bottom, highlightbackground="purple4", highlightthickness=2, bg = "thistle1")
                                                                        frame_muestra_mascotas.pack(side = "top", expand = True,fill = "both")
                                                                        frame_muestra_mascotas.pack_propagate(False)

                                                                        #AGREGAR LOS LABEL DONDE SE MUESTRA CADA MASCOTA:

                                                                        for i in range(len(mascotas_disponibles)):

                                                                            # LABEL DEL NÚMERO DE LA MASCOTA
                                                                            label_criterio = tk.Label(frame_muestra_mascotas, text=("Mascota " + str(i+1)),font= ("Times New Roman",10), bg = "plum1" )

                                                                            label_criterio.grid(row = i, column = 0, padx=20, pady=8, sticky="e" )

                                                                            # LABEL __str__ MASCOTAS
                                                                            label_entrada = tk.Label(frame_muestra_mascotas, text=(mascotas_disponibles[i].__str__()),font= ("Times New Roman",10), bg = "plum1")
                                                                            label_entrada.grid(row = i, column = 1, padx=20, pady=8, sticky="w")


                                                                        #FIELDFRAME PARA LA ELECCIÓN DE LA MASCOTA 
                                                                        lista_datos = ["Numero mascota"]
                                                                        lista_editables = [True]
                                                                        valores_por_defecto = [""]
                                                                        tipos_esperados = {"Numero ascota": int}
                                                                        combobox_items = {"Numero mascota": list(range(1,(len(mascotas_disponibles)+1)))}

                                                                        frame_seleccionar_mascota = FieldFrame(frame_bottom, "Mascota", lista_datos, "Seleccione la mascota",lista_editables,tipos_esperados, valores_por_defecto, combobox_items)

                                                                        frame_seleccionar_mascota.pack(side = "bottom", expand= True, fill = "both")

                                                                        # EVENTO AL DAR CLICK EN EL BOTÓN CONTINUAR EN (frame_elegir_mascota) ----

                                                                        def mostrar_resultados():
                                                                            eleccion_mascota = frame_seleccionar_mascota.getEntradas()

                                                                            if eleccion_mascota != False:
                                                                                num_mascota = int(eleccion_mascota[0]) 

                                                                                # MASCOTA Y CLIENTE PARA REGISTRAR LA ADOPCIÓN
                                                                                mascota_adoptada = mascotas_disponibles [(num_mascota)-1]

                                                                                adoptador = Cliente(datos_cliente[0], int(datos_cliente[1]), int(datos_cliente[2]),int(datos_cliente[3]), datos_cliente[4])

                                                                                # CREAR EL OBJETO ADOPCIÓN
                                                                                adopcion = Adopcion(mascota_adoptada,adoptador)
                                
                                                                                 # REGISTRAMOS LA ADOPCIÓN ADOPCIÓN EN SU SEDE CORRESPONDIENTE
                                                                                sede_seleccionada.registrar_adopcion(adopcion)

                                                                                #ASIGNARLE 5 PUNTOS AL CLIENTE POR LA ADOPCIÓN
                                                                                adopcion.getCliente().agregar_puntos(5)

                                                                                messagebox.showinfo("Puntos canjeables", "Sr./Sra " + adoptador.getNombre() +  " usted ha ganado 5 puntos que serán agregados a su saldo de puntos. Estos puntos son canjeables para obtener descuentos en nuestros servicios y productos de nuestras tiendas.\nEn este momento tiene un total de " + str(adoptador.getPuntos()) + " puntos.")

                                                                                #MOSTRAR RESULTADOS
                                                                                frame_seleccionar_mascota.destroy()
                                                                                frame_muestra_mascotas. destroy()

                                                                                frame_resultado_adopcion = Frame(frame_bottom, bg="thistle1", highlightbackground="purple4", highlightthickness=2 )                                                                                
                                                                                frame_resultado_adopcion.pack(expand=True, fill="both")
                                                                                # Label de factura1
                                                                                factura = tk.Label(frame_resultado_adopcion, text="----- DETALLES ADOPCIÓN -----", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                                                factura.pack(side="top", pady=30)
                                                                                # Label de factura2
                                                                                factura = tk.Label(frame_resultado_adopcion, text=adopcion.__str__(), font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                                                factura.pack(side="top")
                                                                                # Label de factura3
                                                                                factura = tk.Label(frame_resultado_adopcion, text=f"Gracias {adopcion.getCliente().getNombre()} por darle un hogar a {adopcion.getAnimal().getNombre()}", font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                                                factura.pack(side="top")
                                                                                # Label de factura4
                                                                                factura = tk.Label(frame_resultado_adopcion, text="-------------------------------", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                                                factura.pack(side="top")

                                                                                # botón final
                                                                                inicio = tk.Button(frame_resultado_adopcion, text="Salir", font=("Verdana", 10), bg="white", command=adoptarAnimal)
                                                                                inicio.pack(side="top")





                                                                        frame_seleccionar_mascota.funAceptar(mostrar_resultados, "continuar")

                                                            frame_eleccion_tipo.funAceptar(lista_filtro_tipo, "Continuar")
                                                      
                                                frame_modo_visualizacion.funAceptar(mostrar_animales_disponibles, "continuar")
  
                                    frame_sede.funAceptar(eleccion_modovisualizar, "continuar")

                        frame_encuesta.funAceptar(eleccion_sede, "Continuar")
             
        frame_datos_cliente.funAceptar(encuesta, "Continuar")
                



    def agendar_servicio():
        def funVacia():
            pass

        # LIMPIAMOS EL FRAME BOTTOM Y AÑADIMOS LA DESCRIPCIÓN
        clear_frame_bottom()
        formato_frame_top("Agendar Servicio", "En las diferentes sedes de AdoptaLove ofrecemos distintos servicios.\nPor favor selecciona una sede para comenzar a agendar un servicio de los ofertados para tu máscota")

    
        #FIELDFRAME PARA ESCOGER SEDE
        lista_campo = ["Servicio:"]
        lista_habilitado = [True] 
        tipo_esperados = {"Servicio:": str}
        valor_por_defecto = [""]
        dicRespuestas = {"Servicio:": ["BELLO: Guardería", "ITAGÜI: Veterinaria", "MEDELLÍN: Peluqueria"]}

        frame_eleccion_sede = FieldFrame(frame_bottom, "Seleccione una sede", lista_campo, "Sede con servicio ofertado", lista_habilitado, tipo_esperados, valor_por_defecto, dicRespuestas)
        frame_eleccion_sede.pack(expand=True, fill="both")
    
        # FUNCIÓN PARA EL BOTÓN ACEPTAR DEL (frame_eleccion_sede)
        def escogerSede():
            
            sede_escogida = frame_eleccion_sede.getEntradas()

            if sede_escogida != False:

                frame_eleccion_sede.lista_entradas[0].config(state="disabled")
                frame_eleccion_sede.boton_limpiar.config(command=funVacia)
                frame_eleccion_sede.boton_aceptar.config(command=funVacia)

                lista_animales=[]

                if sede_escogida[0] == "ITAGÜI: Veterinaria":
                    lista_animales = ["Perro", "Gato", "Conejo", "Hámster", "Otro"]
                else:
                    lista_animales = ["Perro", "Gato", "Otro"]
                    
                # Combobox de comprobar que el animal sea correcto ---------
                lista_campo = ["Animal:"]
                listahabilitado = [True] 
                dictipo = {"Animal:": str}
                valor = [""]
                dicRespuestas = {"Animal:": lista_animales}

                frame_tipo_mascota = FieldFrame(frame_bottom, "Especie", lista_campo, "Tipo de su animal", listahabilitado, dictipo, valor, dicRespuestas)
                frame_tipo_mascota.pack(expand=True, fill="both") 
                
                # FUNCION DEL BOTON frame_tipo_mascota
                def empleados_disponibles():
                    tipo_animal = frame_tipo_mascota.getEntradas()
                        
                    if tipo_animal != False:

                        # SI EL SERVICIO NO ESTÁ DISPONIBLE PARA SU MASCOTA, SE LE INFORMA SOBRE ELLO:
                        if tipo_animal[0] == "Otro":
                            messagebox.showinfo("Servicio no disponible", "Por el momento, el servicio solo se encuentra disponible para los animales mostrados en las opciones")         
                            agendar_servicio()

                        # SI EL SERVICIO SI ESTÁ DISPONIBLE
                        else:

                            sede_seleccionada = None
                            profesion = ""

                            # SE VERIFICA CUAL ES LA SEDE SELECCIONADAA
                            if (sede_escogida[0] =="BELLO: Guardería"):
                                sede_seleccionada = sedes[0]
                                profesion = "Cuidador"

                            elif (sede_escogida[0] =="ITAGÜI: Veterinaria"):
                                sede_seleccionada = sedes[1]
                                profesion = "Veterinario"
                            
                            else:
                                sede_seleccionada = sedes[2]
                                profesion = "Peluquero"

                            # SE OBTENIENEN LOS EMPLEADOS DISPONIBLES PARA ATENDER CITAS
                            lista_empleados = sede_seleccionada.tiene_empleados()
                            for i in lista_empleados:
                                print(i)   

                            # SI NO HAY EMPLEADOS CON DISPONIBILIDAD, SE INFORMA SOBRE ELLO
                            if (len(lista_empleados) ==0 ):
                                messagebox.showinfo("Indisponibilidad de citas", "Actualmente, debido a la falta de disponibilidad de citas, no es posible continuar con el proceso de agendamiento")
                                agendar_servicio()

                            else:
                                # SI HAY EMPLEADOS DISPONIBLES, SE LE MUESTRAN PARA QUE SELECCIONE UNO:
                                frame_tipo_mascota.destroy()
                                frame_eleccion_sede.destroy()
                                
                                frame_muestra_empleados = tk.Frame(frame_bottom, highlightbackground="purple4", highlightthickness=2, bg = "thistle1")
                                frame_muestra_empleados.pack(side = "top", expand = True,fill = "both")
                                frame_muestra_empleados.pack_propagate(False)

                                #AGREGAR LOS LABEL DONDE SE MUESTRA CADA MASCOTA:

                                for i in range(len(lista_empleados)):
                                    # LABEL DEL NÚMERO DE LA MASCOTA
                                    label_criterio = tk.Label(frame_muestra_empleados, text=(profesion + " " + str(i+1)),font= ("Times New Roman",10), bg = "plum1" )

                                    label_criterio.grid(row = i, column = 0, padx=20, pady=8, sticky="e" )

                                     # LABEL __str__mascotas
                                    label_entrada = tk.Label(frame_muestra_empleados, text=(lista_empleados[i].__str__()),font= ("Times New Roman",10), bg = "plum1")
                                    label_entrada.grid(row = i, column = 1, padx=20, pady=8, sticky="w")


                                lista_datos = ["Numero " + profesion]
                                lista_editables = [True]
                                valores_por_defecto = [""]
                                tipos_esperados = {"Numero " + profesion: int}
                                combobox_items = {"Numero " + profesion: list(range(1,(len(lista_empleados)+1)))}

                                frame_seleccionar_empleado = FieldFrame(frame_bottom, profesion, lista_datos, "Seleccione el " + profesion, lista_editables,tipos_esperados, valores_por_defecto, combobox_items)

                                frame_seleccionar_empleado.pack(side = "bottom", expand= True, fill = "both")

                                def eleccionDia():
                                    eleccion_empleado = frame_seleccionar_empleado.getEntradas()
                                    if eleccion_empleado != False:
                                        frame_seleccionar_empleado.destroy()
                                        frame_muestra_empleados.destroy()
                                    
                                        empleado_seleccionado = lista_empleados[int(eleccion_empleado[0]) - 1]


                                        lista_dias = ["Día"]
                                        lista_editables = [True]
                                        valores_por_defecto = [""]
                                        tipos_esperados = {"Día": str}
                                        combobox_items = {"Día": ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sábado"]}

                                        frame_seleccionar_dia = FieldFrame(frame_bottom, "Dia para la cita", lista_dias, "Seleccione el día", lista_editables,tipos_esperados, valores_por_defecto, combobox_items)
                                        frame_seleccionar_dia.pack(expand=True, fill="both") 

                                        def cupos_dia():
                                            dic = {"Lunes": 0, "Martes":1, "Miercoles":2, "Jueves":3, "Viernes": 4, "Sábado":5}   

                                            eleccion_dia = frame_seleccionar_dia.getEntradas()

                                            if eleccion_dia != False:
                                                frame_seleccionar_dia.lista_entradas[0].config(state="disabled")
                                                frame_seleccionar_dia.boton_aceptar.config(command=funVacia)
                                                frame_seleccionar_dia.boton_limpiar.config(command=funVacia)

                                                num_dia = dic[eleccion_dia[0]]

                                                #CUPOS DISPONIBLES DEL EMPLEADO EN EL DIA SELECCIONADO
                                                cupos_disponibles = empleado_seleccionado.cupos_disponibles(num_dia)   

                                                for i in cupos_disponibles:
                                                    print(i) 

                                                if len(cupos_disponibles)==0:
                                                     messagebox.showinfo("Indisponibilidad de cupos", "El proceso de agendamiento de cita no podrá continuar porque el empleado seleccionado no cuenta con cupos disponibles para atender en el dia solicitado")
                                                     agendar_servicio()
                                                else:

                                                    lista_cupos = ["Hora"]
                                                    lista_editables = [True]
                                                    valores_por_defecto = [""]
                                                    tipos_esperados = {"Hora": str}
                                                    combobox_items = {"Hora": cupos_disponibles}

                                                    frame_seleccionar_cupo = FieldFrame(frame_bottom, "Horario", lista_cupos, "Seleccione cupo", lista_editables,tipos_esperados, valores_por_defecto, combobox_items)
                                                    frame_seleccionar_cupo.pack(expand=True, fill="both") 


                                                    def datos_cliente ():
                                                        eleccion_cupo = frame_seleccionar_cupo.getEntradas()
                                                        
                                                        if eleccion_cupo!=False:
                                                            frame_seleccionar_cupo.destroy()
                                                            frame_seleccionar_dia.destroy()

                                                            cupo_seleccionado= None

                                                            for i in cupos_disponibles:
                                                                if (i.__str__())== eleccion_cupo[0]:
                                                                    cupo_seleccionado = i

                                                            # Creación FieldFrame
                                                            listaCampos= ["Nombre", "Cédula", "Edad"]
                                                            listahabilitados = [True, True, True]
                                                            valorEsperado = {"Nombre": str, "Cédula": int, "Edad": int} 

                                                            frame_datos_usuario = FieldFrame(frame_bottom, "Información personal", listaCampos, "Sus datos", listahabilitados, valorEsperado)
                                                            frame_datos_usuario.pack(expand=True, fill="both")

                                                            def datos_animal():
                                                                entrada_cliente = frame_datos_usuario.getEntradas()
                                                                
                                                                if entrada_cliente!=False:

                                                                    if int(entrada_cliente[2]) < 18:
                                                                        messagebox.showinfo("Usuario menor de edad", ErrorUsuarioMenor())
                                                                        agendar_servicio()

                                                                    else:

                                                                        if frame_datos_usuario.validar_CC(entrada_cliente[1]):

                                       
                                                                            frame_datos_usuario.destroy()

                                                                             # Creación FieldFrame Mascota
                                                                            if sede_escogida[0] == "ITAGÜI: Veterinaria":
                                                                                lista_animales = ["Perro", "Gato", "Conejo", "Hámster"]
                                                                            else:
                                                                                 lista_animales = ["Perro", "Gato"]


                                                                            listaCampos= ["Nombre", "Edad", "Especie", "Sexo"]
                                                                            listahabilitados = [True, True, True, True]
                                                                            valorEsperado = {"Nombre": str, "Edad": int, "Especie": str, "Sexo": str} 
                                                                            combobox_items = {"Especie": lista_animales, "Sexo": ["Macho", "Hembra"]}
                                                                            listaValores = ["", "", "", ""]

                                                                            frame_datos_animal = FieldFrame(frame_bottom, "Información de la mascota", listaCampos, "Datos", listahabilitados, valorEsperado,listaValores, combobox_items)
                                                                        
                                                                            frame_datos_animal.pack(expand=True, fill="both")

                                                                            def registroDeCita():
                                                                                entrada_animal = frame_datos_animal.getEntradas()

                                                                                if entrada_animal!=False:
                                                                                    animal = Animal(entrada_animal[0],entrada_animal[2],entrada_animal[1],entrada_animal[3])
                                                                                    print(animal)
                                                                                    print(sede_seleccionada)

                                                                                    num_sede = None

                                                                                    if sede_seleccionada.getNombre() == "SEDE BELLO":
                                                                                        num_sede = 1
                                                                                    elif sede_seleccionada.getNombre() == "SEDE ITAGÜI":
                                                                                        num_sede = 2

                                                                                    else:
                                                                                        num_sede = 3


                                                                                    cliente = Cliente(entrada_cliente[0], int(entrada_cliente[2]), int(entrada_cliente[1]))
                                                                                    cliente = sede_seleccionada.is_cliente(cliente)

                                                                                    cita = Cita(cliente,animal, empleado_seleccionado, cupo_seleccionado, num_sede)

                                                                                    print(cita)

                                                                                    if (cliente.getPuntos()>=15):

                                                                                        cliente.disminuir_puntos(15)
                                                                                        cita.aplicarDescuento()
                                                                                        frame_datos_animal.destroy()

                                                                                        frame_factura = Frame(frame_bottom, bg="thistle1", highlightbackground="purple4", highlightthickness=2 )
                                                                                        frame_factura.pack(expand=True, fill="both")
                                                                                        # Label de factura1
                                                                                        factura = tk.Label(frame_factura, text="----- Factura Electrónica -----", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                                                        factura.pack(side="top", pady=30    )
                                                                                        # Label de factura2
                                                                                        factura = tk.Label(frame_factura, text=cita.__str__(), font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                                                        factura.pack(side="top")
                                                                                        # Label de factura3
                                                                                        factura = tk.Label(frame_factura, text=f"Gracias {cliente.getNombre()} por agendar una cita con nosotros, esperamos verte pronto.", font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                                                        factura.pack(side="top")
                                                                                        # Label de factura4
                                                                                        factura = tk.Label(frame_factura, text="-------------------------------", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                                                        factura.pack(side="top")

                                                                                        # botón final
                                                                                        inicio = tk.Button(frame_factura, text="Salir", font=("Verdana", 10), bg="white", command=agendar_servicio)
                                                                                        inicio.pack(side="top")

                                                                                    else:

                                                                                        frame_datos_animal.destroy()

                                                                                        frame_factura = Frame(frame_bottom, bg="thistle1", highlightbackground="purple4", highlightthickness=2 )
                                                                                        frame_factura.pack(expand=True, fill="both")
                                                                                        # Label de factura1
                                                                                        factura = tk.Label(frame_factura, text="----- Factura Electrónica -----", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                                                        factura.pack(side="top", pady=30)
                                                                                        # Label de factura2
                                                                                        factura = tk.Label(frame_factura, text=cita.__str__(), font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                                                        factura.pack(side="top")
                                                                                        # Label de factura3
                                                                                        factura = tk.Label(frame_factura, text=f"Gracias {cliente.getNombre()} por agendar una cita con nosotros, esperamos verte pronto.", font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                                                        factura.pack(side="top")
                                                                                        # Label de factura4
                                                                                        factura = tk.Label(frame_factura, text="-------------------------------", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                                                        factura.pack(side="top")

                                                                                        # botón final
                                                                                        inicio = tk.Button(frame_factura, text="Salir", font=("Verdana", 10), bg="white", command=agendar_servicio)
                                                                                        inicio.pack(side="top")

                                                                                    print(cita)
                                                                                        

                                                                            frame_datos_animal.funAceptar(registroDeCita, "Continuar")
                                                            frame_datos_usuario.funAceptar(datos_animal, "Continuar")
                                                    frame_seleccionar_cupo.funAceptar(datos_cliente, "Continuar")
                                        frame_seleccionar_dia.funAceptar(cupos_dia, "Continuar")                                
                                frame_seleccionar_empleado.funAceptar(eleccionDia,"Continuar")
                frame_tipo_mascota.funAceptar(empleados_disponibles, "Continuar")                      
        frame_eleccion_sede.funAceptar(escogerSede, "Continuar")




    def tienda():
        # Función vacia (Sirve para deshabilitar Botones)
        def funVacia():
            pass

        # Limpiamos el frame botom y añadimos un título
        clear_frame_bottom()
        formato_frame_top("Tienda para mascotas", "En AdoptaLove ofrecemos todo lo que su mascota necesita para garantizar su bienestar y felicidad.\n Contamos con una amplia selección de productos de la más alta calidad, asegurando los mejores precios para su conveniencia.")
        
        # Inicio de la tienda --------------------------------------------
        listacampo = ["Elección"]
        listahabilitado = [True]
        DicTipos = {"Elección": str}
        valor = [""]
        diccionario ={"Elección":["Filtrar por tipo", "Mostrar todo"]}
        # Pregunta de si desea filtrar
        inicioTienda = FieldFrame(frame_bottom, "¿Cómo desea ver los productos?", listacampo, "Su elección", listahabilitado, DicTipos, valor, diccionario)
        inicioTienda.pack(expand=True, fill="both")

        # Funcion para el botón continuar de inicioTienda
        def proceso_2_Tienda():
            filtro = inicioTienda.getEntradas()
            if filtro != False: 
                if filtro[0] == "Mostrar todo": # Caso de que quiere ver todos los productos
                    inicioTienda.pack_forget()

                    productos = tienda1.getProductos() # lista con los productos de la tienda
                    comunas = 0 # Columnas para los label
                    filas = 0 # Filas para los label
                    lista_comobox = [] # lista para el combobox de escoger Animal
                    frame_produtos = tk.Frame(frame_bottom, bg="thistle1", highlightbackground="purple4", highlightthickness=2) # Frame para acomodar todo ---------------------------------
                    frame_produtos.pack(expand=True, fill="both")

                    for i in productos: # recorremos la lista de productos para imprimirlos
                        lista_comobox.append(f"{str(productos.index(i)+1)} {i.getNombre()}")
                        tk.Label(frame_produtos, text=i.__str__(), font = ("Times New Roman", 8), fg= "purple", bg = "thistle1").grid(row=filas, column=comunas, padx=8, pady=10, sticky="nsew")
                        filas+=1
                        if filas == 4:
                            comunas+=1
                            filas = 0

                    # Entradas para comprar producto
                    tk.Label(frame_produtos, text="Seleccione el producto:",  font=("Times New Roman", 14, "bold", "underline"), fg="purple4", bg="thistle1").grid(row=0, column=7, padx=15)
                    selec_producto = ttk.Combobox(frame_produtos, values=lista_comobox, state="readonly")
                    selec_producto.grid(row=0, column=8, padx=15, sticky="ew")

                    tk.Label(frame_produtos, text="Unidades del producto",  font=("Times New Roman", 14, "bold", "underline"), fg="purple4", bg="thistle1").grid(row=1, column=7, padx=15)
                    cantidad_producto = tk.Entry(frame_produtos)
                    cantidad_producto.grid(row=1, column=8, padx=15)

                    # Funcion limpiar
                    def funborrar(): 
                        selec_producto.set('')  # RESTABLECER EL COMBOBOX
                        cantidad_producto.delete("0", "end")  # BORRAR ENTRADAS NORMALES

                    # Boton limpiar
                    limpiar = tk.Button(frame_produtos, text="Limpiar", font=("Verdana", 10), bg="white", command=funborrar)
                    limpiar.grid(row=2, column=7, padx=15)

                    # Función botón de continuar
                    def funcontinuar():
                        if selec_producto.get()!='' and cantidad_producto.get()!="":
                            puede = True
                            try:
                                int(cantidad_producto.get())
                            except ValueError:
                                puede = False
                                messagebox.showerror("Error de tipo","El valor ingresado no es un número")
                            if puede==True:
                                cantidad = int(cantidad_producto.get())
                                partir = selec_producto.get().split()
                                indice = int(partir[0])-1
                                comparador = tienda1.listaProductos[indice].getCantidadUnidades()

                                if (cantidad<=comparador and cantidad>=0):
                                    producto = tienda1.listaProductos[indice]
                                    continuar.config(command=funVacia)
                                    messagebox.showinfo("Proceso de compra",f"Se va a procesar la compra de {cantidad} unidades de {producto.getNombre()} para {producto.getTipoAnimal()}. \n\nSus datos serán registrados para realizar la compra.")
                                    frame_produtos.destroy()
                                    
                                    # FieldFrame para registrar el usuario ---------------------------------
                                    # Función botón de aceptar del Nuevo FieldFrame
                                    def registroCompra():
                                        datos_cliente = registrarUsuario.getEntradas()
                                        if datos_cliente != False:
                                            if registrarUsuario.validar_CC(datos_cliente[1]):
                                                if int(datos_cliente[2])<=140 and int(datos_cliente[2])>6:
                                                    cliente = Cliente(datos_cliente[0], int(datos_cliente[2]), int(datos_cliente[1])) # Cliente para llamar a compra
                                                    registrarUsuario.destroy()
                                                    # Creamos un frame para mostrar factura
                                                    frame_factura = Frame(frame_bottom, bg="thistle1", highlightbackground="purple4", highlightthickness=2)
                                                    frame_factura.pack(expand=True, fill="both")
            
                                                    # Label de factura1
                                                    factura = tk.Label(frame_factura, text="----- Factura Electrónica -----", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                    factura.pack(side="top", pady=30)
                                                    # Label de factura2
                                                    factura = tk.Label(frame_factura, text=tienda1.compra(indice+1, cliente, sede1,cantidad), font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                    factura.pack(side="top")
                                                    # Label de factura3
                                                    factura = tk.Label(frame_factura, text=f"Gracias {cliente.getNombre()} por visitar nuestra tienda, esperamos verte pronto.", font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                    factura.pack(side="top")
                                                    # Label de factura4
                                                    factura = tk.Label(frame_factura, text="-------------------------------", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                    factura.pack(side="top")

                                                    # botón final
                                                    inicio = tk.Button(frame_factura, text="Salir", font=("Verdana", 10), bg="white", command=tienda)
                                                    inicio.pack(side="top")

                                                else: 
                                                    messagebox.showerror("Error de edad","La edad ingresada es invalida")

                                    # Creación FieldFrame
                                    listaCampos= ["Nombre", "Cédula", "Edad"]
                                    listahabilitados = [True, True, True]
                                    valorEsperado = {"Nombre": str, "Cédula": int, "Edad": int} 

                                    registrarUsuario = FieldFrame(frame_bottom, "Registro de la compra:", listaCampos, "Sus datos personales:", listahabilitados, valorEsperado)
                                    registrarUsuario.pack(expand=True, fill="both")

                                    # Botón de Comprar
                                    registrarUsuario.funAceptar(registroCompra, "Finalizar")


                                else:
                                    messagebox.showerror("Error Fuera de rango",ErrorFueraRango())
                        else:
                            messagebox.showerror("Error en campos","Faltan campos por rellenar")

                    # Boton continuar
                    continuar = tk.Button(frame_produtos,text="Comprar", font=("Verdana", 10), bg="white", command=funcontinuar)
                    continuar.grid(row=2 , column=8, padx=15)
                else:
                    # deshabilitamos para 
                    inicioTienda.boton_aceptar.config(command=funVacia)
                    inicioTienda.boton_limpiar.config(command=funVacia)
                    combo = inicioTienda.lista_entradas[0]
                    combo.config(state="disabled") # Deshabilitamos la entrada para que ya no pueda hacer nada

                    # Función para controlar el filtro
                    def controlFiltrar():
                        filtro_escogido = combo_filtrar.getEntradas()
                        if filtro_escogido != False:
                            filtro = filtro_escogido[0]
                            inicioTienda.pack_forget()
                            combo_filtrar.destroy()

                            productos = tienda1.getProductos() # lista con los productos de la tienda
                            comunas = 0 # Columnas para los label
                            filas = 0 # Filas para los label
                            lista_comobox = [] # lista para el combobox de escoger Animal
                            frame_produtos = tk.Frame(frame_bottom, bg="thistle1", highlightbackground="purple4", highlightthickness=2) # Frame para acomodar todo ---------------------------------
                            frame_produtos.pack(expand=True, fill="both")

                            for i in productos: # recorremos la lista de productos para imprimirlos
                                if i.getTipoAnimal()==filtro or i.getTipoAnimal()=="Uso general":
                                    lista_comobox.append(f"{str(productos.index(i)+1)} {i.getNombre()}")
                                    tk.Label(frame_produtos, text=i.__str__(), font = ("Times New Roman", 8), fg= "purple", bg = "thistle1").grid(row=filas, column=comunas, padx=8, pady=10, sticky="nsew")
                                    filas+=1
                                    if filas == 4:
                                        comunas+=1
                                        filas = 0
                                        
                            # Entradas para comprar producto
                            tk.Label(frame_produtos, text="Seleccione el producto:",  font=("Times New Roman", 14, "bold", "underline"), fg="purple4", bg="thistle1").grid(row=0, column=7, padx=15)
                            selec_producto = ttk.Combobox(frame_produtos, values=lista_comobox, state="readonly")
                            selec_producto.grid(row=0, column=8, padx=15, sticky="ew")

                            tk.Label(frame_produtos, text="Unidades del producto",  font=("Times New Roman", 14, "bold", "underline"), fg="purple4", bg="thistle1").grid(row=1, column=7, padx=15)
                            cantidad_producto = tk.Entry(frame_produtos)
                            cantidad_producto.grid(row=1, column=8, padx=15)

                            # Funcion limpiar
                            def funborrar(): 
                                selec_producto.set('')  # RESTABLECER EL COMBOBOX
                                cantidad_producto.delete("0", "end")  # BORRAR ENTRADAS NORMALES

                            # Boton limpiar
                            limpiar = tk.Button(frame_produtos, text="Limpiar", font=("Verdana", 10), bg="white", command=funborrar)
                            limpiar.grid(row=2, column=7, padx=15)

                            # Función botón de continuar
                            def funcontinuar():
                                if selec_producto.get()!='' and cantidad_producto.get()!="":
                                    puede = True
                                    try:
                                        int(cantidad_producto.get())
                                    except ValueError:
                                        puede = False
                                        messagebox.showerror("Error de tipo","El valor ingresado no es un número")
                                    if puede==True:
                                        cantidad = int(cantidad_producto.get())
                                        partir = selec_producto.get().split()
                                        indice = int(partir[0])-1
                                        comparador = tienda1.listaProductos[indice].getCantidadUnidades()

                                        if (cantidad<=comparador and cantidad>=0):
                                            producto = tienda1.listaProductos[indice]
                                            continuar.config(command=funVacia)
                                            messagebox.showinfo("Proceso de compra",f"Se va a procesar la compra de {cantidad} unidades de {producto.getNombre()} para {producto.getTipoAnimal()}. \n\nSus datos serán registrados para realizar la compra.")
                                            frame_produtos.destroy()
                                            
                                            # FieldFrame para registrar el usuario ---------------------------------
                                            # Función botón de aceptar del Nuevo FieldFrame
                                            def registroCompra():
                                                datos_cliente = registrarUsuario.getEntradas()
                                                if datos_cliente != False:
                                                    if registrarUsuario.validar_CC(datos_cliente[1]):
                                                        if int(datos_cliente[2])<=140 and int(datos_cliente[2])>6:
                                                            cliente = Cliente(datos_cliente[0], int(datos_cliente[2]), int(datos_cliente[1])) # Cliente para llamar a compra
                                                            registrarUsuario.destroy()
                                                            # Creamos un frame para mostrar factura
                                                            frame_factura = Frame(frame_bottom, bg="thistle1", highlightbackground="purple4", highlightthickness=2)
                                                            frame_factura.pack(expand=True, fill="both")
                    
                                                            # Label de factura1
                                                            factura = tk.Label(frame_factura, text="----- Factura Electrónica -----", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                            factura.pack(side="top", pady=30)
                                                            # Label de factura2
                                                            factura = tk.Label(frame_factura, text=tienda1.compra(indice+1, cliente, sede1,cantidad), font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                            factura.pack(side="top")
                                                            # Label de factura3
                                                            factura = tk.Label(frame_factura, text=f"Gracias {cliente.getNombre()} por visitar nuestra tienda, esperamos verte pronto.", font=("Times New Roman", 14, "bold"), fg="purple4", bg="thistle1")
                                                            factura.pack(side="top")
                                                            # Label de factura4
                                                            factura = tk.Label(frame_factura, text="-------------------------------", font=("Times New Roman", 20, "bold"), fg="purple4", bg="thistle1")
                                                            factura.pack(side="top")

                                                            # botón final
                                                            inicio = tk.Button(frame_factura, text="Salir", font=("Verdana", 10), bg="white", command=tienda)
                                                            inicio.pack(side="top")

                                                        else: 
                                                            messagebox.showerror("Error de edad","La edad ingresada es invalida")

                                            # Creación FieldFrame
                                            listaCampos= ["Nombre", "Cédula", "Edad"]
                                            listahabilitados = [True, True, True]
                                            valorEsperado = {"Nombre": str, "Cédula": int, "Edad": int} 

                                            registrarUsuario = FieldFrame(frame_bottom, "Registro de la compra:", listaCampos, "Sus datos personales:", listahabilitados, valorEsperado)
                                            registrarUsuario.pack(expand=True, fill="both")

                                            # Botón de Comprar
                                            registrarUsuario.funAceptar(registroCompra, "Finalizar")


                                        else:
                                            messagebox.showerror("Error Fuera de Rango",ErrorFueraRango())
                                else:
                                    messagebox.showerror("Error en campos","Faltan campos por rellenar")

                            # Boton continuar
                            continuar = tk.Button(frame_produtos,text="Comprar", font=("Verdana", 10), bg="white", command=funcontinuar)
                            continuar.grid(row=2 , column=8, padx=15)





                    # Combobox con opciones para filtrar
                    listacampo = ["Seleccione el filtro"]
                    listahabilitado = [True] 
                    dictipo = {"Seleccione el filtro": str}
                    valor = [""]
                    dicRespuestas = {"Seleccione el filtro": ["perros", "gatos", "hamsters", "conejos", "aves"]} 

                    combo_filtrar = FieldFrame(frame_bottom, "¿Para cual tipo de animal?", listacampo, "Tipo de Animal", listahabilitado, dictipo, valor, dicRespuestas)
                    combo_filtrar.pack(expand=True, fill="both")

                    combo_filtrar.funAceptar(controlFiltrar, "Continuar")

        # Botón de comenzar 
        inicioTienda.funAceptar(proceso_2_Tienda, "Comenzar")

    
    def socializar():
        clear_frame_bottom()

        texto = "Si deseas encontrar nuevos amigos para ti y tu mascota, socializar te permitirá hacerlo."
        
        # Configuración del marco superior
        formato_frame_top("Socializar", texto)
        
        # Crear un frame inicial para la selección de opción
        listaOpciones = ["Registrarse", "Hacer Match"]
        listaEditables = [True, True]
        dicTipos = {"Opción": str}

        frame_inicio = FieldFrame(frame_bottom, "Inicio", ["Opción"], "Selecciona una opción", listaEditables, dicTipos, listaOpciones)
        frame_inicio.pack(expand=True, fill="both")

        cliente_defecto = Cliente("Sari", 30, 123456789, True)
        mascota_defecto = Animal("Luna", 5, "amigable,activo,calmado,jugueton,tranquilo")
        cliente_defecto._mascota = mascota_defecto
        
        socializar_instance = Socializar()  # Instancia de la clase Socializar

        def buscar_matches(cliente):  
            posibles_matches = socializar_instance.buscar_posibles_matches(cliente)
            if not posibles_matches:
                posibles_matches.append(cliente_defecto)
            
            def mostrar_matches():
                # Ocultar el frame actual de datos del cliente
                frame_inicio.pack_forget()

                # Crear un nuevo frame para mostrar los resultados de los matches
                frame_Matches = Frame(frame_bottom)
                frame_Matches.pack(expand=True, fill="both")

                # Crear labels para los resultados
                header_label = Label(frame_Matches, text="Resultados de Matches")
                header_label.pack()

                # Mostrar los datos de los posibles matches
                for i, match in enumerate(posibles_matches):
                    match_label = Label(frame_Matches, text=f"{i+1}. Cliente: {match._nombre}, Mascota: {match._mascota._nombre}")
                    match_label.pack()

                def hacer_match():
                    seleccion = seleccion_entry.get()  # Obtener el valor del entry
                    try:
                        seleccion = int(seleccion) - 1

                        if 0 <= seleccion < len(posibles_matches):
                            cliente_seleccionado = posibles_matches[seleccion]
                            if cliente_seleccionado == cliente_defecto:
                                nueva_cita = Cita(cliente, cliente_defecto)  # Asegúrate de que ambos argumentos sean Cliente
                            else:
                                nueva_cita = Cita(cliente, cliente_seleccionado)  # Asegúrate de que ambos argumentos sean Cliente
                            socializar_instance.citas.append(nueva_cita)
                            messagebox.showinfo("Match Realizado", f"¡Has hecho match con {cliente_seleccionado._nombre} y su mascota {cliente_seleccionado._mascota._nombre}!")
                            
                            # Limpiar el frame de resultados de matches y volver al inicio
                            frame_Matches.pack_forget()  # Ocultar el frame de matches
                            socializar()  # Volver a mostrar el frame de inicio
                        else:
                            messagebox.showerror("Error", "Selección no válida.")
                    except ValueError:
                        messagebox.showerror("Error", "Entrada no válida. Debe ser un número.")


                # Crear un label y un entry para ingresar el número del cliente
                seleccion_label = Label(frame_Matches, text="Seleccione el número del cliente con el que desea hacer match:")
                seleccion_label.pack()
                seleccion_entry = Entry(frame_Matches)
                seleccion_entry.pack()

                # Configurar el botón para realizar el match
                hacer_match_button = Button(frame_Matches, text="Match", command=hacer_match)
                hacer_match_button.pack()
            
            # Crear un nuevo botón para mostrar los resultados de los matches
            boton_buscar_matches = Button(frame_bottom, text="Buscar", command=mostrar_matches)
            boton_buscar_matches.pack()
        
        def registrar_cliente():
            clear_frame_bottom()

            texto = "Por favor, completa los datos del cliente y su mascota para registrarse."

            # Configuración del marco superior
            formato_frame_top("Registrarse", texto)
            
            # Creación del FieldFrame para recolectar los datos del cliente
            listaCampos = ["Nombre", "Edad", "Celular", "Deseas formar parte de socializar? (True/False)"]
            listaEditables = [True, True, True, True]
            listaValores = ["", "", "", ""]
            dicTipos = {"Nombre": str, "Edad": int, "Celular": int, "Deseas formar parte de socializar? (True/False)": bool}

            frame_cliente = FieldFrame(frame_bottom, "Cliente", listaCampos, "Datos del Cliente", listaEditables, dicTipos, listaValores)
            frame_cliente.pack(expand=True, fill="both")

            def guardar_cliente():
                datos_cliente = frame_cliente.getEntradas()  # Recolectar los datos del cliente
                if datos_cliente:  # Verificar que no sean falsos o vacíos
                    # Crear el objeto Cliente
                    nuevo_cliente = Cliente(datos_cliente[0], datos_cliente[1], datos_cliente[2], datos_cliente[3])
                    
                    # Llamar a la función registrar_mascota pasándole el nuevo cliente
                    registrar_mascota(nuevo_cliente)

            # Configurar el botón para aceptar los datos del cliente y proceder al registro de mascota
            frame_cliente.funAceptar(guardar_cliente, "Registrar")

        def registrar_mascota(cliente):
            clear_frame_bottom()

            # Crear un nuevo FieldFrame para registrar los datos de la mascota
            listaMascota = ["Nombre", "Edad", "Características"]
            listaEditables = [True, True, True]
            dicTiposMascota = {"Nombre": str, "Edad": int, "Características": str}

            frame_Mascota = FieldFrame(frame_bottom, "Mascota", listaMascota, "Datos de la Mascota", listaEditables, dicTiposMascota)
            frame_Mascota.pack(expand=True, fill="both")

            def guardar_mascota():
                datos_mascota = frame_Mascota.getEntradas()  # Recolectar datos de la mascota
                if datos_mascota:
                    # Crear un objeto Mascota
                    mascota = Animal(datos_mascota[0], datos_mascota[1], datos_mascota[2].split(","))
                    
                    # Asignar la mascota al cliente
                    cliente._mascota = mascota
                    
                    # Registrar el cliente en Socializar
                    socializar_instance.registrar_cliente(cliente)
                    
                    messagebox.showinfo("Registro Exitoso", f"¡Cliente {cliente._nombre} y su mascota {mascota._nombre} registrados exitosamente!")
                    
                    # Limpiar el frame de la mascota y proceder a buscar matches
                    frame_Mascota.pack_forget()  # Ocultar el frame de la mascota
                    buscar_matches(cliente)  # Proceder a buscar matches

            # Configurar el botón para guardar los datos de la mascota
            frame_Mascota.funAceptar(guardar_mascota, "Registrar")
            frame_inicio.pack()

        def seleccionar_opcion():
            opcion = frame_inicio.getEntradas()  # Recolectar la opción seleccionada
            if opcion:
                if opcion[0] == "Registrarse":
                    frame_inicio.pack_forget()
                    registrar_cliente()
                elif opcion[0] == "Hacer Match":
                    frame_inicio.pack_forget()
                    
                    # Si no hay clientes registrados, usar el cliente por defecto
                    if not socializar_instance.clientes:  # Acceso correcto al atributo
                        messagebox.showinfo("Cliente por defecto", "No hay clientes registrados. Usaremos un cliente por defecto.")
                        socializar_instance.registrar_cliente(cliente_defecto)
                        buscar_matches(cliente_defecto)
                    else:
                        # Llamar a la función para buscar matches con el cliente registrado
                        cliente_registrado = socializar_instance.clientes[-1]  # Seleccionar el último cliente registrado
                        buscar_matches(cliente_registrado)

        # Configurar el botón para continuar según la opción seleccionada
        frame_inicio.funAceptar(seleccionar_opcion, "Continuar")

    def funeraria():
        texto = "Aquí va la descripción de la funcionalidad :)"
        formato_frame_top("Funcionalidad funeraria", texto)

        # LIMPIAR EL CONTENIDO DEL FRAME_BOTTOM
        clear_frame_bottom()
        # Crear un objeto Field Frame
        listaCampos = ["Sedes"]
        listaEditables = [True]
        listaValores = [""]
        dicTipos = {"Sedes": str}
        combobox_items = {"Sedes": ["Sede Bello", "Sede Itagüi", "Sede Medellín"]}

        frame = FieldFrame(frame_bottom, "Centro de adopción", listaCampos, "Escoja una sede", listaEditables, dicTipos, listaValores, combobox_items)
        frame.pack(expand=True, fill="both")
        messagebox.showinfo("Información", "Por favor, seleccione el centro de adopción más cercano")

        # Declarar el frame_visitas fuera para que esté disponible
        frame_visitas = None

        def serviciosSede():

            sede_seleccionada = frame.getEntradas()

            # Crear la funeraria según la sede seleccionada
            if "Sede Bello" in sede_seleccionada:
                funeraria_seleccionada = Funeraria(sedes[0])
                funeraria_convert = sedes[0].getNombre# Sede Bello
            elif "Sede Itagüi" in sede_seleccionada:
                funeraria_seleccionada = Funeraria(sedes[1])  # Sede Itagüi
            elif "Sede Medellín" in sede_seleccionada:
                funeraria_seleccionada = Funeraria(sedes[2])  # Sede Medellín

            def mostrarCementerio(objetos, frame_objetos_anterior = None):
                # Crear un Canvas dentro de frame_bottom
                canvas = tk.Canvas(frame_bottom, borderwidth=3, background="thistle1")
                
                # Crear un Frame dentro del Canvas para contener los objetos
                frame_objetos = tk.Frame(canvas, bg="thistle1", highlightbackground="purple4", highlightthickness=2)
                
                # Crear una ventana en el Canvas que contiene el Frame
                canvas.create_window((0, 0), window=frame_objetos)

                # Scrollbar para el Canvas
                vsb = tk.Scrollbar(canvas, orient="vertical", command=canvas.yview)
                canvas.configure(yscrollcommand=vsb.set)
                

                # Posicionar Canvas y Scrollbar en frame_bottom
                canvas.pack(side="top", fill="both", expand=True, anchor="center")
                vsb.pack(side="right", fill="y")

                frame_objetos.columnconfigure(0, weight=1)
                frame_objetos.rowconfigure(0, weight=0)

                # Ajustar el tamaño de frame_objetos para que ocupe todo el Canvas
                frame_objetos.update_idletasks()  # Asegúrate de que el frame esté completamente actualizado
                canvas.config(scrollregion=canvas.bbox("all"))
                frame_objetos.pack(side="top", fill="both", expand=True, anchor="center")

                # Añadir contenido al frame_objetos
                resultado_visita = objetos
                if resultado_visita:
                    filas = 0  # Control de filas en el grid
                    for linea in resultado_visita.split("\n"):  # Dividir las líneas del texto
                        if linea.strip():  # Mostrar solo líneas no vacías
                            tk.Label(frame_objetos, text=linea, font=("Times New Roman", 13), fg="purple", bg="thistle1").grid(row=filas, column=0, padx=0, pady=10, sticky="nsew")
                            filas += 1  # Incrementar fila para el siguiente objeto

                # Actualizar el tamaño del scroll region una vez que todos los widgets estén agregados
                frame_objetos.update_idletasks()
                canvas.config(scrollregion=canvas.bbox("all"))

                return frame_objetos, canvas

            def visitaCementerio(seleccion, frame_anterior):
                frame_anterior.pack_forget()
                resultado = funeraria_seleccionada.visita(seleccion)
                frame_cementerio, canvas = mostrarCementerio(resultado)
                listaCampos = ["Agregar flores"]
                combobox_items = {"Agregar flores": ["Sí", "No"]}
                listaEditables = [True]
                listaValores = [""]
                frame_flores = FieldFrame(frame_bottom, "Agregar flores", listaCampos, "¿Desea agregar flores?", listaEditables, dicTipos, listaValores, combobox_items)
                frame_flores.pack(expand=True, fill="both")

                def opcionFlores():
                    seleccion_flores = frame_flores.getEntradas()[0]
                    if seleccion_flores == "Sí":
                        retorno = frame_flores.funAceptar(manejarFlores(funeraria_seleccionada, seleccion, frame_flores, frame_cementerio, canvas), "OPCION SÍ")
                    elif seleccion_flores == "No":
                        retorno = frame_flores.funAceptar(funeraria, "OPCIÓN NO")
                    return retorno
                
                frame_flores.funAceptar(opcionFlores, "NINGUNA")

            def manejarFlores(funeraria_seleccionada, seleccion, frame_anterior, frame_objetos, canvas1):
                print(type(frame_anterior))
                print(type(frame_objetos))
                frame_anterior.pack_forget()
                listaCampos = ["Flores", seleccion]
                listaEditables = [True, True]
                listaValores = ["", ""]
                
                if seleccion == "tumbas":
                    combobox_items_flores = {"Flores": ["Rosas", "Lirios", "Tulipanes"], seleccion: [f"Tumba {i+1}" for i in range(len(funeraria_seleccionada.getTumbas()))]}
                    frame_flores_opciones = FieldFrame(frame_bottom, "Opciones de flores", listaCampos, "Seleccione una flor y una tumba", listaEditables, dicTipos, listaValores, combobox_items_flores)
                else:
                    combobox_items_flores = {"Flores": ["Rosas", "Lirios", "Tulipanes"], seleccion: [f"Osario {i+1}" for i in range(len(funeraria_seleccionada.getCenizas()))]}
                    frame_flores_opciones = FieldFrame(frame_bottom, "Opciones de flores", listaCampos, "Seleccione una flor y un osario", listaEditables, dicTipos, listaValores, combobox_items_flores)

                frame_flores_opciones.pack(expand=True, fill="both")

                def agregarFlores():
                    flor_seleccionada = frame_flores_opciones.getEntradas()[0]
                    opcion_seleccionada = int(frame_flores_opciones.getEntradas()[1].split(" ")[-1]) - 1
                    if seleccion == "tumbas":
                        mensaje = funeraria_seleccionada.florTumbas(opcion_seleccionada, flor_seleccionada)
                    else:
                        mensaje = funeraria_seleccionada.florCenizas(opcion_seleccionada, flor_seleccionada)

                    print(mensaje)
                    frame_flores_opciones.pack_forget()
                    frame_objetos.pack_forget()
                    canvas1.pack_forget()
                    resultado_con_flor = funeraria_seleccionada.visita(seleccion)
                    frame_resultado_nuevo, canvas2 = mostrarCementerio(resultado_con_flor, frame_objetos)
                    print(type(frame_resultado_nuevo))

                    return frame_resultado_nuevo
                
                frame_flores_opciones.funAceptar(agregarFlores, "Agregar flores")

            def inicioProcesoDatos(accion, seleccion):
                listaCampos = ["Nombre", "Edad", "Cédula", "Número de celular","Dirección"]
                listaEditables = [True, True, True, True, True]
                listaValores = ["", "", "", "", ""]
                dicTipos = {"Nombre": str, "Edad": int, "Cédula": int, "Número de celular": int, "Dirección": str}
                frame_datos_usuario = FieldFrame(frame_bottom, f"Información para {accion}", listaCampos, "Ingresa tus datos", listaEditables, dicTipos, listaValores)
                frame_datos_usuario.pack(expand=True, fill="both")

                def pedirDatosMascota():
                    datos_cliente = frame_datos_usuario.getEntradas()
                    cliente = Cliente(datos_cliente[0], datos_cliente[1], datos_cliente[2], datos_cliente[3], datos_cliente[4])
                    print(cliente)
                    frame_datos_usuario.pack_forget()
                    if accion == "la compra":
                        listaCampos = ["Nombre que tenía", "Tipo de animal", "Edad con la que murió", "Sexo", "Fecha de fallecimiento", "Años a adquirir el producto"]
                        listaEditables = [True, True, True, True, True, False]
                        listaValores = ["", "", "", "", "dia/mes/año", "de por vida"]
                        dicTipos = {"Nombre que tenía":str, "Tipo de animal":str, "Edad con la que murió":int, "Sexo":str, "Fecha de fallecimiento":str, "Años a adquirir el producto":int}
                        frame_datos_mascota = FieldFrame(frame_bottom, "Información de la mascota", listaCampos, "Ingresa sus datos", listaEditables, dicTipos, listaValores)
                        frame_datos_mascota.pack(expand=True, fill="both")
                    else:
                        listaCampos = ["Nombre que tenía", "Tipo de animal", "Edad con la que murió", "Sexo", "Fecha de fallecimiento", "Años a adquirir el producto"]
                        listaEditables = [True, True, True, True, True, True]
                        listaValores = ["", "", "", "", "dia/mes/año", ""]
                        dicTipos = {"Nombre que tenía":str, "Tipo de animal":str, "Edad con la que murió":int, "Sexo":str, "Fecha de fallecimiento":str, "Años a adquirir el producto":int}
                        frame_datos_mascota = FieldFrame(frame_bottom, "Información de la mascota", listaCampos, "Ingresa sus datos", listaEditables, dicTipos, listaValores)
                        frame_datos_mascota.pack(expand=True, fill="both")
                        

                    def mensajeMascota():
                        datos_mascota = frame_datos_mascota.getEntradas()
                        mascota = Animal(datos_mascota[0], datos_mascota[1], datos_mascota[2], datos_mascota[3])
                        print(mascota)
                        frame_datos_mascota.pack_forget()
                        listaCampos = ["Mensaje"]
                        listaEditables = [True]
                        listaValores = [""]
                        dicTipos = {"Mensaje":str}
                        frame_mensaje = FieldFrame(frame_bottom, f"Mensaje para tu mascota", listaCampos, "Escribe el mensaje", listaEditables, dicTipos, listaValores)
                        frame_mensaje.pack(expand=True, fill="both")
                        messagebox.showinfo("Información", "Agrega el mensaje que quieras para tu mascota")

                        # Expande el Entry correspondiente a "Mensaje" solo en este caso
                        for entrada in frame_mensaje.lista_entradas:
                            entrada.grid(sticky="nsew", padx=30)  # Solo afecta a las entradas de este frame

                        def guardarEnCementerio():
                            mensaje = frame_mensaje.getEntradas()
                            años = datos_mascota[5]
                            print(mensaje)

                            if seleccion == "tumbas":
                                if accion == "la compra":
                                    muerto = Muerto(mascota, datos_mascota[4], mensaje[0], cliente, "de por vida", seleccion)
                                    Funeraria.tumbas.append(muerto)
                                    messagebox.showinfo("Información","Su compra ha sido exitosa.")
                                    messagebox.showinfo("Información de pago", "A su dirección se le enviará la factura, y se le estará contactando por teléfono.\nTotal a pagar por el terreno de por vida es igual a: $4000000")
                                    print(muerto)
                                else:
                                    muerto = Muerto(mascota, datos_mascota[4], mensaje[0], cliente, datos_mascota[5], seleccion)
                                    Funeraria.tumbas.append(muerto)
                                    messagebox.showinfo("Información","Su alquiler ha sido exitoso.")
                                    messagebox.showinfo("Información de pago", f"A su dirección se le enviará la factura, y se le estará contactando por teléfono.\nTotal a pagar por el terreno los {años} años de alquiler es igual a: ${años*500000}")
                                    print(muerto)
                            elif seleccion == "cenizas":
                                if accion == "la compra":
                                    muerto = Muerto(mascota, datos_mascota[4], mensaje[0], cliente, "de por vida", seleccion)
                                    Funeraria.cenizas.append(muerto)
                                    messagebox.showinfo("Información","Su compra ha sido exitosa.")
                                    messagebox.showinfo("Información de pago", "A su dirección se le enviará la factura, y se le estará contactando por teléfono.\nTotal a pagar por el osario de por vida es igual a: $2000000")
                                    print(muerto)
                                else:
                                    muerto = Muerto(mascota, datos_mascota[4], mensaje[0], cliente, datos_mascota[5], seleccion)
                                    Funeraria.cenizas.append(muerto)
                                    messagebox.showinfo("Información","Su alquiler ha sido exitoso.")
                                    print(muerto)

                        # Llamar a guardarEnCementerio al aceptar
                        frame_mensaje.funAceptar(lambda: [guardarEnCementerio(), visitaCementerio(seleccion, frame_mensaje)], "Continuar")

                    frame_datos_mascota.funAceptar(mensajeMascota, "Continuar")
     
                frame_datos_usuario.funAceptar(pedirDatosMascota, "Continuar")

            def mostrarServicios():
                servicio_seleccionado = frame_servicios.getEntradas()

                for i in servicio_seleccionado:
                    if i == "Cremación":
                        if funeraria_seleccionada.espacioCenizas():
                            listaCampos = ["Acciones"]
                            listaEditables = [True]
                            listaValores = [""]
                            combobox_items = {"Acciones": ["Comprar osario", "Alquilar osario"]}
                            frame_opciones = FieldFrame(frame_bottom, "Opciones para cremación", listaCampos, "Escoja una opción", listaEditables, dicTipos, listaValores, combobox_items)
                            frame_opciones.funAceptar(mostrarServicios, "Continuar")
                            frame_opciones.pack(expand=True, fill="both")
                            messagebox.showinfo("Información", "¡Si hay espacio disponible!")

                            def manejarAccionOsario():
                                accion_seleccionada = frame_opciones.getEntradas()[0]
                                if accion_seleccionada == "Comprar osario":
                                    print("Has seleccionado comprar un osario.")
                                    frame_servicios.pack_forget()
                                    frame.pack_forget()
                                    frame_opciones.pack_forget()
                                    inicioProcesoDatos("la compra", "cenizas")
                                    messagebox.showinfo("Información", f"Vas a comprar un osario en la {sede_seleccionada[0]}")

                                elif accion_seleccionada == "Alquilar osario":
                                    print("Has seleccionado alquilar un osario.")
                                    frame_servicios.pack_forget()
                                    frame.pack_forget()
                                    frame_opciones.pack_forget()
                                    inicioProcesoDatos("el alquiler", "cenizas")
                                    messagebox.showinfo("Información", f"Vas a alquilar un osario en la {sede_seleccionada[0]}")

                            frame_opciones.funAceptar(manejarAccionOsario, "Continuar")
                            frame_opciones.pack(expand=True, fill="both")
                        else:
                            print("No hay espacio para cenizas.")
                    
                    elif i == "Entierro":
                        if funeraria_seleccionada.espacioTumbas():
                            listaCampos = ["Acciones"]
                            listaEditables = [True]
                            listaValores = [""]
                            combobox_items = {"Acciones": ["Comprar terreno", "Alquilar terreno"]}
                            frame_opciones = FieldFrame(frame_bottom, "Opciones para entierro", listaCampos, "Escoja una opción", listaEditables, dicTipos, listaValores, combobox_items)
                            frame_opciones.funAceptar(mostrarServicios, "Continuar")
                            frame_opciones.pack(expand=True, fill="both")

                            def manejarAccionTumba():
                                accion_seleccionada = frame_opciones.getEntradas()[0]
                                if accion_seleccionada == "Comprar terreno":
                                    print("Has seleccionado comprar un terreno.")
                                    frame_servicios.pack_forget()
                                    frame.pack_forget()
                                    frame_opciones.pack_forget()
                                    inicioProcesoDatos("la compra", "tumbas")

                                elif accion_seleccionada == "Alquilar terreno":
                                    print("Has seleccionado alquilar un terreno.")
                                    frame_servicios.pack_forget()
                                    frame.pack_forget()
                                    frame_opciones.pack_forget()
                                    inicioProcesoDatos("el alquiler", "tumbas")

                            frame_opciones.funAceptar(manejarAccionTumba, "Continuar")
                            frame_opciones.pack(expand=True, fill="both")
                        else:
                            print("No hay espacio para tumbas.")

                    elif i == "Visitar cementerio":
                        listaCampos = ["Visitar"]
                        combobox_items = {"Visitar": ["Osarios", "Tumbas"]}
                        listaEditables = [True]
                        listaValores = [""]
                        nonlocal frame_visitas
                        frame_visitas = FieldFrame(frame_bottom, "Lugar a visitar", listaCampos, "Escoja una opción", listaEditables,dicTipos, listaValores, combobox_items)
                        frame_visitas.funAceptar(mostrarVisitas, "Continuar")
                        frame_visitas.pack(expand=True, fill="both")

            def mostrarVisitas():
                lugar_seleccionado = frame_visitas.getEntradas()[0]

                if lugar_seleccionado == "Tumbas":
                    frame.pack_forget()
                    frame_servicios.pack_forget()
                    visitaCementerio("tumbas", frame_visitas)

                elif lugar_seleccionado == "Osarios":
                    frame.pack_forget()
                    frame_servicios.pack_forget()
                    visitaCementerio("cenizas", frame_visitas)

            # Mostrar los servicios disponibles según la sede seleccionada
            listaCampos = ["Servicios"]
            listaEditables = [True]
            listaValores = [""]
            dicTipos = {"Servicios": str}
            combobox_items = {"Servicios": ["Cremación", "Entierro", "Visitar cementerio"]}

            frame_servicios = FieldFrame(frame_bottom, "Servicios funerarios", listaCampos, "Escoja un servicio", listaEditables, dicTipos, listaValores, combobox_items)
            frame_servicios.funAceptar(mostrarServicios, "Continuar")
            frame_servicios.pack(expand=True, fill="both")

        frame.funAceptar(serviciosSede, "Continuar")

    # ---- Menu --------
    
    # crear la barra de menu
    menubar = tk.Menu(vent_principal)

    #asociar la barra con la ventana de inicio
    vent_principal.config(menu = menubar)

    # menu archivo
    menu_1 = tk.Menu(menubar, tearoff=0, font=("Arial",10))
    menubar.add_cascade(label = "Archivo", menu = menu_1)

    menu_1.add_command(label = "Aplicación", command = descripcion_aplicacion)
    menu_1.add_separator()
    menu_1.add_command(label = "Salir", command = salir)

    # menu procesos y consultas
    menu_2 = tk.Menu(menubar, tearoff=0, font=("Arial",9))
    menubar.add_cascade(label = "Procesos y consultas", menu = menu_2)

    menu_2.add_command(label = "Adoptar una mascota", command = adoptarAnimal)
    menu_2.add_separator()
    menu_2.add_command(label = "Agendar servicio", command = agendar_servicio)
    menu_2.add_separator()
    menu_2.add_command(label = "Tienda para mascotas", command = tienda)
    menu_2.add_separator()
    menu_2.add_command(label = "Socializar", command = socializar)
    menu_2.add_separator()
    menu_2.add_command(label = "Funeraria", command = funeraria)

    # menu ayuda
    menu_3 = tk.Menu(menubar, tearoff=0, font=("Arial",10))
    menubar.add_cascade(label = "Ayuda", menu = menu_3)

    menu_3.add_command(label = "Acerca de", command = info_desarrolladores)

    # FRAME PRINCIPAL (MARCO)

    frame_principal = tk.Frame(vent_principal, bg = "#B89AD6")
    frame_principal.pack(expand= True, fill="both")

    # Frame superior (en el principal)
    frame_top = tk.Frame(frame_principal, bg = "thistle1", highlightbackground="purple4", highlightthickness=2)
    frame_top.pack(side = "top", padx=10, pady=10, expand= True, fill= "both")
    frame_top.pack_propagate(False)

    titulo_1 = tk.Label(frame_top, text = "AdoptaLove", font=("Lucida Handwriting", 45, "bold"), fg = "purple4", bg = "thistle1")
    titulo_1.pack(pady=10, anchor='center', expand=True)

    descripcionFun = tk.Label(frame_top, bg = "thistle1")
    descripcionFun.pack(side = "bottom", expand=True, fill = "both", pady =3)
  
    # Frame inferior (en el principal)-------
    frame_bottom = tk.Frame(frame_principal, bg = "#B89AD6")
    frame_bottom.pack(side = "bottom", padx=5, pady=5, expand= True, fill= "both",ipady= 130)
    frame_bottom.pack_propagate(False)

    # sub frame izquierdo de frame inferior
    frame_b_left= tk.Frame(frame_bottom, bg = "thistle1", highlightbackground="purple4", highlightthickness=2)
    frame_b_left.pack(side= "left",padx=5, pady=5, expand= True, fill= "both")
    frame_b_left.pack_propagate(False)

    titulo_2 = tk.Label(frame_b_left, text= "¿Cómo utilizar nuestra aplicación?", font = ("Times New Roman", 14), fg= "purple4", bg = "plum1")
    titulo_2.pack(side="top", padx=5, pady=5)

    explicacion_uso = (
        "Esta aplicación está diseñada para gestionar diversas funcionalidades\n relacionadas con la adopción de mascotas "
        "y servicios asociados\n para sus cuidados. En la barra de menú en la parte superior, encontrará\n tres secciones de "
        "la aplicación para realizar varias tareas.\n\n"
        "En el menú Archivo puedes obtener una descripción general sobre la aplicación\n y su propósito en la opción 'Aplicación'. "
        "También encontrarás la opción 'Salir'\n para cerrar la ventana principal y regresar al inicio.\n\n"
        "En Procesos y consultas podrás interactuar con las funcionalidades\n principales de la aplicación. Puedes seleccionar y hacer uso "
        "de los diferentes\n servicios que te proporcionamos como usuario.\n\n En el menú Ayuda podrás encontrar la opción 'Acerca de', "
        "que muestra\n información sobre los desarrolladores de la aplicación."
    )

    texto_2 = tk.Label (frame_b_left, text = explicacion_uso, font = ("Times New Roman", 14), fg= "purple", bg = "thistle1")
    texto_2.pack(side="top", padx=5, pady=5)

    #sub frame derecho de frame inferior
    frame_b_right= tk.Frame(frame_bottom, bg = "thistle1", highlightbackground="purple4", highlightthickness=2)
    frame_b_right.pack(side= "right", padx=5, pady=5, expand= True, fill= "both")
    frame_b_right.pack_propagate(False)

    titulo_3 = tk.Label(frame_b_right, text= "¿Qué se puede hacer?", font = ("Times New Roman", 14), fg= "purple4", bg = "plum1")
    titulo_3.pack(side="top", padx=5, pady=5)

    explicacion_hace = (
        "Las acciones más destacadas que se podrán realizar se encuentran en el\n menú procesos y consultas, dentro de las opciones "
        "que se brindan\n podrás adoptar una mascota, agendar servicios como citas veterinarias\n de peluquería y guardería, también"
        "podrás visitar la tienda para comprar\n productos para tu mascota, socializar con otros dueños y acceder a\n servicios funerarios "
        "si es necesario."
    )

    texto_3 = tk.Label (frame_b_right, text = explicacion_hace,font = ("Times New Roman", 14), fg= "purple", bg = "thistle1")
    texto_3.pack(side="top", padx=5, pady=5)
