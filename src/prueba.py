import tkinter as tk

# Crear la ventana
vent_inicio = tk.Tk()
vent_inicio.geometry("1100x500")
vent_inicio.config(padx = 100, pady = 100)

# Frame grande inferior (p4)
frame_left_bottom = tk.Frame(vent_inicio, bg="thistle1")
frame_left_bottom.pack(side="top", padx=5, pady=5, expand=True, fill="both")

# Crear el botón con la imagen
imagen_sistema = tk.Button(
    frame_left_bottom, 
    text="Click para ingresar al sistema\n", 
    bg="thistle1", 
    command=lambda: print("Abriendo sistema..."), 
    compound="top", 
    font=("Times New Roman", 14), 
    fg="purple4",
    width=10,  # Definir un ancho máximo
    height=10  # Definir un alto máximo
)

# Cargar la imagen usando PhotoImage de Tkinter
imagen1 = tk.PhotoImage(file="src/imagenes/sistema1.png")

# Configurar la imagen en el botón
imagen_sistema.config(image=imagen1)

# Empaquetar el botón
imagen_sistema.pack(expand=True, fill="both")

# Guardar la referencia de la imagen
imagen_sistema.image = imagen1

vent_inicio.mainloop()
