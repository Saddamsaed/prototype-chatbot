from flask import Flask, send_file, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get("/")
def index_get():
    return render_template("home.html")

@app.get("/download")
def download_cv():
    p = './static/AI Systems Development Engineer.pdf'
    return send_file(p, as_attachment=True)

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    response = get_response(text)  
    message = {"answer": response}
    return jsonify(message) 


if __name__ == "__main__":
    app.run(debug=True)    