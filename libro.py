class Libro:
    def __init__(
        self,
        idLibro,
        titulo,
        autor,
        genero,
        anoPubli,
        ISBN,
        estado,
        donante,
        dispo,
        receptor="Sin lector",  # Es a quien fue donado
    ):
        self.__idLibro = idLibro
        self.__titulo = titulo
        self.__autor = autor
        self.__genero = genero
        self.__anoPubli = anoPubli
        self.__ISBN = ISBN
        self.__estado = estado
        self.__dispo = dispo
        self.__donante = donante
        self.__receptor = receptor

    @property
    def idLibro(self):
        return self.__idLibro

    @idLibro.setter
    def idLibro(self, setId):
        self.idLibro = setId

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, setTitu):
        self.titulo = setTitu

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, setAutor):
        self.autor = setAutor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, setGenero):
        self.genero = setGenero

    @property
    def anoPubli(self):
        return self.__anoPubli

    @anoPubli.setter
    def anoPubli(self, setAno):
        self.anoPubli = setAno

    @property
    def ISBN(self):
        return self.__ISBN

    @ISBN.setter
    def ISBN(self, setISBN):
        self.ISBN = setISBN

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, setEstado):
        self.estado = setEstado

    @property
    def dispo(self):
        return self.__dispo

    @dispo.setter
    def dispo(self, setDispo):
        self.__dispo = setDispo

    @property
    def donante(self):
        return self.__donante

    @donante.setter
    def donante(self, setDonante):
        self.__donante = setDonante

    @property
    def receptor(self):
        return self.__receptor

    @receptor.setter
    def receptor(self, setReceptor):
        self.__receptor = setReceptor

    def __str__(self) -> str:
        return (
            f"\n"
            f"- ID: {self.__idLibro}\n"
            f"- Título: {self.__titulo}\n"
            f"- Autor: {self.__autor}\n"
            f"- Género: {self.__genero}\n"
            f"- Año de Publicación: {self.__anoPubli}\n"
            f"- ISBN: {self.__ISBN}\n"
            f"- Estado: {self.__estado}\n"
            f"- Disponible: {self.__dispo}\n"
            f"- Donante: {self.__donante}\n"
            f"- Lector: {self.receptor}"
        )

    def cambiarDispo(self, cambiarDispo):
        if cambiarDispo == "Pendiente" or cambiarDispo == "pendiente":
            self.__estado = "Donado"
            self.__dispo = "No disponible"
        elif cambiarDispo == "No disponible":
            print("Error de solicitud el libro ya estaba no disponible")

    def cambiarDispo(self, cambiarDispo):
        if cambiarDispo == "Devuelto" or cambiarDispo == "Devuelto":
            self.__estado = "Devuelto"
            self.__dispo = "Disponible"
        else:
            print("Error de solicitud el libro ya estaba no disponible")

    def cambiarReceptor(self, nuevoReceptor):
        self.__receptor = nuevoReceptor


class LibroNoFicci(Libro):
    def __init__(
        self,
        idLibro,
        titulo,
        autor,
        genero,
        anoPubli,
        ISBN,
        estado,
        dispo,
        donante,
        areaConoci,
    ):
        super().__init__(
            idLibro, titulo, autor, genero, anoPubli, ISBN, estado, dispo, donante
        )
        self.__areaConoci = areaConoci

    @property
    def areaConoci(self):
        return self.__areaConoci

    @areaConoci.setter
    def areaConoci(self, setArea):
        self.areaConoci = setArea


class LibroFiccion(Libro):
    def __init__(
        self,
        idLibro,
        titulo,
        autor,
        genero,
        anoPubli,
        ISBN,
        estado,
        dispo,
        donante,
        serie,
        numSerie,
    ):
        super().__init__(
            idLibro, titulo, autor, genero, anoPubli, ISBN, estado, dispo, donante
        )
        self.__serie = serie
        self.__numSerie = numSerie

    @property
    def serie(self):
        return self.__serie

    @serie.setter
    def serie(self, setSerie):
        self.__serie = setSerie

    @property
    def numSerie(self):
        return self.__numSerie

    @numSerie.setter
    def numSerie(self, setNumSerie):
        self.__numSerie = setNumSerie
