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
    "Sin donar",
    donador1,
    "Disponible",
    "moralidad",
)
libro2 = libroNoFic(
    "1001",
    "Introduccion al Psicoanalisis",
    "Sigmund Freud",
    "Psicología",
    date3.year,
    135,
    "Sin donar",
    donador2,
    "Disponible",
    "psicoanalisis",
)

libro3 = libroFic(
    "1002",
    "La senda del perdedor",
    "Charles Bukowsky",
    "Novela",
    date4.year,
    154,
    "Usado",
    donador2,
    "Disponible",
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
    "Sin donar",
    donador2,
    "Disponible",
    2,
    3,
)
# PRIMER SOLICITUD
print("--------------------SOLICITUD 1-------------------------")
solicitud1 = soli("Pendiente", fechaActual, lector2, libro1)  # Se genera solicitud
print(solicitud1)
libro1.cambiarDispo(solicitud1.estado)
print(libro1)
respuesta = donador1.respuesta("Aceptar", solicitud1.estado)  # respuesta
solicitud1.cambiarEstado(respuesta)  # CAMBIA EL ESTADO CON LA RESPUESTA
donador1.respuesta(
    "Aceptar", solicitud1.estado
)  # INTENTO DE VOLVER A ACEPTAR LA SOLICITUD
print("Verifico si el estado la solicitud está resulto" + str(solicitud1.estado))
devolverLibro = lector2.devolverLibro("Devolver")
libro1.devolver(devolverLibro)
libro1.cambiarReceptor(lector2)  # Se cambia lector a la nueva persona
print(libro1)  # Se vuelve a los datos anteriores
donador1.pedirLibroDonado(libro1.receptor)  # solicita libro que dono


print("-----------------Solicitud 2 -------------------")

solicitud2 = soli("Pendiente", fechaActual, lector1, libro3)
print(solicitud2)
libro3.cambiarDispo(solicitud2.estado)
print(libro3)
respuesta = donador1.respuesta("Aceptar", solicitud2.estado)  # respuesta
solicitud2.cambiarEstado(respuesta)  # CAMBIA EL ESTADO CON LA RESPUESTA
donador1.respuesta(
    "Aceptar", solicitud2.estado
)  # INTENTO DE VOLVER A ACEPTAR LA SOLICITUD
print("Verifico si el estado la solicitud está resulto" + str(solicitud2.estado))
devolverLibro = lector1.devolverLibro("Devolver")
libro3.devolver(devolverLibro)
libro3.cambiarReceptor(lector1)  # Se cambia lector a la nueva persona
print(libro3)  # Se vuelve a los datos anteriores
donador1.pedirLibroDonado(libro3.receptor)  # solicita libro que dono
