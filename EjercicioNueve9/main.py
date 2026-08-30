#Podría ser necesario instalar matplotlyb de forma manual.

from grafica import grafico_barras, grafico_lineas, grafico_puntos

x = []
cubos = []
for i in range(-100,101):
    x.append(i)
    cubos.append(i**3)
    
print("\nLista de X: ")
print(x)
print("\nLista de cubos:")
print(cubos)

grafico_barras(x,cubos)
grafico_lineas(x,cubos)
grafico_puntos(x,cubos)