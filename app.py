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
class Predict(Resource):
    """ predict endpoint.
    """

    @classmethod
    def post(cls):
        """.
        """
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
        return jsonify({"msg": "Error: not a JSON or no email key in your request"})


if __name__ == "__main__":
    app.run(debug=True)
