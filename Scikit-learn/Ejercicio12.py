import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

datos = {
    "edad": [18, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    "ingreso": [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
    "compro": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

d = pd.DataFrame(datos)
x = d[["edad","ingreso"]]
y = d["compro"]

# Experimentar con la división de datos (test_size)
for ts in (0.2, 0.3, 0.5):
    Xa, Xb, ya, yb = train_test_split(x, y, test_size=ts, random_state=42)
    modelos2 = LogisticRegression().fit(Xa, ya)
    precision = accuracy_score(yb, modelos2.predict(Xb))
    print(ts, precision * 100)