import sqlite3

database = "database.sqlite"

conn = sqlite3.connect(database)

print("Connection successful")

import pandas as pd 

conn.execute("""
    CREATE TABLE IF NOT EXISTS students
    (ID INTEGER PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     CLASS VARCHAR(10) NOT NULL,
     AGE INT DEFAULT(10),
     GRADE VARCHAR(5) NOT NULL);
""")
conn.execute("""
    INSERT INTO students VALUES
    (1, "Michael", "Grade 10", 14, "A");
""")
conn.execute("""
    INSERT INTO students VALUES
    (2, "John", "Grade 9", 15, "A");
""")
conn.execute("""
    INSERT INTO students VALUES
    (3, "Sarah", "Grade 10", 14, "C");
""")

print("Table created successfully")
tables = pd.read_sql("""
    SELECT * FROM sqlite_master
    WHERE type = "table";
""", conn)
print(tables)

students = pd.read_sql("""
   SELECT * FROM students;
""", conn)

print(students) 
