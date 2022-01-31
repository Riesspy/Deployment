

import os
import pandas as pd
import joblib

from flask_restx import Resource, Api 
from flask import Flask, request, jsonify, make_response 


app = Flask(__name__)
api = Api(app,
        title='Wine-o-meter',
        description='ML in production',
)



@api.route('/predict', methods=["POST"])
class Predict(Resource):
    @classmethod
    def post(cls):
         # Check if request has a JSON content
        if request.json:
            # Get the JSON as dictionnary
            req = request.get_json()
            print(f"request : {req}")
            print(req.keys())

            # Check mandatory key
            if "input" in req.keys():
                # Load model
                model_file = os.path.join("./model/model.joblib")
                reg = joblib.load(model_file)

                # Predict
                prediction = reg.predict(req["input"])
                prediction = prediction.tolist()

                # return prediction
                # return jsonify({"predict": prediction}), 200
                data = {"predict": prediction}
                return make_response(jsonify(data), 200)
        return jsonify({"msg": "Error: not a JSON in your request"})


if __name__ == "__main__":
    app.run(debug=True)
