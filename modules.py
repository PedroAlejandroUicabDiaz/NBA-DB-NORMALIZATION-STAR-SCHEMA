import os
import mysql.connector
import getpass

#get password
def get_password(): 
    password = getpass.getpass("password: ")
    return password

#loggin
def login():
    user = input('User: ')
    password = get_password()
    mydb = mysql.connector.connect(
    host="localhost",
    user=user,
    password=password
    )
    return mydb

#verify if our bd exists
def show_db(mydb):
    c = mydb.cursor()
    c.execute("SHOW DATABASES")
    for dbs in c:
        if dbs[0] ==  'NBA_DB':
            print('The datase already exists')
        else:
            pass

#creating our NBA db
def create_NBA_db(mydb):
    c = mydb.cursor()
    c.execute("CREATE DATABASE NBA_DB")
    print("Database NBA_DB has been created")

#creating our STAR NBA db
def create_SNBA_db(mydb):
    c = mydb.cursor()
    c.execute("CREATE DATABASE S_NBA_DB")
    print("Database STAR NBA has been created")

#making game table
def game_t(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')
    try:
        structure = "GAME_ID int NOT NULL,\
                    GAME_STATUS_TEXT CHAR(50) NOT NULL,\
                    SEASON_ID int NOT NULL,\
                    HOME_TEAM_ID int NOT NULL,\
                    PTS_home float,\
                    FG_PCT_home float,\
                    FT_PCT_home float,\
                    FG3_PCT_home float,\
                    AST_home float,\
                    REB_home float,\
                    VISITOR_TEAM_ID int NOT NULL,\
                    PTS_away float,\
                    FG_PCT_away float,\
                    FT_PCT_away float,\
                    FG3_PCT_away float,\
                    AST_away float,\
                    REB_away float,\
                    HOME_TEAM_WINS boolean NOT NULL,\
                    PRIMARY KEY (GAME_ID)"
        c.execute(f'CREATE TABLE Games ({structure})')
    except:
        pass
  
#making Arenas table
def Arenas_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')
    #try to build
    try:
        structure = "ARENA_ID int NOT NULL,\
                    ARENA_NAME char(50) NOT NULL,\
                    ARENACAPACITY float NOT NULL,\
                    PRIMARY KEY (ARENA_ID )"
        c.execute(f'CREATE TABLE Arenas ({structure})')
    #if it exists just pass
    except:
        #print('Algo paso')
        pass  

#Making cities table
def Cities_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "CITY_ID int NOT NULL,\
                    CITY_NAME char(50) NOT NULL,\
                    ARENA_ID int NOT NULL,\
                    PRIMARY KEY (CITY_ID)"
        c.execute(f'CREATE TABLE Cities ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass
    
#Making Teams table
def Teams_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')
    
    #try to build
    try:
        structure = "TEAM_ID int NOT NULL,\
                    TEAM_NAME char(50) NOT NULL,\
                    ABBREVIATION char(10) NOT NULL,\
                    NICKNAME char(50) NOT NULL,\
                    YEARFOUNDED int NOT NULL,\
                    MIN_YEAR int NOT NULL,\
                    MAX_YEAR int NOT NULL,\
                    CITY_ID int NOT NULL,\
                    OWNER char(50) NOT NULL,\
                    GENERALMANAGER char(50) NOT NULL,\
                    HEADCOACH char(50) NOT NULL,\
                    LEAGUE_ID char(50) NOT NULL,\
                    DLEAGUEAFFILIATION char(50) NOT NULL,\
                    PRIMARY KEY (TEAM_ID)"
        c.execute(f'CREATE TABLE Teams ({structure})')

    #if it exists just pass
    except:
        pass
    
#Making Seasons table
def Seasons_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "SEASON_ID int NOT NULL,\
                    YEAR int NOT NULL,\
                    PRIMARY KEY (SEASON_ID)"
        c.execute(f'CREATE TABLE Seasons ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass
    
#Making PLayers table
def Players_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "PLAYER_ID int NOT NULL,\
                    PLAYER_NAME char(50) NOT NULL,\
                    PRIMARY KEY (PLAYER_ID)"
        c.execute(f'CREATE TABLE Players ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass

#Making players at team table
def player_at_the_season(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "ID int NOT NULL,\
                    PLAYER_ID int NOT NULL,\
                    TEAM_ID int NOT NULL,\
                    SEASON_ID int NOT NULL,\
                    PRIMARY KEY (ID)"

        c.execute(f'CREATE TABLE Players_at_team_in_season ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass
    
#Making Game_details table
def Game_details_T(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #try to build
    try:
        structure = "ID int NOT NULL,\
                    GAME_ID int NOT NULL,\
                    TEAM_ID int NOT NULL,\
                    PLAYER_ID int NOT NULL,\
                    START_POSITION char(50),\
                    COMMENT char(200),\
                    MIN char(50),\
                    FGM float,\
                    FGA float,\
                    FG_PCT float,\
                    FG3M float,\
                    FG3A float,\
                    FG3_PCT float,\
                    FTM float,\
                    FTA float,\
                    FT_PCT float,\
                    OREB float,\
                    DREB float,\
                    AST float,\
                    STL float,\
                    BLK float,\
                    TO_ float,\
                    PF float,\
                    PTS float,\
                    PLUS_MINUS float,\
                    PRIMARY KEY (ID)"

        c.execute(f'CREATE TABLE Game_details ({structure})')

    #if it exists just pass
    except:
        #print('Algo paso ')
        pass
    
#delete our NBA db
def delete_NBA_db(mydb):
    c = mydb.cursor()
    c.execute('DROP DATABASE IF EXISTS NBA_DB')

#delete our db
def delete_SNBA_db(mydb):
    c = mydb.cursor()
    c.execute('DROP DATABASE IF EXISTS S_NBA_DB')

#show tables
def show_tables(mydb):
    c = mydb.cursor()
    c.execute('SHOW TABLES')
    print("Tables: ")
    for i in c:
        print(i)

# CREATING TABLES FOR STAR SQUEMA
def building_SNBA(mydb):

    #Season
    def Season_s(mydb):
        c = mydb.cursor()
        c.execute('USE S_NBA_DB')

        try:
            structure = "SEASON_ID int NOT NULL,\
                        YEAR int NOT NULL,\
                        PRIMARY KEY (SEASON_ID)"
            c.execute(f'CREATE TABLE Season ({structure})')
            print("Season created.")
        except:
            pass

    #Games
    def Games_s(mydb):
        c = mydb.cursor()
        c.execute('USE S_NBA_DB')

        try:
            structure = "GAME_ID int NOT NULL,\
                        GAME_STATUS_TEXT char(50) NOT NULL,\
                        TEAM_NAME_home char(50) NOT NULL,\
                        CITY_NAME_home char(50) NOT NULL,\
                        ARENA_NAME_home char(50) NOT NULL,\
                        PTS_home float,\
                        FG_PCT_home float,\
                        FT_PCT_home float,\
                        FG3_PCT_home float,\
                        AST_home float,\
                        REB_home float,\
                        VISITOR_TEAM_ID int NOT NULL,\
                        PTS_away float,\
                        FG_PCT_away float,\
                        FT_PCT_away float,\
                        FG3_PCT_away float,\
                        AST_away float,\
                        REB_away float,\
                        HOME_TEAM_WINS boolean NOT NULL,\
                        PRIMARY KEY (GAME_ID)"
            c.execute(f'CREATE TABLE Game ({structure})')

            print("Games created.")
        except:
            pass

    #Player
    def Player_s(mydb):
        c = mydb.cursor()
        c.execute('USE S_NBA_DB')

        try:
            structure = "PLAYER_ID int NOT NULL,\
                        PLAYER_NAME char(50) NOT NULL,\
                        PRIMARY KEY (PLAYER_ID)"
            c.execute(f'CREATE TABLE Player ({structure})')
            print("Player created.")
        except:
            pass

    #Teams
    def Teams_s(mydb):
        c = mydb.cursor()
        c.execute('USE S_NBA_DB')

        try:
            structure = "TEAM_ID int NOT NULL,\
                        TEAM_NAME char(50) NOT NULL,\
                        ABBREVIATION char(10) NOT NULL,\
                        NICKNAME char(50) NOT NULL,\
                        YEARFOUNDED int NOT NULL,\
                        MIN_YEAR int NOT NULL,\
                        MAX_YEAR int NOT NULL,\
                        CITY_NAME char(50) NOT NULL,\
                        ARENA_NAME char(50) NOT NULL,\
                        ARENACAPACITY float NOT NULL,\
                        OWNER char(50) NOT NULL,\
                        GENERALMANAGER char(50) NOT NULL,\
                        HEADCOACH char(50) NOT NULL,\
                        LEAGUE_ID char(50) NOT NULL,\
                        DLEAGUEAFFILIATION char(50) NOT NULL,\
                        PRIMARY KEY (TEAM_ID)"
            c.execute(f'CREATE TABLE Teams ({structure})')
            print("Teams created.")
        except:
            pass

    #Statistics
    def Statistics_s(mydb):
        c = mydb.cursor()
        c.execute('USE S_NBA_DB')

        try:
            structure = "ID int AUTO_INCREMENT,\
                        PLAYER_ID int NOT NULL,\
                        SEASON_ID int NOT NULL,\
                        GAME_ID int NOT NULL,\
                        TEAM_ID int NOT NULL,\
                        START_POSITION char(50),\
                        COMMENT char(200),\
                        MIN char(50),\
                        FGM float,\
                        FGA float,\
                        FG_PCT float,\
                        FG3M float,\
                        FG3A float,\
                        FG3_PCT float,\
                        FTM float,\
                        FTA float,\
                        FT_PCT float,\
                        OREB float,\
                        DREB float,\
                        AST float,\
                        STL float,\
                        BLK float,\
                        TO_ float,\
                        PF float,\
                        PTS float,\
                        PLUS_MINUS float,\
                        PRIMARY KEY (ID)"

            c.execute(f'CREATE TABLE Statistics ({structure})')
            print("statistics created.")
        except:
            pass
    
    Season_s(mydb)
    Games_s(mydb)
    Player_s(mydb)
    Teams_s(mydb)
    Statistics_s(mydb)

def relations_NBA_DB(mydb):
    c = mydb.cursor()
    c.execute('USE NBA_DB')

    #cities relations
    c.execute('ALTER TABLE Cities ADD FOREIGN KEY (ARENA_ID) REFERENCES Arenas(ARENA_ID);')

    #teams relations
    c.execute('ALTER TABLE Teams ADD FOREIGN KEY (CITY_ID) REFERENCES Cities(CITY_ID);')

    #game details relations
    c.execute('ALTER TABLE Game_details ADD FOREIGN KEY (GAME_ID) REFERENCES Games(GAME_ID);')
    c.execute('ALTER TABLE Game_details ADD FOREIGN KEY (TEAM_ID) REFERENCES Teams(TEAM_ID);')
    c.execute('ALTER TABLE Game_details ADD FOREIGN KEY (PLAYER_ID) REFERENCES Players(PLAYER_ID);')

    #games relations
    c.execute('ALTER TABLE Games ADD FOREIGN KEY (SEASON_ID) REFERENCES Seasons(SEASON_ID);')
    c.execute('ALTER TABLE Games ADD FOREIGN KEY (HOME_TEAM_ID) REFERENCES Teams(TEAM_ID);')
    c.execute('ALTER TABLE Games ADD FOREIGN KEY (VISITOR_TEAM_ID) REFERENCES Teams(TEAM_ID);')

    #player at team
    c.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (PLAYER_ID) REFERENCES Players(PLAYER_ID);')
    c.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (TEAM_ID) REFERENCES Teams(TEAM_ID);')
    c.execute('ALTER TABLE Players_at_team_in_season ADD FOREIGN KEY (SEASON_ID) REFERENCES Seasons(SEASON_ID);')

def look_relation_NBA_DB(mydb):
    c = mydb.cursor()
    c.execute('SELECT * FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_SCHEMA="NBA_DB"')
    print("\nRelations:")
    for i in c:
        print(i)


def relations_SNBA_DB(mydb):
    c = mydb.cursor()
    c.execute('USE S_NBA_DB')

    # Statistic relations
    c.execute('ALTER TABLE Statistics ADD FOREIGN KEY (PLAYER_ID) REFERENCES Player(PLAYER_ID);')
    c.execute('ALTER TABLE Statistics ADD FOREIGN KEY (SEASON_ID) REFERENCES Season(SEASON_ID);')
    c.execute('ALTER TABLE Statistics ADD FOREIGN KEY (GAME_ID) REFERENCES Game(GAME_ID);')
    c.execute('ALTER TABLE Statistics ADD FOREIGN KEY (TEAM_ID) REFERENCES Teams(TEAM_ID);')

def look_relation_SNBA_DB(mydb):
    c = mydb.cursor()
    c.execute('SELECT * FROM INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS WHERE CONSTRAINT_SCHEMA="S_NBA_DB"')
    print("\nRelations:")
    for i in c:
        print(i)

def copy_data_to_new_squema(mydb):
    c = mydb.cursor()

    # Season data
    c.execute('INSERT INTO S_NBA_DB.Season SELECT * FROM NBA_DB.Seasons;')
    print('Seasons data has been copied to new Squema')

    # Player data
    c.execute('INSERT INTO S_NBA_DB.Player SELECT * FROM NBA_DB.Players;')
    print('Player data has been copied to new Squema')

    # Team data
    c.execute('INSERT INTO S_NBA_DB.Teams SELECT NBA_DB.Teams.TEAM_ID,NBA_DB.Teams.TEAM_NAME,NBA_DB.Teams.ABBREVIATION,NBA_DB.Teams.NICKNAME,NBA_DB.Teams.YEARFOUNDED,NBA_DB.Teams.MIN_YEAR,NBA_DB.Teams.MAX_YEAR,NBA_DB.Cities.CITY_NAME,NBA_DB.Arenas.ARENA_NAME,NBA_DB.Arenas.ARENACAPACITY,NBA_DB.Teams.OWNER,NBA_DB.Teams.GENERALMANAGER,NBA_DB.Teams.HEADCOACH,NBA_DB.Teams.LEAGUE_ID,NBA_DB.Teams.DLEAGUEAFFILIATION FROM NBA_DB.Teams,NBA_DB.Cities,NBA_DB.Arenas;')
    print('Team data has been copied to new Squema')

    # Game data
    c.execute('INSERT INTO S_NBA_DB.Game SELECT NBA_DB.Games.GAME_ID,NBA_DB.Games.GAME_STATUS_TEXT,NBA_DB.Teams.TEAM_NAME,NBA_DB.Cities.CITY_NAME,NBA_DB.Arenas.ARENA_NAME,NBA_DB.Games.PTS_home,NBA_DB.Games.FG_PCT_home,NBA_DB.Games.FT_PCT_home,NBA_DB.Games.FG3_PCT_home,NBA_DB.Games.AST_home, NBA_DB.Games.REB_home,NBA_DB.Games.VISITOR_TEAM_ID,NBA_DB.Games.PTS_away,NBA_DB.Games.FG_PCT_away,NBA_DB.Games.FT_PCT_away,NBA_DB.Games.FG3_PCT_away,NBA_DB.Games.AST_away,NBA_DB.Games.REB_away,NBA_DB.Games.HOME_TEAM_WINS FROM NBA_DB.Games,NBA_DB.Teams,NBA_DB.Cities,NBA_DB.Arenas;')
    print('Team data has been copied to new Squema')

    # Statistics data
    c.execute('INSERT INTO S_NBA_DB.Statistics SELECT NBA_DB.Players.PLAYER_ID,NBA_DB.Seasons.SEASON_ID,NBA_DB.Games.GAME_ID,NBA_DB.Teams.TEAM_ID,NBA_DB.Game_details.START_POSITION,NBA_DB.Game_details.COMMENT,NBA_DB.Game_details.MIN,NBA_DB.Game_details.FGM,NBA_DB.Game_details.FGA,NBA_DB.Game_details.FG_PCT,NBA_DB.Game_details.FG3M,NBA_DB.Game_details.FG3A,NBA_DB.Game_details.FG3_PCT,NBA_DB.Game_details.FTM,NBA_DB.Game_details.FTA,NBA_DB.Game_details.FT_PCT,NBA_DB.Game_details.OREB,NBA_DB.Game_details.DREB,NBA_DB.Game_details.AST,NBA_DB.Game_details.STL,NBA_DB.Game_details.BLK,NBA_DB.Game_details.TO_,NBA_DB.Game_details.PF,NBA_DB.Game_details.PTS,NBA_DB.Game_details.PLUS_MINUS FROM NBA_DB.Players,NBA_DB.Seasons,NBA_DB.Games,NBA_DB.Teams,NBA_DB.Game_details;')
    print('Statistics data has been copied to new Squema')

    mydb.commit()





    

