# Reto rápido de programación
# Ingresar número enteros a una matriz de 
# N filas con M columnas y reemplazar por
# el número 0 todos los elementos qur 
# forman la letra U.
import os
import random
import numpy as np
os.system('cls')


# Primero vamos a generar las dimensiones de la matriz
""" def size():
    # Se generan de manera aleatoria los valores
    n = random.randint(2,10)
    m = random.randint(2,10)
    # Se valida que las filas sean 
    if (n > 2):
        print('Valores aceptados')
    else:
        size()
    return n, m
# Los valores que devuelve la función están
# en una tupla
valores = size()
n = valores[0]
m = valores[1] """
n,m = 8,8

# Se crea la matriz
matriz = np.zeros((n,m),dtype=int)

# Recorrer la matriz
for i in range(n):
    for j in range(m):
        if (i == n-1):
            matriz[i][j] = 0
        elif (j == 0 or j == m-1):
            matriz[i][j] = 0
        else:
            matriz[i][j] = random.randint(1,9)
print(matriz)
