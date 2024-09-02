from usuario import Usuario as user
from libro import Libro as lb
from libro import LibroNoFicci as libroNoFic
from libro import LibroFiccion as libroFic
from donador import Donador as don
from direccion import Direccion as dir
from solicitud import Solicitud as soli
import datetime as dt

date1 = dt.date(1997, 2, 8)
date2 = dt.date(1878, 4, 5)
date3 = dt.date(1917, 5, 4)
date4 = dt.date(1999, 2, 9)
fechaActual = dt.datetime.now()

direccion1 = dir("Colombia", "Bogotá", "Asturias", "Oriental", "33", "44")
direccion2 = dir("EEUU", "los angeles", "sidny", "sur", "55", "456")

lector1 = user(200, "Andres", "Giraldo", "angiraldo@gmail.com", date4)
lector2 = user(201, "Jaime", "Montoya", "Jmontoya@gmail.com", date1)

donador1 = don(
    100, "Sebastian", "Acevedo", "Sebasacepo@hotmail.com", date1, "12321332", direccion1
)
donador2 = don(
    101, "Hermez", "Trimegistro", "Hertrime@hotmail.com", date4, "323432434", direccion2
)

libro1 = libroNoFic(
    "1000",
    "Humano demasiado humano",
    "Friedrich Nietzche",
    "Filosofia",
    date2.year,
    123,
    "nuevo",
    1,
    donador1,
    "moralidad",
)
libro2 = libroNoFic(
    "1001",
    "Introduccion al Psicoanalisis",
    "Sigmund Freud",
    "Psicología",
    date3.year,
    135,
    "usado",
    1,
    donador2,
    "psicoanalisis",
)

libro3 = libroFic(
    "1002",
    "La senda del perdedor",
    "Charles Bukowsky",
    "Novela",
    date4.year,
    154,
    "nuevo",
    1,
    donador1,
    1,
    2,
)
libro4 = libroFic(
    "1003",
    "yo, robot",
    "Isaac Asimov",
    "cyberpunk",
    date4.year,
    199,
    "nuevo",
    1,
    donador2,
    2,
    3,
)
# PRIMER SOLICITUD
print("--------------------SOLICITUD 1--------------")
solicitud1 = soli(100000, 2, fechaActual, lector2, libro1)  # Se genera solicitud

libro1.dispo = lector1.solicitud(solicitud1.libro.dispo)

# el 1 para indicar que la acepta y el 0 para rechazar
respuesta = donador1.respuesta(1)
solicitud1.estado = solicitud1.resSolicitud(respuesta)
libro1.dispo = respuesta
print(str(libro1) + " ahora")
print("-----------------------------------------")

print("--------------Intento de responder dos veces una colicitud--------------")
# el 1 para indicar que la acepta y el 0 para rechazar
solicitud1.estado = solicitud1.resSolicitud(respuesta)

print("-----------------------------------------")

print("--------------------devolucion 1--------------")
respuesta = user.devolverLibro(lector2, respuesta)  # Devolviendo el libro
libro1.dispo = respuesta
print(str(libro1) + " ahora")  # Ya el libro esta disponible de nuevo
respuesta = user.devolverLibro(
    lector2, respuesta
)  # Intento de devolver un libro ya devuelto
print("-----------------------------------------")
