import pickle
import pandas as pd
import os

# Ruta al modelo entrenado
MODEL_PATH = os.path.join('models', 'model.pkl')

def cargar_modelo():
    """Carga el modelo entrenado desde un archivo .pkl"""
    with open(MODEL_PATH, 'rb') as file:
        model = pickle.load(file)
    return model

def predecir(data):
    """Realiza la predicción basada en los datos ingresados"""
    modelo = cargar_modelo()
    # Convertir los datos a un DataFrame
    df = pd.DataFrame([data])
    # Realizar la predicción
    prediccion = modelo.predict(df)
    return prediccion[0]

def cargar_datos(file_path):
    """Carga los datos de un archivo Excel para análisis o entrenamiento"""
    df = pd.read_excel(file_path)
    return df
