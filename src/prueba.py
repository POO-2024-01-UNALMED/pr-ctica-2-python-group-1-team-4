import tkinter as tk 
from PIL import Image, ImageTk  # Importar módulos necesarios de Pillow

# Creamos la ventana de inicio
vent_inicio = tk.Tk()

# Darle un color a la ventana de inicio
vent_inicio.configure(bg='#f7f7f7')  # Fondo gris claro para un look limpio y moderno

# Establecer el espacio entre los bordes de la ventana y los widgets que contenga
vent_inicio.config(padx=5, pady=5)

# -------------------- EVENTOS -------------------------

def mostrar_bienvenida():
    # Crear o actualizar el texto en el frame_left_top (p3) con la bienvenida
    bienvenida = (
        "¡Bienvenido a AdoptaLove! \n\n"
        "Estamos encantados de que estés aquí. Este es un centro integral para el cuidado de mascotas, "
        "donde puedes encontrar una variedad de servicios y productos para el bienestar de tus amigos peludos. "
        "Explora nuestras opciones y si tienes alguna pregunta, no dudes en contactarnos."
    )

    # Limpiar cualquier texto previo si existe:
    for widget in frame_left_top.winfo_children():
        widget.destroy()
    
    # Crear un Text widget para mostrar la bienvenida con altura y anchura fija:
    text_bienvenida = tk.Text(frame_left_top, bg="#ffffff", wrap="word", height=10, width=40, font=("Arial", 11))
    text_bienvenida.insert("1.0", bienvenida)
    text_bienvenida.config(state="disabled")  # Hacer el Text de solo lectura
    text_bienvenida.pack(expand=True, fill="both")

def mostrar_descripcion():
    # Crear o actualizar el texto en el frame_left_top (p3) cuando se elija la opción "Descripción"
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

    # Limpiar cualquier texto previo si existe:
    for widget in frame_left_top.winfo_children():
        widget.destroy()
    
    # Crear un Text widget para mostrar la descripción con altura y anchura fija
    text_descripcion = tk.Text(frame_left_top, bg="#ffffff", wrap="word", height=10, width=40, font=("Arial", 11))
    text_descripcion.insert("1.0", descripcion)
    text_descripcion.config(state="disabled")  # Hacer el Text de solo lectura
    text_descripcion.pack(expand=True, fill="both")

def salir():
    # Cerrar la ventana cuando se elija la opción "Salir"
    vent_inicio.quit()

# Hojas de vida de los desarrolladores
hojas_de_vida = ["Oky Ruiz De La Rosa, 18 años, de San Andrés de Sotavento Córdoba "
                 "estudiante de ingeniería de sistemas e informática en la Universidad Nacional"
                 "de Colombia",

                 "Salomé Murillo Gaviria, xx años, de Medellín Antioquia "
                 "estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia", 

                 "Daniel Zapata, xx años, de Medellín Antioquia "
                 "estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia",

                 "Nicolas Zambrano, xx años, de Medellín Antioquia "
                 "estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia"]

# Rutas de las imágenes de los desarrolladores
imagenes = [["src/imagenes/Oky1.png","src/imagenes/Oky2.png","src/imagenes/Oky3.png","src/imagenes/Oky4.png"],
            ["src/imagenes/Salome1.png","src/imagenes/Salome2.png","src/imagenes/Salome3.png","src/imagenes/Salome4.png"],
            ["src/imagenes/Daniel1.png","src/imagenes/Daniel2.png","src/imagenes/Daniel3.png","src/imagenes/Daniel4.png"],
            ["src/imagenes/Nico1.png", "src/imagenes/Nico2.png","src/imagenes/Nico3.png", "src/imagenes/Nico4.png"]]

# Declarar las variables globales para almacenar las referencias de las imágenes y el contador de clicks
imagenes_labels = []
contador_click = 0

def actualizar_hojaVida_Imagenes(event):
    global contador_click, imagenes_labels

    # Cambiar el contenido de Text (hojas_vida) en p5
    hojas_vida.config(state='normal')
    hojas_vida.delete(1.0, 'end')
    hojas_vida.insert(1.0, hojas_de_vida[contador_click])
    hojas_vida.config(state="disabled")

    # Asignar las imágenes a los label de los sub-frames de p6
    lista_imagenes = imagenes[contador_click]

    # Redimensionar imágenes
    imagen1_redi = Image.open(lista_imagenes[0]).resize((200,180), Image.LANCZOS)
    imagen2_redi = Image.open(lista_imagenes[1]).resize((200,180), Image.LANCZOS)
    imagen3_redi = Image.open(lista_imagenes[2]).resize((200,180), Image.LANCZOS)
    imagen4_redi = Image.open(lista_imagenes[3]).resize((200,180), Image.LANCZOS)

    # Imágenes redimensionadas
    imagen1 = ImageTk.PhotoImage(imagen1_redi)
    imagen2 = ImageTk.PhotoImage(imagen2_redi)
    imagen3 = ImageTk.PhotoImage(imagen3_redi)
    imagen4 = ImageTk.PhotoImage(imagen4_redi)

    # Actualizar el label con su imagen
    label_p6_tl.config(image=imagen1)
    label_p6_tr.config(image=imagen2)
    label_p6_bl.config(image=imagen3)
    label_p6_br.config(image=imagen4)

    # Almacenar las referencias de las imágenes para evitar que sean recolectadas
    imagenes_labels = [imagen1, imagen2, imagen3, imagen4]

    # Aumentar el índice
    contador_click = (contador_click + 1) % len(hojas_de_vida)

# ---------------- MENÚ --------------------

# Crear la barra de menú 
menu_bar = tk.Menu(vent_inicio)

# Asociar la barra de menú con la ventana de inicio
vent_inicio.config(menu=menu_bar)

menu_1 = tk.Menu(menu_bar, tearoff=0, font=("Arial", 10))
menu_bar.add_cascade(label="Inicio", menu=menu_1)

menu_1.add_command(label="Descripción", command=mostrar_descripcion)
menu_1.add_separator()
menu_1.add_command(label="Salir", command=salir)

# --- -------- Crear los frames principales (p1) y (p2) -----------

# Frame grande izquierdo (p1):
frame_left = tk.Frame(vent_inicio, bg="#ffffff", bd="1", relief="solid")  # Blanco para claridad y contraste

# Empaquetar el frame izquierdo en la ventana
frame_left.pack(side="left", padx=5, pady=5, expand=True, fill="both")

# Frame grande derecho (p2):
frame_right = tk.Frame(vent_inicio, bg="#ffffff", bd="1", relief="solid")  # Blanco para uniformidad

# Empaquetar el frame derecho en la ventana
frame_right.pack(side="left", padx=5, pady=5, expand=True, fill="both")

# ------------------------------------------

# Crear los sub-frames dentro del frame izquierdo (p1):

# Frame superior (p3)
frame_left_top = tk.Frame(frame_left, bg="#f0f0f0", bd="1", relief="solid")  # Gris muy claro para un sutil contraste

# Empaquetar el frame p3 en el frame p1
frame_left_top.pack(side="top", padx=5, pady=5, expand=True, fill="both")
frame_left_top.pack_propagate(False)  # Evitar que el frame cambie su tamaño con los widgets internos

# Frame inferior (p4)
frame_left_bottom = tk.Frame(frame_left, bg="#f0f0f0", bd="1", relief="solid")  # Misma tonalidad para coherencia

# Empaquetar el frame p4 en el frame p1
frame_left_bottom.pack(side="bottom", padx=5, pady=5, expand=True, fill="both", ipady=85)

# ------------------------------------------

# Crear los sub-frames dentro del frame derecho (p2):

# Frame superior (p5)
frame_right_top = tk.Frame(frame_right, bg="#f0f0f0", bd="1", relief="solid")  # Manteniendo la coherencia de diseño

# Empaquetar el frame p5 en el frame p2
frame_right_top.pack(side="top", padx=5, pady=5, expand=True, fill="both")

# Crear el widget de texto para mostrar las hojas de vida
hojas_vida = tk.Text(frame_right_top, wrap="word", height=10, width=40, font=("Arial", 11))
hojas_vida.config(state="disabled")  # Hacer el Text de solo lectura
hojas_vida.pack(expand=True, fill="both")

# Frame inferior (p6)
frame_right_bottom = tk.Frame(frame_right, bg="#f0f0f0", bd="1", relief="solid")  # Fondo gris claro para coherencia

# Empaquetar el frame p6 en el frame p2
frame_right_bottom.pack(side="bottom", padx=5, pady=5, expand=True, fill="both")

# Crear los sub-sub-frames dentro del frame p6
frame_p6_tl = tk.Frame(frame_right_bottom, bg="#ffffff", bd="1", relief="solid")
frame_p6_tr = tk.Frame(frame_right_bottom, bg="#ffffff", bd="1", relief="solid")
frame_p6_bl = tk.Frame(frame_right_bottom, bg="#ffffff", bd="1", relief="solid")
frame_p6_br = tk.Frame(frame_right_bottom, bg="#ffffff", bd="1", relief="solid")

# Empaquetar los sub-sub-frames
frame_p6_tl.pack(side="left", padx=5, pady=5, expand=True, fill="both")
frame_p6_tr.pack(side="left", padx=5, pady=5, expand=True, fill="both")
frame_p6_bl.pack(side="left", padx=5, pady=5, expand=True, fill="both")
frame_p6_br.pack(side="left", padx=5, pady=5, expand=True, fill="both")

# Crear los Labels para las imágenes en los sub-sub-frames
label_p6_tl = tk.Label(frame_p6_tl)
label_p6_tr = tk.Label(frame_p6_tr)
label_p6_bl = tk.Label(frame_p6_bl)
label_p6_br = tk.Label(frame_p6_br)

label_p6_tl.pack(expand=True, fill="both")
label_p6_tr.pack(expand=True, fill="both")
label_p6_bl.pack(expand=True, fill="both")
label_p6_br.pack(expand=True, fill="both")

# Asociar el evento de click a cualquier parte de p6
frame_right_bottom.bind("<Button-1>", actualizar_hojaVida_Imagenes)

# Mostrar mensaje de bienvenida por defecto
mostrar_bienvenida()

# Ejecutar la ventana de inicio
vent_inicio.mainloop()
