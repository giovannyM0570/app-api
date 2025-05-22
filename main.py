from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hallo dit is mijn eerste project"

@app.route("/test")
def test():
    return "hall"

if __name__ == "__main__":
    app.run()