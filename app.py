from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return '<a href="'+request.path+'students"> Hello World!</a>'


if __name__ == '__main__':
    app.run(debug=True)