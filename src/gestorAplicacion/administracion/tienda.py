from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from gestorAplicacion.componentes.producto import Producto
    from gestorAplicacion.componentes.empleado import Empleado
    from gestorAplicacion.administracion.centroAdopcion import CentroAdopcion
    from componentes.cliente import Cliente

#DANIEL ALBERTO ZAPATA CASTAÑO
#OKY RUIZ DE LA ROSA
#SALOMÉ MURILLO GAVIRIA
#NICOLAS DAVID ZAMBRANO MURCIA
	
#DESCRIPCIÓN DE LA CLASE:
#Gestiona el inventario de productos disponibles para la venta, permitiendo a los clientes realizar compras.

class Tienda:

    ##Atributo, la lista general de los productos 
    listaProductos = []

    ##Constructor -------------------------------------------------------------------------------
    def __init__(self, empleado: Empleado) -> None:
        _listaEmpleados = []
        _listaEmpleados.append(empleado)

    ##Setter and Getter -------------------------------------------------------------------------
    
    def getEmpleados(self):
        return self._listaEmpleados 
    
    @classmethod
    def getProductos(cls):
        return cls.listaProductos
    
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
            tipo = i.getEspecie()
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