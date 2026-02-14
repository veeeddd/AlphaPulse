# config.py

# Assets to monitor
TICKERS = ["AAPL", "TSLA", "NVDA", "MSFT", "AMD", "GOOGL", "AMZN", "META", "NFLX", "BRK-B",
    "JPM", "V", "UNH", "MA", "HD", "PG", "BAC", "DIS", "ADBE", "CRM", "XOM", "CVX",
    "COST", "PEP", "KO", "AVGO", "CSCO", "ORCL", "ACN", "ABT", "LIN", "MRK", "TMO"]

# Storage Path (DuckDB persistent file)
DB_PATH = "alphapulse.db"

# NLP Model (Specialized FinBERT for Finance)
MODEL_NAME = "ProsusAI/finbert"

# Scraping Limits
NEWS_LIMIT = 30