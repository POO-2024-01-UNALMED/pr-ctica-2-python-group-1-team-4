import tkinter as tk
from tkinter import*
from tkinter import ttk
from tkinter import messagebox

class FieldFrame(Frame):
    
    # CONSTRUCTOR FIELDFRAME
    def __init__(self, frame_principal, titulo_campos, campos, titulo_entradas, habilatado,tipos_esperados=None, Valores = None, combobox = None ):
        #CONTRUCTOR DEL FRAME PADRE
        super().__init__(frame_principal, height= 800 , width= 1000, bg ="thistle1", highlightbackground="purple4", highlightthickness=2,)

        self.titulo_campos = titulo_campos  # titulo criterios
        self.campos = campos # nombre de cada campo
        self.titulo_entradas = titulo_entradas # tirulo de las entradas
        self.habilitado = habilatado # 
        self.valores = Valores # valores por defecto de las entradas
        self.combobox_items = combobox or {}

        self.tipos_esperados = tipos_esperados or {}  # Diccionario con los tipos esperados por campo
        self.entradas = [] # Lista que guarda las entradas

        # CREAR Y EMPAQUETAR LABELS DE LOS TITULOS
        Label_titulo_criterios = tk.Label(self, text = self.titulo_campos, font=("Lucida Handwriting", 11, "bold"), fg = "purple4", bg = "plum1")
        Label_titulo_criterios.grid(row=0, column=0, padx=5, pady=10)
        
        Label_titulo_entradas = tk.Label(self, text = self.titulo_entradas, font=("Lucida Handwriting", 11, "bold"), fg = "purple4", bg = "plum1")
        Label_titulo_entradas.grid(row=0, column=1, padx=5, pady=10)
        
        for i in range(0, len(self.campos)):

            # LABEL CRITERIOS
            label_criterio = tk.Label(self, text=self.campos[i], font=("Times New Roman",10), bg="plum3", fg="purple")
            label_criterio.grid(row=i+1, column=0, padx= 350, pady=15)

            #CAMPOS DE TEXTO ENTRADAS
            if self.campos[i] in self.combobox_items:
                entradaValor = ttk.Combobox(self, values=self.combobox_items[campos[i]], state="readonly")
                entradaValor.grid(row=i+1, column=1, padx=5, pady=5)
                if self.valores is not None:
                    entradaValor.set(self.valores[i])

            else:
                entradaValor = tk.Entry(self)
                entradaValor.grid(column=1, row=i+1, padx = 5, pady = 5)
                if self.valores is not None:
                    entradaValor.insert(0, self.valores[i])

                if self.habilitado is not None and not self.habilitado[i]:
                    entradaValor.configure(state=tk.DISABLED)
            
            self.entradas.append(entradaValor)

        # BOTÓN ACEPTAR 
        self.boton_aceptar = tk.Button(self, text="aceptar", font=("Verdana", 10), bg="white", width=6, height=1)
        self.boton_aceptar.grid(column=1, row=len(self.campos)+1)

        # BOTÓN LIMPIAR
        tk.Button(self, text="Limpiar", font=("Verdana", 10), bg="white", width=6, height=1, command=self.funborrar).grid(column=0, row=len(self.campos)+1)


    def funborrar(self):
        for entrada in self.entradas:
            entrada.delete("0", "end")

    def funAceptar(self, funcion):
        self.boton_aceptar.config(command=funcion)

    def getValue(self, Criterio):
        index = self.campos.index(Criterio)
        return self.entradas[index].get()
    
    def getEntradas(self):
        listaValores = []
        listaVacios = ""
        for i in range(0, len(self.campos)):
            if self.habilitado[i] == True:
                valor = self.getValue(self.campos[i])
                if valor == "":
                    listaVacios += " " + (self.campos[i])
                else:
                    # Validar el tipo de dato esperado
                    tipo_esperado = self.tipos_esperados.get(self.campos[i], str)
                    if not self.validar_tipo(valor, tipo_esperado):
                        messagebox.showerror("Error", f"El campo {self.campos[i]} debe ser de tipo {tipo_esperado.__name__}.")
                        return False
                    listaValores.append(valor)

        if (len(listaVacios)>0):
            messagebox.showerror("Error","Hay entradas sin llenar: " + listaVacios)
            return False
        else:
            for i in listaValores:
                print(i)
            return listaValores
    
    def validar_tipo(self, valor, tipo_esperado):
        try:
            tipo_esperado(valor)
            return True
        except ValueError:
            return False
                                      
# -----------------------------------------------------
