import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class FieldFrame(Frame):
    
    # CONSTRUCTOR FIELDFRAME
    def __init__(self, frame_principal, titulo_campos, lista_criterios, titulo_entradas, lista_habilitados, tipos_esperados=None, Valores=None, combobox=None):
        # CONSTRUCTOR DEL FRAME PADRE
        super().__init__(frame_principal, bg="thistle1", highlightbackground="purple4", highlightthickness=2)
        self.titulo_campos = titulo_campos  # Título de criterios
        self.lista_criterios = lista_criterios # Nombres de cada criterio
        self.titulo_entradas = titulo_entradas # Título de las entradas
        self.lista_habilitados = lista_habilitados
        self.lista_valores = Valores # Lista de valores por defecto de las entradas
        self.combobox_items = combobox or {}

        self.tipos_esperados = tipos_esperados or {}  # Diccionario con los tipos esperados por campo
        self.lista_entradas = [] # Lista que guarda las Entrys o comboboxes

        # CREAR Y EMPAQUETAR LABELS DE LOS TITULOS
        Label_titulo_criterios = tk.Label(self, text=self.titulo_campos, font=("Lucida Handwriting", 11, "bold"), fg="purple4", bg="plum1")
        Label_titulo_criterios.grid(row=0, column=0, padx=5, pady=10)
        
        Label_titulo_entradas = tk.Label(self, text=self.titulo_entradas, font=("Lucida Handwriting", 11, "bold"), fg="purple4", bg="plum1")
        Label_titulo_entradas.grid(row=0, column=1, padx=5, pady=10)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        for i in range(len(self.lista_criterios)):
            # LABEL CRITERIOS
            label_criterio = tk.Label(self, text=self.lista_criterios[i], font=("Times New Roman", 10), bg="plum3", fg="purple")
            label_criterio.grid(row=i+1, column=0, padx=5, pady=15)

            # CAMPOS DE TEXTO ENTRADAS
            if self.lista_criterios[i] in self.combobox_items:
                entradaValor = ttk.Combobox(self, values=self.combobox_items[self.lista_criterios[i]], state="readonly")
                entradaValor.grid(row=i+1, column=1, padx=5, pady=10,sticky= "ns")
                if self.lista_valores is not None:
                    entradaValor.set(self.lista_valores[i])
            else:
                entradaValor = tk.Entry(self)
                entradaValor.grid(row=i+1, column=1, padx=5, pady=5)
                if self.lista_valores is not None:
                    entradaValor.insert(0, self.lista_valores[i])

                if self.lista_habilitados is not None and not self.lista_habilitados[i]:
                    entradaValor.configure(state=tk.DISABLED)
            
            self.lista_entradas.append(entradaValor)

        # BOTÓN ACEPTAR 
        self.boton_aceptar = tk.Button(self, text="Aceptar", font=("Verdana", 10), bg="white", width=6, height=1)
        self.boton_aceptar.grid(row=len(self.lista_criterios)+1, column=1, padx=5, pady=10)

        # BOTÓN LIMPIAR
        tk.Button(self, text="Limpiar", font=("Verdana", 10), bg="white", width=6, height=1, command=self.funborrar).grid(row=len(self.lista_criterios)+1, column=0, padx=5, pady=10)

        self.grid_rowconfigure(len(self.lista_criterios)+1, weight=1)

    def funborrar(self):
        for entrada in self.lista_entradas:
            if isinstance(entrada, ttk.Combobox):  # Si es un Combobox
                entrada.set('')  # Restablecer el combobox
            else:
                entrada.delete("0", "end")  # Borrar entradas normales

    def funAceptar(self, funcion):
        self.boton_aceptar.config(command=funcion)

    def getValue(self, Criterio):
        index = self.lista_criterios.index(Criterio)
        return self.lista_entradas[index].get()
    
    def getEntradas(self):
        listaValores = []
        listaVacios = ""
        for i in range(len(self.lista_criterios)):
            if self.lista_habilitados[i] == True:
                valor = self.getValue(self.lista_criterios[i])
                if valor == "":
                    listaVacios += " " + (self.lista_criterios[i])
                else:
                    # Validar el tipo de dato esperado
                    tipo_esperado = self.tipos_esperados.get(self.lista_criterios[i], str)
                    if not self.validar_tipo(valor, tipo_esperado):
                        messagebox.showerror("Error", f"El campo {self.lista_criterios[i]} debe ser de tipo {tipo_esperado.__name__}.")
                        return False
                    listaValores.append(valor)

        if len(listaVacios) > 0:
            messagebox.showerror("Error", "Hay entradas sin llenar: " + listaVacios)
            return False
        else:
            return listaValores
    
    def validar_tipo(self, valor, tipo_esperado):
        try:
            tipo_esperado(valor)
            return True
        except ValueError:
            return False
