import mysql.connector
import pandas as pd
import numpy as np
import getpass
import os


# READING CSVs
arenas_db = pd.read_csv('data_cleanned/arenas.csv',index_col=False)
cities_db = pd.read_csv('data_cleanned/cities.csv',index_col=False)
game_details_db = pd.read_csv('data_cleanned/game_details_db.csv',index_col=False)
games_db = pd.read_csv('data_cleanned/games_db.csv',index_col=False)
players_at_team_in_season_db = pd.read_csv('data_cleanned/players_at_team_in_season.csv',index_col=False)
players_db = pd.read_csv('data_cleanned/players_db.csv',index_col=False)
season_db = pd.read_csv('data_cleanned/season.csv',index_col=False)
teams_db = pd.read_csv('data_cleanned/teams_db.csv',index_col=False)

print(arenas_db.columns,'\n*********\n',cities_db.columns,'\n*********\n',game_details_db.columns,'\n*********\n',games_db.columns,'\n*********\n',players_at_team_in_season_db.columns,'\n*********\n',players_db.columns,'\n*********\n',season_db.columns,'\n*********\n',teams_db.columns)


"""# GETTING USER AUTHENTICATION
user = input('User: ')
password = getpass.getpass("password: ")

# STABLISHING CONNECTION TO THE DATABSE
connection = mysql.connector.connect(host='localhost',
                                            database='NBA_DB',
                                            user=user,
                                            password=password)



mySql_insert_query = INSERT INTO Arenas (ARENA_ID, ARENA_NAME, ARENACAPACITY) 
                            VALUES (%s, %s, %s) 

records_to_insert = arenas_db.to_numpy().tolist()

cursor = connection.cursor()
cursor.executemany(mySql_insert_query, records_to_insert)
connection.commit()

cursor.close()
connection.close()"""
