import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

datos = {
    "edad": [18, 22, 25, 30, 35, 40, 45, 50, 55, 60],
    "ingreso": [1.2, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5],
    "compro": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

d = pd.DataFrame(datos)
x = d[["edad","ingreso"]]
y = d["compro"]

X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
modelo = LogisticRegression()
modelo.fit(X_train, y_train)

# Probar con clientes nuevos
nuevos = pd.DataFrame({"edad":[28, 52], "ingreso":[2.2, 4.8]})
for p in modelo.predict(nuevos):
    print("si compra" if p == 1 else "no compra")