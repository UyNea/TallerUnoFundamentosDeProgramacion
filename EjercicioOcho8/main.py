#Podría ser necesario instalar matplotlyb de forma manual.

from grafica import grafico_barras, grafico_lineas, grafico_puntos

nombres = []
edades = []

cantidad = int(input("¿Cuantas personas se desea ingesar?: "))

for i in range(cantidad):
    nombre = input(f"Ingrese el nombre de la persona {i+1}: ")
    edad = int(input(f"Ingrese la edad de {nombre}: "))
    nombres.append(nombre)
    edades.append(edad)

print("\nLista de nombres: ")
print(nombres)
print("\nLista de edades:")
print(edades)

grafico_puntos(nombres, edades)
grafico_lineas(nombres, edades)
grafico_barras(nombres, edades)