import pandas as pd
import yfinance as yf
from db_manager import get_connection

def run_simple_backtest(ticker, threshold=0.85, hold_days=3):
    """
    Simple event-based backtester:
    - Signal: Alpha Score >= threshold
    - Strategy: Buy at close, Hold for X days, Sell at close.
    """
    with get_connection() as conn:
        sentiment_df = conn.execute(f"SELECT * FROM alpha_scores WHERE ticker = '{ticker}'").df()
    
    if sentiment_df.empty: return "No data."

    # Fetch price data for the window
    start_date = sentiment_df['timestamp'].min().date()
    prices = yf.Ticker(ticker).history(start=start_date)
    
    results = []
    for _, row in sentiment_df.iterrows():
        if row['alpha_score'] >= threshold:
            signal_date = row['timestamp'].date()
            try:
                # Find entry price (day after signal)
                entry_price = prices.loc[signal_date:].iloc[0]['Close']
                # Find exit price (X days later)
                exit_price = prices.loc[signal_date:].iloc[hold_days]['Close']
                
                pct_change = (exit_price - entry_price) / entry_price
                results.append(pct_change)
            except:
                continue # Skip if date is too recent or market closed

    if not results: return "Not enough signals to backtest."
    
    avg_return = sum(results) / len(results)
    win_rate = len([r for r in results if r > 0]) / len(results)
    
    return {
        "ticker": ticker,
        "signals_found": len(results),
        "avg_return_per_trade": f"{avg_return:.2%}",
        "win_rate": f"{win_rate:.2%}"
    }

if __name__ == "__main__":
    from config import TICKERS
    for t in TICKERS:
        print(f"Backtesting {t}: {run_simple_backtest(t)}")