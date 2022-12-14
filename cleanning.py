#Import libraries
from zlib import DEF_BUF_SIZE
import mysql.connector
import pandas as pd
import numpy as np

# GAMES DETAILS
def games_details_cleanning():
    gd = pd.read_csv('data/games_details.csv')
    game_details = gd.drop(['TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_NAME', 'REB'], axis = 1)
    game_details['ID'] = np.arange(len(game_details))
    game_details = game_details.reindex(columns=['ID','GAME_ID','TEAM_ID','PLAYER_ID','START_POSITION','COMMENT','MIN','FGM','FGA','FG_PCT','FG3M','FG3A','FG3_PCT','FTM','FTA','FT_PCT','OREB','DREB','AST','STL','BLK','TO_','PF','PTS','PLUS_MINUS'])
    game_details = game_details.fillna(0)
    game_details.to_csv('data_cleanned/game_details_db.csv',index = False)

# GAMES
def games():
    games = pd.read_csv('data/games.csv')
    years = games.SEASON.unique()
    years.sort()
    season = pd.DataFrame()
    season['Year'] = years
    games = games.drop(['GAME_DATE_EST', 'TEAM_ID_home', 'TEAM_ID_away'], axis = 1)
    games.rename(columns={"SEASON": "SEASON_ID"}, inplace=True)
    
    for i, val in enumerate(season.values):
        games.loc[games['SEASON_ID'] == val[0], 'SEASON_ID'] = i
    

    games = games.reindex(columns = ['GAME_ID','GAME_STATUS_TEXT', 'SEASON_ID', 'HOME_TEAM_ID', 'PTS_home', 'FG_PCT_home', 'FT_PCT_home', 'FG3_PCT_home', 'AST_home', 'REB_home', 'VISITOR_TEAM_ID', 'PTS_away', 'FG_PCT_away', 'FT_PCT_away', 'FG3_PCT_away', 'AST_away', 'REB_away', 'HOME_TEAM_WINS'])
    games = games.fillna(0)
    games.to_csv('data_cleanned/games_db.csv',index = False)

# TEAM
def teams():
    teams = pd.read_csv('data/teams.csv')
    teams = teams.drop(['ARENA', 'ARENACAPACITY'], axis = 1)
    
    teams = teams.rename(columns = {'CITY':'TEAM_NAME'})
    teams['CITY_ID'] = [0, 1, 2, 3, 4, 5, 6, 8, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29] 
    teams = teams.reindex(columns=['TEAM_ID','TEAM_NAME','ABBREVIATION','NICKNAME','YEARFOUNDED','MIN_YEAR', 'MAX_YEAR', 'CITY_ID', 'OWNER','GENERALMANAGER','HEADCOACH','LEAGUE_ID','DLEAGUEAFFILIATION'])
    teams.to_csv('data_cleanned/teams_db.csv',index = False)

# SEASON
def season():
    games = pd.read_csv('data/games.csv')
    years = games.SEASON.unique()
    years.sort()
    season = pd.DataFrame()
    season['YEAR'] = years
    season['SEASON_ID'] = np.arange(0, 18)

    season = season.reindex(columns = ['SEASON_ID', 'YEAR'])
    season.to_csv('data_cleanned/season.csv', index = False)

# PLAYERS AT TEAM
def players_at_team():
    games = pd.read_csv('data/games.csv')
    years = games.SEASON.unique()
    years.sort()
    season = pd.DataFrame()
    season['Year'] = years
    players_d = pd.read_csv('data/players.csv')
    joined = players_d[players_d['SEASON'] == 2019].copy()
    
    for i, val in enumerate(season.values):
        players_d.loc[players_d['SEASON'] == val[0], 'SEASON'] = i
    
    players_at_team_in_season = players_d.rename(columns = {'SEASON':'SEASON_ID'})
    players_at_team_in_season['ID'] = np.arange(len(players_at_team_in_season))
    players_at_team_in_season = players_at_team_in_season.reindex()
    column = list(players_at_team_in_season.columns)
    column[0], column[1], column[2], column[3], column[4] = column[4], column[0], column[1], column[2], column[3]
    players_at_team_in_season = players_at_team_in_season[column]

    players_at_team_in_season = players_at_team_in_season.reindex(columns=['ID','PLAYER_ID','TEAM_ID','SEASON_ID'])
    players_at_team_in_season.to_csv('data_cleanned/players_at_team_in_season.csv', index = False)

# PLAYERS TABLE
def players():
    players = pd.read_csv('data/players.csv')
    players = players.drop(['TEAM_ID', 'SEASON'], axis = 1)
    players = players.reindex(columns=['PLAYER_ID','PLAYER_NAME'])

    players.to_csv('data_cleanned/players_db.csv',index = False)

# ARENAS
def arenas():
    arenas = pd.DataFrame()
    teams = pd.read_csv('data/teams.csv')
    arenas['ARENA_NAME'] =  teams['ARENA']
    arenas['ARENACAPACITY'] = teams['ARENACAPACITY'].fillna(0)
    arenas['ARENA_ID'] = np.arange(len(arenas))
    
    arenas = arenas.reindex(columns = ['ARENA_ID','ARENA_NAME','ARENACAPACITY'])
    arenas.to_csv('data_cleanned/arenas.csv',index = False)

# CITIES
def cities():
    teams = pd.read_csv('data/teams.csv')
    arenas = pd.read_csv('data_cleanned/arenas.csv')
    cities = pd.DataFrame()

    cities['CITY_NAME'] = teams['CITY']
    cities['ARENA_ID'] = arenas['ARENA_ID']

    cities['CITY_ID'] = np.arange(len(cities))

    cities = cities.reindex(columns=['CITY_ID','CITY_NAME','ARENA_ID'])

    cities.to_csv('data_cleanned/cities.csv',index = False)