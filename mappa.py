from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/popular")
def popular():
    return render_template("popular.html")

@app.route("/starto")
def start():
    return render_template("get_start.html")

if __name__ == "__main__":
    app.run(debug=True)