def leer_cantidad_empleados():
    n = int(input("Ingrese la cantidad de empleados: "))
    if n <= 0:
        print("La cantidad debe ser mayor que cero.")
        return 0
    return n

def leer_salario_minimo():
    smin = float(input("Ingrese el salario mínimo SMVL: "))
    if smin <= 0:
        print("El salario mínimo debe ser mayor que cero.")
        return 0
    return smin

def leer_empleado():
    nombre = input("Ingrese el nombre del empleado: ")
    salario_basico = float(input("Ingrese el salario básico del empleado: "))
    deducciones = float(input("Ingrese las deducciones del empleado: "))

    if salario_basico <= 0:
        print("El salario básico debe ser mayor que cero.")

    if deducciones < 0:
        print("Las deducciones no pueden ser negativas.")

    salario_neto = salario_basico - deducciones

    empleado = {
        "nombre": nombre,
        "salario_basico": salario_basico,
        "deducciones": deducciones,
        "salario_neto": salario_neto,
    }
    return empleado

def calcular_promedio_salarios(empleados):
    total = 0

    for empleado in empleados:
        total = total + empleado["salario_basico"]

    if len(empleados) == 0:
        return 0

    promedio = total / len(empleados)
    return promedio

def contar_empleados_mas_de_4_salarios(empleados, salario_minimo):
    contador = 0

    for empleado in empleados:
        if empleado["salario_basico"] > 4 * salario_minimo:
            contador = contador + 1

    return contador

def buscar_mayor_salario(empleados):
    mayor = empleados[0]

    for empleado in empleados:
        if empleado["salario_basico"] > mayor["salario_basico"]:
            mayor = empleado

    return mayor

def buscar_menor_salario_neto(empleados):
    menor = empleados[0]

    for empleado in empleados:
        if empleado["salario_neto"] < menor["salario_neto"]:
            menor = empleado

    return menor
def calcular_porcentaje(cantidad, total):
    if total == 0:
        return 0
    porcentaje = (cantidad * 100) / total
    return porcentaje

def mostrar_salario_neto(nombre, salario_neto):
    print(f"El salario neto de {nombre} es: {salario_neto:.2f}")