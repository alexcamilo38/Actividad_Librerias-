import numpy as np

notas = np.array([7.5, 8.0, 6.5, 9.0, 5.5, 8.5])

print("Las notas son:")
print(notas)

print("Promedio: ", notas.mean())
print("Nota maxima: ", notas.max())
print("Nota minima: ", notas.min())
print("Desviacion: ", notas.std())