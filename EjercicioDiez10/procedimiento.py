import matplotlib.pyplot as plt
import statistics

def grafico_barras(entero, aleatorio):
    plt.bar(entero, aleatorio)

    plt.xlabel("Entero")
    plt.ylabel("Valor Aleatorio")
    plt.title("Tabla")

    plt.show()
    
def medidas(aleatorio):
    media = statistics.mean(aleatorio)
    mediana = statistics.median(aleatorio)
    desviacion = statistics.stdev(aleatorio)
    
    print(f"Media: {media} \nMediana: {mediana} \nDesviación: {desviacion}")