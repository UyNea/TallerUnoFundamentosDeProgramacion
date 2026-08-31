from funciones import (
    leer_cantidad_empleados,
    leer_salario_minimo,
    leer_empleado,
    calcular_promedio_salarios,
    contar_empleados_mas_de_4_salarios,
    buscar_mayor_salario,
    buscar_menor_salario_neto,
    calcular_porcentaje,
    mostrar_salario_neto,
)
def main():
    n = leer_cantidad_empleados()
    salario_minimo = leer_salario_minimo()

    empleados = []
    if n > 0:
        for i in range(n):
            empleado = leer_empleado()
            empleados.append(empleado)
            mostrar_salario_neto(empleado["nombre"], empleado["salario_neto"])

    promedio = calcular_promedio_salarios(empleados)
    contador = contar_empleados_mas_de_4_salarios(empleados, salario_minimo)
    porcentaje = calcular_porcentaje(contador, n)

    mayor = buscar_mayor_salario(empleados)
    menor = buscar_menor_salario_neto(empleados)

    resultados = [
        f"El promedio de salarios básicos es: {promedio:.2f}",
        f"El porcentaje de empleados que ganan más de 4 salarios mínimos es: {porcentaje:.2f}%",
        f"El nombre del empleado que gana mayor salario básico es: {mayor['nombre']}",
        f"El nombre del empleado con menor salario neto es: {menor['nombre']}",
    ]
    for resultado in resultados:
        print(resultado)
            
if __name__ == "__main__":
    main()