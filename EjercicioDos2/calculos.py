
import math

def VelIniMovil(VelFin, Aceleracion, Distancia):
    VelIni = math.sqrt((VelFin**2) - (2 * Aceleracion * Distancia))
    return VelIni

def VelIniAutomovil(VelFin, Aceleracion, Tiempo):
    VelIni = VelFin - (Aceleracion * Tiempo)
    return VelIni
