from flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/api/predict', methods=['POST'])
def predict():
    data = request.json
    age = int(data['age'])
    prediction = model.predict(np.array([[age]]))
    prediction[0]=round(float(prediction[0]), 3)
    return jsonify({'predictions': prediction[0]})

@app.route('/api', methods=['GET'])
def base():
    
    return jsonify({'message': "Welcome!"})

if __name__ == '__main__':
    app.run(debug=True)
