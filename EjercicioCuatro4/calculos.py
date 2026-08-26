def Registro_estudiante(numero_estudiantes):
    estudiantes = []

    if numero_estudiantes <= 0:
        print("Debe ingresar al menos un estudiante.")
        return estudiantes

    for _ in range(numero_estudiantes):
        estudiante = {
            "nombre": input("Ingrese el nombre del estudiante: "),
            "apellido": input("Ingrese el apellido del estudiante: "),
            "nota_definitiva": float(input("Ingrese la nota definitiva: "))
        }
        estudiantes.append(estudiante)

    suma_notas = 0
    estudiante_mayor = estudiantes[0]
    estudiante_menor = estudiantes[0]

    for estudiante in estudiantes:
        nota = estudiante["nota_definitiva"]
        suma_notas += nota

        if nota > estudiante_mayor["nota_definitiva"]:
            estudiante_mayor = estudiante
        elif nota < estudiante_menor["nota_definitiva"]:
            estudiante_menor = estudiante

    promedio = suma_notas / numero_estudiantes

    print(f"Promedio de notas definitivas: {promedio:.2f}")
    print(
        f"Mayor nota: {estudiante_mayor['nombre']} "
        f"{estudiante_mayor['apellido']}"
    )
    print(
        f"Menor nota: {estudiante_menor['nombre']} "
        f"{estudiante_menor['apellido']}"
    )

    return estudiantes