from calculo import calcular_nota_Exam_Final

Parcial_1= float(input("Por favor ingresa tu nota del primer parcial: "))
Seguimiento_Lab_1 = float(input("Por favor ingresa tu nota del seguimiento de laboratorio 1: "))
Quiz_1 = float(input("Por favor ingresa tu nota del quiz 1: "))
Parcial_2= float(input("Por favor ingresa tu nota del segundo parcial: "))
Seguimiento_Lab_2 = float(input("Por favor ingresa tu nota del seguimiento de laboratorio 2: "))

Exam_Fin = calcular_nota_Exam_Final(Parcial_1, Seguimiento_Lab_1, Quiz_1, Parcial_2, Seguimiento_Lab_2)
if Exam_Fin <= 1.0:
    print("La nota que necesitas en el examen final es: ", Exam_Fin," No te preocupes, vas bien.")
elif Exam_Fin <= 2.0:
    print("La nota que necesitas en el examen final es: ", Exam_Fin, "Un poco más alto, pero se puede.")
elif Exam_Fin <= 3.0:
    print("La nota que necesitas en el examen final es: ", Exam_Fin, "Es muy dificil.")
elif Exam_Fin >= 4.0:
    print("La nota que necesitas en el examen final es: ", Exam_Fin, "Es muy dificil.")
else:
    print("La nota que necesitas en el examen final es: ", Exam_Fin, " lo cual es imposible de alcanzar.")