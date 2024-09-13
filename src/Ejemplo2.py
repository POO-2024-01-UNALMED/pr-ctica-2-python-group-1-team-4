import tkinter as tk
from tkinter import Entry, messagebox
from FieldFrame import FieldFrame

# Ventana 
ventana = tk.Tk()
ventana.title("Uso del FieldFrame")
ventana.geometry("300x315")


# Creación de un objeto Field Frame

listaCampos = ["Nombre", "Cédula", "Dirección",  "Sexo"]
listaEditables = [True, True, False, True]
listaValores = ["Fulanito", "3303022", "Hola", "Nunca"]
combobox_items = {"Sexo": ["Masculino", "Femenino", "Otro"]}



frame = FieldFrame(ventana, "Persona" ,listaCampos, "Sus datos", listaEditables, listaValores, combobox_items)
frame.place(x=10, y=10)


ventana.mainloop()

# ----------------------------------------
