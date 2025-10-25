from flask import Flask, render_template, request, jsonify
import base64
import json
import requests
import traceback
import os

API_URL = os.environ.get("API_URL", "https://489t3f0kga.execute-api.us-east-1.amazonaws.com/strees/root")

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("live.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.json
        img_b64 = data.get("image")
        if not img_b64:
            return jsonify({"error": "No image provided"}), 400

        payload = json.dumps({"image": img_b64})
        headers = {"Content-Type": "application/json"}

        # Send to Lambda
        resp = requests.post(API_URL, data=payload, headers=headers, timeout=10)
        resp.raise_for_status()  # Raise exception for HTTP errors

        # Parse nested JSON body safely
        resp_json = resp.json()
        body_str = resp_json.get("body", "{}")
        body = json.loads(body_str) if isinstance(body_str, str) else body_str

        return jsonify(body)

    except Exception as e:
        # Log full traceback to Docker logs
        print("=== ERROR in /analyze ===")
        traceback.print_exc()
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # Listen on all interfaces inside container
    app.run(host="0.0.0.0", port=5000)
