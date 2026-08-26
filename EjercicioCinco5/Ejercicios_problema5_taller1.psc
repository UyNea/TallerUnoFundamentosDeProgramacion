
	Algoritmo Ejercicios_problema5_taller1
		Definir n,cont4 Como Entero
		Definir sbas, snet,ded  Como Real
		Definir promsb, sumasb,porc4, maySbas, smin Como Real
		Definir nom, nomMaySb,nomMenSnet Como Caracter
		Imprimir "ingrese la cantidad de empleados"
		Leer n 
		Imprimir  "Ingrese el salario minimo SMVL"
		Leer smin 
		sumasb=0 //Acumulador
		cont4=07//contador de empleados que ganan más de 4 salarios mínimos
		nomMaySb=""
		maySbas=0 
		nomMenSnet=""
		menSnet=100000000
		para i=1 hasta n 
			Imprimir "Ingrese el nombre del empleado"
			Leer nom
			Imprimir "Ingrese el salario básico del empelado:"
			Leer sbas
			Imprimir "Ingrese las deducciones del empelado: "
			Leer ded
			sumasb=sumasb+sbas
			snet=sbas-ded
			Imprimir "El salario neto de ",nom, " es: ",snet
			si sbas > 4*smin Entonces
				
			finSi
			si sbas > maySbas Entonces
				
			FinSi
			si snet < menSnet Entonces 
				menSnet=snet
				nomMenSnet=nom
				
				
			FinSi
			si snet < menSnet Entonces
				menSnet=snet
				nomMenSnet=nom
				
			FinSi
		FinPara
		promsb=sumasb/n
		porc4=(cont4*100)
		imprimir "el promedio de salarios básicos es: ",promsb
		Imprimir "El porcentaje de empleados que ganan más de 4 salario mínimos es: ", porc4
		Imprimir "El nombre del empleado que gana mayor salario básico es: ",nomMaySb
		Imprimir "El nombre del empleado menor salario neto es:", nomMenSnet
		
		
		
		
FinAlgoritmo

