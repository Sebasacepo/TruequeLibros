class Solicitud:
    def __init__(self, idSolicitud, estado, fechaSolicitud, usuario, libro):
        self.__idSolicitud = idSolicitud
        self.__estado = estado
        self.__fechaSolicitud = fechaSolicitud
        self.__usuario = usuario
        self.__libro = libro

    @property
    def idSolicitud(self):
        return self.__idSolicitud

    @idSolicitud.setter
    def idSolicitud(self, setIdSol):
        self.__idSolicitud = setIdSol

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, getEstado):
        self.__estado = getEstado

    @property
    def fechaSolicitud(self):
        return self.__fechaSolicitud

    @fechaSolicitud.getter
    def fechaSolicitud(self, setfechaSol):
        self.__fechaSolicitud = setfechaSol

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, setUsuario):
        self.__usuario = setUsuario

    @property
    def libro(self):
        return self.__libro

    @libro.setter
    def libro(self, setLibro):
        self.__libro = setLibro

    def resSolicitud(self, respuesta):  # Es la respuesta a la solicitud
        if respuesta == 1 or respuesta == 0:  # Validar que no tenga respuesta
            print("La solicitud ya tiene respuesta")
        else:
            if respuesta == 1:
                print("Estado de la solicitud: Rechazada")
                return 1
            elif respuesta == 0:
                print("Estado de la solicitud: Aceptada")
                return 0
            else:
                print("Estado de la solicitud: Pendiente")
                return respuesta
