import numpy as np
ventas = np.array([120000, 95000, 150000, 80000, 200000, 175000, 110000])
print('Las ventas son:')
print(ventas)

ventas_aumento = ventas * 1.1
print("Las ventas con el aumento", ventas_aumento)
print("El total de la semana",ventas_aumento.sum())