import tkinter as tk
from tkinter import messagebox

def abrir_ventana(vent_inicio):

    # crear la ventana principal
    vent_principal = tk.Toplevel(vent_inicio)  # Crear una ventana secundaria

    # asignarle el nombre, dimenciones iniciales y color de fondo
    vent_principal.title("AdoptaLove")
    vent_principal.geometry("1100x500")
    vent_principal.configure(bg='LightBlue1') 
    vent_principal.config(padx = 15, pady = 15)

    # ------ EVENTOS ------
    
    def descripcion_aplicacion():
         messagebox.showinfo("Información básica de la aplicación","La aplicación se encarga se gestionar procesos tales como ...")

    def salir():
        vent_principal.destroy()  # Cerrar la ventana principal
        vent_inicio.deiconify()  # Mostrar nuevamente la ventana de inicio

    def info_desarrolladores():
        messagebox.showinfo("Autores de la aplicación","Oky Ruiz De La Rosa\nSalomé murillo Gaviria\nNicolas David Zambrano Murcia\nDaniel Alberto Zapata Castaño")

    # ----- funcionalidades -------
    def adoptar_mascota():
        pass

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
  
    # Frame inferior (en el principal)-------
    frame_bottom = tk.Frame(frame_principal, bg = "#B89AD6")
    frame_bottom.pack(side = "bottom", padx=5, pady=5, expand= True, fill= "both",ipady= 130)

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
        "Las acciones más desctacadas que se podrán realizar se encuentran en el\n menú procesos y consultas, dentro de las opciones "
        "que se brindan\n podrás adoptar una mascota, agendar servicios como citas veterinarias\n de peluquería y guardería, también"
        "podrás visitar la tienda para comprar\n productos para tu mascota, socializar con otros dueños y acceder a\n servicios funerarios "
        "si es necesario."
    )

    texto_3 = tk.Label (frame_b_right, text = explicacion_hace,font = ("Times New Roman", 14), fg= "purple", bg = "thistle1")
    texto_3.pack(side="top", padx=5, pady=5)








