"""
docstring to make pylint happy.
"""

import os
import joblib # type: ignore
import pandas as pd # type: ignore
from flask_restx import Resource, Api # type: ignore
from flask import Flask, request, jsonify, make_response # type: ignore


app = Flask(__name__)
api = Api(app,
        version='1.0',
        title='ML in production',
        description='Deployment_Project.',
)




@api.route('/predict', methods=["POST"])
def index():
    # Check if request has a JSON content
    if request.json:
        # Get the JSON as dictionnary
        req = request.get_json()
        # Check mandatory key
        if "input" in req.keys():
            # Load model
            classifier = joblib.load("./model/model.joblib")
            # Predict
            prediction = classifier.predict([req["input"]])
            # Return the result as JSON but first we need to transform the
            # result so as to be serializable by jsonify()
            prediction = str(prediction[0])
            return jsonify({"predict": prediction}), 200
    return jsonify({"msg": "Error: not a JSON key in your request"})


if __name__ == "__main__":
    app.run(debug=True)
