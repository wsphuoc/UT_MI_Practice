import os
from flask import Flask, request, jsonify
import numpy as np
import joblib


app = Flask(__name__)
model = joblib.load(os.environ.get("MODEL_PATH", "models_practice_1/spam_email_model.pkl"))
vectorizer = joblib.load(os.environ.get("TRANSFORM_PATH", "models_practice_1/spam_email_transform.pkl"))

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    text = request.json.get('text', None) 
    
    if text is None:
        return jsonify({'error': 'No provide enough text email message'}), 400
    
    try:
        # Convert the data to a numpy array
        data_np = vectorizer.transform([text])
        
        # Make predictions using the model
        predictions = model.predict(data_np).astype(np.int)
        
        # Convert predictions to a list of floats
        spam = bool(predictions.flatten().tolist()[0])
        
        # Return the predictions as a JSON response
        return jsonify({'spam': spam})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)