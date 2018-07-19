# Run with
# FLASK_APP=web_app.py python -m flask run --host=0.0.0.0
# Accessible at http://192.168.1.71:5000

import os
import json
import pandas as pd

from flask import Flask, request, render_template
from keras import backend
from keras.models import load_model
from sklearn.utils import shuffle

from preprocessing import *
from config import *

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        # y_predicted = web_collect_classify_activity(model)
        # predicted_activity = one_hot_to_label(y_predicted)
        with backend.get_session().graph.as_default() as g:
            payload = request.form['payload_json']
            model = load_model(MODEL_PATH)
            df = pd.read_json(payload)
            y_predicted, _ = test_model(model, df)
            predicted_activity = one_hot_to_label(y_predicted)
            return render_template('activity.html', activity=predicted_activity)
    else:
        return render_template('index.html')

def test_model(model, data):
    X_test, y_test = get_convoluted_data(data)
    X_test, y_test = shuffle(X_test, y_test, random_state=0)

    # Make predictions
    y_predicted = model.predict(X_test)
    y_predicted = np.asarray([softmax_to_one_hot(y) for y in y_predicted])
    for actual, predicted in zip(y_test, y_predicted):
        print("Actual: ", one_hot_to_label(actual), "\t Predicted: ", one_hot_to_label(predicted))

    return y_predicted, y_test

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
