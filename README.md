Stock Intelligence Dashboard

A full-stack stock analytics dashboard built using FastAPI, SQLite, Pandas, and Chart.js.
The project collects real stock market data, processes it, and visualizes it using interactive charts including candlestick charts with volume.

This project demonstrates backend API design, data processing, frontend visualization, and Docker-based deployment.

🚀 Features
🔹 Backend (FastAPI)

REST APIs with Swagger documentation

Dynamic stock discovery from database

Pagination & sector-wise filtering

Stock comparison API

Summary metrics (52-week high/low, average close)

🔹 Data Processing

Real stock data using yfinance

Data cleaning & transformation using Pandas

Metrics calculated:

Daily return

Volatility

Moving averages

🔹 Frontend Dashboard

Line chart & Candlestick (OHLC) chart

Volume bars under candlesticks

Sector filter (IT, Banking, FMCG, Energy, Infra)

Pagination for 100+ stocks

Top Gainer & Top Loser

Stock comparison

Dark mode UI

🔹 DevOps

Dockerized backend

Cloud-ready deployment (Render compatible)

🧱 Tech Stack
Layer	Technology
Language	Python
Backend	FastAPI
Database	SQLite
Data	Pandas, NumPy, yfinance
Frontend	HTML, CSS, JavaScript
Charts	Chart.js + Financial Plugin
DevOps	Docker
📂 Project Structure
stock-dashboard/
│
├── app/
│   └── main.py
│
├── data/
│   └── *.csv
│
├── frontend/
│   └── index.html
│
├── stocks.db
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md

⚙️ How to Run Locally
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Start Backend
python -m uvicorn app.main:app --reload


Open Swagger UI:

http://127.0.0.1:8000/docs

3️⃣ Open Frontend

Open this file in browser:

frontend/index.html

🐳 Run with Docker
Build Image
docker build -t stock-dashboard .

Run Container
docker run -p 8000:8000 stock-dashboard

🔌 API Endpoints
Endpoint	Description
/companies	Paginated stock list
/data/{symbol}	Historical stock data
/summary/{symbol}	High/Low/Average
/compare	Compare two stocks

Example:

GET /companies?page=1&limit=10&sector=BANK

🧠 Design Highlights

No hardcoded stock symbols

Backend-driven pagination

Sector-based filtering

Frontend decoupled from backend

Candlestick + volume visualization

Dockerized for deployment consistency

🔮 Future Improvements

Technical indicators (RSI, EMA)

Caching (Redis)

Authentication & portfolios

PostgreSQL instead of SQLite

ML-based price prediction