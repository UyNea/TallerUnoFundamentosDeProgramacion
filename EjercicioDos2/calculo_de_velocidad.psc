Algoritmo calculo_de_velocidad
	Definir opcion Como Entero
	Definir VelFin, Aceleracion, Distancia, VelIni, Tiempo Como Real
	
	Escribir "hola, bienvenido a nuestro sistema de medición de velocidad"
	Escribir "por favor ingrese una opción "
	Escribir " 1. calcular velocidad inicial de un movil"
	Escribir " 2. calcular la velocidad inicial de un Automovil "
	leer opcion
	
	si opcion = 1 Entonces
		Escribir "Ha elegido calcular la velocidad inicial de un móvil"
		Escribir "Ingrese la velocidad final"
		Leer VelFin
		Escribir "Ingrese la aceleración"
		Leer Aceleracion
		Escribir "ingrese la distancia total recorrida"
		Leer Distancia
		
		VelIni <- RC((VelFin^2) - (2*Aceleracion* Distancia))
		
		Escribir " La velocidad inicial del movil es de:", VelIni
	SiNo
		si opcion = 2 Entonces
			Escribir "Ha elegido calcular la velocidad inicial de un Automóvil"
			Escribir "Ingrese la distancia"
			Leer Distancia
			Escribir "Ingrese la aceleración"
			Leer Aceleracion
			Escribir "ingrese el tiempo"
			Leer Tiempo
			
			VelIni <- Distancia/Tiempo- Aceleracion*Tiempo/2
			
			Escribir " La velocidad inicial del Automovil es de:", VelIni
		SiNo
			Escribir "Opcion incorrecta"
		FinSi
		
	FinSi
	
FinAlgoritmo
