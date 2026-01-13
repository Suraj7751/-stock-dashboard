from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, inspect
import pandas as pd
from typing import Optional

# ---------------- DATABASE ----------------
engine = create_engine("sqlite:///stocks.db", echo=False)

# ---------------- APP ----------------
app = FastAPI(
    title="Stock Intelligence Dashboard",
    version="1.0"
)

# ---------------- CORS ----------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------- SECTOR MAP ----------------
STOCK_SECTORS = {
    "INFY": "IT",
    "TCS": "IT",
    "HCLTECH": "IT",

    "HDFCBANK": "BANK",
    "ICICIBANK": "BANK",
    "SBIN": "BANK",
    "AXISBANK": "BANK",

    "RELIANCE": "ENERGY",
    "ONGC": "ENERGY",

    "ITC": "FMCG",
    "HINDUNILVR": "FMCG",

    "LT": "INFRA"
}

# ---------------- COMPANIES (PAGINATED + SECTOR) ----------------
@app.get("/companies")
def get_companies(
    page: int = 1,
    limit: int = 10,
    sector: Optional[str] = None
):
    inspector = inspect(engine)
    tables = inspector.get_table_names()

    companies = [t.upper() for t in tables]

    if sector:
        companies = [c for c in companies if STOCK_SECTORS.get(c) == sector]

    total = len(companies)
    start = (page - 1) * limit
    end = start + limit

    return {
        "data": companies[start:end],
        "page": page,
        "limit": limit,
        "total": total
    }

# ---------------- STOCK DATA ----------------
@app.get("/data/{symbol}")
def get_stock_data(symbol: str):
    try:
        df = pd.read_sql(symbol.lower(), engine)
    except Exception:
        raise HTTPException(status_code=404, detail="Stock not found")

    return df.tail(90).to_dict(orient="records")

# ---------------- SUMMARY ----------------
@app.get("/summary/{symbol}")
def get_summary(symbol: str):
    try:
        df = pd.read_sql(symbol.lower(), engine)
    except Exception:
        raise HTTPException(status_code=404, detail="Stock not found")

    return {
        "52_week_high": float(df["High"].max()),
        "52_week_low": float(df["Low"].min()),
        "average_close": float(df["Close"].mean())
    }

# ---------------- COMPARE ----------------
@app.get("/compare")
def compare(symbol1: str, symbol2: str):
    try:
        df1 = pd.read_sql(symbol1.lower(), engine)
        df2 = pd.read_sql(symbol2.lower(), engine)
    except Exception:
        raise HTTPException(status_code=404, detail="Stock not found")

    return {
        symbol1: float(df1["daily_return"].mean()),
        symbol2: float(df2["daily_return"].mean())
    }
