import tkinter as tk 
from PIL import Image, ImageTk  # Importar módulos necesarios de Pillow
import vent_principal

# Creamos la ventana de inicio
vent_inicio = tk.Tk()

# asignar un titulo
vent_inicio.title("AdoptaLove")

# Dimensiones iniciales
vent_inicio.geometry("640x440")

# Darle un color a la ventana de inicio
vent_inicio.configure(bg='pink') 

# Establecer el espacio entre los bordes de la ventana y los widgets que contenga
vent_inicio.config(padx = 5, pady = 5)

# -------------------- EVENTOS -------------------------

def mostrar_bienvenida():

    # Crear y actualizar el texto en el frame_left_top (p3) con la bienvenida
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
    text_bienvenida = tk.Text(frame_left_top, bg = "pink", wrap = "word", height = 10, width = 40, font = ("Arial", 11))
    text_bienvenida.insert("1.0", bienvenida)
    text_bienvenida.config(state = "disabled")  # Hacer el Text de solo lectura
    text_bienvenida.pack(expand=True, fill = "both")

def mostrar_descripcion():

    # Crear y actualizar el texto en el frame_left_top (p3) cuando se elija la opción "Descripcion"
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
    text_descripcion = tk.Text(frame_left_top, bg = "pink", wrap="word", height=10, width=40, font=("Arial", 11))
    text_descripcion.insert("1.0", descripcion)
    text_descripcion.config(state = "disabled")  # Hacer el Text de solo lectura
    text_descripcion.pack(expand=True, fill="both")

def salir():
    # Cerrar la ventana cuando se elija la opcion "salir"
    vent_inicio.quit()


# Hojas de vida de los desarrolladores
hojas_de_vida = ["Oky Ruiz De La Rosa, 18 años, de San Andrés de Sotavento Córdoba "
                 "estudiante de ingeniería de sistemas e informática en la Universidad Nacional"
                 "de Colombia",

                 "Salomé Murillo Gaviria, xx años, de medellín Antioquia "
                 "estudiante de ingeniería de sistema en la universidad nacional de Colombia", 

                 "Daniel Zapata, xx años, de medellín Antioquia "
                 "estudiante de ingeniería de sistema en la universidad nacional de Colombia",

                 "Nicolas Zambrano, xx años, de medellín Antioquia "
                 "estudiante de ingeniería de sistema en la universidad nacional de Colombia"]


# Rutas de las imagenes de los desarrolladores
imagenes = [["src/imagenes/Oky1.png","src/imagenes/Oky2.png","src/imagenes/Oky3.png","src/imagenes/Oky4.png"],
            ["src/imagenes/Salome1.png","src/imagenes/Salome2.png","src/imagenes/Salome3.png","src/imagenes/Salome4.png"],
            ["src/imagenes/Daniel1.png","src/imagenes/Daniel2.png","src/imagenes/Daniel3.png","src/imagenes/Daniel4.png"],
            ["src/imagenes/Nico1.png", "src/imagenes/Nico2.png","src/imagenes/Nico3.png", "src/imagenes/Nico4.png"]]

# Declarar las variables globales para almacenar las referencias de las imágenes y el contador de click's en p5
imagenes_labels = []
contador_click = 0

def actualizar_hojaVida_Imagenes(event):
    global contador_click, imagenes_labels

    # cambiar el contenido de Text (hojas_vida) en p5 -----
    hojas_vida.config(state= 'normal')
    hojas_vida.delete(1.0, 'end')
    hojas_vida.insert(1.0, hojas_de_vida[contador_click])
    hojas_vida.config(state="disabled")

    # Asignar las imagenes a los label de los sub frames de p6 -----

    # Obtener las imagenes según el desarrollador
    lista_imagenes = imagenes[contador_click]

    # Redimencionar imagenes
    imagen1_redi = Image.open(lista_imagenes[0]).resize((300,190), Image.LANCZOS)
    imagen2_redi = Image.open(lista_imagenes[1]).resize((300,190), Image.LANCZOS)
    imagen3_redi = Image.open(lista_imagenes[2]).resize((300,190), Image.LANCZOS)
    imagen4_redi = Image.open(lista_imagenes[3]).resize((300,190), Image.LANCZOS)

    # Imagenes redimensionadas
    imagen1 = ImageTk.PhotoImage(imagen1_redi)
    imagen2 = ImageTk.PhotoImage(imagen2_redi)
    imagen3 = ImageTk.PhotoImage(imagen3_redi)
    imagen4 = ImageTk.PhotoImage(imagen4_redi)

    # Actualizar el label con su imagen
    label_p6_tl.config(image = imagen1)
    label_p6_tr.config(image = imagen2)
    label_p6_bl.config(image = imagen3)
    label_p6_br.config(image = imagen4)

     # Almacenar las referencias de las imágenes para evitar que sean recolectadas
    imagenes_labels = [imagen1, imagen2, imagen3, imagen4]

    # Aumentar el indice
    contador_click = (contador_click + 1) % (len(hojas_de_vida))


# Rutas de las imagenes del sistema
rutas_imagen_sistema =["src/imagenes/sistema1.png", "src/imagenes/sistema2.png","src/imagenes/sistema3.png",
                       "src/imagenes/sistema4.png","src/imagenes/sistema5.png"]
salidas_p4 = 1
nueva_imagen = None

def cambiar_imagen_sistema(event):
    global salidas_p4, nueva_imagen

    imagen_siguiente= Image.open(rutas_imagen_sistema[salidas_p4]).resize((603,380), Image.LANCZOS)
    imagen_siguiente = ImageTk.PhotoImage(imagen_siguiente)

    # actualizar imagen
    imagen_sistema.config(image = imagen_siguiente)

    #Referenciar imagen para evitar que sea recolectada
    nueva_imagen = imagen_siguiente

    # Aumenta el indice de salidas
    salidas_p4 = (salidas_p4 + 1) % len(rutas_imagen_sistema)

def abrir_vent_principal():
    vent_inicio.withdraw() #ocultar la ventana de inicio

    vent_principal.abrir_ventana(vent_inicio)

#---------------- MENÚ --------------------

# Crear la barra de menú 
menu_bar = tk.Menu(vent_inicio)

# asociar la barra de menú con la ventana de inicio
vent_inicio.config(menu=menu_bar)

menu_1 = tk.Menu(menu_bar, tearoff=0, font=("Arial",10))
menu_bar.add_cascade(label = "Inicio", menu = menu_1)

menu_1.add_command(label = "Descripción", command = mostrar_descripcion)
menu_1.add_separator()
menu_1.add_command(label = "Salir", command= salir)

# --- -------- Crear los frames principales (p1) y (p2) -----------

# Frame grande izquierdo (p1):
frame_left= tk.Frame(vent_inicio, bg = 'pink', bd = "1", relief = "solid")

# empaquetar el frame izquierdo en la ventana
frame_left.pack(side = "left", padx = 5, pady = 5, expand = True, fill = "both")

# Frame grande derecho (p2):
frame_right= tk.Frame(vent_inicio, bg = 'pink', bd = "1", relief ="solid")

# empaquetar el frame derecho en la ventana
frame_right.pack(side = "left", padx = 5, pady = 5, expand = True, fill = "both")

# ------------------------------------------

# Crear los sub - frames dentro del frame izquiedo (p1):

# frame superior (p3)
frame_left_top = tk.Frame(frame_left, bg = "pink", bd ="1", relief= "solid")

# empaquetar el frame p3 en el frame p1
frame_left_top.pack(side = "top", padx = 5, pady = 5, expand = True, fill = "both")
frame_left_top.pack_propagate(False)  # Evitar que el frame cambie su tamaño con los widgets internos

# frame inferior (p4)
frame_left_bottom = tk.Frame(frame_left,bg = "white", bd ="1", relief= "solid")

# empaquetar el frame p4 en el frame p1                                            #ipady para aumentar la altura
frame_left_bottom.pack(side = "bottom", padx = 5, pady = 5, expand = True, fill = "both", ipady=95)
frame_left_bottom.pack_propagate(False) # Evitar que el frame cambie su tamaño

# crear el botón que va a tener las imagenes del sistema
imagen_sistema = tk.Button(frame_left_bottom, text = "Click para dirigirse a la ventana principal\n",command= abrir_vent_principal,compound= "top",bg = "pink", font=("Arial",11))
imagen_sistema.pack(expand=True, fill= "both")

# Agregar la primera imagen que se visualizará al iniciar
primer_imagen = Image.open("src/imagenes/sistema1.png").resize((603,380), Image.LANCZOS)
primer_imagen = ImageTk.PhotoImage(primer_imagen)
imagen_sistema.config(image = primer_imagen)

# Asignar el evento para que cambie en el momento de que el puntero salga de el Label
imagen_sistema.bind("<Leave>",cambiar_imagen_sistema)

# ------------------------------------------

# crear los sub - frames dentro del frame derecho(p2):

# frame superior (p5)
frame_right_top = tk.Frame(frame_right, bg = "pink", bd ="1", relief= "solid")

#empaquetar el frame p5 en el frame p2
frame_right_top.pack(side = "top", padx = 5, pady = 5, expand = True, fill = "both")
frame_right_top.pack_propagate(False)  # Evitar que el frame cambie su tamaño con los widgets internos

# Crear el widget que va a tener las hojas de vida de los desarrolladores en (p5)
hojas_vida = tk.Text(frame_right_top, bg= "pink", wrap="word", height = 10, width = 40, font=("Arial", 11))
hojas_vida.insert(1.0, "\n\n\n\n\n" + (25*"  ") + "Hojas de vida de los desarrolladores")
hojas_vida.config(state="disabled")
hojas_vida.pack(expand=True, fill="both")
hojas_vida.bind("<Button-1>", actualizar_hojaVida_Imagenes) # asignarle el oyente al evento

# frame inferior (p6)
frame_right_bottom = tk.Frame(frame_right,bg = "pink", bd ="1", relief= "solid")

#empaquetar el frame p6 en el frame p2                                             #ipady para aumentar la altura
frame_right_bottom.pack(side = "bottom", padx = 5, pady = 5, expand = True, fill = "both", ipady = 90 )

# ------------------------------------------

# Configurar las proporciones de las filas y columnas en  p6 (frame_right_bottom) para las 4 fotos de cada desarrollador
frame_right_bottom.grid_rowconfigure(0, weight = 1)  # Fila 0
frame_right_bottom.grid_rowconfigure(1, weight = 1)  # Fila 1
frame_right_bottom.grid_columnconfigure(0, weight = 1)  # Columna 0
frame_right_bottom.grid_columnconfigure(1, weight = 1)  # Columna 1

# Crear los sub-frames de p6:
frame_p6_tl = tk.Frame(frame_right_bottom, bg = "pink", bd = "1", relief = "solid") # superior izquierdo
frame_p6_tr = tk.Frame(frame_right_bottom, bg = "pink", bd = "1", relief = "solid") # superior derecho
frame_p6_bl = tk.Frame(frame_right_bottom, bg = "pink", bd = "1", relief = "solid") # inferior izquierdo
frame_p6_br = tk.Frame(frame_right_bottom, bg = "pink", bd = "1", relief = "solid") # inferior derecho

# Evitar que los sub-frames cambien de tamaño con sus contenidos
frame_p6_tl.pack_propagate(False)
frame_p6_tr.pack_propagate(False)
frame_p6_bl.pack_propagate(False)
frame_p6_br.pack_propagate(False)

# Agregar los sub-frames a su cuadrícula en p6
frame_p6_tl.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
frame_p6_tr.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
frame_p6_bl.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
frame_p6_br.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

# crear los label que contendran las imagenes en los sub-frames de p6

label_p6_tl= tk.Label(frame_p6_tl, bg = "pink")
label_p6_tl.pack(expand = True, fill= "both", padx=2, pady=2)

label_p6_tr= tk.Label(frame_p6_tr, bg = "pink")
label_p6_tr.pack(expand = True, fill= "both", padx=2, pady=2)

label_p6_bl= tk.Label(frame_p6_bl, bg = "pink")
label_p6_bl.pack(expand = True, fill= "both", padx=2, pady=2)

label_p6_br= tk.Label(frame_p6_br, bg = "pink")
label_p6_br.pack(expand = True, fill= "both", padx=2, pady=2)

# mostrar la venta y sus componentes
mostrar_bienvenida()  # Mostrar el texto de bienvenida al iniciar la aplicación
vent_inicio.mainloop()
