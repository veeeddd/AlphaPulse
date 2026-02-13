from alerts import check_alpha_threshold
from scraper import AlphaScraper
from inference_engine import SentimentEngine
from db_manager import get_connection, init_db
from config import TICKERS

def run_alpha_pulse():
    # 1. Initialize all components
    init_db()
    scraper = AlphaScraper()
    engine = SentimentEngine()
    
    conn = get_connection()
    
    print("\n--- Starting AlphaPulse Pipeline ---")
    
    for ticker in TICKERS:
        # 2. Fetch News with Day 6 Fault Tolerance
        headlines = scraper.fetch_news(ticker)
        
        for text in headlines:
            # 3. Analyze Sentiment using FinBERT
            result = engine.analyze_sentiment(text)
            
            # 4. Save to DuckDB for Historical Backtesting
            conn.execute("""
                INSERT INTO alpha_scores (ticker, headline, alpha_score, sentiment)
                VALUES (?, ?, ?, ?)
            """, (ticker, text, result['confidence'], result['sentiment']))
            
            # 5. Day 10: Check for High-Alpha Signals
            # This will trigger a console alert and log to alpha_alerts.log
            check_alpha_threshold(ticker, result['confidence'], text)
            
        print(f"[OK] Processed {len(headlines)} headlines for {ticker}.")

    conn.close()
    print("\n--- Pipeline Run Complete. Database Updated. ---")

if __name__ == "__main__":
    run_alpha_pulse()