import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os

horas = np.array([6, 7, 8, 9, 17, 18, 19, 20]).reshape(-1, 1)  # Horas pico
ica = np.array([55, 60, 65, 70, 75, 80, 85, 90])  # ICA correspondiente

modelo = LinearRegression()
modelo.fit(horas, ica)

def predecir_ica(hora):

    return modelo.predict(np.array([[hora]]))[0]

def generar_grafico():

    if not os.path.exists('static'):
        os.makedirs('static')
    
    plt.figure(figsize=(10, 6))
    plt.scatter(horas, ica, color='blue', label='Datos reales')
    plt.plot(horas, modelo.predict(horas), color='red', label='Regresión lineal')
    plt.title('Regresión Lineal: Hora del Día vs. ICA en Usaquén')
    plt.xlabel('Hora del Día')
    plt.ylabel('Índice de Calidad del Aire (ICA)')
    plt.legend()
    plt.grid(True)
    plt.savefig('static/grafico.png')
    plt.close()
