# ventana2.py
import tkinter as tk

def cerrar_ventana(ventana_2, ventana_1):
    ventana_2.destroy()  # Cerrar la ventana 2
    ventana_1.deiconify()  # Mostrar nuevamente la ventana 1

def abrir_ventana(ventana_1):
    ventana_2 = tk.Toplevel(ventana_1)  # Crear una ventana secundaria
    ventana_2.title("Ventana 2")

    # Botón para cerrar la Ventana 2 y restaurar la Ventana 1
    boton_cerrar = tk.Button(ventana_2, text="Cerrar Ventana 2", command=lambda: cerrar_ventana(ventana_2, ventana_1))
    boton_cerrar.pack(padx=20, pady=20)

