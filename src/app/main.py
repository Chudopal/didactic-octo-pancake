"""Simple flask app."""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    """Simple flask method."""
    return "Hello"


@app.route('/add')
def add():
    """Add two digits."""
    return str(
        int(request.args.get("a")) +
        int(request.args.get("b"))
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
