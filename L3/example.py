from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def main():
    return "Hello world"


@app.route('/api/', methods=['GET', 'POST'])
def api():
    return jsonify(
        {
            "Amy": request.args.get('a')
        })


app.run(debug=True)

