from tkinter import messagebox
class ErrorAplicacion(Exception):

    #SE DISPARA CUANDO SE DETECTA UN ERROR EN LA APLICACIÓN
    def __init__(self, mensajeEspecifico):
        self.mensajeBase = "Manejo de errores de la Aplicación"

        super().__init__(f"{self.mensajeBase}: {mensajeEspecifico}")


#ERRORES DE TIPO A (REALIZACIÓN DE SERVICIOS)
class ErrorGenerativo(ErrorAplicacion):
    def __init__(self, mensaje="Error al realizar una operación en los servicios o tienda."):
        super().__init__(mensaje)
        
class ErrorUnidadesInsuficientes(ErrorGenerativo):
    def __init__(self):
        super().__init__("Se ha seleccionado más unidades de las existentes")

class ErrorFueraRango(ErrorGenerativo):
    def __init__(self):
        super().__init__("Error generado al ingresar un número fuera del rango socilitado.")

# Error sugerido 1 (Búsqueda sin resultados)
class ErrorBusquedaInvalida(ErrorGenerativo):
    # Se dispara cuando el usuario realiza una búsqueda y no se encuentran resultados
    def __init__(self, descripcion):
        super().__init__(f"No se encontraron resultados para la búsqueda realizada. {descripcion}")


# Errores de tipo B (Acciones del usuario)
class ErrorAccionUsuario(ErrorAplicacion):
    def __init__(self, mensaje="Error generado por una acción del usuario."):
        super().__init__(mensaje)

class ErrorDigitos_Cel_CC(ErrorAccionUsuario):
    # Se dispara cuando el usuario ingresa correctamente un numero de cédula o celular
    def __init__(self, numero, descripcion_error):
        super().__init__(f"El número de {numero} está incorrecto, {descripcion_error} ")


class ErrorUsuarioMenor(ErrorAccionUsuario):
    # Se disparará cuando el usuario ingresa una edad menor a 18 años.
    def __init__(self):
        super().__init__("No podemos continuar con el proceso, la edad del usuario debe ser mayor o igual a 18 años.")

# Error sugerido 2 (espacios sin rellenar en FieldFrame)
class ErrorFormularioVacio(ErrorAccionUsuario):
    # Se dispara cuando el usuario no rellena todos los espacios del formulario y da click en aceptar
    def __init__(self, espacios):
        super().__init__(f"Espacios sin rellenar ({', '.join(espacios)})")

