import socket
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return {
        "message": "Hello from Kubernetes!",
        "hostname": socket.gethostname()
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)