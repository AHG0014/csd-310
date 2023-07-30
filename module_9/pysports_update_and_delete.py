#Import STATEMENTS
"Name: Autumn Gooding"
"Date: 7/29/2023"
"Class: CYBER410"

#import statements for MySQL
import mysql.connector
from mysql.connector import errorcode

#configuring database
config = {
    "user": "pysports_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

def show_players(cursor, title):
    # This is used to execute the inner join

    # inner join query 
    
    cursor.execute("SELECT player_id, first_name, last_name, team_name \
                    FROM player \
                    INNER JOIN team \
                        ON player.team_id = team.team_id;")
 
    players = cursor.fetchall()

    print("\n  -- {} --".format(title))
    
    #information on players
    for player in players:
        print("  Player ID: {}\n  First Name: {}\n  Last Name: {}\n  Team Name: {}\n".format(player[0], player[1], player[2], player[3]))

try: 

    db = mysql.connector.connect(**config) # connecting to the pysports database 

    cursor = db.cursor()

    # With this we will be able to insert a player
    add_player = ("INSERT INTO player(first_name, last_name, team_id)"
                 "VALUES(%s, %s, %s)")

    # new player info
    player_info = ("Smeagol", "Shire Folk", 1)

    cursor.execute(add_player, player_info)

    db.commit()

    # shows all players in the record table in the database
    show_players(cursor, "DISPLAYING PLAYERS AFTER INSERT")

    # this will update the teams records
    update_player = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")

    cursor.execute(update_player)

    # show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER UPDATE")

    # this will remove/delete player  
    delete_player = ("DELETE FROM player WHERE first_name = 'Smeagol'")

    cursor.execute(delete_player)

    # show all records in the player table 
    show_players(cursor, "DISPLAYING PLAYERS AFTER DELETE")

    input("\n\n  Press any key to continue... ")

except mysql.connector.Error as err:
    """ handle errors """ 

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("  The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("  The specified database does not exist")

    else:
        print(err)

finally:
    """ close the connection to MySQL """

    db.close()