import json
import os
from pathlib import Path
from dotenv import load_dotenv
from flask import Flask, request

# get port
ROOT_DIR = Path(__file__).resolve().parent.parent  # go up 2 levels, needs testing
# print(ROOT_DIR)
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

@app.route("/query/")
def send_query():
    """
    Endpoint for getting result of questionaire from model
    """
    body = json.loads(request.data)
    input_answers = body.get("answers")
    # check if array and is length 10
    if 1 == 2: # place holder
        return failure_response("missing input", 400)
    return success_response({"hello": [2, 3]}, 201)
    # send label back!

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = MODEL_PORT, debug = "true")
