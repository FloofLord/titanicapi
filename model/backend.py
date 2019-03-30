from flask import Flask, request, jsonify
import pickle
import json
import requests
import pandas as pd
from sklearn.externals import joblib
import numpy as np

app = Flask(__name__)

@app.route("/")
def hello():
    return "<p>Hello</p>"

# Pclass  Sex   Age  SibSp  Parch      Fare
@app.route('/api/predict/', methods=['POST'])
def predict():
    json = request.get_json()
    #print(json)
    df = pd.DataFrame(json)
    #print(df)
    prediction = model.predict(df)
   # print(prediction)
    return jsonify(prediction.tolist())


if __name__ == "__main__":
    model = joblib.load('model.pkl')
    app.run(debug=True, host ='0.0.0.0')
