# importamos pandas
import pandas as pd

# Datos del problema
estudiantes = {
    "horas_estudio": [2, 4, 5, 6, 8, 10, 3, 7, 9, 1],
    "asistencia": [60, 70, 75, 80, 90, 95, 65, 85, 92, 50],
    "aprobo": [0, 0, 1, 1, 1, 1, 0, 1, 1, 0],
}

# Creamos el DataFrame
df = pd.DataFrame(estudiantes)

# Mostramos estadísticas descriptivas
print("Estadisticas Descriptivas")
print(df.describe())

# Agregamos la columna 'promedio_semanal' (horas diarias promedio)
df["promedio_semanal"] = df["horas_estudio"] / 7

print("\n DataFrame con la nueva columna ")
print(df)

# Filtramos estudiantes que aprobaron con menos de 6 horas de estudio
aprobados_poco_estudio = df[(df["aprobo"] == 1) & (df["horas_estudio"] < 6)]

print("\n Estudiantes que aprobaron con menos de 6 horas de estudio ")
print(aprobados_poco_estudio)

# importamos numpy
import numpy as np

# Calculamos promedio y desviación estándar de la columna asistencia
promedio_asistencia = np.mean(df["asistencia"])
desviacion_asistencia = np.std(df["asistencia"], ddof=0)  # ddof=0 para desviación estándar poblacional

print(f"Promedio de asistencia: {promedio_asistencia:.2f}%")
print(f"Desviación estándar de asistencia: {desviacion_asistencia:.2f}%")


# importamos sklearn
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Definimos características (X) y variable objetivo (y)
X = df[["horas_estudio", "asistencia"]]
y = df["aprobo"]

# Instanciamos y entrenar el modelo
modelo = LogisticRegression()
modelo.fit(X, y)

# Evaluamos la precisión (accuracy) sobre el conjunto de entrenamiento
predicciones_train = modelo.predict(X)
precision = accuracy_score(y, predicciones_train)

print(f"Precisión del modelo (Accuracy): {precision * 100:.2f}%")

# Predecimos para un estudiante que estudia 5 horas y tiene 78% de asistencia
nuevo_estudiante = [[5, 78]]
prediccion = modelo.predict(nuevo_estudiante)[0]
probabilidad = modelo.predict_proba(nuevo_estudiante)[0][1]

resultado_texto = "Aprobado" if prediccion == 1 else "Reprobado"
print(f"\nPredicción para (5 horas estudio, 78% asistencia): {resultado_texto} (Clase: {prediccion})")
print(f"Probabilidad de aprobar: {probabilidad * 100:.2f}%")
