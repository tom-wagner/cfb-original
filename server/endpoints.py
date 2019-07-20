import flask
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return "Yes!!"


app.run(debug=True)
