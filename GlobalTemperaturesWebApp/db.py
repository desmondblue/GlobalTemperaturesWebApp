import sqlite3 as sql
import pandas as pd
import os
# Initializing database and tables

conn = sql.connect(os.path.join("Database/global_land_temp_db.db"))
with open(os.path.join('./Scripts/inital_script.sql'), "r") as f:
    conn.executescript(f.read())
    conn.commit()
# Reading data from file
df = pd.read_csv(os.path.join("./Dataset/GlobalLandTemperaturesByCity.csv"))
conn.executemany("INSERT INTO Global_Land_Temperatures_By_City VALUES(strftime('%s',?),?,?,?,?,?,?)", df.values.tolist())
conn.commit()
print("Database Created Successfully.")
conn.close()
