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

# CREACIÓN DE OBJETOS BASE -----------------------------


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
        tk.Button(self, text="Limpiar", font=("Verdana", 10), bg="white", width=6, height=1, command=self.funborrar).grid(row=len(self.lista_criterios)+1, column=0, padx=5, pady=2)

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

    def adoptar_mascota():

        clear_frame_bottom()
        
        # Creación de un objeto Field Frame
        listaCampos = ["Nombre", "Cédula", "Dirección","edad" ,"Sexo", "pregunta"]
        listaEditables = [True, True, False,True, True, True]
        listaValores = ["", "", "", "","", ""]
        dicTipos = {"Nombre": str, "Cédula": int, "Dirección": str,"edad": int, "Sexo": str, "pregunta":str}

        combobox_items = {"Sexo": ["Masculino", "Femenino", "Otro"], "pregunta":["Messi", "Cristiano"]}

        frame = FieldFrame(frame_bottom, "Persona" ,listaCampos, "Sus datos", listaEditables, dicTipos, listaValores, combobox_items)
        #frame.place(x =0, y = 0 , width=1236, height= 418)
        frame.pack(expand=True, fill="both")

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

    def agendar_servicio():
        pass

    def tienda():
        pass

    def socializar():
        pass

    def funeraria():
        pass

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

    menu_2.add_command(label = "Adoptar una mascota", command = adoptar_mascota)
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




    


    










