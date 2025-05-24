from flask import Flask, request, jsonify, render_template, url_for
import pickle
import os
import numpy as np

MODEL_PATH = os.path.join('models')

app = Flask(__name__)

ESTACIONES = ['KENNEDY', 'LAS FERIAS', 'CARVAJAL', 'FONTIBON', 'PTE ARANDA', 'USAQUEN', 'SUBA']

modelos = {}
for estacion in ESTACIONES:
    modelo_path = os.path.join(MODEL_PATH, f'model_{estacion}.pkl')
    try:
        with open(modelo_path, 'rb') as file:
            modelos[estacion] = pickle.load(file)
    except FileNotFoundError:
        print(f"Modelo para {estacion} no encontrado. Asegúrese de haber entrenado y guardado los modelos correctamente.")



@app.route('/')
def menu():
    return render_template('menu.html')

@app.route('/refuerzo')
def index():
    q_table = np.load("models/q_table.npy")
    return render_template("index.html", q_table=q_table.tolist())


@app.route('/pagina')
def pagina():
    return render_template('pagina.html', estaciones=ESTACIONES)

@app.route('/entendimiento')
def entendimiento():
    return render_template('entendimiento.html')

@app.route('/ingenieriadatos')
def ingenieria_datos():
    return render_template('IngenieriaDatos.html')

@app.route('/ingenieriamodelo')
def ingenieria_modelo():
    return render_template('ingenieriamodelo.html')

@app.route('/evaluacion')
def evaluacion():
    return render_template('evaluacion.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        if not data or 'biciusuarios' not in data or 'estacion' not in data or 'periodo' not in data:
            return jsonify({'error': 'Se requieren los campos biciusuarios, estacion y periodo'}), 400

        biciusuarios = data['biciusuarios']
        estacion = data['estacion'].upper()
        periodo = data['periodo']

        if estacion not in modelos:
            return jsonify({'error': f'La estación {estacion} no está disponible para predicción.'}), 400

        modelo = modelos[estacion]
        prediccion = modelo.predict([[biciusuarios, periodo]])[0]
        prediccion = round(prediccion, 4)

        return jsonify({'prediccion': prediccion})

    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)