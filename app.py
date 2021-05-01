from flask import Flask
from flask_marshmallow import Marshmallow

app = Flask(__name__)
ma = Marshmallow(app)


@app.route("/")
def index_page():
    return "Hello World"


if __name__ == '__main__':
    app.run()
