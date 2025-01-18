from flask import Flask, request, jsonify, render_template
from experta import *

app = Flask(__name__)

# Ruta principal
@app.route("/")
def index():
    return render_template("index.html")

class DiagnosticoComputadora(KnowledgeEngine):
    def __init__(self):
        super().__init__()
        self.sugerencia = ""

    @Rule(Fact(problema="pantalla_negra"))
    def problema_pantalla(self):
        self.sugerencia = "Sugerencia: Revisa si el cable del monitor está conectado."

    @Rule(Fact(problema="sin_conexion_internet"))
    def problema_internet(self):
        self.sugerencia = "Sugerencia: Verifica si el módem está encendido y conectado."

    @Rule(Fact(problema="teclado_no_funciona"))
    def problema_teclado(self):
        self.sugerencia = "Sugerencia: Revisa si el teclado está bien conectado o prueba con otro puerto USB."

    @Rule(Fact(problema="audio_no_funciona"))
    def problema_audio(self):
        self.sugerencia = "Sugerencia: Verifica si los altavoces están encendidos o si el volumen está silenciado."

@app.route("/diagnosticar-formulario", methods=["GET", "POST"])
def diagnosticar_formulario():
    if request.method == "POST":
        problema = request.form.get("problema", "No especificado")

        engine = DiagnosticoComputadora()
        engine.reset()
        engine.declare(Fact(problema=problema))
        engine.run()

    # Formulario HTML para ingresar el problema
    return f"""
        <h1 style="text-align: center; margin-top: 50px;">Diagnóstico:</h1>
        <p style="text-align: center; font-size: 18px;">{engine.sugerencia}</p>
        <div style="text-align: center; margin-top: 30px;">
            <a href="/" style="
                background-color: #4CAF50; /* Verde */
                color: white; /* Texto blanco */
                padding: 10px 20px; /* Espaciado interno */
                text-decoration: none; /* Sin subrayado */
                border-radius: 5px; /* Esquinas redondeadas */
                font-size: 16px; /* Tamaño del texto */
                font-weight: bold; /* Texto en negrita */
            ">
                Volver
            </a>
        </div>
    """
if __name__ == "__main__":
        import os
        port = int(os.environ.get("PORT", 5000))  # Render asignará un puerto en la variable de entorno PORT
        app.run(host="0.0.0.0", port=port)

 