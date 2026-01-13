import pandas as pd
import os

data_folder = "data"

for file in os.listdir(data_folder):

    # ✅ Process only individual stock files
    if not file.endswith(".csv") or file == "stocks.csv":
        continue

    path = os.path.join(data_folder, file)

    if os.path.getsize(path) == 0:
        print(f"⚠️ Skipping empty file: {file}")
        continue

    df = pd.read_csv(path)

    # Convert Date
    if "Date" in df.columns:
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

    # Convert numeric columns
    price_cols = ["Open", "High", "Low", "Close", "Adj Close", "Volume"]
    for col in price_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Forward fill
    df = df.ffill()

    # Metrics
    df["daily_return"] = (df["Close"] - df["Open"]) / df["Open"]
    df["ma_7"] = df["Close"].rolling(7).mean()
    df["volatility"] = df["daily_return"].rolling(7).std()

    df.to_csv(path, index=False)
    print(f"✅ Processed: {file}")

print("🎉 Stock files processed successfully")
