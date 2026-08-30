def ResultadoImaginario(a, b, discriminante):
    real = -b / (2*a)
    imaginario = (abs(discriminante)**0.5) / abs(2*a)

    print("Las soluciones IMAGINARIAS de la ecuación son:")
    print(f"x1 = {real} + {imaginario:.2f}i")
    print(f"x2 = {real} - {imaginario:.2f}i")
    print("La ecuación no tiene soluciones reales.")
    
def ResultadoUnico(a, b):
    x = -b / (2*a)
    print(f"La solución de la ecuación es: x = {x}")
    

def ResultadoDoble(a, b, discriminante):
    x1 = (-b + discriminante**0.5) / (2*a)
    x2 = (-b - discriminante**0.5) / (2*a)
    print(f"Las soluciones de la ecuación son: \nx1 = {x1} \nx2 = {x2}")