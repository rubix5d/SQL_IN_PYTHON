import sqlite3

database = "basicdata.sqlite"

conn = sqlite3.connect(database)

print("Connection successful")

import pandas as pd 

tables = pd.read_sql("""
   SELECT * FROM sqlite_master
                     WHERE type = "table";

""", conn)

players = pd.read_sql("""
 SELECT * FROM Player
                      ORDER BY Bowling_skill DESC;
                      
""", conn)
# print(tables)
print(players)