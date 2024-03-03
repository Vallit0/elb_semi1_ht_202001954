from flask import Flask, jsonify

app = Flask(__name__)

# Endpoint /check que retorna un código 200 (OK)
@app.route('/check', methods=['GET'])
def check_status():
    return '', 200

# Endpoint / que retorna un objeto JSON
@app.route('/', methods=['GET'])
def get_data():
    return jsonify({
        "Instancia": "Instancia #2 - API #2",
        "Curso": "Seminario de Sistemas 1",
        "Estudiante": "Estuardo Sebastian Valle Bances - 202001954"
    })

if __name__ == '__main__':
    app.run(debug=True, port=5000)
