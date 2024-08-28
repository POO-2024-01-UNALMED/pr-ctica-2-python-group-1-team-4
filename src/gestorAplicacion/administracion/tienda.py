class Tienda:

    ##Atributo, la lista general de los productos 
    listaProdutos = []

    ##Constructor
    def __init__(self, centroAdopcion, empleado) -> None:
        _centro = centroAdopcion 
        _listaEmpleados = []
        _listaEmpleados.append(empleado)

    ##Setter and Getter 
    def getEmpleados(self):
        return self._listaEmpleados 

    def agregarEmpleados(self, *empleados):
        for i in empleados:
            self._listaEmpleados.append(i) ##Se agrega la cantidad de empleados que se hayan pasado

    def setCentro(self, centro):
        self._centro = centro
    
    def getCentro(self):
        return self._centro
    
    ##Métodos
    def inventario(cls):
        resultado = ""
        indice = 1
        for i in cls.listaProdutos:
            resultado += str(indice)+". "
            resultado += i+"\n"
            indice += 1