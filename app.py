import base64

from flask import Flask, render_template, request
from flask_cors import CORS

from MeasureVariable import MeasureVariable
from RecognizeFace import RecognizeFace

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 100 * 1024 * 1024
CORS(
    app,
    supports_credentials=True
)


@app.route("/", methods=["GET"])
def IndexHTML():
    return render_template("index.html")


@app.route("/measure-variable", methods=["POST"])
def CallMeasureVariable():
    with open("images/img2.jpg", mode="wb") as file:
        file.write(base64.b64decode(request.json["image"]))
    return {"variable": MeasureVariable(), "recognition": RecognizeFace("images/img2.jpg")["result"]}


@app.route("/recognize-face", methods=["GET"])
def CallRecognizeFace():
    img_url = "images/img2.jpg"
    return RecognizeFace("images/img2.jpg")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8082, debug=True)
