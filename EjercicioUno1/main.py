
x0= 0.0 
y0= 0.0

x1= float(input("ingrese x1: "))
y1= float(input("ingrese y1: "))
plac_1= (input("ingrese la placa del vehículo 1: "))
x2= float(input("ingrese x2: "))
y2= float(input("ingrese y2: "))
plac_2= (input("ingrese la placa del vehículo 2: "))
x3= float(input("ingrese x3: "))
y3= float(input("ingrese y3: "))
plac_3= (input("ingrese la placa del vehículo 3: "))


sqrt1= ((x0-x1)**2 + (y0-y1)**2)**(0.5)
sqrt2= ((x0-x2)**2 + (y0-y2)**2)**(0.5)
sqrt3= ((x0-x3)**2 + (y0-y3)**2)**(0.5)

print ("El punto 1 es: (" + str(sqrt1) + ")")
print ("El punto 2 es: (" + str(sqrt2) + ")")
print ("El punto 3 es: (" + str(sqrt3) + ")")


if sqrt1 < sqrt2 :
    if sqrt1 < sqrt3:
        print ("El vehiculo 1 con placas " + plac_1 + " es el mas cercano al origen")
    else:
        print ("El vehiculo 3 con placas " + plac_3 + " es el mas cercano al origen")
else:
    if sqrt2 < sqrt3:
        print ("El vehiculo 2 con placas " + plac_2 + " es el mas cercano al origen")
    else:
        print ("El vehiculo 3 con placas " + plac_3 + " es el mas cercano al origen")
        
