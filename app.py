from flask import Flask, request, jsonify
from flask_cors import CORS
# from google.colab import userdata
from google import genai
from google.genai import types
# from IPython.display import Markdown

print("Hello world")
app = Flask(__name__)
CORS(app)
# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
GOOGLE_API_KEY="AIzaSyAMveklntNsU81Msld_yXfKt0jl8gTJ6zY"
client = genai.Client(api_key=GOOGLE_API_KEY)
MODEL_ID = "gemini-2.0-flash-exp" # @param ["gemini-1.5-flash-8b","gemini-1.5-flash-002","gemini-1.5-pro-002","gemini-2.0-flash-exp"] {"allow-input":true}

@app.route("/",methods=["GET"])
def home():
    result = [{"name": "juan pablo", "role": "web developer", "description": "super good"},{"name": "maria del pilar", "role": "dibujante arquitectonica", "description": "super good"}]
    return jsonify(result)

# create a customer
@app.route("/answerthis",methods=["POST"])
def create_customer():
    try:
        data = request.json
        name = data.get("name")
        prompt = data.get("prompt")

        response = client.models.generate_content(
            model=MODEL_ID,
            contents=prompt
        )
        # Markdown(response.text)
        print(response.text)

        return response.text, 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)