import pickle
import os
import numpy as np

MODEL_DIR = os.path.join('models')

ESTACIONES = ['KENNEDY', 'LAS FERIAS', 'CARVAJAL', 'FONTIBON', 'PTE ARANDA', 'USAQUEN', 'SUBA']

def cargar_modelo(estacion):
    """ Carga el modelo correspondiente a una estación. """
    model_path = os.path.join(MODEL_DIR, f'model_{estacion}.pkl')
    if os.path.exists(model_path):
        with open(model_path, 'rb') as file:
            return pickle.load(file)
    else:
        raise FileNotFoundError(f"Modelo no encontrado para la estación {estacion}")

def predecir(data):
    """ Realiza la predicción del nivel de PM2.5 para una estación específica. """
    biciusuarios = data.get('biciusuarios')
    estacion = data.get('estacion')

    if not biciusuarios or not estacion:
        return {'error': 'Los campos biciusuarios y estacion son obligatorios'}

    if estacion not in ESTACIONES:
        return {'error': f'La estación {estacion} no está disponible para predicción'}

    try:
        modelo = cargar_modelo(estacion)
        prediccion = modelo.predict(np.array([[biciusuarios]]))[0]
        return prediccion
    except Exception as e:
        return {'error': str(e)}

if __name__ == "__main__":
    ejemplo = {'biciusuarios': 50, 'estacion': 'KENNEDY'}
    resultado = predecir(ejemplo)
    print("Resultado de la predicción:", resultado)
