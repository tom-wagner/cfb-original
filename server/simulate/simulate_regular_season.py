from typing import Dict
from statistics import mean
from collections import Counter
from random import random as rand_float

from server.constants.likelihoods import LIKELIHOODS
from server.external_apis.cf_data import CFData
from server.ratings.inputs.data.team_ratings import TEAM_RATINGS


def trim_game(game: Dict) -> Dict:
    return {'home_team': game['home_team'], 'away_team': game['away_team'], 'neutral_site': game['neutral_site']}


def add_ratings_and_simulate(game, team_ratings):
    adj_game = add_ratings_to_game(game, team_ratings)
    simulated_game = simulate_game(adj_game)
    return simulated_game


def simulate_game(game):
    return game['home_team'] if game['home_team_win_pct'] > rand_float() else game['away_team']


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


class SimulateRegularSeason:
    def __init__(self, year: int):
        self.schedule = CFData().get_schedule(year=year)
        self.simulation_results = {team: {x: 0 for x in range(14)} for team in TEAM_RATINGS.keys()}
        self.trim_schedule()
        # TODO: Consider passing a parameter here to add_ratings called `ratings_to_include` and make it a set of the
        # ratings that should be included in the simulation
        self.add_ratings()

    def run(self, num_of_sims: int):
        for _ in range(num_of_sims):
            simulated_season = [simulate_game(game) for game in self.schedule]
            wins = Counter(simulated_season)
            for k, v in wins.items():
                if self.simulation_results.get(k):
                    self.simulation_results[k][v] += 1

    def add_ratings(self):
        self.schedule = [add_ratings_to_game(game, TEAM_RATINGS) for game in self.schedule]

    def trim_schedule(self):
        self.schedule = [trim_game(g) for g in self.schedule]


# s = SimulateRegularSeason(2019)
# s.run(10000)
#
# # TODO: Simulation results appear to be underestimating good teams --> see Ohio State and Michigan, are they working?
# print(s.simulation_results)
