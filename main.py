"""
Run with
export FLASK_DEBUG=1
FLASK_APP=main.py python -m flask run --host=0.0.0.0
"""

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

@app.route("/", methods = ['POST'])
def index():
    if request.method == 'POST':
        with backend.get_session().graph.as_default() as g:
            try:
                payload = request.form[PAYLOAD_KEY]
            except:
                return render_template('error.html', error="Wrong payload")
            model = load_model(MODEL_PATH)
            df = pd.read_json(payload)
            y_predicted = test_model(model, df)
            predicted_activity = one_hot_to_label(y_predicted)
            return render_template('response.html', activity=predicted_activity)

def test_model(model, data):
    X_test, y_test = get_convoluted_data(data)
    X_test, _ = shuffle(X_test, y_test, random_state=0)
    y_predicted = model.predict(X_test)
    y_predicted = np.asarray([softmax_to_one_hot(y) for y in y_predicted])

    return y_predicted

if __name__ == '__main__':
    app.run(host='0.0.0.0')
