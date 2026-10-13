import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}

df = pd.DataFrame(inventario)

df["valor_inventario"] = df["precio"] * df["stock"]
df["reponer"] = df["stock"] < 10
print(df)