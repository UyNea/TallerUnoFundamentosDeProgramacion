def serie_fibonacci(cantidad_terminos):
    numeros_fibonacci = []
    numero_actual = 1
    numero_siguiente = 1
    for i in range(cantidad_terminos):
        numeros_fibonacci.append(numero_actual)
        numero_actual, numero_siguiente = numero_siguiente, numero_actual + numero_siguiente
    return numeros_fibonacci


def serie_fibonacci_alternada(cantidad_terminos):
    numeros_alternados = []
    numero_actual = 1
    numero_siguiente = 1
    for posicion in range(cantidad_terminos):
        if posicion % 2 == 0:
            numeros_alternados.append(-numero_actual)
        else:
            numeros_alternados.append(numero_actual)
        numero_actual, numero_siguiente = numero_siguiente, numero_actual + numero_siguiente
    return numeros_alternados


def ejercicio_11_3(cantidad_terminos):
    suma_total = 0
    for i in range(1, cantidad_terminos + 1):
        termino = i * i * (2 * i + 3)
        suma_total += termino
    return suma_total


def ejercicio_11_4(cantidad_terminos):
    suma_total = 0
    for i in range(30, cantidad_terminos + 1):
        termino = i - 0.5 * (2 * i - 3)
        suma_total += termino
    return suma_total


def ejercicio_11_5(valores):
    cantidad_valores = len(valores)
    promedio = sum(valores) / cantidad_valores
    suma_diferencias_cuadrado = 0
    for valor in valores:
        diferencia = valor - promedio
        suma_diferencias_cuadrado += diferencia ** 2
    desviacion_estandar = (suma_diferencias_cuadrado / cantidad_valores) ** 0.5
    return desviacion_estandar


def ejercicio_11_6(cantidad_terminos):
    suma_total = 0
    for i in range(1, cantidad_terminos + 1):
        for j in range(1, cantidad_terminos + 1):
            suma_total += 1 / (i + j)
    return suma_total
