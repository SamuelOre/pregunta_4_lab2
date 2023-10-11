import math

def calcular_f(n, m):
    suma = 0
    for k in range(n - m + 1):
        denominador = math.factorial(k) * math.factorial(m - 1) * math.factorial(n - (k + m))
        termino = ((-1) ** k * math.factorial(n)) / denominador
        suma += termino
    return suma

n = 5  # número de actividades individuales

for m in range(1, n + 1):
    resultado = calcular_f(n, m)
    print(f"f({m}) = {resultado}")






