import pandas as pd
import numpy as np
import os

year = input("Year: ")
csv = "data/matches/" + year + ".csv"

matches = pd.read_csv(csv)

columns = ['Team', 'GamesPlayed', 'Points', 'GoalsFor', 'GoalsAgainst', 'GoalDifference', 'Shots', 'ShotsPerGame']

#create dataframe
df = pd.DataFrame(columns=columns)

def parsedata():
    global df
    for row in matches.itertuples():
        points(row)
        goals(row)
        shots(row)
    for row in df.itertuples():
        df.at[row.Index, 'ShotsPerGame'] = row.Shots/38
    df = df.sort_values('Points', ascending=False)
    df = df.reset_index(drop=True)

#points data from row
def points(row):
    global df
    result = row.FTR
    home = row.HomeTeam
    away = row.AwayTeam

    if home not in df.Team.values:
        df = df.append({'Team': home, 'GamesPlayed': 0, 'Points': 0, 'GoalsFor': 0, 'GoalsAgainst': 0, 'GoalDifference': 0, 'Shots':0}, ignore_index=True)
    if away not in df.Team.values:
        df = df.append({'Team': away, 'GamesPlayed': 0, 'Points': 0, 'GoalsFor': 0, 'GoalsAgainst': 0, 'GoalDifference': 0, 'Shots':0}, ignore_index=True)

    if result == 'H':
        df.loc[df.index[df['Team'] == home], 'Points'] += 3
    elif result == 'A':
        df.loc[df.index[df['Team'] == away], 'Points'] += 3
    else:
        df.loc[df.index[df['Team'] == home], 'Points'] += 1
        df.loc[df.index[df['Team'] == away], 'Points'] += 1

    df.loc[df.index[df['Team'] == home], 'GamesPlayed'] += 1
    df.loc[df.index[df['Team'] == away], 'GamesPlayed'] += 1

def goals(row):
    global df
    homegoals = row.FTHG
    awaygoals = row.FTAG
    home = row.HomeTeam
    away = row.AwayTeam
    df.loc[df.index[df['Team'] == home], 'GoalsFor'] += homegoals
    df.loc[df.index[df['Team'] == home], 'GoalsAgainst'] += awaygoals
    df.loc[df.index[df['Team'] == away], 'GoalsFor'] += awaygoals
    df.loc[df.index[df['Team'] == away], 'GoalsAgainst'] += homegoals

    df.loc[df.index[df['Team'] == home], 'GoalDifference'] += homegoals-awaygoals
    df.loc[df.index[df['Team'] == away], 'GoalDifference'] += awaygoals-homegoals

def shots(row):
    global df
    home = row.HomeTeam
    away = row.AwayTeam

    df.loc[df.index[df['Team'] == home], 'Shots'] += row.HS
    df.loc[df.index[df['Team'] == away], 'Shots'] += row.AS




def tocsv():
    outname = year + '.csv'

    outdir = './data/standings'

    fullname = os.path.join(outdir, outname)    

    df.to_csv(fullname)

parsedata()
tocsv()