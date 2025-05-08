from flask import Flask, render_template, request
from Regresion import predecir_ica, generar_grafico

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            hora = float(request.form['hora'])
            if 0 <= hora <= 23:
                resultado = round(predecir_ica(hora), 2)
            else:
                resultado = "Por favor, ingrese una hora válida entre 0 y 23."
        except ValueError:
            resultado = "Entrada no válida. Por favor, ingrese un número."
    
    generar_grafico()
    return render_template('pagina.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
