import tkinter as tk

def mostrar_frame(frame, menu, titulo):
    # Cambia la barra de menú según la escena
    vent_inicio.config(menu=menu)
    # Cambia el título de la ventana
    vent_inicio.title(titulo)
    # Trae el frame al frente
    frame.tkraise()
    
def crear_frame_principal():
    # Crear el frame principal
    frame_principal = tk.Frame(vent_inicio)
    frame_principal.grid(row=0, column=0, sticky="nsew")


#----------------------------------------------------------------CODIGO QUE YA ESTÁ EN vent_inicio------------------------------------------------
    def salir():
        vent_inicio.quit()

    # Crear las barras de menú
    global menu_principal
    
    # Menú de la ventana principal
    menu_principal = tk.Menu(vent_inicio)
    
    # asociar la barra de menú con la ventana de inicio
    vent_inicio.config(menu=menu_principal)

    menu_opciones = tk.Menu(menu_principal, tearoff=0)
    menu_principal.add_cascade(label = "Inicio", menu = menu_opciones)

    menu_opciones.add_command(label =" Descripción")
    menu_opciones.add_separator()
    menu_opciones.add_command(label = "Salir", command= salir)

    # crear los frames principales -----

    # frame grande izquierdo (p1):
    frame_left= tk.Frame(frame_principal,bg = "white", bd = "2", relief="solid")

    # empaquetar el frame izquierdo en la ventana
    frame_left.pack(side = "left", padx=5, pady =5, expand=True, fill= "both")

    # Frame grande derecho (p2):
    frame_right= tk.Frame(frame_principal, bg = "white", bd = "2", relief="solid")

    # empaquetar el frame derecho en la ventana
    frame_right.pack(side = "left", padx=5, pady =5, expand=True, fill = "both")

    # --------

    # crear los frames dentro del frame izquiedo (p1):

    # frame superior (p3)
    frame_left_top = tk.Frame(frame_left, bg = "white", bd ="2", relief= "solid")

    #empaquetar el frame p3 en el frame p1
    frame_left_top.pack(side = "top", padx=5, pady=5, expand = True, fill = "both")
    frame_left_top.pack_propagate(False)  # Evitar que el frame cambie su tamaño con los widgets internos

    # frame inferior (p4)
    frame_left_bottom = tk.Frame(frame_left,bg = "white", bd ="2", relief= "solid")

    #empaquetar el frame p4 en el frame p1                                          #ipady para aumentar la altura
    frame_left_bottom.pack(side = "bottom", padx=5, pady=5, expand = True, fill = "both", ipady=55)

    # -------

    # crear los frames dentro del frame derecho(p2):

    # frame superior (p5)
    frame_right_top = tk.Frame(frame_right, bg = "white",bd ="2", relief= "solid")

    #empaquetar el frame p5 en el frame p2
    frame_right_top.pack(side = "top", padx=5, pady=5, expand = True, fill = "both")

    # frame inferior (p6)
    frame_right_bottom = tk.Frame(frame_right,bg = "white", bd ="2", relief= "solid")

    #empaquetar el frame p6 en el frame p2
    frame_right_bottom.pack(side = "bottom", padx=5, pady=5, expand = True, fill = "both", ipady=48 )

    # ------

    # Configurar las proporciones de las filas y columnas en  p6 (frame_right_bottom)
    frame_right_bottom.grid_rowconfigure(0, weight=1)  # Fila 0
    frame_right_bottom.grid_rowconfigure(1, weight=1)  # Fila 1
    frame_right_bottom.grid_columnconfigure(0, weight=1)  # Columna 0
    frame_right_bottom.grid_columnconfigure(1, weight=1)  # Columna 1

    # Crear los sub-frames de p6 
    frame_p6_tl = tk.Frame(frame_right_bottom, bg="lightblue", bd=2, relief="solid") #superior izquierdo
    frame_p6_tr = tk.Frame(frame_right_bottom, bg="lightblue", bd=2, relief="solid") #superior derecho
    frame_p6_bl = tk.Frame(frame_right_bottom, bg="lightblue", bd=2, relief="solid") #inferior izquierdo
    frame_p6_br = tk.Frame(frame_right_bottom, bg="lightblue", bd=2, relief="solid") #inferior derecho

    # Agregar los sub-frames a su cuadrícula en p6
    frame_p6_tl.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
    frame_p6_tr.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
    frame_p6_bl.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
    frame_p6_br.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

#-----------------------------------------------------------------------------------HASTA AQUÍ EL CODIGO DE vent_inicio------------------------------------------------

    # Ubicar y crear el botón de cambio de ventana en p4
    btn_abrir_escena = tk.Button(frame_left_bottom, text="Abrir Nueva Ventana",
    command=lambda: mostrar_frame(frame_nueva_escena, menu_nueva_escena, "Nueva Escena"))
    btn_abrir_escena.pack(side = "bottom", padx=40, pady=40, expand = True, fill = "both")

    return frame_principal

def crear_frame_nueva_escena():
    # Crear el frame de la nueva escena
    frame_nueva_escena = tk.Frame(vent_inicio)
    frame_nueva_escena.grid(row=0, column=0, sticky="nsew")

    # Contenido del frame de la nueva escena
    label_nueva_escena = tk.Label(frame_nueva_escena, text="Esta es la nueva escena")
    label_nueva_escena.pack(pady=20)
    btn_volver = tk.Button(frame_nueva_escena, text="Volver a la ventana principal", 
    command=lambda: mostrar_frame(frame_principal, menu_principal, "Ventana Principal"))
    btn_volver.pack()

    # Crear las barras de menú
    global menu_nueva_escena

    # Menú de la nueva escena
    menu_nueva_escena = tk.Menu(vent_inicio)
    menu_nueva_escena.add_command(label="Opción 1 Nueva Escena")
    menu_nueva_escena.add_command(label="Opción 2 Nueva Escena")

    return frame_nueva_escena


# Ventana principal
vent_inicio = tk.Tk()
vent_inicio.title("Ventana Principal")
vent_inicio.geometry("1400x800")

# Configurar el grid para que todos los frames ocupen el mismo espacio
vent_inicio.rowconfigure(0, weight=1)
vent_inicio.columnconfigure(0, weight=1)

# Crear frames
frame_principal = crear_frame_principal()
frame_nueva_escena = crear_frame_nueva_escena()

# Mostrar el frame inicial (ventana principal) con su barra de menú
mostrar_frame(frame_principal, menu_principal, "Ventana Principal")

vent_inicio.mainloop()
