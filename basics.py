import sqlite3

database = "basicdata.sqlite"

conn = sqlite3.connect(database)

print("Connection successful")

import pandas as pd

teams = pd.read_sql(""" SELECT *
                     FROM Player_Match WHERE Team_Id IN (1,2);""", conn)


print(teams)

new_teams = pd.read_sql(""" SELECT * 
                        FROM Team
                        WHERE Team_Name LIKE 'De%';
""", conn)

print(new_teams)