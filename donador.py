from usuario import Usuario


class Donador(Usuario):
    def __init__(
        self,
        idUsuario,
        nomUsuario,
        apellido,
        email,
        fechaNacimiento,
        telefono,
        direccion,
    ):
        super().__init__(idUsuario, nomUsuario, apellido, email, fechaNacimiento)
        self.__telefono = telefono
        self.__direccion = direccion

    @property
    def telefono(self):
        return self.__telefono

    @telefono.setter
    def telefono(self, setTel):
        self.__telefono = setTel

    @property
    def direccion(self):
        return self.__direccion

    @direccion.setter
    def direcccion(self, setDir):
        self.__direccion = setDir

    def respuesta(self, resp, pendiente):
        if pendiente == "Pendiente" or pendiente == "pendiente":
            if (
                resp == "Aceptar" or resp == "aceptar"
            ):  # el 1 es para aceptar la respuesta
                print("El donante a aceptado la solicitud")
                print("Puedes pasar a recoger el libro ahora")
                return "Aceptada"
            else:  # cualquier otra respuesta es para rechazar, lo mas optimo es 0
                print("Lo sentimos, su solicitud fue rechazada")
                return "Rechazada"
        elif pendiente == "Aceptada" or "Rechazada" or "aceptada" or "rechazada":
            print("No se puede ejecutar por que la solicitud ya tiene respuesta")
            return None

    def pedirLibroDonado(self, lector):
        if lector == "sin lector" or "Sin lector":
            print("No puedes pedir un libro que donaste")
