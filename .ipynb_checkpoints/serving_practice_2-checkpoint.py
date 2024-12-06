import os
from flask import Flask, request, jsonify
import numpy as np
import joblib


app = Flask(__name__)
model = joblib.load(os.environ.get("MODEL_PATH", "models_practice_2/sale_forcasting.pkl"))
scaler = joblib.load(os.environ.get("SCALER_PATH", "models_practice_2/sale_forcasting_scaler.pkl"))

@app.route('/predict', methods=['POST'])
def predict():
    # Get the data from the request
    price_per_unit = request.json.get('price_per_unit', None)
    unit_solds = request.json.get('unit_solds', None)
    operationg_profit = request.json.get('operationg_profit', None)    
    
    if None in [price_per_unit, unit_solds, operationg_profit]:
        return jsonify({'error': 'No provide enough data'}), 400
    
    try:
        # Convert the data to a numpy array
        data_np = scaler.transform([[price_per_unit, unit_solds, operationg_profit]])
        print(data_np)
        
        # Make predictions using the model
        predictions = model.predict(data_np).astype(np.int)
        
        # Convert predictions to a list of floats
        prices = predictions.flatten().tolist()
        
        # Return the predictions as a JSON response
        return jsonify({'sale_units': abs(prices[0])})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)