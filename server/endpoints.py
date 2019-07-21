import requests
from flask import Flask, json, request
from flask_cors import CORS

from server.external_apis.cf_data import CFData
from server.ratings.inputs.data.team_ratings import TEAM_RATINGS

app = Flask(__name__)
CORS(app)


@app.route("/teams", method=['GET'])
def index():
    return json.jsonify(TEAM_RATINGS)


@app.route("/schedule", methods=['GET'])
def schedule():
    try:
        res = CFData().get("games", year=request.args.get('year'))
        return json.jsonify(res.json())

    # TODO: Improve error handling and consider moving to CFData file or base_api.py file
    # https://stackoverflow.com/questions/16511337/correct-way-to-try-except-using-python-requests-module
    except Exception as e:
        return dict(error="Error fetching schedule", detail=e)


app.run(debug=True)
