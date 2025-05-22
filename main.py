from flask import flask
app = flask(_name_)

@app.route("/")
def home():
    return "hallo dit is mijn eerste projectt"

if __name__ == "__main__":
    app.run()