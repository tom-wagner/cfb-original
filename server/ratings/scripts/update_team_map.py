import csv
from typing import Dict, List
from server.constants.constants import CFD, SP_PLUS, FPI, ENTROPY, MASSEY

RATINGS_ORDER_IN_CSV = [CFD, SP_PLUS, FPI, ENTROPY, MASSEY]


def convert_csv_to_json(csv_file: any) -> Dict:
    """return a dict that includes the teams spelling for each of the selected ratings sources"""
    next(csv_file)  # skip headers
    return {row[0]: {rtg_service: team for rtg_service, team in zip(RATINGS_ORDER_IN_CSV, row)} for row in csv_file}


# encoding: https://stackoverflow.com/a/49150749
with open('../inputs/team_map.csv', encoding='utf-8-sig') as teams_file:
    csv_reader = csv.reader(teams_file, delimiter=',')
    team_strings = convert_csv_to_json(csv_reader)

    # for now ==> copy to team_map and use formatter
    print(team_strings)
