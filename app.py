from flask import Flask, jsonify, render_template, request
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/")
def index():
    return "Bienvenue sur le site AI!"

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json()
    message = data.get("message")
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"Réponds : {message}",
        max_tokens=100
    )
    return jsonify({"response": response.choices[0].text.strip()})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
