import tkinter as tk
from tkinter import*
from tkinter import ttk

class FieldFrame(Frame):
    
    # CONSTRUCTOR FIELDFRAME
    def __init__(self, frame_principal, titulo_campos, campos, titulo_entradas, habilatado, Valores = None, combobox = None ):
        #CONTRUCTOR DEL FRAME PADRE
        super().__init__(frame_principal, height= 260 , width=300, bg ="thistle1", highlightbackground="purple4", highlightthickness=2 )

        self.titulo_campos = titulo_campos  
        self.campos = campos
        self.titulo_entradas = titulo_entradas
        self.habilitado = habilatado
        self.valores = Valores
        self.combobox_items = combobox or {}

        self.elementos = []

        # CREAR Y EMPAQUETAR LABELS DE LOS TITULOS
        Label_titulo_criterios = tk.Label(self, text = self.titulo_campos, font=("Lucida Handwriting", 11, "bold"), fg = "purple4", bg = "plum1")
        Label_titulo_criterios.grid(row=0, column=0)
        
        Label_titulo_entradas = tk.Label(self, text = self.titulo_entradas, font=("Lucida Handwriting", 11, "bold"), fg = "purple4", bg = "plum1")
        Label_titulo_entradas.grid(row=0, column=1)
        
        for i in range(0, len(self.campos)):

            # LABEL CRITERIOS
            label_criterio = tk.Label(self, text=self.campos[i], font=("Times New Roman",10), bg="plum3", fg="purple")
            label_criterio.grid(row=i+1, column=0)

            #CAMPOS DE TEXTO ENTRADAS
            if self.campos[i] in self.combobox_items:
                entradaValor = ttk.Combobox(self, values=self.combobox_items[campos[i]])
                entradaValor.grid(row=i+1, column=1)
                if self.valores is not None:
                    entradaValor.set(self.valores[i])
            else:
                entradaValor = tk.Entry(self)
                entradaValor.grid(column=1, row=i+1)
                if self.valores is not None:
                    entradaValor.insert(0, self.valores[i])

                if self.habilitado is not None and not self.habilitado[i]:
                    entradaValor.configure(state=tk.DISABLED)
            
            self.elementos.append(entradaValor)
        
        tk.Button(self, text="Borrar", font=("Verdana", 12), bg="white", width=5, height=2).grid(column=1, row=len(self.campos)+1)

    def funborrar(self):
        for entrada in self.elementos:
            entrada.delete("0", "end")
            
# -----------------------------------------------------
