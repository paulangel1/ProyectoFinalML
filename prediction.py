import pickle
import pandas as pd
import os

# Ruta al modelo entrenado
MODEL_PATH = os.path.join('models', 'model.pkl')

def cargar_modelo():
    """ Carga el modelo entrenado desde el archivo .pkl """
    try:
        with open(MODEL_PATH, 'rb') as file:
            model = pickle.load(file)
        return model
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {MODEL_PATH}. Asegúrate de haber entrenado el modelo.")
        return None

def predecir(datos):
    """
    Realiza la predicción de PM2.5 basado en el promedio de biciusuarios.
    
    Args:
        datos: Puede ser un número o un diccionario con una clave 'biciusuarios'
    
    Returns:
        Predicción del nivel de PM2.5 o mensaje de error
    """
    # Extraer el valor de biciusuarios del diccionario si es un diccionario
    if isinstance(datos, dict) and 'biciusuarios' in datos:
        prom_biciusuarios = float(datos['biciusuarios'])
    else:
        # Si no es diccionario, asumir que es directamente el valor numérico
        try:
            prom_biciusuarios = float(datos)
        except (ValueError, TypeError):
            return {"error": "Formato de datos invalido. Se esperaba un número o un diccionario con 'biciusuarios'"}
    
    modelo = cargar_modelo()
    if modelo:
        # Convertir a DataFrame para que sea compatible con el modelo
        data = pd.DataFrame({'PromBiciusuarios': [prom_biciusuarios]})
        prediccion = modelo.predict(data)
        return round(float(prediccion[0]), 2)
    else:
        return {"error": "Modelo no cargado. Verifica el archivo model.pkl."}

# Prueba rápida (Eliminar o comentar en producción)
if __name__ == "__main__":
    # Prueba con un valor ejemplo
    ejemplo = 100  # Número de biciusuarios promedio
    resultado = predecir(ejemplo)
    print(f"Predicción de PM2.5 para {ejemplo} biciusuarios: {resultado}")
    
    # Prueba con un diccionario (como vendría de app.py)
    ejemplo_dict = {'biciusuarios': 150}
    resultado_dict = predecir(ejemplo_dict)
    print(f"Predicción de PM2.5 para {ejemplo_dict['biciusuarios']} biciusuarios (desde dict): {resultado_dict}")