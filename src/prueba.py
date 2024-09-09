import tkinter as tk
from PIL import Image, ImageTk

# Lista de hojas de vida y rutas de imágenes
hojas_de_vida = [
    "Oky Ruiz De La Rosa, 18 años, de San Andrés de Sotavento Córdoba "
    "estudiante de ingeniería de sistemas e informática en la Universidad Nacional de Colombia",
    "Salomé Murillo Gaviria, xx años, de Medellín Antioquia "
    "estudiante de ingeniería de sistema en la universidad nacional de Colombia", 
    "Daniel Zapata, xx años, de Medellín Antioquia "
    "estudiante de ingeniería de sistema en la universidad nacional de Colombia",
    "Nicolas Zambrano, xx años, de Medellín Antioquia "
    "estudiante de ingeniería de sistema en la universidad nacional de Colombia"
]

imagenes = [
    "src/imagenes/Oky1.png", "src/imagenes/Oky2.png", "src/imagenes/Oky3.png", "src/imagenes/Oky4.png",
    "src/imagenes/Daniel1.png", "src/imagenes/Daniel2.png", "src/imagenes/Daniel3.png", "src/imagenes/Daniel4.png",
    "src/imagenes/Salome1.png", "src/imagenes/Salome2.png", "src/imagenes/Salome3.png", "src/imagenes/Salome4.png",
    "src/imagenes/Nico1.png", "src/imagenes/Nico2.png", "src/imagenes/Nico3.png", "src/imagenes/Nico4.png"
]

indice_actual = 0  # Para rastrear el índice actual

def actualizar_hoja_vida_y_imagenes(event):
    global indice_actual

    # Actualizar el texto del widget de hojas de vida
    hojas_vida.config(state="normal")
    hojas_vida.delete("1.0", tk.END)
    hojas_vida.insert("1.0", hojas_de_vida[indice_actual])
    hojas_vida.config(state="disabled")

    # Sub-frames de p6
    sub_frames = [frame_p6_tl, frame_p6_tr, frame_p6_bl, frame_p6_br]
    
    for i, frame in enumerate(sub_frames):
        # Limpiar cualquier widget previo
        for widget in frame.winfo_children():
            widget.destroy()
        
        # Obtener las dimensiones actuales del frame
        frame.update_idletasks()  # Asegurar que las dimensiones estén actualizadas
        frame_width = frame.winfo_width()
        frame_height = frame.winfo_height()
        
        # Cargar y redimensionar la imagen
        img_path = imagenes[indice_actual * 4 + i]
        img = Image.open(img_path)
        img = img.resize((frame_width, frame_height), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        
        # Crear el Label para la imagen y empacarlo
        lbl = tk.Label(frame, image=photo, bd=0)
        lbl.image = photo  # Mantener referencia de la imagen
        lbl.pack(expand=True, fill="both")

    # Incrementar el índice actual y volver al inicio si llega al final
    indice_actual = (indice_actual + 1) % len(hojas_de_vida)

# Crear la ventana de inicio y la estructura general
vent_inicio = tk.Tk()
vent_inicio.config(padx=5, pady=5)

# Frame grande derecho (p2):
frame_right = tk.Frame(vent_inicio, bg="white", bd="1", relief="solid")
frame_right.pack(side="left", padx=5, pady=5, expand=True, fill="both")

# Frame superior derecho (p5):
frame_right_top = tk.Frame(frame_right, bg="white", bd="1", relief="solid")
frame_right_top.pack(side="top", padx=5, pady=5, expand=True, fill="both")
frame_right_top.pack_propagate(False)

# Crear el widget de texto que mostrará las hojas de vida
hojas_vida = tk.Text(frame_right_top, background="pink", wrap="word", height=10, width=40, font=("Arial", 11))
hojas_vida.insert("1.0", "\n\n\n\n\n\n" + (25 * "  ") + "Hojas de vida de los desarrolladores")
hojas_vida.config(state="disabled")
hojas_vida.pack(expand=True, fill="both")
hojas_vida.bind("<Button-1>", actualizar_hoja_vida_y_imagenes)

# Frame inferior derecho (p6)
frame_right_bottom = tk.Frame(frame_right, bg="white", bd="1", relief="solid")
frame_right_bottom.pack(side="bottom", padx=5, pady=5, expand=True, fill="both", ipady=50)
frame_right_bottom.grid_rowconfigure(0, weight=1)
frame_right_bottom.grid_rowconfigure(1, weight=1)
frame_right_bottom.grid_columnconfigure(0, weight=1)
frame_right_bottom.grid_columnconfigure(1, weight=1)

# Crear los sub-frames en p6
frame_p6_tl = tk.Frame(frame_right_bottom, bg="lightblue", bd="1", relief="solid")  # superior izquierdo
frame_p6_tr = tk.Frame(frame_right_bottom, bg="lightgreen", bd="1", relief="solid")  # superior derecho
frame_p6_bl = tk.Frame(frame_right_bottom, bg="pink", bd="1", relief="solid")  # inferior izquierdo
frame_p6_br = tk.Frame(frame_right_bottom, bg="orange", bd="1", relief="solid")  # inferior derecho

# Evitar que los frames cambien de tamaño con los widgets internos
for sub_frame in [frame_p6_tl, frame_p6_tr, frame_p6_bl, frame_p6_br]:
    sub_frame.grid_propagate(False)

# Posicionar los sub-frames en la cuadrícula de p6
frame_p6_tl.grid(row=0, column=0, padx=2, pady=2, sticky="nsew")
frame_p6_tr.grid(row=0, column=1, padx=2, pady=2, sticky="nsew")
frame_p6_bl.grid(row=1, column=0, padx=2, pady=2, sticky="nsew")
frame_p6_br.grid(row=1, column=1, padx=2, pady=2, sticky="nsew")

vent_inicio.mainloop()
