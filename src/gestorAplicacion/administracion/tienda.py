from componentes.producto import Producto
from componentes.empleado import Empleado
from centroAdopcion import CentroAdopcion

class Tienda:

    ##Atributo, la lista general de los productos 
    listaProdutos = []

    ##Constructor
    def __init__(self, centroAdopcion : CentroAdopcion, empleado: Empleado) -> None:
        _centro = centroAdopcion 
        _listaEmpleados = []
        _listaEmpleados.append(empleado)

    ##Setter and Getter 
    def getEmpleados(self):
        return self._listaEmpleados 

    def agregarEmpleados(self, *empleados : Empleado):
        for i in empleados:
            self._listaEmpleados.append(i) 
        #Se agrega la cantidad de empleados que se hayan pasado

    def setCentro(self, centro):
        self._centro = centro
    
    def getCentro(self):
        return self._centro
    
    ##Métodos
    def inventario(cls):
        resultado = ""
        indice = 0
        for i in cls.listaProdutos:
            indice += 1
            resultado += str(indice)+". "
            resultado += str(i)+"\n"


    def filtrar(cls, filtro):
        resultado = ""
        indice = 0
        for i in cls.listaProdutos:
            indice+=1
            tipo = i.getTipoAnimal()
            if tipo=="Uso general" or tipo==filtro:
                resultado += str(indice)+". "
                resultado += str(i)+"\n"
                indice += 1

    