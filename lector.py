from usuario import Usuario as usuario


class Lector(usuario):
    def __init__(self, idUsuario, nomUsuario, apellido, email, fechaNacimiento):
        super().__init__(idUsuario, nomUsuario, apellido, email, fechaNacimiento)
