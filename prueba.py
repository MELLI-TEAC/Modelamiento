import random

def simulacion_covid():
    positivos = 0
    pruebas = 0
    while positivos == 0:
        pruebas += 1
        if random.random() < 0.6:
            positivos += 1
    return pruebas

def pruebas_promedio(n):
    total_pruebas = 0
    for i in range(n):
        total_pruebas += simulacion_covid()
    return total_pruebas / n

print(pruebas_promedio(500))