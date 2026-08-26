from formulas import crear_recta, calcular_recta, graficar_rectas


rectas = []

for i in range(2):

    print("Recta " + str(i + 1))

    recta = crear_recta()

    rectas.append(recta)


for i in range(len(rectas)):

    calcular_recta(rectas[i])

    print("Resultados de la Recta " + str(i + 1))
    pendiente = rectas[i]["pendiente"]
    if pendiente is None:
        print("Pendiente: indefinida (recta vertical)")
    else:
        print("Pendiente: " + str(pendiente))
    print("Distancia: " + str(rectas[i]["distancia"]))


graficar_rectas(rectas)