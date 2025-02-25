from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

def run_ollama3_chatbot(user_input):
    process = subprocess.Popen(
        ["python", "ollama3_chatbot.py"],  # manca il file
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=user_input)
    return stdout.strip()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    response = run_ollama3_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
