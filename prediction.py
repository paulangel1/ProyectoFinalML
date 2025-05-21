import os
import pickle
import pandas as pd

MODEL_DIR = 'models'
ESTACIONES = ['KENNEDY', 'LAS FERIAS', 'CARVAJAL', 'FONTIBON', 'PTE ARANDA', 'USAQUEN', 'SUBA']

def cargar_modelo(estacion):
    """ Carga el modelo correspondiente a la estación """
    model_path = os.path.join(MODEL_DIR, f'model_{estacion.lower()}.pkl')
    if not os.path.exists(model_path):
        raise FileNotFoundError(f'Modelo para {estacion} no encontrado.')
    with open(model_path, 'rb') as file:
        modelo = pickle.load(file)
    return modelo

def predecir(estacion, biciusuarios, periodo):
    try:
        modelo = cargar_modelo(estacion)
        # Realizar la predicción incluyendo el período
        entrada = [[biciusuarios, periodo]]
        prediccion = modelo.predict(entrada)[0]
        # Redondear a 4 decimales
        return round(prediccion, 4)
    except Exception as e:
        return str(e)

if __name__ == "__main__":
    # Ejemplo de predicción
    estacion = 'KENNEDY'
    biciusuarios = 2000
    periodo = 2025
    print(predecir(estacion, biciusuarios, periodo))