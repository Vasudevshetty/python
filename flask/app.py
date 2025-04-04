from flask import Flask

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the Flask app!"


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
