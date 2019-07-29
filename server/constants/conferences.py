# code used to make CONFERENCES constant below:
# CONFS = {c: dict(teams=[], **v) for c, v in CONFERENCES.items()}
# for team in js:
#     curr_conf, team_name = team['conference'], team['school']
#     if curr_conf in CONFS:
#         conf_teams = CONFS[curr_conf]['teams']
#         conf_teams.append(team_name)
#         CONFS[curr_conf]['teams'] = conf_teams
#
#         division = team['division']
#         if division:
#             conf_divisions = CONFS[curr_conf].get('divisions') or {}
#             if division in conf_divisions:
#                 div_teams = conf_divisions[division]
#                 div_teams.append(team_name)
#             else:
#                 conf_divisions[division] = [team_name]
#             CONFS[curr_conf]['divisions'] = conf_divisions
#
# print(CONFS)

DETAILED_CONFERENCES = {
    'ACC': {
        'teams': [
            'Boston College',
            'Clemson',
            'Duke',
            'Florida State',
            'Georgia Tech',
            'Louisville',
            'Miami',
            'NC State',
            'North Carolina',
            'Pittsburgh',
            'Syracuse',
            'Virginia',
            'Virginia Tech',
            'Wake Forest'
        ],
        'abbreviation': 'ACC',
        'id': 1,
        'name': 'ACC',
        'short_name': 'Atlantic Coast Conference',
        'divisions': {
            'Atlantic': [
                'Boston College',
                'Clemson',
                'Florida State',
                'Louisville',
                'NC State',
                'Syracuse',
                'Wake Forest'
            ],
            'Coastal': [
                'Duke',
                'Georgia Tech',
                'Miami',
                'North Carolina',
                'Pittsburgh',
                'Virginia',
                'Virginia Tech'
            ]
        }
    },
    'Big 12': {
        'teams': [
            'Baylor',
            'Iowa State',
            'Kansas',
            'Kansas State',
            'Oklahoma',
            'Oklahoma State',
            'TCU',
            'Texas',
            'Texas Tech',
            'West Virginia'
        ],
        'abbreviation': 'B12',
        'id': 4,
        'name': 'Big 12',
        'short_name': 'Big 12 Conference'
    },
    'Big Ten': {
        'teams': [
            'Illinois',
            'Indiana',
            'Iowa',
            'Maryland',
            'Michigan',
            'Michigan State',
            'Minnesota',
            'Nebraska',
            'Northwestern',
            'Ohio State',
            'Penn State',
            'Purdue',
            'Rutgers',
            'Wisconsin'
        ],
        'abbreviation': 'B1G',
        'id': 5,
        'name': 'Big Ten',
        'short_name': 'Big Ten Conference',
        'divisions': {
            'West': [
                'Illinois',
                'Iowa',
                'Minnesota',
                'Nebraska',
                'Northwestern',
                'Purdue',
                'Wisconsin'
            ],
            'East': [
                'Indiana',
                'Maryland',
                'Michigan',
                'Michigan State',
                'Ohio State',
                'Penn State',
                'Rutgers'
            ]
        }
    },
    'SEC': {
        'teams': [
            'Alabama',
            'Arkansas',
            'Auburn',
            'Florida',
            'Georgia',
            'Kentucky',
            'LSU',
            'Mississippi State',
            'Missouri',
            'Ole Miss',
            'South Carolina',
            'Tennessee',
            'Texas A&M',
            'Vanderbilt'
        ],
        'abbreviation': 'SEC',
        'id': 8,
        'name': 'SEC',
        'short_name': 'Southeastern Conference',
        'divisions': {
            'West': [
                'Alabama',
                'Arkansas',
                'Auburn',
                'LSU',
                'Mississippi State',
                'Ole Miss',
                'Texas A&M'
            ],
            'East': [
                'Florida',
                'Georgia',
                'Kentucky',
                'Missouri',
                'South Carolina',
                'Tennessee',
                'Vanderbilt'
            ]
        }
    },
    'Pac-12': {
        'teams': [
            'Arizona',
            'Arizona State',
            'California',
            'Colorado',
            'Oregon',
            'Oregon State',
            'Stanford',
            'UCLA',
            'USC',
            'Utah',
            'Washington',
            'Washington State'
        ],
        'abbreviation': 'PAC',
        'id': 9,
        'name': 'Pac-12',
        'short_name': 'Pac-12 Conference',
        'divisions': {
            'South': [
                'Arizona',
                'Arizona State',
                'Colorado',
                'UCLA',
                'USC',
                'Utah'
            ],
            'North': [
                'California',
                'Oregon',
                'Oregon State',
                'Stanford',
                'Washington',
                'Washington State'
            ]
        }
    },
    'Conference USA': {
        'teams': [
            'Charlotte',
            'Florida Atlantic',
            'Florida International',
            'Louisiana Tech',
            'Marshall',
            'Middle Tennessee',
            'North Texas',
            'Old Dominion',
            'Rice',
            'Southern Mississippi',
            'UAB',
            'UTEP',
            'UT San Antonio',
            'Western Kentucky'
        ],
        'abbreviation': 'CUSA',
        'id': 12,
        'name': 'Conference USA',
        'short_name': 'Conference USA',
        'divisions': {
            'East': [
                'Charlotte',
                'Florida Atlantic',
                'Florida International',
                'Marshall',
                'Middle Tennessee',
                'Old Dominion',
                'Western Kentucky'
            ],
            'West': [
                'Louisiana Tech',
                'North Texas',
                'Rice',
                'Southern Mississippi',
                'UAB',
                'UTEP',
                'UT San Antonio'
            ]
        }
    },
    'Mid-American': {
        'teams': [
            'Akron',
            'Ball State',
            'Bowling Green',
            'Buffalo',
            'Central Michigan',
            'Eastern Michigan',
            'Kent State',
            'Miami (OH)',
            'Northern Illinois',
            'Ohio',
            'Toledo',
            'Western Michigan'
        ],
        'abbreviation': 'MAC',
        'id': 15,
        'name': 'Mid-American',
        'short_name': 'Mid-American Conference',
        'divisions': {
            'East': [
                'Akron',
                'Bowling Green',
                'Buffalo',
                'Kent State',
                'Miami (OH)',
                'Ohio'
            ],
            'West': [
                'Ball State',
                'Central Michigan',
                'Eastern Michigan',
                'Northern Illinois',
                'Toledo',
                'Western Michigan'
            ]
        }
    },
    'Mountain West': {
        'teams': [
            'Air Force',
            'Boise State',
            'Colorado State',
            'Fresno State',
            "Hawai'i",
            'Nevada',
            'New Mexico',
            'San Diego State',
            'San José State',
            'UNLV',
            'Utah State',
            'Wyoming'
        ],
        'abbreviation': 'MWC',
        'id': 17,
        'name': 'Mountain West',
        'short_name': 'Mountain West Conference',
        'divisions': {
            'Mountain': [
                'Air Force',
                'Boise State',
                'Colorado State',
                'New Mexico',
                'Utah State',
                'Wyoming'
            ],
            'West': [
                'Fresno State',
                "Hawai'i",
                'Nevada',
                'San Diego State',
                'San José State',
                'UNLV'
            ]
        }
    },
    'FBS Independents': {
        'teams': [
            'Army',
            'BYU',
            'Notre Dame',
            'UMass'
        ],
        'abbreviation': 'Ind',
        'id': 18,
        'name': 'FBS Independents',
        'short_name': 'FBS Independents'
    },
    'Sun Belt': {
        'teams': [
            'Appalachian State',
            'Arkansas State',
            'Coastal Carolina',
            'Georgia Southern',
            'Georgia State',
            'Louisiana',
            'Louisiana Monroe',
            'South Alabama',
            'Texas State',
            'Troy'
        ],
        'abbreviation': 'SBC',
        'id': 37,
        'name': 'Sun Belt',
        'short_name': 'Sun Belt Conference'
    },
    'American Athletic': {
        'teams': [
            'Cincinnati',
            'Connecticut',
            'East Carolina',
            'Houston',
            'Memphis',
            'Navy',
            'SMU',
            'South Florida',
            'Temple',
            'Tulane',
            'Tulsa',
            'UCF'
        ],
        'abbreviation': 'AAC',
        'id': 151,
        'name': 'American Athletic',
        'short_name': 'American Athletic Conference',
        'divisions': {
            'East': [
                'Cincinnati',
                'Connecticut',
                'East Carolina',
                'South Florida',
                'Temple',
                'UCF'
            ],
            'West': [
                'Houston',
                'Memphis',
                'Navy',
                'SMU',
                'Tulane',
                'Tulsa'
            ]
        }
    },
    'Western': {
        'teams': [

        ],
        'abbreviation': 'Western',
        'id': 201,
        'name': 'Western',
        'short_name': 'Western Conference'
    },
    'Missouri Valley': {
        'teams': [

        ],
        'abbreviation': 'MVC',
        'id': 208,
        'name': 'Missouri Valley',
        'short_name': 'Missouri Valley Conference'
    },
    'Rocky Mountain': {
        'teams': [

        ],
        'abbreviation': 'RMC',
        'id': 203,
        'name': 'Rocky Mountain',
        'short_name': 'Rocky Mountain Conference'
    },
    'Southwest': {
        'teams': [

        ],
        'abbreviation': 'SWC',
        'id': 204,
        'name': 'Southwest',
        'short_name': 'Southwest Conference'
    },
    'Pacific': {
        'teams': [

        ],
        'abbreviation': 'PCC',
        'id': 205,
        'name': 'Pacific',
        'short_name': 'Pacific Coast Conference'
    },
    'Southern': {
        'teams': [

        ],
        'abbreviation': 'Southern',
        'id': 206,
        'name': 'Southern',
        'short_name': 'Southern Conference'
    },
    'Big 6': {
        'teams': [

        ],
        'abbreviation': 'Big 6',
        'id': 207,
        'name': 'Big 6',
        'short_name': 'Big 6 Conference'
    },
    'Mountain State': {
        'teams': [

        ],
        'abbreviation': 'MSAC',
        'id': 209,
        'name': 'Mountain State',
        'short_name': 'Mountain State Athletic Conference'
    },
    'Big 7': {
        'teams': [

        ],
        'abbreviation': 'Big 7',
        'id': 210,
        'name': 'Big 7',
        'short_name': 'Big 7 Conference'
    },
    'Skyline': {
        'teams': [

        ],
        'abbreviation': 'Skyline',
        'id': 211,
        'name': 'Skyline',
        'short_name': 'Skyline Conference'
    },
    'Ivy': {
        'teams': [

        ],
        'abbreviation': 'Ivy',
        'id': 212,
        'name': 'Ivy',
        'short_name': 'The Ivy League'
    },
    'AAWU': {
        'teams': [

        ],
        'abbreviation': 'AAWU',
        'id': 213,
        'name': 'AAWU',
        'short_name': 'Athletic Association of Western Universities'
    },
    'Big 8': {
        'teams': [

        ],
        'abbreviation': 'Big 8',
        'id': 214,
        'name': 'Big 8',
        'short_name': 'Big 8 Conference'
    },
    'Western Athletic': {
        'teams': [

        ],
        'abbreviation': 'WAC',
        'id': 215,
        'name': 'Western Athletic',
        'short_name': 'Western Athletic Conference'
    },
    'Pac-8': {
        'teams': [

        ],
        'abbreviation': 'Pac-8',
        'id': 216,
        'name': 'Pac-8',
        'short_name': 'Pacific 8 Conference'
    },
    'PCAA': {
        'teams': [

        ],
        'abbreviation': 'PCAA',
        'id': 217,
        'name': 'PCAA',
        'short_name': 'Pacific Coast Athletic Association'
    },
    'Southland': {
        'teams': [

        ],
        'abbreviation': 'Southland',
        'id': 218,
        'name': 'Southland',
        'short_name': 'Southland Conference'
    },
    'SWAC': {
        'teams': [

        ],
        'abbreviation': 'SWAC',
        'id': 219,
        'name': 'SWAC',
        'short_name': 'Southwest Athletic Conference'
    },
    'Pac-10': {
        'teams': [

        ],
        'abbreviation': 'Pac-10',
        'id': 220,
        'name': 'Pac-10',
        'short_name': 'Pacific 10'
    },
    'Big West': {
        'teams': [

        ],
        'abbreviation': 'BW',
        'id': 221,
        'name': 'Big West',
        'short_name': 'Big West Conference'
    },
    'Big East': {
        'teams': [

        ],
        'abbreviation': 'BE',
        'id': 222,
        'name': 'Big East',
        'short_name': 'Big East Conference'
    },
    'Border': {
        'teams': [

        ],
        'abbreviation': 'BIAA',
        'id': 223,
        'name': 'Border',
        'short_name': 'Border Intercollegiate Athletic Association'
    }
}

# TODO -- HOW TO DO THIS??

MAJOR_CONFERENCES = {'ACC', 'Big 12', 'Big Ten', 'SEC', 'Pac-12', 'Conference USA', 'Mid-American', 'Mountain West',
                     'Sun Belt', 'American Athletic'}

CONFERENCES = {k: v for k, v in DETAILED_CONFERENCES.items() if k in MAJOR_CONFERENCES}
