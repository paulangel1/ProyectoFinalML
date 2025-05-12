from flask import Flask, render_template, request
import pandas as pd
# Importa otras bibliotecas que necesites

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenido a mi aplicación Flask para Machine Learning"

# Añade más rutas según necesites

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)