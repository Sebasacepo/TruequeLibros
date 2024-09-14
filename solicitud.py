class Solicitud:
    idContador = 100000  # Variable de clase para autoincrementar el ID

    def __init__(self, estado, fechaSolicitud, usuario, libro):
        self.__idSolicitud = (
            Solicitud.idContador
        )  # Asigna el valor actual del contador al ID de la solicitud
        Solicitud.idContador += 1  # Incrementa el contador para la siguiente solicitud
        self.__estado = estado  # Estado de la solicitud
        self.__fechaSolicitud = fechaSolicitud
        self.__usuario = usuario
        self.__libro = libro

    @property
    def idSolicitud(self):
        return self.__idSolicitud

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, setEstado):
        self.__estado = setEstado

    @property
    def fechaSolicitud(self):
        return self.__fechaSolicitud

    @fechaSolicitud.setter
    def fechaSolicitud(self, setFechaSol):
        self.__fechaSolicitud = setFechaSol

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

    def cambiarEstado(self, cambio):
        self.__estado = cambio

    def __str__(self) -> str:
        fecha_formateada = self.__fechaSolicitud.strftime("%Y-%m-%d %H:%M:%S")
        usuario_str = str(self.__usuario) if self.__usuario else "No asignado"
        libro_str = str(self.__libro) if self.__libro else "No asignado"
        return (
            f"Solicitud:\n"
            f"  - ID: {self.__idSolicitud}\n"
            f"  - Estado: {self.__estado}\n"
            f"  - Fecha: {fecha_formateada}\n"
            f"  - Usuario: {usuario_str}\n"
            f"  - LIBRO: {libro_str}"
        )
