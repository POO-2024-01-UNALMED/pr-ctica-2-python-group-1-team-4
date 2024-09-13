from tkinter import Frame, Label, Entry

class Fliedframe(Frame):
    
    criteriosLabel = []
    Entradas = []

    def __init__(self, ventana, listaCampos, listaEditables):
        super.__init__(ventana)
        self.listaCampos=listaCampos
        self.listaEditables=listaEditables

        for i in range(0, len(listaCampos)):
            self.criteriosLabel.append(Label(self, text= self.listaCampos[i], bg="white", font= ("Arial", 11)))
            self.criteriosLabel[i].grid(row= i, column=0, padx= 50, pady= 10)

            if (listaEditables[i]==False):
                self.Entradas.append(Entry(self, width=60, state="disabled"))
                self.Entradas[i].grid(row = i, column=1, padx=50, pady= 10)
                