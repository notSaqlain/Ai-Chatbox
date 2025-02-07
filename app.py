from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

# Function to run your Ollama3 chatbot
def run_ollama3_chatbot(user_input):
    # Replace this with the actual command to run your chatbot
    process = subprocess.Popen(
        ["python", "ollama3_chatbot.py"],  # Path to your chatbot script
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout, stderr = process.communicate(input=user_input)
    return stdout.strip()

# Route to serve the frontend
@app.route("/")
def home():
    return render_template("index.html")

# Route to handle chatbot requests
@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No message provided"}), 400

    # Get the chatbot's response
    response = run_ollama3_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)