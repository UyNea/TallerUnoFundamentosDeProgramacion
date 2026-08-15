def calcular_nota_Exam_Final(Parcial_1, Seguimiento_Lab_1, Quiz_1, Parcial_2, Seguimiento_Lab_2):
    
 Nota_definitiva = 3.0
 Exam_Fin = (Nota_definitiva - (Parcial_1 * 0.20) - (Seguimiento_Lab_1 * 0.10) - (Quiz_1 * 0.10) - (Parcial_2 * 0.20) - (Seguimiento_Lab_2 * 0.10)) / 0.30
 return Exam_Fin
