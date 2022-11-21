#pip3 install mysql-connector-python
import mysql.connector
import modules as md
import cleanning as cl
import insertion as ins
import os


try:
    os.system('mkdir data_cleanned')
except:
    pass

#DATA CLEANNING
cl.games_details_cleanning()

cl.games()

cl.teams()

cl.season()

cl.players_at_team()

cl.players()

cl.arenas()

cl.cities()


#DATA INFRASTRUCTURE
mydb = md.login()

#create our db
try:
    md.delete_NBA_db(mydb)
    md.create_NBA_db(mydb)
except:
    pass

#verify if it exists
md.show_db(mydb)

#Arenas table
md.Arenas_T(mydb)

#Cities table
md.Cities_T(mydb)

#Teams table
md.Teams_T(mydb)

#Games Table
md.game_t(mydb)

#seasons Table
md.Seasons_T(mydb)

#players Table
md.Players_T(mydb)

#players at team in season
md.player_at_the_season(mydb)

#game Datails
md.Game_details_T(mydb)

#show tables
md.show_tables(mydb)

#relations
md.relations_NBA_DB(mydb)

#looks relations
md.look_relation_NBA_DB(mydb)

print('\nDatabase, tables and relationships have been created succesfully!')

#data insertion
ins.insertion()

print('\n\nData was inserted succesfully!')

#create our S db
try:
    md.delete_SNBA_db(mydb)
    md.create_SNBA_db(mydb)
except:
    pass

#start squema - only tables
md.building_SNBA(mydb)

#relations SNBA_DB
md.relations_SNBA_DB(mydb)

#look star schema relationships
md.look_relation_SNBA_DB(mydb)

print('\n\n\nDatabase, tables and relationships have been created succesfully (STAR SCHEMA)!')

# copy data from old schema to start squema
md.copy_data_to_new_squema(mydb)

print('\n\n All data has been migrated to new Squema!')






