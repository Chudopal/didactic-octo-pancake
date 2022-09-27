"""Simple flask app."""
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Simple flask method."""
    return "Hello"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
