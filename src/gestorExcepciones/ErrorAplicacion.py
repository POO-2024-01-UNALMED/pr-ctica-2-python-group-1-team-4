from tkinter import messagebox


class ErrorAplicacion(Exception):
    # Se dispara cuando se detecta un error en la aplicación
    def __init__(self, mensajeEspecifico):
        self.mensajeBase = "Error: "
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

class ErrorFueraRango(ErrorGenerativo):
    def __init__(self):
        super().__init__("Error generado al ingresar un número fuera del rango socilitado.")

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

class ErrorDigitos_Cel_CC(ErrorAccionUsuario):
   # Se dispara cuando el usuario no selecciona un elemento de un menú desplegable y da click en aceptar
    def __init__(self, numero, digitos):
        super().__init__(f"El número de {numero} está incorrecto. Debe tener al menos {digitos} digitos.")
        self._numero = numero
        self._digitos =digitos

    def mostrarMensaje(self):
        messagebox.showerror("Error","El número de " +str(self._numero) + " está incorrecto. Debe tener al menos " + str(self._digitos) + " digitos.")



class ErrorUsuarioMenor(ErrorAccionUsuario):
    # Se disparará cuando el usuario ingresa una edad menor a 18 años.
    def __init__(self):
        super().__init__("La edad del usuario debe ser mayor o igual a 18 años.")

# Error sugerido 2 (espacios sin rellenar en FieldFrame)
class ErrorFormularioVacio(ErrorAccionUsuario):
    # Se dispara cuando el usuario no rellena todos los espacios del formulario y da click en aceptar
    def __init__(self, espacios):
        super().__init__(f"Espacios sin rellenar ({', '.join(espacios)})")

