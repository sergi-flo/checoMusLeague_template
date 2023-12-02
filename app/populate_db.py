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
    except Exception:
        print("Tables already created!! Skipping...")
    finally:
        conn.commit()
        cursor.close()
        conn.close()
        print("Done")
