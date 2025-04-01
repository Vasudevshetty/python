from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def welcome():
    return "Welcome to the Flask app!"


@app.route("/index", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form["name"]
        return f"Name: {name}"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
