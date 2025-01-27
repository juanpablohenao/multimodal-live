from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/",methods=["GET"])
def home():
    result = [{"name": "juan pablo", "role": "web developer", "description": "super good"},{"name": "maria del pilar", "role": "dibujante arquitectonica", "description": "super good"}]
    return jsonify(result)

if __name__ == "__main__":
    app.run()