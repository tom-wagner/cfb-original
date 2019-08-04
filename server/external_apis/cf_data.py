import requests

from server.constants.team_map import TEAM_MAP

BASE_CFD_API = "https://api.collegefootballdata.com"


class CFData:
    def __init__(self):
        self.base_path = BASE_CFD_API

    def get(self, route: str, **params):
        return requests.get(f'{self.base_path}/{route}', params=params)

    def get_schedule(self, year: int, conference: str):
        if conference:
            return self.get("games", year=year, conference=conference).json()
        return self.get("games", year=year).json()

    def get_teams(self):
        return self.get("teams").json()
