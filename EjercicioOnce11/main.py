from ecuaciones import *

print("MENU DE EJERCICIOS")
print("1. Serie Fibonacci Clasica")
print("2. Serie Fibonacci Alternada")
print("3. Sumatoria i^2(2i+3)")
print("4. Sumatoria Algebraica")
print("5. Desviacion Estandar")
print("6. Doble Sumatoria")

opcion = int(input("\nElige una opcion (1-6): "))
cantidad_terminos = int(input("Ingresa cantidad de terminos: "))

if opcion == 1:
    resultado = sum(serie_fibonacci(cantidad_terminos))
    print("Resultado 11.1:")
    print(resultado)
elif opcion == 2:
    resultado = sum(serie_fibonacci_alternada(cantidad_terminos))
    print("Resultado 11.2:")
    print(resultado)
elif opcion == 3:
    resultado = ejercicio_11_3(cantidad_terminos)
    print("Resultado 11.3:")
    print(resultado)
elif opcion == 4:
    resultado = ejercicio_11_4(cantidad_terminos)
    print("Resultado 11.4:")
    print(resultado)
elif opcion == 5:
    valores = list(map(int, input("Ingresa numeros separados por espacio: ").split()))
    resultado = ejercicio_11_5(valores)
    print("Resultado 11.5:")
    print(resultado)
elif opcion == 6:
    resultado = ejercicio_11_6(cantidad_terminos)
    print("Resultado 11.6:")
    print(resultado)
else:
    print("Opcion no valida")
