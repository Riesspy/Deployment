"""
test api
"""

import requests

# predict endpoint
APP_URL = "https://whitewinee.herokuapp.com/predict"
response = requests.post(APP_URL, json={
    "input": [[7.0, 0.27, 0.36, 20.7, 0.045, 45.0, 170.0, 1.001, 3.0, 0.45, 8.8]]
})
print(response.json())

# fetchdata endpoint
APP_URL = "https://whitewinee.herokuapp.com/fetchdata"
response = requests.post(APP_URL, json={
    "column": "citric acid"
})
print(response.json())
