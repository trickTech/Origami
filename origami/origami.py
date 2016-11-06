from flask import Flask

app = Flask(__name__)


@app.route('/')
def init_commit():
    return "Hello world"


if __name__ == "__main__":
    app.run(debug=True)
