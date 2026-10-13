import numpy as np
calificacion = np.array([
    [8.5, 7.0, 9.0, 8.0], # Carlos
    [6.0, 7.5, 8.0, 7.0], # Ana
    [9.0, 8.5, 9.5, 9.0], # Luis
])

print('el promedio de Carlos, Ana y Luis es de',calificacion.mean(axis=0))
print('Prmedio de cada materia',calificacion.mean(axis=1))