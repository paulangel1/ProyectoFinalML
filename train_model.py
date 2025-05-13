# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# Rutas
DATA_PATH = os.path.join('data', 'NivelesPorAño.csv')
MODEL_PATH = os.path.join('models', 'model.pkl')

def cargar_datos(file_path):
    """ Carga el dataset desde un archivo CSV y procesa los datos. """
    # Cargar el archivo
    df = pd.read_csv(file_path, sep=';')  # Asumiendo que el separador es punto y coma
    
    # Imprimir información sobre el DataFrame para depuración
    print("Columnas disponibles:", df.columns.tolist())
    print("Primeras filas del DataFrame:")
    print(df.head())
    
    # Verificar si las estaciones están en el DataFrame
    estaciones = ['KENNEDY', 'LAS FERIAS', 'CARVAJAL', 'FONTIBON', 'PTE ARANDA', 'USAQUEN', 'SUBA']
    estaciones_presentes = [est for est in estaciones if est in df.columns]
    
    if not estaciones_presentes:
        raise ValueError(f"Ninguna de las estaciones {estaciones} está presente en el DataFrame. Columnas disponibles: {df.columns.tolist()}")
    
    # Usar solo las estaciones que están presentes
    print(f"Estaciones encontradas: {estaciones_presentes}")
    df["Promedio_PM25"] = df[estaciones_presentes].mean(axis=1)
    
    return df

def entrenar_modelo(df):
    """ Entrena el modelo de regresión lineal. """
    # Variables predictoras y objetivo
    X = df[['PromBiciusuarios']]
    y = df['Promedio_PM25']

    # Dividir el conjunto de datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Entrenar el modelo
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    return modelo

def guardar_modelo(model, path):
    """ Guarda el modelo entrenado en un archivo .pkl """
    with open(path, 'wb') as file:
        pickle.dump(model, file)
    print(f"Modelo guardado en: {path}")

def main():
    # Cargar datos
    print("Cargando datos...")
    datos = cargar_datos(DATA_PATH)

    # Entrenar el modelo
    print("Entrenando modelo...")
    modelo = entrenar_modelo(datos)

    # Guardar el modelo
    print("Guardando modelo...")
    guardar_modelo(modelo, MODEL_PATH)

if __name__ == "__main__":
    main()
