from componentes.producto import Producto
from componentes.empleado import Empleado
from centroAdopcion import CentroAdopcion
from componentes.cliente import Cliente

class Tienda:

    ##Atributo, la lista general de los productos 
    listaProductos = []

    ##Constructor -------------------------------------------------------------------------------
    def __init__(self, centroAdopcion : CentroAdopcion, empleado: Empleado) -> None:
        _centro = centroAdopcion 
        _listaEmpleados = []
        _listaEmpleados.append(empleado)

    ##Setter and Getter -------------------------------------------------------------------------
    def getEmpleados(self):
        return self._listaEmpleados 

    def setCentro(self, centro):
        self._centro = centro
    
    def getCentro(self):
        return self._centro
    
    def agregarProductos(cls, *productos : Producto):
        for i in productos:
            cls.listaProductos.append(i) 
        #Se agrega la cantidad de productos que se hayan pasado
        
    def agregarEmpleados(self, *empleados : Empleado):
        for i in empleados:
            self._listaEmpleados.append(i) 
        #Se agrega la cantidad de empleados que se hayan pasado
    
    ##Métodos ---------------------------------------------------------------------------------
    def inventario(cls):

        #Acomuladores para retornar
        resultado = ""
        indice = 0
        #Recorrer la lista e ir concatenando
        for i in cls.listaProductos:
            indice += 1
            resultado += str(indice)+". "
            resultado += str(i)+"\n"
        #Devolver el resultado final 
        return resultado


    def filtrar(cls, filtro):

        #Acomuladores para retornar
        resultado = "" 
        indice = 0
        #Recorrer la lista e ir concatenando
        for i in cls.listaProductos:
            indice+=1
            tipo = i.getTipoAnimal()
            #Control para concatenar solo los prodcutos deseados
            if tipo=="Uso general" or tipo==filtro:
                resultado += str(indice)+". "
                resultado += str(i)+"\n"
                indice += 1
        #Devolver el resultado final 
        return resultado
    
    def compra(cls, indice: int, cliente: Cliente, cantidad = 1 ):

        #Control del índice
        if indice<= len(cls.listaProductos) and indice>=0:
            indice-=1
            ProductoCantidad = cls.listaProductos[indice].getCantidadUnidades()

            #Control de cantidad unidades
            if (ProductoCantidad>=cantidad):
                producto = cls.listaProductos[indice]
                #Se actualiza la nueva cantidad de producto
                producto.setCantidadUnidades(ProductoCantidad-cantidad)

                #Se elimina el producto de la lista, si quedó sin unidades
                if (producto.getCantidadUnidades==0):
                    cls.listaProductos.pop(indice)
                
                #Control de las salidas
                if (cantidad==1):
                    return f"Se ha comprado una unidad de: {producto.getNombre()}, total a pagar: {producto.getPrecio()}."
                else:
                    return f"Se han comprado, {cantidad} unidades de {producto.getNombre()}, total a pagar: {producto.getPrecio()*cantidad}."
                
            else:
                return "Cantidad inválida, no se pudo realizar la compra"
        else:
            return "Índice inválido, no se pudo realizar la compra."