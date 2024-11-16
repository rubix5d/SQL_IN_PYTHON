import sqlite3

database = "basicdata.sqlite"

conn = sqlite3.connect(database)

print("Connection successful")

import pandas as pd

table = pd.read_sql("""
    SELECT * FROM sqlite_master
    WHERE type="table";
""", conn)

# print(table)

teams = pd.read_sql("""
    SELECT * FROM team;
""", conn)

# print(teams)

players = pd.read_sql("""
     SELECT * FROM player
     ORDER BY Bowling_skill DESC;
""", conn)

# print(players)

matches = pd.read_sql("""
    SELECT SUM(Extra_Runs) FROM Extra_Runs
""", conn)

print(matches)