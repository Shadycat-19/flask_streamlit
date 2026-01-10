from flask import Flask, request, jsonify
import google.generativeai as genai
import PIL.Image
import os
from dotenv import load_dotenv

load_dotenv() # This loads the variables from .env

api_key = os.getenv("API_KEY")
print(f"My key is: {api_key}")
app = Flask(__name__)

# Configure Gemini
genai.configure(api_key= api_key)
model = genai.GenerativeModel('gemini-3-flash-preview')

@app.route('/describe', methods=['POST'])
def describe_image():
    if 'image' not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    file = request.files['image']
    img = PIL.Image.open(file)

    # Prompting Gemini
    response = model.generate_content(["Describe this image in detail.", img])

    return jsonify({"description": response.text})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
