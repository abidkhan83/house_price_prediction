from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load model and columns
model = pickle.load(open('home_prices_model.pickle', 'rb'))
with open('columns.json', 'r') as f:
    data_columns = json.load(f)['data_columns']

locations = data_columns[3:]  # Skip sqft, bath, bhk

@app.route('/')
def index():
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form
    try:
        sqft = float(data['area'])
        bath = int(data['bath'])
        bhk = int(data['bhk'])
        location = data['location'].strip().lower()

        # Prepare model input
        x = np.zeros(len(data_columns))
        x[0] = sqft
        x[1] = bath
        x[2] = bhk
        if location in data_columns:
            loc_index = data_columns.index(location)
            x[loc_index] = 1

        predicted_price = model.predict([x])[0]
        return jsonify({'price': round(predicted_price, 2)})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
