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

    def mostrar_descripcion():
        # Crear o actualizar el texto en el frame_left_top (p3)
        descripcion = (
            "El proyecto AdoptaLove es un centro integral para el cuidado de mascotas que ofrece una "
            "variedad de servicios y productos diseñados para satisfacer las necesidades de los animales "
            "y sus dueños. Su objetivo principal es facilitar y promover la adopción responsable de "
            "mascotas, conectando de manera efectiva a animales en busca de un hogar con personas "
            "interesadas en brindarles amor y cuidado. \n"
            "Además de los servicios de adopción, AdoptaLove proporciona atención veterinaria, "
            "peluquería y guardería para mascotas, asegurando el bienestar y la comodidad de los "
            "animales. Para complementar esta oferta, AdoptaLove cuenta con tiendas donde los dueños "
            "pueden adquirir productos esenciales para el cuidado de sus mascotas."
        )
        
        # Limpiar cualquier texto previo si existe
        for widget in frame_left_top.winfo_children():
            widget.destroy()
        
        # Crear un Text widget para mostrar la descripción con altura y anchura fija
        text_descripcion = tk.Text(frame_left_top, bg="white", wrap="word", height=10, width=40, font=("Arial", 11))
        text_descripcion.insert("1.0", descripcion)
        text_descripcion.config(state="disabled")  # Hacer el Text de solo lectura
        text_descripcion.pack(expand=True, fill="both")

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

    menu_opciones.add_command(label =" Descripción", command= mostrar_descripcion)
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

    # Ubicar y crear el botón de cambio de ventana en p4
    btn_abrir_escena = tk.Button(frame_left_bottom, text="Abrir Nueva Ventana",
    command=lambda: mostrar_frame(frame_nueva_escena, menu_nueva_escena, "Nueva Escena"))
    btn_abrir_escena.pack(side = "bottom", padx=40, pady=40, expand = True, fill = "both")


    def mostrar_bienvenida():
        # Crear o actualizar el texto en el frame_left_top (p3) con la bienvenida
        bienvenida = (
            "¡Bienvenido a AdoptaLove! \n\n"
            "Estamos encantados de que estés aquí. Este es un centro integral para el cuidado de mascotas, "
            "donde puedes encontrar una variedad de servicios y productos para el bienestar de tus amigos peludos. "
            "Explora nuestras opciones y si tienes alguna pregunta, no dudes en contactarnos."
        )

        # Limpiar cualquier texto previo si existe
        for widget in frame_left_top.winfo_children():
            widget.destroy()
        
        # Crear un Text widget para mostrar la bienvenida con altura y anchura fija
        text_bienvenida = tk.Text(frame_left_top, bg="white", wrap="word", height=10, width=40, font=("Arial", 11))
        text_bienvenida.insert("1.0", bienvenida)
        text_bienvenida.config(state="disabled")  # Hacer el Text de solo lectura
        text_bienvenida.pack(expand=True, fill="both")

    mostrar_bienvenida()

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
vent_inicio.geometry("300x300")

# Configurar el grid para que todos los frames ocupen el mismo espacio
vent_inicio.rowconfigure(0, weight=1)
vent_inicio.columnconfigure(0, weight=1)

# Crear frames
frame_principal = crear_frame_principal()
frame_nueva_escena = crear_frame_nueva_escena()

# Mostrar el frame inicial (ventana principal) con su barra de menú
mostrar_frame(frame_principal, menu_principal, "Ventana Principal")

vent_inicio.mainloop()
