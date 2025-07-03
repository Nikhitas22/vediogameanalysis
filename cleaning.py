import pandas as pd
import numpy as np
# Loading csv files
games = pd.read_csv("games.csv")
sales = pd.read_csv("vgsales.csv")

games.rename(columns={
    'Release Date': 'Release_Date',
    'Times Listed': 'Times_Listed',
    'Number of Reviews': 'Number_of_Reviews'
}, inplace=True)

if 'Unnamed: 0' in games.columns:
    games.drop(columns=['Unnamed: 0'], inplace=True)

if 'Unnamed: 0' in sales.columns:
    sales.drop(columns=['Unnamed: 0'], inplace=True)
if 'Rank' in sales.columns:
    sales.drop(columns=['Rank'], inplace=True)




# Renaming for for consistency

games.rename(columns={'Title': 'Gamename'}, inplace=True)
sales.rename(columns={'Name': 'Gamename'}, inplace=True)

#Drop duplicate rows

games.drop_duplicates(inplace=True)
sales.drop_duplicates(inplace=True)

# Drop row with missing critical values

games.dropna(subset=['Gamename', 'Rating', 'Plays'], inplace=True)
sales.dropna(subset=['Gamename', 'Global_Sales'], inplace=True)

#Convert to Numeric
games['Rating'] =pd.to_numeric(games['Rating'], errors='coerce')
games['Plays'] =pd.to_numeric(games['Plays'], errors='coerce')
sales['Global_Sales'] =pd.to_numeric(sales['Global_Sales'], errors='coerce')

# Cleanup of Nans After conversion
games.dropna(subset=['Rating','Plays'], inplace=True)
sales.dropna(subset=['Global_Sales'], inplace=True)


# Step 2 
#Normalize fields Genre, Platform & Publisher Name

for col in ['Genres', 'Platform', 'Publisher']:
    if col in sales.columns:
        sales[col] = sales[col].astype(str).str.strip().str.lower()

for col in ['Genres','Platform', 'Team']:
    if col in games.columns:
        games[col] = games[col].astype(str).str.strip().str.lower()


# Only filter Genre if it exists
if 'Genres' in games.columns:
    games = games[~games['Genres'].isin(['', '[]', 'nan', 'none'])]

games['Gamename'] = games['Gamename'].str.strip().str.lower()
sales['Gamename'] = sales['Gamename'].str.strip().str.lower()

#Step 3
#Standardize date and category format

if 'Release_Date' in games.columns:
    games['Release_Date'] = pd.to_datetime(games['Release_Date'], errors= 'coerce')


if 'Year' in sales.columns:
    sales['Year'] = pd.to_numeric(sales['Year'], errors='coerce')

#Final cleanup

games.dropna(inplace=True)
sales.dropna(inplace=True)

print("✅ Cleaning complete!")
print("games shape:", games.shape)
print("sales shape:", sales.shape)


import sqlite3

conn = sqlite3.connect("vediogames.db")
cursor = conn.cursor()
cursor.execute("PRAGMA foreign_keys = ON;")

cursor.execute("DROP TABLE If Exists merged_data;")
cursor.execute("DROP TABLE If Exists vgsales;")
cursor.execute("DROP TABLE If Exists games;")

cursor.execute("""
CREATE TABLE games (
    Gamename TEXT PRIMARY KEY,
    Release_Date  TEXT,
    Team TEXT,
    Rating  REAL,
    Times_Listed INTEGER,
    Number_of_Reviews INTEGER,
    Genres TEXT,
    Summary TEXT,
    Reviews TEXT,
    Plays INTEGER,
    Playing INTEGER,
    Backlogs INTEGER,
    Wishlist INTEGER               
)
""")

cursor.execute("""
CREATE TABLE vgsales(
    Gamename TEXT,
    Platform TEXT,
    Year INTEGER,
    Genre TEXT,
    Publisher TEXT,
    NA_Sales REAL,
    EU_Sales REAL,
    JP_Sales REAL,
    Other_Sales REAL,
    Global_Sales REAL,
    FOREIGN KEY(Gamename) REFERENCES games(Gamename)
)
""")


games.to_sql('games',conn, if_exists='append', index=False)
sales = sales[sales['Gamename'].isin(games['Gamename'])]
sales.to_sql('vgsales', conn, if_exists='append', index=False)


cursor.execute("""
CREATE TABLE merged_data AS
SELECT
    v.Gamename,
    v.Platform,
    v.Year,
    v.Genre,
    v.Publisher,
    v.NA_Sales,
    v.EU_Sales,
    v.JP_Sales,
    v.Other_Sales,
    v.Global_Sales,
    g.Release_Date,
    g.Team,
    g.Rating,
    g.Times_Listed,
    g.Number_of_Reviews,
    g.Genres,
    g.Summary,
    g.Reviews,
    g.Plays,
    g.Playing,        
    g.Backlogs,
    g.Wishlist
FROm vgsales v
INNER JOIN games g ON v.Gamename =  g. Gamename;            
""")


conn.commit()
conn.close()
print("All tables created using join")        

