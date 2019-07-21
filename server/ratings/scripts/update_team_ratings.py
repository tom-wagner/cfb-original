import csv
from typing import Dict

from server.constants.constants import CFD, SP_PLUS, FPI, ENTROPY, MASSEY
from server.constants.team_map import team_map

RATINGS_ORDER_IN_CSV = [CFD, SP_PLUS, FPI, ENTROPY, MASSEY]


# def convert_csv_to_json(csv_file: any) -> Dict:
#     """return a dict that includes the teams spelling for each of the selected ratings sources"""
#     next(csv_file)  # skip headers
#     return {row[0]: {rtg_service: team for rtg_service, team in zip(RATINGS_ORDER_IN_CSV, row)} for row in csv_file}
#
#
# # encoding: https://stackoverflow.com/a/49150749
# with open('../inputs/team_map.csv', encoding='utf-8-sig') as teams_file:
#     csv_reader = csv.reader(teams_file, delimiter=',')
#     team_strings = convert_csv_to_json(csv_reader)
#
#     # for now ==> copy to team_map and use formatter
#     print(team_strings)


def get_csv_data_for_path(file_path: str) -> any:
    with open(file_path, encoding='utf-8-sig') as file:
        csv_reader = csv.reader(file, delimiter=',')
        rating_system = next(csv_reader)[1]
        return rating_system, [row for row in csv_reader]


def read_csvs(files_to_read: Dict):
    res = {team: {} for team in team_map}
    for k, v in files_to_read.items():
        rating_system, file_data = get_csv_data_for_path(v)
        print(rating_system)
        print(team_map[rating_system])
        for row in file_data:
            pass
            # print(row)


BASE_PATH = "../inputs/data"
file_paths_dict = dict(SP_PLUS=f'{BASE_PATH}/{SP_PLUS}.csv',
                       FPI=f'{BASE_PATH}/{FPI}.csv',
                       ENTROPY=f'{BASE_PATH}/{ENTROPY}.csv',
                       MASSEY=f'{BASE_PATH}/{MASSEY}.csv')

read_csvs(file_paths_dict)
