<<<<<<< HEAD
import os
import pickle
import pandas as pd
=======
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import os

DATA_PATH = os.path.join('data', 'NivelesPorAño.csv')
MODEL_DIR = os.path.join('models')
os.makedirs(MODEL_DIR, exist_ok=True)
>>>>>>> 93192b8a138ec015f8271419180a8693280c9282

MODEL_DIR = 'models'
ESTACIONES = ['KENNEDY', 'LAS FERIAS', 'CARVAJAL', 'FONTIBON', 'PTE ARANDA', 'USAQUEN', 'SUBA']

<<<<<<< HEAD
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
=======
def cargar_datos(file_path):
    """ Carga el dataset desde un archivo CSV y procesa los datos. """
    df = pd.read_csv(file_path, sep=';')
    estaciones_presentes = [est for est in ESTACIONES if est in df.columns]

    if not estaciones_presentes:
        raise ValueError(f"Ninguna de las estaciones {ESTACIONES} está presente en el DataFrame.")

    df["Promedio_PM25"] = df[estaciones_presentes].mean(axis=1)

    df["Inverso_Biciusuarios"] = 1 / df["PromBiciusuarios"].replace(0, float('inf'))

    return df


def entrenar_modelos_por_estacion(df):
    """ Entrena un modelo independiente por estación/localidad considerando el año. """
    modelos = {}

    for estacion in ESTACIONES:
        if estacion in df.columns:
            print(f"Entrenando modelo para {estacion}...")

            X = df[['PromBiciusuarios', 'Periodo']]
            y = df[estacion]

            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

            modelo = LinearRegression()
            modelo.fit(X_train, y_train)

            modelo_path = os.path.join(MODEL_DIR, f'model_{estacion}.pkl')
            with open(modelo_path, 'wb') as file:
                pickle.dump(modelo, file)

            modelos[estacion] = modelo_path
            print(f"Modelo para {estacion} guardado en {modelo_path}")

    return modelos

def main():
    print("Cargando datos...")
    datos = cargar_datos(DATA_PATH)

    print("Entrenando modelos por estación...")
    entrenar_modelos_por_estacion(datos)

if __name__ == "__main__":
    main()
>>>>>>> 93192b8a138ec015f8271419180a8693280c9282
