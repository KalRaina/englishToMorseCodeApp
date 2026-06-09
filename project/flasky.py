from flask import Flask, render_template, request
from lettersToMorseCodeAudioWebApp import generateWAV, convertToMorse

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])

def index():
    output = ""
    if request.method == "POST":
        text = request.form["input_text"]
        output = convertToMorse(text)
        generateWAV(output)

    return render_template("web.html", output=output)

if __name__ == "__main__":
    app.run(debug=True)