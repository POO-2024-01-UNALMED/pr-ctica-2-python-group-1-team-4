class ErrorAplicacion(Exception):
    # Se dispara cuando se detecta un error en la aplicación
    def __init__(self, mensajeEspecifico):
        self.mensajeBase = "Manejo de errores de la Aplicación"
        # Mensaje de error que se mostrará al usuario, se concatena con el mensaje específico
        super().__init__(f"{self.mensajeBase}: {mensajeEspecifico}")

#------------------------------------------------------------------------------------------

# Subclases de ErrorAplicacion (ErrorGenerativo, ErrorAccionUsuario)

# Errores de tipo A (Realizacion de servicios)
class ErrorGenerativo(ErrorAplicacion):
    def __init__(self, mensaje="Error al realizar una operación en los servicios o tienda."):
        super().__init__(mensaje)
        
class ErrorUnidadesInsuficientes(ErrorGenerativo):
    def __init__(self):
        super().__init__("Error generado al seleccionar más unidades de las existentes.")

class ErrorSerivicioImpedido(ErrorGenerativo):
    def __init__(self):
        super().__init__("Error generado al seleccionar un tipo de mascota no autorizado.")

# Error sugerido 1 (Búsqueda sin resultados)
class ErrorBusquedaInvalida(ErrorGenerativo):
    # Se dispara cuando el usuario realiza una búsqueda y no se encuentran resultados
    def __init__(self):
        super().__init__("No se encontraron resultados para la búsqueda realizada.")

# ----------------------------------------------------------------------------------------

# Errores de tipo B (Acciones del usuario)
class ErrorAccionUsuario(ErrorAplicacion):
    def __init__(self, mensaje="Error generado por una acción del usuario."):
        super().__init__(mensaje)

class ErrorSeleccionDesplegable(ErrorAccionUsuario):
    # Se dispara cuando el usuario no selecciona un elemento de un menú desplegable y da click en aceptar
    def __init__(self):
        super().__init__("Hay al menos un elemento del menú desplegable sin seleccionar.")

class ErrorUsuarioMenor(ErrorAccionUsuario):
    # Se disparará cuando el usuario ingresa una edad menor a 18 años.
    def __init__(self):
        super().__init__("La edad del usuario debe ser mayor o igual a 18 años.")

# Error sugerido 2 (espacios sin rellenar en FieldFrame)
class ErrorFormularioVacio(ErrorGenerativo):
    # Se dispara cuando el usuario no rellena todos los espacios del formulario y da click en aceptar
    def __init__(self, espacios):
        super().__init__(f"Espacios sin rellenar ({', '.join(espacios)})")

#---------------------------------------------------------------------------------------

#pruebas de que se imprimen los mensajes de error
def pruebasExcepciones():
    try:
        raise ErrorSerivicioImpedido()
    except ErrorAplicacion as e:
        print(e)
pruebasExcepciones()

