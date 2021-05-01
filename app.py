from flask import Flask, request
from werkzeug.middleware.proxy_fix import ProxyFix

from views import auth

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

app.register_blueprint(auth.bp)


@app.route("/", methods=["GET", "POST"])
def index_page():
    if request.method == "POST":
        return "POST: Hello World"
    else:
        return "GET: Hello World"


if __name__ == "__main__":
    app.run()
