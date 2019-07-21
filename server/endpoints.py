from flask import Flask, json
from flask_cors import CORS
from server.ratings.inputs.data.team_ratings import TEAM_RATINGS

app = Flask(__name__)
CORS(app)


@app.route("/")
def index():
    return json.jsonify(TEAM_RATINGS)


app.run(debug=True)
