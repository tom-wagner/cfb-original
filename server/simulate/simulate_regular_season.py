from typing import Dict, List
from statistics import mean
from collections import Counter
from random import random as rand_float

from server.constants.likelihoods import LIKELIHOODS
from server.constants.teams import TEAMS
from server.external_apis.cf_data import CFData
from server.ratings.inputs.data.team_ratings import TEAM_RATINGS


def trim_game(game: Dict) -> Dict:
    return {'home_team': game['home_team'], 'away_team': game['away_team'], 'neutral_site': game['neutral_site']}


def add_ratings_and_simulate(game, team_ratings):
    adj_game = add_ratings_to_game(game, team_ratings)
    simulated_game = simulate_game(adj_game)
    return simulated_game


def simulate_game(game):
    home_team, away_team = game['home_team'], game['away_team']
    winner = game['home_team'] if game['home_team_win_pct'] > rand_float() else game['away_team']
    are_both_teams_division_one = TEAMS.get(home_team) and TEAMS.get(away_team)
    is_conf_game = are_both_teams_division_one and TEAMS[home_team]['conference'] == TEAMS[away_team]['conference']
    return dict(winner=winner, is_conf_game=is_conf_game)


def add_ratings_to_game(game: Dict, team_ratings: Dict) -> Dict:
    adj_game = add_proj_margin_to_game(game, team_ratings)
    return adj_game


def get_net_power_rating(ratings: Dict) -> float:
    return mean([rating for rating in ratings.values()])


def set_default_margin(game, teams_dict, home_team, away_team):
    """Add a default margin if one of the teams is not rated by S&P+"""
    # TODO: Add some logic that factors in the known teams S&P+
    # Ex: Gophers favored by 20-25 over FBS team but Alamaba favored by way more
    DEFAULT_MARGIN = 28
    return DEFAULT_MARGIN if home_team in teams_dict else -DEFAULT_MARGIN


def add_proj_margin_to_game(game, team_ratings):
    home_team, away_team = game['home_team'], game['away_team']
    if home_team in team_ratings and away_team in team_ratings:
        home_team_ratings, away_team_ratings = team_ratings[home_team], team_ratings[away_team]
        game['away_team_rtgs'], game['home_team_rtgs'] = home_team_ratings, away_team_ratings
        ht_net_power, at_net_power = (get_net_power_rating(r) for r in (home_team_ratings, away_team_ratings))
        game['ht_net_power_rtg'], game['away_team_net_power_rtg'] = ht_net_power, at_net_power

        if not game['neutral_site']:
            game['home_team_projected_margin'] = round(ht_net_power + 2.5 - at_net_power, 1)
        else:
            game['home_team_projected_margin'] = round(ht_net_power - at_net_power, 1)

    else:
        game['home_team_projected_margin'] = set_default_margin(game, team_ratings, home_team, away_team)

    proj_margin = game['home_team_projected_margin']
    game['home_team_win_pct'] = LIKELIHOODS[proj_margin] if proj_margin > 0 else 1 - LIKELIHOODS[abs(proj_margin)]
    return game


def get_empty_wins_dict():
    return {x: 0 for x in range(14)}


class SimulateRegularSeason:
    def __init__(self, year: int, conference: str):
        self.schedule = self.transform_schedule(year, conference)
        self.simulation_results = {
            team: {
                'conference_results': get_empty_wins_dict(),
                'non_conference_results': get_empty_wins_dict(),
                'total_wins': get_empty_wins_dict(),
            }
            for team in TEAM_RATINGS.keys()
        }

    @staticmethod
    def transform_schedule(year: int, conference: str):
        raw_schedule = CFData().get_schedule(year=year, conference=conference)
        trimmed_schedule = [trim_game(g) for g in raw_schedule]
        # TODO: Consider passing a parameter here to add_ratings called `ratings_to_include` and make it a set of the
        # ratings that should be included in the simulation
        augmented_schedule = [add_ratings_to_game(game, TEAM_RATINGS) for game in trimmed_schedule]
        return augmented_schedule

    def run(self, num_of_sims: int):
        for _ in range(num_of_sims):
            simulated_season = [simulate_game(game) for game in self.schedule]

            conf_games, nc_games = [], []
            for game in simulated_season:
                conf_games.append(game['winner']) if game['is_conf_game'] else nc_games.append(game['winner'])
            conf_wins, nc_wins = Counter(conf_games), Counter(nc_games)
            total_wins = dict(conf_wins+nc_wins)

            for season_segment, results in (
                    ('conference_results', conf_wins), ('non_conference_results', nc_wins), ('total_wins', total_wins)):
                for k, v in results.items():
                    if self.simulation_results.get(k):
                        self.simulation_results[k][season_segment][v] += 1


# s = SimulateRegularSeason(year=2019, conference='B1G')
# s.run(10)
#
# # TODO: Simulation results appear to be underestimating good teams --> see Ohio State and Michigan, are they working?
# print(s.simulation_results)
