import os
import requests
import pandas as pd
from sqlalchemy import create_engine, text

CSV_URL = "https://raw.githubusercontent.com/JebinAbraham/C00313624_BigData_Project/refs/heads/main/UNSW_NB15_testing-set.csv" 
DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "root")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "rootpassword")
DB_NAME = os.environ.get("DB_NAME", "testdb")
TABLE_NAME = "raw_data.csv"

def main():
    # Download CSV
    r = requests.get(CSV_URL)
    r.raise_for_status()
    with open("raw_data.csv", "wb") as f:
        f.write(r.content)
    
    df = pd.read_csv("raw_data.csv")
    
    engine = create_engine(f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

    # Drop table if exists
    with engine.connect() as conn:
        conn.execute(text(f"DROP TABLE IF EXISTS {TABLE_NAME}"))

    # Insert data
    df.to_sql(TABLE_NAME, engine, if_exists='replace', index=False)
    print("Data ingestion completed successfully.")

if __name__ == "__main__":
    main()
