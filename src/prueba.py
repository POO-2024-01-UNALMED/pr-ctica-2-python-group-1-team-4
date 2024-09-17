import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Mascotas")

# Crear el frame donde se van a ubicar los labels
frame = tk.Frame(root)
frame.pack(expand=True, fill='both')

# Configurar el frame para que las columnas se expandan de manera uniforme
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)

# Crear y ubicar los labels de manera centrada usando grid
label_mascota1 = tk.Label(frame, text="Mascota1",font= ("Times New Roman",12),bg = "pink")
label_mascota1.grid(row=0, column=0, padx=10, pady=10, sticky="e")  # Alinear a la derecha (east)

label_nombre1 = tk.Label(frame, text="Nombre1 mi nombre es oky ruiz de la rosa y tengo 2 años", font= ("Times New Roman",12))
label_nombre1.grid(row=0, column=1, padx=10, pady=10, sticky="w")  # Alinear a la izquierda (west)

label_mascota2 = tk.Label(frame, text="Mascota2", bg = "pink", font= ("Times New Roman",12))
label_mascota2.grid(row=1, column=0, padx=10, pady=10, sticky="e")

label_nombre2 = tk.Label(frame, text="Nombre2 la verdad no se que decir", font= ("Times New Roman",12))
label_nombre2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

# Iniciar el bucle principal de la aplicación
root.mainloop()

