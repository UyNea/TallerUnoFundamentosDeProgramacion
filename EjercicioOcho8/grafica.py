import matplotlib.pyplot as plt

def grafico_barras(nombres, edades):
    plt.bar(nombres, edades)

    plt.xlabel("Personas")
    plt.ylabel("Edad")
    plt.title("Edades de las personas")

    plt.ylim(bottom=0)
    plt.yticks(range(0, max(edades) + 5, 5))

    plt.show()


def grafico_puntos(nombres, edades):
    plt.scatter(nombres, edades)

    plt.xlabel("Personas")
    plt.ylabel("Edad")
    plt.title("Edades de las personas")

    plt.ylim(bottom=0)
    plt.yticks(range(0, max(edades) + 5, 5))

    plt.show()


def grafico_lineas(nombres, edades):
    plt.plot(nombres, edades)

    plt.xlabel("Personas")
    plt.ylabel("Edad")
    plt.title("Edades de las personas")

    plt.ylim(bottom=0)
    plt.yticks(range(0, max(edades) + 5, 5))

    plt.show()