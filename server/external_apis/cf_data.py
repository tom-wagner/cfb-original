import requests

BASE_CFD_API = "https://api.collegefootballdata.com"


class CFData:
    def __init__(self):
        self.base_path = BASE_CFD_API

    def get(self, route: str, **params):
        resp = requests.get(f'{self.base_path}/{route}', params=params)
        return resp

    def get_schedule(self, year: int):
        return self.get("games", year=year).json()

