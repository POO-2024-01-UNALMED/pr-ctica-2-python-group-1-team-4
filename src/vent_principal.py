import tkinter as tk
from tkinter import messagebox

def abrir_ventana(vent_inicio):

    # crear la ventana principal
    vent_principal = tk.Toplevel(vent_inicio)  # Crear una ventana secundaria

    # asignarle el nombre
    vent_principal.title("AdoptaLove")

    # dar las dimensiones iniciales
    vent_principal.geometry("640x440")

    # ------ EVENTOS ------
    
    def descripcion_aplicacion():
         messagebox.showinfo("Aplicación"," falta esto")

    def cerrar_ventana():
        vent_principal.destroy()  # Cerrar la ventana principal
        vent_inicio.deiconify()  # Mostrar nuevamente la ventana de inicio

    def info_desarrolladores():
        messagebox.showinfo("Desarrolladores","Oky Ruiz De La Rosa\nSalomé murillo Gaviria\nNicolas David Zambrano Murcia\nDaniel Alberto Zapata Castaño")

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

    # ---- Menu ------
    
    # crear la barra de menu
    menubar = tk.Menu(vent_principal)

    #asociar la barra con la ventana de inicio
    vent_principal.config(menu = menubar)

    # menu archivo
    menu_1 = tk.Menu(menubar, tearoff=0, font=("Arial",10))
    menubar.add_cascade(label = "Archivo", menu = menu_1)

    menu_1.add_command(label = "Aplicación", command = descripcion_aplicacion)
    menu_1.add_separator()
    menu_1.add_command(label = "Salir", command = cerrar_ventana)

    # menu procesos y consultas
    menu_2 = tk.Menu(menubar, tearoff=0, font=("Arial",10))
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





    # Botón para cerrar la Ventana 2 y restaurar la Ventana 1
    boton_cerrar = tk.Button(vent_principal, text="Cerrar Ventana principal", command=lambda: cerrar_ventana(vent_principal, vent_inicio))
    boton_cerrar.pack(padx=20, pady=20)