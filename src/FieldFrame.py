from tkinter import *
import tkinter as tk
from multimethod import multimethod

class FieldFrame(Frame):

     # Constructor para formularios -------------------------------------------------------------
    def __init__(self, ventana, listaCampo, listaEditables, listaValores = None):
        # Creación del frame
        super().__init__(ventana, bg="cyan", height=260, width=230)

        # Se guardan las listas (ésto es para más adelante cuando se haga el control de las entradas)
        self._listaTextosEditables = [] 
        self._listaEntradasEditables = []
        contadorCiclos = 0  
        self.botónAceptar = None

        # Creación de los label y las entradas
        for i in range(len(listaCampo)):
            texto = tk.Label(self, text=listaCampo[i], font=("Calibri", 12) , bg="white")
            texto.grid(row=i, column=0, padx=10, pady=10)

            if (listaEditables[i]==False):
                entrada = tk.Entry(self,textvariable=tk.StringVar(ventana), state=DISABLED)
                entrada.grid(row=i, column= 1, padx=20, pady=10)
                if (listaValores!=None):
                    entrada.insert(0, listaValores[i])
            else:
                # Se guardan en listas los nombres de los campos editables (para luego ser consultados más fácil)
                self._listaTextosEditables.append(listaCampo[i])
                entrada = tk.Entry(self,textvariable=tk.StringVar(ventana))
                entrada.grid(row=i, column= 1, padx=20, pady=10)
                if (listaValores!=None):
                    entrada.insert(0, listaValores[i])
                self._listaEntradasEditables.append(entrada) # Lista de entradas editables

            contadorCiclos += 1 # Variable utilizada para acomodar los botones al final 

        # Botón para eliminar texto de las entradas
        borrar = tk.Button(self, text="Borrar", font=("Calibri", 12), fg="black", bg="white", command=self.borrar, width=5)
        borrar.grid(row=contadorCiclos, column=1, padx=20, pady=3)
        
        # Botón de aceptar
        aceptar = tk.Button(self, text="Aceptar", font=("Calibri", 12), fg="black", bg="white", command=None, width=6)
        aceptar.grid(row=contadorCiclos, column=0, padx=20, pady=3)

        self.botónAceptar = aceptar # Guardamos nuestro botón de aceptar, para que se pueda acceder luego 

    # Métodos ----------------------------------------------------------------------------------------
    # Darle una función al botón de aceptar
    def ConfigurarAceptar(self, commando):
        self.botónAceptar.config(command=commando)

    # Función para obtener un valor 
    def getValue(self, NombreValor): # Nombre Valor debe ser un string 
        index = self._listaTextosEditables.index(NombreValor)
        return self._listaEntradasEditables[index].get()

    # Función para el botón borrar 
    def borrar(self):
        for entrada in self._listaEntradasEditables:
            entrada.delete("0","end")

    # Método para comprobar que si se están guardando bien los textos y los entry editables (no prestar atención)
    def getCamposEditables(self):
        resultado = ""
        for i in range(0, len(self._listaTextosEditables)):
            resultado += "Registro"+str(i+1)+" "+str(self._listaTextosEditables[i])+str(self._listaEntradasEditables[i])+"\n"
        return resultado