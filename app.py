import base64

from flask import Flask, request
from flask_cors import CORS

from MeasureVariable import MeasureVariable

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024
CORS(
    app,
    supports_credentials=True
)


@app.route("/measure-variable", methods=["POST"])
def MeasureVariable():
    with open("images/img2.jpg", mode="wb") as file:
        file.write(base64.b64decode(request.json["image"]))
    return MeasureVariable()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
