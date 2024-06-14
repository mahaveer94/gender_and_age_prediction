from flask import Flask, request, jsonify, render_template
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io

# Initialize Flask application
app = Flask(__name__)

# Load the pre-trained model
model = None
file_path = 'D:/GENDER_PREDICTION/age_gender_model.h5'

try:
    model = load_model(file_path)
    print("Model loaded successfully.")
except Exception as e:
    print(f"Failed to load model: {e}")

# Gender dictionary
gender_dict = {0: 'Male', 1: 'Female'}

# Function to preprocess image
def preprocess_image(img):
    img = img.convert('L')  # Convert to grayscale
    img = img.resize((128, 128))  # Resize to model's expected sizing
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Expand dimensions to match model's expected input shape
    img_array /= 255.0  # Normalize pixel values
    return img_array

# Route to handle predictions
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Check if a valid image file was uploaded
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'})
        
        file = request.files['file']
        
        # Read and preprocess the image
        img = Image.open(io.BytesIO(file.read()))
        img_array = preprocess_image(img)
        
        # Predict gender and age
        pred_gender, pred_age = model.predict(img_array)
        
        # Format prediction output
        gender_prediction = gender_dict[int(np.round(pred_gender[0][0]))]
        age_prediction = int(np.round(pred_age[0][0]))
        
        return jsonify({'gender': gender_prediction, 'age': age_prediction})

# Home route - to render a basic upload form
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
