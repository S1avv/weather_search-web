from flask import Flask, request, jsonify
from settings import api_key
from translate import Translator
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)


@app.route("/weather", methods=['POST'])
def get_weather():
    data = request.get_json()
    if not data or 'city' not in data:
        return 400
    
    city = data['city']
    
    response = requests.post(f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}")

    if "error" in response.json():
        return 400

    data_main = response.json()

    data = response.json().get("current").get("condition")["text"]

    translator = Translator(to_lang="ru")
    translation = translator.translate(data)

    data_main.get("current").get("condition")["text"] = translation

    return jsonify(data_main)

if __name__ == "__main__":
    app.run(debug=True)
