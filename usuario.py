class Usuario:
    def __init__(self, idUsuario, nomUsuario, apellido, email, fechaNacimiento):
        self.__idUsuario = idUsuario
        self.__nomUsuario = nomUsuario
        self.__apellido = apellido
        self.__email = email
        self.__fechaNacimiento = fechaNacimiento

    @property
    def idUsuario(self):
        return self.__idUsuario

    @idUsuario.setter
    def idUsuario(self, idUsu):
        self.__idUsuario = idUsu

    @property
    def nomUsuario(self):
        return self.__nomUsuario

    @nomUsuario.setter
    def nomUsuario(self, nomUsu):
        self.__nomUsuario = nomUsu

    @property
    def apellido(self):
        return self.__apellido

    @apellido.setter
    def apellido(self, apellidoUsu):
        self.__apellido = apellidoUsu

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    @property
    def fechaNacimiento(self):
        return self.__fechaNacimiento

    @fechaNacimiento.setter
    def fechaNacimiento(self, fechaNaci):
        self.__fechaNacimiento = fechaNaci

    def __str__(self) -> str:
        return self.__nomUsuario

    def solicitud(self, libroDispo):  # el 1 es para decir que esta disponible
        if libroDispo == 1:
            print("El libro esta disponible")
            print("Solicitud hecha correctamente")
            print("Espere la respuesta del donador")
            return 0  # Retorna 0 para indicarle al sistema que ya no estara disponible
        else:
            print("el libro no esta disponible")
            return 1
            # retorna el mismo caracter para indicar que no seguira disponible

    def devolverLibro(self, estado):
        if estado == "Donado" or "donado":
            print("El libro fue devuelto correctamente")
            return "Devuelto"
        else:
            print("Error al devolver, este libro no fue prestado o no existe")
            return None
