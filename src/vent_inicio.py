import tkinter as tk 
from tkinter import messagebox

# Creamos la ventana de inicio
vent_inicio = tk.Tk()

# Establecer el espacio entre los bordes de la ventana y los widgets
vent_inicio.config(padx=5, pady=5)

# MENÚ ---------

# instanciar un objeto de tipo menu
menu_bar = tk.Menu(vent_inicio)

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

# asociar la barra de menú con la ventana de inicio
vent_inicio.config(menu=menu_bar)

menu_opciones = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label = "Inicio", menu = menu_opciones)

menu_opciones.add_command(label =" Descripción", command= mostrar_descripcion)
menu_opciones.add_separator()
menu_opciones.add_command(label = "Salir", command= salir)

# --------------------------

# crear los frames principales -----

# frame grande izquierdo (p1):
frame_left= tk.Frame(vent_inicio,bg = "white", bd = "2", relief="solid")

# empaquetar el frame izquierdo en la ventana
frame_left.pack(side = "left", padx=5, pady =5, expand=True, fill= "both")

# Frame grande derecho (p2):
frame_right= tk.Frame(vent_inicio, bg = "white", bd = "2", relief="solid")

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


# mostrar la venta y sus componentes
mostrar_bienvenida()  # Mostrar el texto de bienvenida al iniciar la aplicación
vent_inicio.mainloop()




