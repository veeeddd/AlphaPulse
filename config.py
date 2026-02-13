# config.py

# Assets to monitor
TICKERS = ["AAPL", "TSLA", "NVDA", "MSFT", "AMD"]

# Storage Path (DuckDB persistent file)
DB_PATH = "alphapulse.db"

# NLP Model (Specialized FinBERT for Finance)
MODEL_NAME = "ProsusAI/finbert"

# Scraping Limits
NEWS_LIMIT = 5