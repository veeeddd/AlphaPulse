import pandas as pd
from backtest_engine import run_simple_backtest
from config import TICKERS

def optimize_thresholds():
    print("--- 🚀 Starting Alpha Threshold Optimization ---")
    results = []
    
    # Testing a range of thresholds to find the highest win rate
    test_range = [0.5, 0.6, 0.7, 0.75, 0.8, 0.82, 0.85, 0.9]
    
    for ticker in TICKERS:
        best_win_rate = 0
        best_threshold = 0
        
        for t in test_range:
            report = run_simple_backtest(ticker, threshold=t)
            
            if isinstance(report, dict):
                wr_str = report['win_rate'].replace('%', '')
                wr = float(wr_str)
                
                if wr > best_win_rate:
                    best_win_rate = wr
                    best_threshold = t
        
        if best_threshold > 0:
            print(f"[WINNER] {ticker}: Best Threshold is {best_threshold} (Win Rate: {best_win_rate}%)")
            results.append({"ticker": ticker, "threshold": best_threshold})
        else:
            print(f"[!] {ticker}: No profitable signals found in current data.")

if __name__ == "__main__":
    optimize_thresholds()