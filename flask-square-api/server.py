import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/square", methods=["GET"])
def square():
    try:
        number = float(request.args.get("number", 0))
        return jsonify({"square": number ** 2})
    except Exception:
        return jsonify({"error": "Invalid number"}), 400

# Render (and many hosts) provide the port via the PORT env var.
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)