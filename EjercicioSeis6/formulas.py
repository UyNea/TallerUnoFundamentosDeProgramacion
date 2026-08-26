import math
import matplotlib.pyplot as plt


def crear_recta():
    while True:
        x1 = float(input("Ingrese x1: "))
        y1 = float(input("Ingrese y1: "))
        x2 = float(input("Ingrese x2: "))
        y2 = float(input("Ingrese y2: "))

        if x1 != x2 or y1 != y2:
            break

        print("Los puntos deben ser diferentes.")

    return {
        "p1": [x1, y1],
        "p2": [x2, y2]
    }


def calcular_pendiente(recta):
    x1, y1 = recta["p1"]
    x2, y2 = recta["p2"]

    if x2 == x1:
        return None

    return (y2 - y1) / (x2 - x1)


def calcular_distancia(recta):
    x1, y1 = recta["p1"]
    x2, y2 = recta["p2"]

    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def calcular_recta(recta):
    recta["pendiente"] = calcular_pendiente(recta)
    recta["distancia"] = calcular_distancia(recta)

    return recta


def graficar_rectas(rectas):
    for i, recta in enumerate(rectas):
        x1, y1 = recta["p1"]
        x2, y2 = recta["p2"]

        if recta["pendiente"] is None:
            plt.axvline(x=x1, label=f"Recta {i + 1}")
        else:
            plt.plot([x1, x2], [y1, y2], marker="o", label=f"Recta {i + 1}")

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Gráfica de las rectas")
    plt.grid(True)
    plt.legend()
    plt.show()