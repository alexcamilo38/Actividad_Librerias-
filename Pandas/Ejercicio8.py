import pandas as pd

inventario = {
    "producto": ["Camisa", "Gorra", "Pantalón", "Medias", "Zapatos"],
    "precio": [45000, 30000, 89000, 8000, 150000],
    "stock": [20, 5, 12, 40, 3]
}

df = pd.DataFrame(inventario)

df_ordenado = df.sort_values(by="precio", ascending=False)

precio_promedio = df["precio"].mean()

print("Inventario ordenado del más caro al más barato:")
print(df_ordenado)

print("El precio promedio de todos los productos es: ", precio_promedio)