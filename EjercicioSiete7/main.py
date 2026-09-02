from procedimiento import ResultadoImaginario, ResultadoUnico, ResultadoDoble

print("ax^2 + bx + c = 0")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
c = float(input("Ingrese el valor de c: "))
discriminante = b**2 - 4*a*c

if discriminante < 0:
    ResultadoImaginario(a, b, discriminante)
elif discriminante == 0:
    ResultadoUnico(a,b)
else:
    ResultadoDoble(a, b, discriminante)