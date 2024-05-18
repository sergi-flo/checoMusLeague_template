import os

import pymysql

# Import get_docker_secrets to get secrets from docker
from utils import get_docker_secrets

# Replace these variables with your actual database credentials
ip = os.environ.get("IP")
database_name = get_docker_secrets("mysql-database")
database_user = get_docker_secrets("mysql-user")
database_user_password = get_docker_secrets("mysql-user-password")

if "__main__" == __name__:
    conn = pymysql.connect(
        host=ip,
        user=database_user,
        password=database_user_password,
        port=int(os.environ.get("PORT")),
    )
    cursor = conn.cursor()
    cursor.execute(f"USE {database_name}")
    try:
        # create and populate the table users for the webpage
        cursor.execute(""" CREATE TABLE season_0(id INT AUTO_INCREMENT PRIMARY KEY,
                                            name VARCHAR(255) UNIQUE NOT NULL,
                                            score FLOAT,
                                            wins INT,
                                            losses INT,
                                            total INT
                                            );""")

        query_users = """INSERT INTO season_0 (name, score, wins, losses, total) 
        VALUES (%s, %s, %s, %s, %s)"""

        with open("players.txt", "r") as players_file:
            players = players_file.readlines()
            for player_name in players:
                if player_name.startswith("#"):
                    continue
                player = (player_name.rstrip().lower(), 1000, 0, 0, 0)
                cursor.execute(query_users, player)
            print("Data inserted into season_0 table successfully.")

        # create and populate the table users for the webpage
        cursor.execute(""" CREATE TABLE games_history_0(id INT AUTO_INCREMENT PRIMARY KEY,
                                            timestamp DATETIME,
                                            winner1 VARCHAR(255),
                                            winner1_percentage FLOAT,
                                            winner1_old_elo FLOAT,
                                            winner1_new_elo FLOAT,
                                            winner2 VARCHAR(255),
                                            winner2_percentage FLOAT,
                                            winner2_old_elo FLOAT,
                                            winner2_new_elo FLOAT,
                                            loser1 VARCHAR(255),
                                            loser1_percentage FLOAT,
                                            loser1_old_elo FLOAT,
                                            loser1_new_elo FLOAT,
                                            loser2 VARCHAR(255),
                                            loser2_percentage FLOAT,
                                            loser2_old_elo FLOAT,
                                            loser2_new_elo FLOAT
                                            );""")
    except Exception:
        print("Tables already created!! Skipping...")
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        print("Done")
