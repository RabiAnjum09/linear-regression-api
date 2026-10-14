
import random
from flask import Flask, jsonify, request

app = Flask(__name__)

STUDENT_ROLL_NUMBER = 33

REGISTRATION_NUMBER = "FA23-BDS-033"

random.seed(STUDENT_ROLL_NUMBER)
a1 = random.uniform(-5, 5)
a2 = random.uniform(-5, 5)
a3 = random.uniform(-5, 5)
b = random.uniform(-10, 10)


@app.get("/health")
def health():
    return jsonify({"status": "healthy"})


@app.get("/predict")
def predict():
    try:
        x1 = float(request.args["x1"])
        x2 = float(request.args["x2"])
        x3 = float(request.args["x3"])
    except (KeyError, ValueError):
        return jsonify({
            "error": "Provide numeric x1, x2 and x3 parameters"
        }), 400

    y = a1*x1 + a2*x2 + a3*x3 + b

    return jsonify({
        "registration number": REGISTRATION_NUMBER,
        "prediction": round(y, 2)
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
