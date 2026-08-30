import matplotlib.pyplot as plt

def grafico_barras(x, cubos):
    plt.bar(x, cubos)

    plt.xlabel("X")
    plt.ylabel("Cubo de X")
    plt.title("Cubo de los números")

    plt.show()


def grafico_puntos(x, cubos):
    plt.scatter(x, cubos)

    plt.xlabel("X")
    plt.ylabel("Cubo de X")
    plt.title("Cubo de los números")

    plt.show()


def grafico_lineas(x, cubos):
    plt.plot(x, cubos)

    plt.xlabel("X")
    plt.ylabel("Cubo de X")
    plt.title("Cubo de los números")

    plt.show()