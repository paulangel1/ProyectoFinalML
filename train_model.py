import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

# Rutas
DATA_PATH = os.path.join('data', 'NivelesPorAño.csv')
MODEL_DIR = 'models'
os.makedirs(MODEL_DIR, exist_ok=True)

# Definir las estaciones
ESTACIONES = ['KENNEDY', 'LAS FERIAS', 'CARVAJAL', 'FONTIBON', 'PTE ARANDA', 'USAQUEN', 'SUBA']

# Cargar datos
def cargar_datos(file_path):
    df = pd.read_csv(file_path, sep=';')

    # Verificar si las estaciones están presentes
    estaciones_presentes = [est for est in ESTACIONES if est in df.columns]
    if not estaciones_presentes:
        raise ValueError(f"Ninguna de las estaciones {ESTACIONES} está presente en el DataFrame.")

    return df, estaciones_presentes

# Entrenar modelo por estación
def entrenar_modelo(df, estacion):
    X = df[['PromBiciusuarios', 'Periodo']]
    y = df[estacion]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    modelo = LinearRegression()
    modelo.fit(X_train, y_train)

    return modelo

# Guardar modelo
def guardar_modelo(model, estacion):
    model_path = os.path.join(MODEL_DIR, f'model_{estacion.lower()}.pkl')
    with open(model_path, 'wb') as file:
        pickle.dump(model, file)

# Ejecutar entrenamiento y guardado para cada estación
def main():
    print("Cargando datos...")
    df, estaciones_presentes = cargar_datos(DATA_PATH)

    for estacion in estaciones_presentes:
        print(f"Entrenando modelo para {estacion}...")
        modelo = entrenar_modelo(df, estacion)
        print(f"Guardando modelo para {estacion}...")
        guardar_modelo(modelo, estacion)

if __name__ == "__main__":
    main()