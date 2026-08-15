from calculos import VelIniMovil, VelIniAutomovil

print ("Bienvenido al programa de medición de velocidades")
print ("1. Calcular velocidad inicial de un Movil")
print ("2. Calcular velocidad inicial de un Automovil")
print ("3. Salir")

opcion = input("Seleccione una opción (1, 2 o 3): ")
if opcion == "1":
    VelFin = float(input("Ingrese la velocidad final del movil: "))
    Aceleracion = float(input("Ingrese la aceleración del movil: "))
    Distancia = float(input("Ingrese la distancia recorrida por el movil: "))
    VelIni = VelIniMovil(VelFin, Aceleracion, Distancia)
    print("La velocidad inicial del movil es:", VelIni)

elif opcion == "2" :
    
    VelFin = float(input("Ingrese la velocidad final del automovil: "))
    Aceleracion = float(input("Ingrese la aceleración del automovil: "))
    Tiempo = float(input("Ingrese el tiempo que ha transcurrido: "))
    VelIni = float(VelIniAutomovil(VelFin, Aceleracion, Tiempo))
    print("La velocidad inicial del automovil es:", VelIni)
    
elif opcion == "3":
    print("Saliendo del programa...")
else:
    print("Opción inválida. Por favor, seleccione una opción válida.")