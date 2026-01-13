import pandas as pd
import os
from app.database import engine

for file in os.listdir("data"):
    symbol = file.replace(".csv", "").lower()
    df = pd.read_csv(f"data/{file}")
    df.to_sql(symbol, engine, if_exists="replace", index=False)

print("✅ Data loaded into database")
