from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Charger le modèle entraîné et le scaler
model = joblib.load('rf_model.pkl')
scaler = joblib.load('scaler.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = np.array(data['features']).reshape(1, -1)
    features = scaler.transform(features)
    prediction = model.predict(features)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)
