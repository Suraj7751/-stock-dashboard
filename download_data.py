import yfinance as yf
import os

# Create data folder if not exists
os.makedirs("data", exist_ok=True)

stocks = {
    "INFY": "INFY.NS",
    "TCS": "TCS.NS",
    "RELIANCE": "RELIANCE.NS",
    "HDFCBANK": "HDFCBANK.NS",
    "ICICIBANK": "ICICIBANK.NS",
    "SBIN": "SBIN.NS",
    "HINDUNILVR": "HINDUNILVR.NS",
    "ITC": "ITC.NS",
    "LT": "LT.NS",
    "AXISBANK": "AXISBANK.NS"
}

for name, symbol in stocks.items():
    print(f"Downloading {name}...")
    df = yf.download(symbol, period="1y")

    if df.empty:
        print(f"⚠️ No data for {name}")
        continue

    df.reset_index(inplace=True)
    df.to_csv(f"data/{name}.csv", index=False)

print("✅ All stock data downloaded successfully")
