from flask import Flask, render_template, redirect
import os

app = Flask(__name__)

@app.route("/")
def home():
    return redirect("https://giovannymartha.nl")
    # return render_template("index.html")

@app.route("/test")
def test():
    return redirect("https://giovannymartha.nl")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render geeft poort door via environment variable
    app.run(host="0.0.0.0", port=port)