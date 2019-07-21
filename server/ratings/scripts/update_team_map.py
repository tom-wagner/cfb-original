import csv
from typing import Dict
from server.constants.constants import CFD, SP_PLUS, FPI, ENTROPY, MASSEY, FIVE_DIMES

# NOTE -- THE FIRST ROW IN CSV MUST MATCH THESE VARIABLES
RATINGS_ORDER_IN_CSV = [CFD, SP_PLUS, FPI, ENTROPY, FIVE_DIMES, MASSEY]


def convert_csv_to_json(csv_file: any) -> Dict:
    """return a dict that includes the teams spelling for each of the selected ratings sources"""
    row_one = next(csv_file)  # skip headers
    adj_csv_file = [[team if team != 'null' else None for team in row] for row in csv_file]  # convert 'null' to None
    return {
        r: {row[idx]: {rtg_service: team
            for rtg_service, team in zip(RATINGS_ORDER_IN_CSV, row)}
            for row in adj_csv_file}
        for idx, r in enumerate(row_one)
    }


# encoding: https://stackoverflow.com/a/49150749
with open('../inputs/team_map.csv', encoding='utf-8-sig') as teams_file:
    csv_reader = csv.reader(teams_file, delimiter=',')
    team_strings = convert_csv_to_json(csv_reader)

    # for now ==> copy to team_map and use formatter
    print(team_strings)
