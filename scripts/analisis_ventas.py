import pandas as pd
import matplotlib.pyplot as plt
import os

# Leer el dataset de ventas desde una ruta relativa
df = pd.read_csv("datos/ventas.csv")

# Convertir la columna de fecha a formato datetime
df["sales_date"] = pd.to_datetime(df["sales_date"])

# Calcular indicadores generales
ventas_totales = df["sales_amount"].sum()
promedio_ventas = df["sales_amount"].mean()
venta_maxima = df["sales_amount"].max()
venta_minima = df["sales_amount"].min()

# Crear columna de mes para agrupar ventas mensuales
df["mes"] = df["sales_date"].dt.to_period("M")

ventas_por_mes = df.groupby("mes")["sales_amount"].sum().reset_index()
ventas_por_mes["mes"] = ventas_por_mes["mes"].astype(str)

# Guardar resumen general
resumen = pd.DataFrame({
    "Indicador": [
        "Ventas totales",
        "Promedio de ventas",
        "Venta maxima",
        "Venta minima"
    ],
    "Valor": [
        ventas_totales,
        promedio_ventas,
        venta_maxima,
        venta_minima
    ]
})

resumen.to_csv("resultados/resumen_ventas.csv", index=False)
ventas_por_mes.to_csv("resultados/ventas_por_mes.csv", index=False)

# Generar gráfico de ventas por mes
plt.figure(figsize=(10, 5))
plt.plot(ventas_por_mes["mes"], ventas_por_mes["sales_amount"], marker="o")
plt.title("Evolución de ventas por mes")
plt.xlabel("Mes")
plt.ylabel("Monto de ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("resultados/grafico_ventas.png")

print("Análisis finalizado correctamente.")
print(resumen)
