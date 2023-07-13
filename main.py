from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/sosi/chlen")
def index():
    return render_template("main/index.html")

@app.route("/<string:name>")
def nefar(name):
    return f"nefar -> {name}"

if __name__ == "__main__":
    app.run(debug=True)