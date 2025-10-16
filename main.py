import pandas as pd
import matplotlib.pyplot as plt

#1
df = pd.read_csv('consumo_energia.csv')
df = df.dropna(subset=['Consumo_kWh'])

#2
df['Fecha'] = pd.to_datetime(df['Fecha'])
df['Mes_Num'] = df['Fecha'].dt.month

#3
filtro = df[(df['Hogar_ID'] == 'Hogar_5') & (df['Consumo_kWh'] > 25)]
print("registros del Hogar_5 con consumo > 25 kWh:")
print(filtro)
print()

#4
promedios = df.groupby(['Hogar_ID', 'Mes_Num'])['Consumo_kWh'].mean().reset_index()
print(" consumo promedio por Hogar y Mes:")
print(promedios)
print()

#5
subset = df[df['Hogar_ID'].isin(['Hogar_1', 'Hogar_2', 'Hogar_3'])]

def clasificar_estacion(mes):
    if mes in [6, 7, 8]:
        return 'Verano'
    elif mes in [12, 1, 2]:
        return 'Invierno'
    else:
        return 'Otro'

subset['Estacion'] = subset['Mes_Num'].apply(clasificar_estacion)

promedios_est = subset.groupby(['Hogar_ID', 'Estacion'])['Consumo_kWh'].mean().unstack()

promedios_est[['Verano', 'Invierno']].plot(kind='bar')
plt.title('comparacion de consumo promedio Verano vs Invierno')
plt.ylabel('Consumo promedio (kWh)')
plt.xlabel('hogar')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

