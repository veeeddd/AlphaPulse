import logging
from datetime import datetime

# Setup logging for audit trails
logging.basicConfig(
    filename='alpha_alerts.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def check_alpha_threshold(ticker, score, headline, threshold=0.85):
    """
    Triggers an alert if the FinBERT score exceeds the confidence threshold.
    """
    if score >= threshold:
        alert_msg = f"🚀 HIGH ALPHA SIGNAL: {ticker} | Score: {score:.2f} | {headline}"
        print(f"\n{alert_msg}")
        logging.info(alert_msg)
        return True
    return False

if __name__ == "__main__":
    # Test Alert
    check_alpha_threshold("NVDA", 0.92, "NVIDIA announces next-gen AI chip with 2x performance.")