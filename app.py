from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/myUniversity.html")
def university():
    return render_template("myUniversity.html")


@app.route("/resume.html")
def resume():
    return render_template("resume.html")


if __name__ == "__main__":
    app.run(debug=True)