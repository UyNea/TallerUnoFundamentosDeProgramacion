
import math

from main import Distancia


def VelIniMovil(VelFin,Aceleracion, Distancia):
   
    VelIni = math.sqrt((VelFin**2) - (2 * Aceleracion * Distancia))
    return VelIni
print("La velocidad inicial es:", VelIniMovil)

def VelIniAutomovil(VelFin,Aceleracion, Tiempo):
    VelIni = Distancia / Tiempo - (Aceleracion * Tiempo/2)
    return VelIni
print("La velocidad inicial del automóvil es:", VelIniAutomovil)