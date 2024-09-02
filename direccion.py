class Direccion:
    def __init__(self, pais, ciudad, barrio, nombreVia, numeroVia, numero) -> None:
        self.__pais = pais
        self.__ciudad = ciudad
        self.__barrio = barrio
        self.__nombreVia = nombreVia
        self.__numeroVia = numeroVia
        self.__numero = numero

    @property
    def pais(self):
        return self.__pais

    @pais.setter
    def pais(self, setPais):
        self.pais = setPais

    @property
    def ciudad(self):
        return self.__ciudad

    @pais.setter
    def ciudad(self, setCiudad):
        self.ciudad = setCiudad

    @property
    def barrio(self):
        return self.__barrio

    @pais.setter
    def barrio(self, setBarrio):
        self.barrio = setBarrio

    @property
    def nombreVia(self):
        return self.__nombreVia

    @pais.setter
    def nombreVia(self, setNombreVia):
        self.nombreVia = setNombreVia

    @property
    def numeroVia(self):
        return self.__numeroVia

    @pais.setter
    def numeroVia(self, setNumeroVia):
        self.numeroVia = setNumeroVia

    @property
    def numero(self):
        return self.__numero

    @pais.setter
    def numero(self, setNumero):
        self.numero = setNumero
