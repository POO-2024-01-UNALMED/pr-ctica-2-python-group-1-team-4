# ventana1.py

import tkinter as tk
import ventana2  # Importamos el segundo módulo

ventana_1 = tk.Tk()
ventana_1.title("Ventana 1")

def abrir_ventana2():
    ventana_1.withdraw()  # Ocultar la ventana 1
    ventana2.abrir_ventana(ventana_1)  # Llamar a la función en ventana2.py para abrir la segunda ventana

# Botón para abrir la Ventana 2
boton_abrir = tk.Button(ventana_1, text="Abrir Ventana 2", command=abrir_ventana2)
boton_abrir.pack(padx=20, pady=20)

ventana_1.mainloop()

