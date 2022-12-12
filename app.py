import base64

from flask import Flask, render_template, request
from flask_cors import CORS

from MeasureVariable import MeasureVariable
from Expression import GetDegreeOfSurprise

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
    return MeasureVariable()

@app.route("/face-recognition", methods=["GET"])
def GetDegreeOfSurpriseFromFace():
    img_url = "images/img2.jpg"
    return GetDegreeOfSurprise(img_url)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8082, debug=True)