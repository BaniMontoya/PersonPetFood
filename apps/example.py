from flask_classful import FlaskView, route
from flask import Flask

app = Flask(__name__)


class TestView(FlaskView):

    def index(self):
        return "<h1>Index</h1>"

    @route('/hello/<world>/')
    def bsicname(self, super):
        return f"<h1>hello world {super}</h1>"


TestView.register(app, route_base='/')


if __name__ == "__main__":
    app.run(debug=True)
