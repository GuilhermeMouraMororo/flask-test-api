from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/square', methods=['GET'])
def square_number():
    try:
        number = float(request.args.get('number'))
        result = number ** 2
        return jsonify({
            "number": number,
            "square": result
        })
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid or missing number parameter"}), 400

if __name__ == "__main__":
    app.run(debug=True)