import json
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request
import joblib
import numpy as np

# load model on server launch:
loaded_model = joblib.load("model.joblib")

# get port
ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
else:
    raise FileNotFoundError(f".env file not found at {ENV_PATH}")
MODEL_PORT = os.getenv("MODEL_PORT")

app = Flask(__name__)

# generalized response formats
def success_response(data, code=200):
    return json.dumps(data), code


def failure_response(message, code=404):
    return json.dumps({"error": message}), code

# routes here

@app.route("/query/", methods=["POST"])
def send_query():
    """
    Endpoint for getting result of questionaire from model
    """
    body = json.loads(request.data)
    input_answers = body.get("answers")
    # check if array and is length 10
    if input_answers is None:
        return failure_response("missing input", 400)
    elif not isinstance(input_answers, list) or len(input_answers) != 10:
        return failure_response("invalid input (not length 10 list)", 400)
    else:
        # send label back!
        return success_response({"result": loaded_model.predict(np.array(input_answers).reshape(1, -1))[0]}, 201)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = MODEL_PORT, debug = "true")

# sent JSON via Postman
# {
#     "answers": [1, 1, 1, 2, 2, 2, 4, 3, 4, 4]
# }