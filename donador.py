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

    def respuesta(self, resp):
        if resp == 1:  # el 1 es para aceptar la respuesta
            print("El donante a aceptado la solicitud")
            print("Puedes pasar a recoger el libro ahora")
            return 0
        else:  # cualquier otra respuesta es para rechazar, lo mas optimo es 0
            print("Lo sentimos, su solicitud fue rechazada")
            return 1
