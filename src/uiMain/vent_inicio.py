import tkinter as tk 
from PIL import Image, ImageTk  # IMPORTAR MÓDULOS DE pillow PARA REDIMENSIONAR IMAGENES
import vent_principal 

# CREAMOS LA VENTANA DE INICIO
vent_inicio = tk.Tk()

# ASIGNAR TITULO, DIMENSIONES INICIALES Y COLOR DE FONDO.
vent_inicio.title("AdoptaLove")
vent_inicio.geometry("1400x800")
vent_inicio.configure(bg='LightBlue1') 

vent_inicio.config(padx = 3, pady = 3) # Establecer el espacio entre los bordes de la ventana y los widgets que contenga

#  -------------------- EVENTOS -------------------------

def mostrar_bienvenida():

    # CREAR Y ACTUALIZAR EL TEXTO EN EL frame_left_top (p3) con la bienvenida inicial
    bienvenida = (
        "\n¡Bienvenido a AdoptaLove! \n\n"
        "Estamos encantados de que estés aquí. Este es un centro integral para el cuidado de mascotas, "
        "donde puedes encontrar una variedad de servicios y productos para el bienestar de tus amigos peludos. "
        "Explora nuestras opciones y si tienes alguna pregunta, no dudes en contactarnos."
    )

    # LIMPIAR CUALQUIER TEXTO PREVIO SI EXISTE
    for widget in frame_left_top.winfo_children():
        widget.destroy()

    # CREAR EL TEXT PARA MOSTRAR LA BIENVENIDA
    text_bienvenida = tk.Text(frame_left_top, bg = "thistle1", wrap = "word",font = ("Times New Roman", 13), fg= "purple")
    text_bienvenida.tag_configure("center", justify= "center") # justificar centrado
    text_bienvenida.insert("1.0", bienvenida)
    text_bienvenida.tag_add("center", "1.0", "end")
    text_bienvenida.config(state = "disabled")  # Hacer el Text de solo lectura
    text_bienvenida.pack(expand=True, fill = "both")

def mostrar_descripcion():

    # CREAR Y ACTUALIZAR EL TEXTO EN EL frame_left_top (p3) CUANDO SE SELECCIONE LA OPCIÓN "DESCRIPCION" EN EL MENÚ INICIO
    descripcion = (
        "AdoptaLove es un centro integral para el cuidado de mascotas que ofrece una "
        "variedad de servicios y productos diseñados para satisfacer las necesidades de los animales "
        "y sus dueños. Su objetivo principal es facilitar y promover la adopción responsable de "
        "mascotas, conectando de manera efectiva a animales en busca de un hogar con personas "
        "interesadas en brindarles amor y cuidado. \n"
        "AdoptaLove también proporciona atención veterinaria, peluquería y guardería para mascotas, "
        "asegurando el bienestar y la comodidad de los animales. Para complementar la oferta, "
        "cuenta con tiendas donde los dueños pueden adquirir productos esenciales"
        "para el cuidado de sus mascotas."
    )

     # LIMPIAR CUALQUIER TEXTO PREVIO SI EXISTE
    for widget in frame_left_top.winfo_children():
        widget.destroy()
    
    #  CREAR EL TEXT PARA MOSTRAR LA DESCRIPCIÓN
    text_descripcion = tk.Text(frame_left_top, bg = "thistle1", wrap="word", height=10, width=40, font = ("Times New Roman", 13), fg= "purple")
    text_descripcion.tag_configure("center", justify= "center") # 
    text_descripcion.insert("1.0", descripcion)
    text_descripcion.tag_add("center", "1.0", "end")
    text_descripcion.config(state = "disabled")  # Hacer el Text de solo lectura
    text_descripcion.pack(expand=True, fill="both")

def salir():

    # CERRAR LA VENTANA CUANDO SE SELECCIONE LA OPCIÓN "SALIR" EN EL MENÚ INICIO
    vent_inicio.quit()


# HOJAS DE VIDA DE LOS DESARROLLADORES
descripcion_desarrolladores = ["Oky Ruiz De La Rosa, 18 años, de San Andrés de Sotavento Córdoba "
                 "estudiante de ingeniería de sistemas e informática en la Universidad Nacional "
                 "de Colombia",

                 "Salomé Murillo Gaviria, xx años, de medellín Antioquia "
                 "estudiante de ingeniería de sistemas en la Universidad nacional de Colombia", 

                 "Daniel Zapata, xx años, de medellín Antioquia "
                 "estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia",

                 "Nicolas Zambrano, xx años, de medellín Antioquia "
                 "estudiante de ingeniería de sistemas en la Universidad Nacional de Colombia"]

# RUTAS DE LAS IMAGENES DE LOS DESARROLLADORES
imagenes_desarrolladores = [["src/imagenes/Oky1.png","src/imagenes/Oky2.png","src/imagenes/Oky3.png","src/imagenes/Oky4.png"],
            ["src/imagenes/Salome1.png","src/imagenes/Salome2.png","src/imagenes/Salome3.png","src/imagenes/Salome4.png"],
            ["src/imagenes/Daniel1.png","src/imagenes/Daniel2.png","src/imagenes/Daniel3.png","src/imagenes/Daniel4.png"],
            ["src/imagenes/Nico1.png", "src/imagenes/Nico2.png","src/imagenes/Nico3.png", "src/imagenes/Nico4.png"]]

# DECLARAR LAS VARIABLES GLOBALES PARA ALMACENAR LAS REFERENCIA DE LAS IMÁGENES Y EL CONTADOR DE CLICK´S EN P5 (frame_right_top)
imagenes_labels = []
contador_click = 0

def actualizar_hojaVida_Imagenes(event):
    global contador_click, imagenes_labels

    # CAMBIAR EL CONTENIDO DEL Text EN P5 (frame_right_top)
    hojas_vida.config(state= 'normal')
    hojas_vida.delete(1.0, 'end')
    hojas_vida.tag_configure("center", justify='center')
    hojas_vida.insert(1.0,"\n" + descripcion_desarrolladores[contador_click])
    hojas_vida.tag_add("center", "1.0", "end")
    hojas_vida.config(state="disabled")

    # ASIGNAR LAS IMAGENES_DESARROLLADORES A LOS LABEL DE LOS SUB FRAME DE P6 (frame_right_bottom) ----

    # OBTENER LAS IMAGENES_DESARROLLADORES SEGÚN EL DESARROLLADOR
    lista_imagenes = imagenes_desarrolladores[contador_click]

    # REDIMENSIONAR IMAGENES
    imagen1 = ImageTk.PhotoImage(Image.open(lista_imagenes[0]).resize((300,197), Image.LANCZOS))
    imagen2 = ImageTk.PhotoImage(Image.open(lista_imagenes[1]).resize((300,197), Image.LANCZOS))
    imagen3 = ImageTk.PhotoImage(Image.open(lista_imagenes[2]).resize((300,198), Image.LANCZOS))
    imagen4 = ImageTk.PhotoImage(Image.open(lista_imagenes[3]).resize((300,198), Image.LANCZOS))

    #ASIGAR CADA IMAGEN A SU LABEL
    label_p6_tl.config(image = imagen1)
    label_p6_tr.config(image = imagen2)
    label_p6_bl.config(image = imagen3)
    label_p6_br.config(image = imagen4)

    # ALMACENAR LAS REFERENCIAS DE LAS IMAGENES PARA EVITAR QUE SEAN RECOLECTADAS(GC)
    imagenes_labels = [imagen1, imagen2, imagen3, imagen4]
    
    #AUMENTAR EL INDICE CONTADOR DE LOS CLICK'S
    contador_click = (contador_click + 1) % (len(descripcion_desarrolladores))

#RUTAS DE LAS IMAGENES DEL SISTEMA
rutas_imagen_sistema =["src/imagenes/sistema1.png", "src/imagenes/sistema2.png","src/imagenes/sistema3.png",
                       "src/imagenes/sistema4.png","src/imagenes/sistema5.png"]

salidas_p4 = 1 # CONTADOR DE LAS VECES QUE EL CURSOR SALE DE P4
nueva_imagen = None # VARIABLE PARA EVITAR QUE LA IMAGEN SEA RECOLECTADA

def cambiar_imagen_sistema(event):
    global salidas_p4, nueva_imagen

    imagen_siguiente= Image.open(rutas_imagen_sistema[salidas_p4]).resize((603,380), Image.LANCZOS)
    imagen_siguiente = ImageTk.PhotoImage(imagen_siguiente)

    # ACTUALIZAR IMAGEN
    imagen_sistema.config(image = imagen_siguiente)

    # REFERENCIAR IMAGEN PARA EVITAR QUE SEA RECOLECTADA
    nueva_imagen = imagen_siguiente

    # AUMENTA EL INDICE DE LAS SALIDAS
    salidas_p4 = (salidas_p4 + 1) % len(rutas_imagen_sistema)



def abrir_vent_principal():

    # OCULTAR LA VENTANA DE INICIO Y ABRIR LA VENTANA PRINCIPAL

    vent_inicio.withdraw() #ocultar la ventana de inicio
    vent_principal.abrir_ventana(vent_inicio)


#  ---------------- MENÚ --------------------

# CREAR LA BARRA DE MENÚ
menu_bar = tk.Menu(vent_inicio)

# ASOCIAR LA BARRA DE MENÚ CON LA VENTANA PRINCIPAL
vent_inicio.config(menu=menu_bar)

menu_1 = tk.Menu(menu_bar, tearoff=0, font=("Arial", 9))
menu_bar.add_cascade(label = "Inicio", menu = menu_1)

menu_1.add_command(label = "Descripción", command = mostrar_descripcion)
menu_1.add_separator()
menu_1.add_command(label = "Salir", command= salir)


# ------------- CREAR LOS FRAMES PRINCIPALES (P1) Y (P2) -----------


# CREAR Y EMPAQUETAR FRAME GRANDE IZQUIERDO (P1) EN LA VENTANA:
frame_left= tk.Frame(vent_inicio, bg = '#B89AD6')

frame_left.pack(side = "left", padx = 5, pady = 5, expand = True, fill = "both")

# CREAR Y EMPAQUETAR FRAME GRANDE DERECHO (P2) EN LA VENTANA:
frame_right= tk.Frame(vent_inicio, bg = '#B89AD6')

frame_right.pack(side = "left", padx = 5, pady = 5, expand = True, fill = "both")

# ------------------------------------------------------------------

# CREAR LOS SUB FRAMES DENTRO DEL FRAME IZQUIERDO (P1)

# CREAR Y EMPAQUETAR EL FRAME SUPERIOR (P3) DE (P1)
frame_left_top = tk.Frame(frame_left, bg = "thistle1", highlightbackground="purple4", highlightthickness=2)

frame_left_top.pack(side = "top", padx = 5, pady = 5, expand = True, fill = "both")
frame_left_top.pack_propagate(False)  # Evitar que el frame cambie su tamaño con los widgets internos

#CREAR Y EMPAQUETAR EL FRAME SUPERIOR (P4) DE (P1)
frame_left_bottom = tk.Frame(frame_left,bg = "thistle1", highlightbackground="purple4", highlightthickness=2)
                    
frame_left_bottom.pack(side = "bottom", padx = 5, pady = 5, expand = True, fill = "both", ipady=105) #ipady para aumentar la altura
frame_left_bottom.pack_propagate(False) # Evitar que el frame cambie su tamaño

# CREAR EL BOTÓN QUE VA A TENER LAS IMAGENES_DESARROLLADORES DEL SISTEMA
imagen_sistema = tk.Button(frame_left_bottom, text = "Click para ingresar al sistema\n", bg = "thistle1", command= abrir_vent_principal, compound= "top", font = ("Times New Roman", 14), fg= "purple4")
imagen_sistema.pack(expand=True, fill= "both")

# AGREGAR LA PRIMERA IMAGEN QUE SE VISUALIZARÁ AL INICIAR 
primer_imagen = Image.open("src/imagenes/sistema1.png").resize((610,380), Image.LANCZOS)
primer_imagen = ImageTk.PhotoImage(primer_imagen)
imagen_sistema.config(image = primer_imagen)

# ASIGNAR EL EVENTO PARA QUE CAMBIE EN EL MOMENTO DE QUE EL PUNTERO SALGA EN EL LABEL
imagen_sistema.bind("<Leave>",cambiar_imagen_sistema)

# ------------------------------------------

# CREAR LOS SUB FRAMES DENTRO DEL FRAME DERECHO (P2)

# CREAR Y EMPAQUETAR EL FRAME SUPERIOR (P5) EN P1
frame_right_top = tk.Frame(frame_right, bg = "thistle1", highlightbackground="purple4", highlightthickness=2, highlightcolor="purple4")

frame_right_top.pack(side = "top", padx = 5, pady = 5, expand = True, fill = "both")
frame_right_top.pack_propagate(False)  # Evitar que el frame cambie su tamaño con los widgets internos

# CREAR EL TEXT QUE VA A TENER LAS HOJAS DE VIDA DE LOS DESARROLLADORES EN (P5)
hojas_vida = tk.Text(frame_right_top, bg= "thistle1", wrap="word", height = 10, width = 40, font = ("Times New Roman", 13), fg= "purple")
hojas_vida.pack(expand=True, fill="both")
hojas_vida.tag_configure("center", justify='center')

# DARLE UN TEXTO INICIAL
hojas_vida.insert("1.0", "\n\n\n    Click para acceder a información sobre los desarrolladores")
hojas_vida.tag_add("center", "1.0", "end")
hojas_vida.config(state="disabled")
hojas_vida.bind("<Button-1>", actualizar_hojaVida_Imagenes) # asignarle el oyente al evento


# CREAR Y EMPAQUETAR EL FRAME INFERIOR (P6) EN P2
frame_right_bottom = tk.Frame(frame_right,bg = "thistle1", highlightbackground="purple4", highlightthickness=2)
frame_right_bottom.pack(side = "bottom", padx = 5, pady = 5, expand = True, fill = "both", ipady = 120 ) #ipady para aumentar la altura

# ------------------------------------------

# CONFIGURAR LAS PROPORCIONES DE LAS FILAS Y COLUMNAS EN P6 (frame_right_bottom) PARA LAS 4 FOTOS DE CADA DESARROLLADOR
frame_right_bottom.grid_rowconfigure(0, weight = 1)  # Fila 0
frame_right_bottom.grid_rowconfigure(1, weight = 1)  # Fila 1
frame_right_bottom.grid_columnconfigure(0, weight = 1)  # Columna 0
frame_right_bottom.grid_columnconfigure(1, weight = 1)  # Columna 1

# CREAR LOS SUB - FRAMES DE P6
frame_p6_tl = tk.Frame(frame_right_bottom, bg = "white", highlightbackground="MediumOrchid1", highlightthickness=3) # superior izquierdo
frame_p6_tr = tk.Frame(frame_right_bottom, bg = "white", highlightbackground="MediumOrchid1", highlightthickness=3) # superior derecho
frame_p6_bl = tk.Frame(frame_right_bottom, bg = "white", highlightbackground="MediumOrchid1", highlightthickness=3) # inferior izquierdo
frame_p6_br = tk.Frame(frame_right_bottom, bg = "white", highlightbackground="MediumOrchid1", highlightthickness=3) # inferior derecho

# EVITAR QUE LOS SUB FRAME CAMBIEN DE TAMAÑO
frame_p6_tl.pack_propagate(False)
frame_p6_tr.pack_propagate(False)
frame_p6_bl.pack_propagate(False)
frame_p6_br.pack_propagate(False) 

# AGREGAR LOS SUBFRAMES A SU CUADRICULA CORRESPONDIENTE EN P6
frame_p6_tl.grid(row=0, column=0, padx=4, pady=4, sticky="nsew")
frame_p6_tr.grid(row=0, column=1, padx=4, pady=4, sticky="nsew")
frame_p6_bl.grid(row=1, column=0, padx=4, pady=4, sticky="nsew")
frame_p6_br.grid(row=1, column=1, padx=4, pady=4, sticky="nsew")

# CREAR LOS LABEL QUE CONTENDRAN LAS IMAGENES_DESARROLLADORES EN LOS SUB_FRAMES DE P6
label_p6_tl= tk.Label(frame_p6_tl, bg = "pink")
label_p6_tl.pack(expand = True, fill= "both")

label_p6_tr= tk.Label(frame_p6_tr, bg = "pink")
label_p6_tr.pack(expand = True, fill= "both")

label_p6_bl= tk.Label(frame_p6_bl, bg = "pink")
label_p6_bl.pack(expand = True, fill= "both")

label_p6_br= tk.Label(frame_p6_br, bg = "pink")
label_p6_br.pack(expand = True, fill= "both")

#CREAR LAS PRIMERA IMAGENES DE LOS 4 DESARROLLADORES
imagen_tl = ImageTk.PhotoImage(Image.open("src/imagenes/Oky1.png").resize((300,197), Image.LANCZOS))
imagen_tr = ImageTk.PhotoImage(Image.open("src/imagenes/Salome1.png").resize((300,197), Image.LANCZOS))
imagen_bl = ImageTk.PhotoImage(Image.open("src/imagenes/Nico1.png").resize((300,197), Image.LANCZOS))
imagen_br = ImageTk.PhotoImage(Image.open("src/imagenes/Daniel1.png").resize((300,197), Image.LANCZOS))

# # AGREGAR CADA IMAGEN A SU LABEL CORRESPONDIENTE
label_p6_tl.config(image=imagen_tl)
label_p6_tr.config(image=imagen_tr)
label_p6_bl.config(image=imagen_bl)
label_p6_br.config(image=imagen_br)

# mostrar la venta y sus componentes
mostrar_bienvenida()  # Mostrar el texto de bienvenida al iniciar la aplicación
vent_inicio.mainloop()
