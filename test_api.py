import requests
import json

try:
    response = requests.post('http://127.0.0.1:5000/predict', json={
        'features': [0.01, 0.46, 0, 0, 0, 0.12, 0.79, 0.17, 0.79, 0, 0, 0, 0.41, 0.19, 0, 0, 0, 0, 0, 1, 1, 0]
    })
    print("Status Code:", response.status_code)
    print("Response:", json.dumps(response.json(), indent=2))
except Exception as e:
    print(f"Error: {str(e)}")
