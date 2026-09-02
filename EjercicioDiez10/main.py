import random
from procedimiento import grafico_barras, medidas

entero = []
aleatorio = []
for i in range(1,21):
    entero.append(i)
    aleatorio.append(random.randint(1,6))

print(entero)
print(aleatorio)

medidas(aleatorio)
grafico_barras(entero,aleatorio)
