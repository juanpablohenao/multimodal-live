from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/",methods=["GET"])
def home():
    result = [{"name": "juan pablo", "role": "web developer", "description": "super good"},{"name": "maria del pilar", "role": "dibujante arquitectonica", "description": "super good"}]
    return jsonify(result)

# create a customer
@app.route("/",methods=["POST"])
def create_customer():
    try:
        data = request.json
        name = data.get("name")
        return jsonify({"msg": f"Customer inserted {name}"}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run()