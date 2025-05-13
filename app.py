from flask import Flask, request, jsonify, render_template
from prediction import predecir

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('pagina.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Obtener los datos de la solicitud
        data = request.get_json()
        
        # Verificar si los datos son válidos
        if not data or 'biciusuarios' not in data:
            return jsonify({'error': 'Se requiere el campo biciusuarios'}), 400
        
        # Realizar la predicción
        resultado = predecir(data)
        
        # Verificar si hay un error en la predicción
        if isinstance(resultado, dict) and 'error' in resultado:
            return jsonify(resultado), 400
        
        # Devolver el resultado como JSON
        return jsonify({'prediccion': resultado})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)