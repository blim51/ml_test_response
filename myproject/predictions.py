import json
import os
from pathlib import Path
from dotenv import load_dotenv
import requests

# precondition: model is hosted on a server

# get port
ROOT_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = ROOT_DIR / ".env"
if ENV_PATH.exists():
    load_dotenv(dotenv_path=ENV_PATH)
else:
    raise FileNotFoundError(f".env file not found at {ENV_PATH}")
MODEL_PORT = os.getenv("MODEL_PORT")
MODEL_ADDRESS = os.getenv("MODEL_ADDRESS")

# precondition: cdata contains all fields correctly filled
def query_model(cdata): # dict of cleaned data from questionaire
    url = f"http://{MODEL_ADDRESS}:{MODEL_PORT}/query/"
    filled_array = [int(cdata[f"answers{x}"]) for x in range(1, 11)]
    # print(filled_array)
    req_body = {
    "answers": filled_array
    }
    response = requests.post(url, json=req_body)
    try:
        # print(response.status_code) # 201
        res_body = response.json()
        return res_body["result"] if "result" in res_body else -1 # label, 1 for e and 0 for i
        # -1 if answers not in response body
    except ValueError:
        print("Not a JSON")
        return -1