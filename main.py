from random import random
from math import log, sqrt, sin, cos, pi, exp

def generarTiempoEntreLlegadas(n,lam=17.755):
    """Acorde con la imagen 2 el tiempo de llegadas se distribuye exponencial con parametro 17.755,
    se simulara el tiempo entre llegadas por medio de la transformada inversa.
    Se reciben dos parametros:
    n = numero de personas que se desea simular
    lam = valor del parametro"""
    return [-1/lam*log(1-random()) for _ in range(n)]


def metodoBoxMuller(media, desvEstand):
    """Implementacion del metodo de transformada inversa Box Muller"""
    r1 = random(); r2 = random()
    x1 = sqrt(-2*log(r1) )*cos(2*pi*r2)
    x2 = sqrt(-2*log(r1) )*sin(2*pi*r2)
    xp1 = media + desvEstand*x1
    xp2 = media + desvEstand*x2
    return xp1,xp2

    
def generarTiempoDeServicioNormal(n,media= 145.86, desvEstand=43.459):
    """Acorde con la imagen 3 el tiempo de servicio del ascensor se distribuye normal con media 145.86 y
    desviacion estandar 43.459. Se simulara el tiempo de servicio normal por meotodo Box-Muller.
    n = numero de personas que desea simular
    media = media con que se ditribuye la distribucion normal
    devEstand = desviacion estandar de la distribucion normal"""
    resultado = []
    for i in range (n//2):
        (xp1, xp2 ) = metodoBoxMuller(media,desvEstand)
        resultado.append( exp(xp1))
        resultado.append( exp(xp2))
    if n%2 == 0:
        return resultado
    else:
        (xp1, xp2 ) = metodoBoxMuller(media,desvEstand)
        resultado.append(xp1)
        return resultado

def generarTiempoDeServicioLognormal(n, media=77.697, desvEstand=49.858 ):
    """Acorde con la imagen 3 el tiempo de servicio del ascensor se distribuye log-normal con media 77.697 y
    desviacion estandar 49.858. Se simulara el tiempo de servicio log-normal por meotodo Box-Muller.
    n = numero de personas que desea simular
    media = media con que se ditribuye la distribucion log-normal
    devEstand = desviacion estandar de la distribucion log-normal
    Usando una modificacion al resultado del metodo box-muller mostrado en la fuente.
    fuente: https://webs.um.es/mpulido/miwiki/lib/exe/fetch.php?id=amio&cache=cache&media=wiki:simt4.pdf"""
    resultado = []
    for i in range (n//2):
        (xp1, xp2 ) = metodoBoxMuller(media,desvEstand)
        resultado.append(xp1)
        resultado.append(xp2)
    if n%2 == 0:
        return resultado
    else:
        (xp1, xp2 ) = metodoBoxMuller(media,desvEstand)
        resultado.append(xp1)
        return resultado

def tLlegadas(tEntreLlegadas):
    """Agregar DOC"""
    tLlegadas = [tEntreLlegadas[0]]
    for i in range (len(tEntreLlegadas) - 1):
        tLlegadas.append(tEntreLlegadas[i] + tEntreLlegadas[i+1])
    return tLlegadas


def simularElevadores(tLlegadas, tServicio1, tServicio2):
    """Agregar DOC"""
    """while(tLlegadas):
        if (tLlegadas < tServicio1 < tServicio2):"""

if __name__ == "__main__":
    x1 = 1; x2 = 2; x3 = 3
    print(x1 < x2 < x3)

    numUsuarios = int(input())
    tEntreLlegadas = generarTiempoEntreLlegadas(numUsuarios)
    tServicios = generarTiempoDeServicioNormal(numUsuarios)
    print(len(tLlegadas))
    print(len(tServicios), tServicios)
